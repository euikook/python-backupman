import subprocess
import datetime
from uuid import uuid4 as uuidgen


RSYNC = ""

def rsync(out, opts, src, dst):
    """
    :param args:
    :param kwargs:
    :return:
    """
    subprocess.Popen(['rsync'])

def dosync(configs):
    """

    :param configs:
    :return:
    """
    print(configs)

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    uuid = uuidgen()

    """
    check command
    """

    """
    check directory
    """

    """
    sync .backupman.excludes
    """

    """
    sync
    """
