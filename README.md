# Incremental Backup using RSYNC+SSH

### Installation

Install from [PyPi](https://pypi.org/project/backupman/)

```
sudo -H pip install backupman
```


Install [Development version](https://github.com/grepos/python-backupman)

```
sudo -H pip -i git+https://github.com/grepos/python-backupman.git
```

## Usages

```
NAME
       backupman - backup script using rsync

NAME
   
SYNOPSIS
       backupman [-i] [-d DAYS] [-e rsh options] <SRC-URI> <BKUP-DST> 


DESCRIPTIONS
       

Mandatory arguments to long options are mandatory for short options too.
       -d,  --delete-old-backup=DAYS
                            delete old backup whitch backups older than DAYS ago.
       -e,  --rsh=RSH-OPTIONS    specify the remote shell to use
       -i,  --incremental        incremental backup
       -r,  --run-as-root        remote rsync command run as root using sudo command
            --help               display this message and exit
            --version            output version information and exit

  SRC-URI: Backup source represented by uri scheme.

  PROTOCOL://[USERNAME[:PASSWORD]@]HOSTNAME[:PORT]/PATH/TO/BACKUP

  Connect to backup source using SSH
    ssh://examples.com/some/directory
    ssh://examples.com:2222/some/directory
    ssh://username@examples.com/home/directory
    ssh://username:password@examples.com/home/directory

  Backup source located in local filesystem
    fs://some/directory
    fs:///some/directory


AUTHOR
       Written by E.K. KIM (euikook@{gmail.com, grepos.com}) 

COPYLIGHT
       The MIT Lisense

       Copyright (c) 2018 E.K. KIM (euikook@gmail.com)

       Permission is hereby granted, free of charge, to any person obtaining 
       a copy of this software and associated documentation files 
       (the "Software"), to deal in the Software without restriction, 
       including without limitation the rights to use, copy, modify, merge, 
       publish, distribute, sublicense, and/or sell copies of the Software, and
       to permit persons to whom the Software is furnished to do so, subject to 
       the following conditions:

       The above copyright notice and this permission notice shall be included 
       in all copies or substantial portions of the Software.

       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
       EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
       OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
       IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
       DAMAGES OR OTHER LIABILITY,
       WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
       FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
       OTHER DEALINGS IN THE SOFTWARE.

SEE ALSO
       please see https://blog.grepos.com/2018/02/20/incremental-backup-using-rsyncssh/
        
```


## Define exclude files

A .backupman.excludes file specifies intentionally unsync files that Rsync should ignore.
Files already synced by Rsync are deleted; see the NOTES below for details.

.backupman.excludes file MUST BE located at TOP OF BACKUP SOURCE.

backupman sync .backupman.excludes first than sycn other.

### Examples

```
/mnt
/proc
/tmp
/sys
/dev
/run
/sys/fs/cgroup
```
