import os
import sys
from . import VERSION

configs = {
    'days': None,
    'ssh-opts': 'ssh',
    'inc-backup': False,
    'host': None,
    'src-dir': None,
    'dst-dir': None
}

"""

"""
def usages(prog):
    print ('Usage: %s [-i] [-d DAYS] [-e rsh options] [-h REMOTE-HOST] <BKUP-SRC> <BKUP-DST>' % prog)
    print ('')
    print("Mandatory arguments to long options are mandatory for short options too.")
    print ("  -d,  --delete-old-backup=DAYS")
    print ("                            delete old backup whitch backups older than DAYS ago.")
    print ("  -e,  --rsh                specify the remote shell to use")
    print ("  -h,  --host               remote host.")
    print ("  -i,  --incremental        incremental backup")
    print ("       --help               display this message and exit")
    print ("       --version            output version information and exit")

def print_version(prog):
    print ('%s version %s' % (prog, VERSION))

import getopt

from .rsync import dosync

def main():
    prog = os.path.basename(sys.argv[0])

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'd:e:h:i', ['delete-old-backup=', 'ssh=', 'host=', 'help', 'version'])
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
            configs['ssh-opts'] = arg

        if opt in ('-h', '--host'):
            configs['host'] = arg

        if opt in ('-i', '--incremental'):
            configs['inc-backup'] = True


    if len(args) is not 2:
        usages(prog)
        exit(2)

    configs['src-dir'] = args[0]
    configs['dst-dir'] = args[1]

    dosync(configs)







