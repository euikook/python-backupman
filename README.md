# Incremental Backup using RSYNC+SSH

### Installation
```
got clone https://github.com/grepos/backupman.git
mkdir -p ~/bin
cp backupman/backupman ~/bin
```

## Usages

```
NAME
       backupman - backup script using rsync

NAME
   
SYNOPSIS
       backupman [-i] [-d DAYS] -e [SSH-OPTS] <BKUP-SRC> <BKUP-DST> 


DESCRIPTIONS
       backupman is rsync front-end script.

       -i, --incremental 
               Incremental Backup.
       -e, --ssh
               SSH option.
       -d, --delete-old-backup=DAYS
               Delete old backup which is backup older than DAYS ago.
       -h, --host 
               Remote host.

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
