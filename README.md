# My Own Scripts (MyOS)

> Personal script compilation that I want to share with you.


## Bash folder

I copy these scripts under profile.d folder (**/etc/profile.d**) so that all users can use them.
If you want to use it in the same session without restart the system or session, you have to execute:

~~~~
$ source /etc/profile.d/<script-name>
~~~~

#### :arrow_forward: 00-cpts.sh
**Explanation**
>
> This function copy a specific file under a folder and add a timestamp as a prefix. It uses **cp** with *-r, -v, -f* and *-p* parameters.

**How to use it**

~~~~
$ cpts file_to_copy destination_folder
$ cpts access.log /home/
'access.log' -> '/home/access.log_20171216041456'
~~~~

#### :arrow_forward: 00-cpts.sh
**Explanation**
>
> This function copy a specific file under a folder and add a timestamp as a prefix. It uses **cp** with *-r, -v, -f* and *-p* parameters.

**How to use it**

~~~~
$ cpts file_to_copy destination_folder
$ cpts access.log /home/
'access.log' -> '/home/access.log_20171216041456'
~~~~
