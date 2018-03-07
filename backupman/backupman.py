import os
import sys
from . import VERSION

configs = {
    'days': None,
    'rsh-opts': '',
    'inc-backup': False,
    'asroot': False,
    'host': None,
    'src-dir': None,
    'dst-dir': None,
}

"""
Source URL Examples
  ssh://[username[:password]@]test-srv-01[:port]/home/
  fs:///home/
"""
def usages(prog):
    print ('Usage: %s [-i] [-d DAYS] [-e rsh options] [-h REMOTE-HOST] <BKUP-SRC> <BKUP-DST>' % prog)
    print ('')
    print("Mandatory arguments to long options are mandatory for short options too.")
    print ("  -d,  --delete-old-backup=DAYS")
    print ("                            delete old backup whitch backups older than DAYS ago.")
    print ("  -e,  --rsh=RSH-OPTIONS    specify the remote shell to use, valid on ssh mode")
    #print ("  -i   --incremental        keep STDIN open even if not attached")
    print ("  -i,  --incremental        incremental backup")

    print ("  -r,  --run-as-root        remote rsync command run as root using sudo command" )
    print ("       --help               display this message and exit")
    print ("       --version            output version information and exit")

def print_version(prog):
    print ('%s version %s' % (prog, VERSION))

import getopt

from urllib.parse import urlparse

from .rsync import dosync

def main():
    prog = os.path.basename(sys.argv[0])

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'd:e:ir', ['delete-old-backup=',
                                                            'rsh=',
                                                            'incremental',
                                                            'run-as-root'
                                                            'help',
                                                            'version'])
    except:
        usages(prog)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('--help',):
            usages(prog)
            sys.exit(0)

        if opt in ('--version',):
            print_version(prog)
            sys.exit(0);

        if opt in ('-d', '--delete-old-backup'):
            try:
                configs['days'] = int(arg)
            except:
                print("argument `%s` is not integer, please check it." % arg)
                sys.exit(-1)

        if opt in ('-e', '--rsh'):
            configs['rsh-opts'] = arg

        if opt in ('-i', '--incremental'):
            configs['inc-backup'] = True

        if opt in ('-r', '--asroot'):
            configs['asroot'] = True


    if len(args) is not 2:
        usages(prog)
        exit(2)


    try:
        uri = urlparse(args[0])
    except Exception as e:
        print("Couldn't not parse source uri: %s" % str(e))

    if uri.scheme == 'ssh' :
        configs['proto'] = 'ssh'
        configs['host'] = uri.netloc
        configs['src-dir'] = uri.path
        configs['port'] = uri.port if uri.port else 22
        configs['username'] = uri.username
        configs['password'] = uri.password
    elif uri.scheme == 'fs':
        configs['proto'] = 'fs'
        configs['host'] = None
        if uri.netloc:
            configs['src-dir'] = os.path.join('/',
                                              os.path.join(uri.netloc,
                                                           uri.path[1:] if uri.path.startswith('/') else uri.path))
        else:
            configs['src-dir'] = uri.path
        configs['rsh'] = None
    else:
        print('Support protofol ssh or fs only!!')
        exit(0)


    configs['dst-dir'] = args[1]

    dosync(configs)








