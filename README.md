# python-backupman

Incremental Backup Using SSH+RSYNC

## Getting Started


### Prerequisites

What things you need to install the software and how to install them

```
sudo apt-get install rsync sshpass
```

### Installing

```
sudo -H pip install git+https://github.com/grepos/python-backupman.git
```


## Running the tests

```
mkdir -p ~/tests/src ~/tests/dst

touch ~/tests/src/a
touch ~/tests/src/b
touch ~/tests/src/c

backupman ssh://localhost/home/username/tests/src /home/username/tests/dst
```


### Break down into end to end tests


### And coding style tests


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

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

## Contributing

Please read
[CONTRIBUTING.md](CONTRIBUTING.md) for
details on our code of conduct, and the process for submitting pull requests to
us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **E.K. KIM** - *Initial work* -
  [GREPOS](https://github.com/grepos)

  See also the list of
  [contributors](https://github.com/grepos/python-backupman/contributors) who participated
  in this project.

  ## License

  This project is licensed under the MIT License - see the
  [LICENSE.md](LICENSE.md) file for details

  ## Acknowledgments

  * Hat tip to anyone who's code was used
  * Inspiration
  * etc



