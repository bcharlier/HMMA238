# Some useful Windows & linux equivalent commands


| **Description**  | Unix       | example in Unix | Windows | example in Windows |
| :--------------- |:------------:| :-------------:|:------:|:-------:|
| change directory  |   `cd`         |                | `cd`       |      |
| change directory to the parent directory |   `cd ..`      |                | `cd ..`    |      |
| Directory path delimiter  |   `/`          | `cd MyName/Desktop/HMMA238`  | `\` |  `cd MyName\Desktop\HMMA238`    |
| List directory contents  | `ls`           |                | `dir`      |      |
| List hidden files  | `ls -a`           |                | `dir /aa`    |      |
| information about a command | `man` or `--help` |    `man ls`        | `/?` | `dir /?`  |
| print all the defined environment | `printenv`     |                | `SET`      |      |
| Clear screen  | `clear`        |                | `cls`      |      |
| print working directory | `pwd`          |                | `chdir`    |      |
| create new directory  |  `mkdir`       | `mkdir newrepo`  | `md`       | `md newrepo` |
| create new file  | `touch`        |  `touch foo.py`  | `type null >>` | `type nul >> foo.py`     |
| delete a file    | `rm`           |    `rm foo.py`   | `del`      | `del foo.py` |
| prints lines of a file matching a pattern | `grep`         |    `grep someword foo.py`   | `find` | `find "someword" foo.py`[^1] |
| create symbolic link | `ln`         |        | `mklink` |          |
| change the permissions of file | `chmod`         |        | `attrib` |         |


[^1]: Quotes are important !


***
## Notes

- Using Unix, if you want to, say, change directory to a directory whose name contains a space, you must include a `\` before the space, othewise it wont be recognized. You don't have to do that if you're using Windows.

- Pattern matching works pretty much the same under Windows, but someone who would run into trouble could take a look [here](https://docs.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-crp-reg-expressions) for more information.

- Some additional documentation can be found [here](http://www.yolinux.com/TUTORIALS/unix_for_dos_users.html) (english) or [there](http://archive.download.redhat.com/pub/redhat/linux/7.1/it/doc/RH-DOCS/fr/rhl-gsg-fr-7.1/ch-doslinux.html) (french).


***

This documentis neither exhaustive nor perfect, anyone who wants to help improve it is welcome. 


