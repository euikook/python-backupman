import os
import sys
import shlex
import datetime
import subprocess
from uuid import uuid4 as uuidgen

"""
Define commands 
"""
CMD_RSYNC = '/usr/bin/rsync'
CMD_SUDO  = '/usr/bin/sudo'
EXCLUDES = ".backupman.excludes"

def is_executable(file):
    return os.path.isfile(file) and os.access(file, os.X_OK)

def makedirs(dirs):
    if sys.version_info[0] < 3:
        if not os.path.isdir(dirs): os.makedirs(dirs)
    else:
        os.makedirs(dirs, exist_ok=True)

def rsync(src, dst, opts, logout=None, verbose=False):
    """
    :param src:
    :param dst:
    :param opts:
    :param logout:
    :param verbose:
    :return:
    """

    devnull = open(os.devnull, 'w')
    if logout is None: logout = devnull

    cmd = """%s %s "%s" "%s" """ % (CMD_RSYNC, opts, src, dst)
    #print(cmd)
    stdout = logout if verbose else devnull
    stderr = subprocess.STDOUT if verbose else stdout

    logout.write(cmd + '\n')
    logout.flush()

    try:
        subprocess.check_call(shlex.split(cmd), stdout=stdout, stderr=stderr)
    except subprocess.CalledProcessError as e:
        logout.write(str(e) + '\n')
        raise e

    logout.flush()

def dosync(configs):
    """
    :param configs:
    :return:
    """

    bkupsrc = """%s:""" % configs['host'] if configs['host'] else ''
    bkupsrc += """%s""" % os.path.join(configs['src-dir'], '').replace(' ', '\ ')
    bkupdst = configs['dst-dir']

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    uuid = uuidgen()

    """
    check command
    """

    cmd_rsync_r = CMD_RSYNC if not configs['asroot'] else CMD_SUDO + " " + CMD_RSYNC
    if not is_executable(CMD_RSYNC):
        print ("command not found 'rsync', please install it.")
        print ("sudo apt-get install -y rsync")

    if configs['asroot'] and not is_executable(CMD_SUDO):
        print("command not found 'sudo', please install it.")
        print("sudo apt-get install -y sudo")


    """
    check directory
    """
    if not os.path.isdir(configs['dst-dir']):
        if not os.path.isfile(configs['dst-dir']):
            print ("Destination directory does not directory. please check it")
            return

        print ("Destination directory does not existed. create it")
        if sys.version_info[0] < 3:
            makedirs(configs['dst-dir'])
        else:
            makedirs(configs['dst-dir'])

    """
    Change Current Working Directory
    """
    os.chdir(configs['dst-dir'])

    rsync_opts  = """ -apvz """

    if not configs['keep']: 
        rsync_opts += """ --delete """

    if configs['proto'] == 'ssh':
        if configs['password']:
            rshopts = " /usr/bin/sshpass -p %s ssh %s " % (configs['password'], configs['rsh-opts'])
        else:
            rshopts = " ssh %s " % configs['rsh-opts']

        if configs['username']:
            rshopts += " -l %s " % configs['username']

        if configs['port'] is not 22:
            rshopts += " -p %d " % configs['port']

        rsync_opts += """ -e "%s" """ % rshopts

    rsync_opts += """ --rsync-path="%s" """ % cmd_rsync_r
    rsync_opts += """ --numeric-ids """

    if configs['inc-backup']:
        logdir = "%s/%s" % (configs['dst-dir'], today)
        bkupname = str(uuid)
    else:
        logdir = configs['dst-dir'] + "/../Log"
        bkupname = os.path.basename(configs['dst-dir'])

    makedirs(logdir)
    logpath = os.path.join(logdir, bkupname + "-" + today + ".log")
    # print(logpath)
    logfile = open(logpath, 'w') # set bufsize to 0
    logfile.write(str(datetime.datetime.now()) + '\n')

    """
    sync .backupman.excludes
    """
    rsync_excl_opts = """ --delete --include "%s" --exclude="*" """ % EXCLUDES

    try:
        rsync(bkupsrc, bkupdst , rsync_opts + rsync_excl_opts, logfile)
    except Exception:
        print ("Error during backup process. please see more details inside log file `%s`" % logpath)
        return

    """
    sync
    """
    if configs['inc-backup']:
        bkupdst = configs['dst-dir'] + "/" + today + "/" + str(uuid)
        makedirs(bkupdst)

    """
    If .backupman.excludes is existed, append --exclude-from option
    """
    excloc = os.path.join(configs['dst-dir'], EXCLUDES)
    if os.path.isfile(excloc):
        rsync_opts += """ --exclude-from "%s" """ % excloc

    try:
        rsync(bkupsrc, bkupdst, rsync_opts, logfile, verbose=True)
    except Exception:
        print ("Error during backup process. please see more details inside log file `%s`" % logpath)
        return

    if not configs['inc-backup']: return

    lastest = os.path.join(configs['dst-dir'], 'lastest')

    if os.path.exists(lastest):
        if not os.path.islink(lastest):
            print ("`%s` is not link. can't create lastest link." % lastest)
            return
        else:
            os.remove(lastest)

    os.symlink(os.path.relpath(bkupdst, configs['dst-dir']), lastest)
