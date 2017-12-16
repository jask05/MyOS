# My Own Scripts (MyOS)

> Personal script compilation that I want to share with you.


## Bash folder

I copy these scripts under profile.d folder (**/etc/profile.d**) so that all users can use them.

#### 00-cpts.sh *filename* *destination-folder*
**Explanation**
> 
> This function copy a specific file under a folder and add a timestamp as a prefix. It uses **cp** with *-r, -v, -f* and *-p* parameters.
 
**How to use it**
> 
> cpts file.txt /home/user/
 
**Example**
> 
> cpts access.log /home/
'access.log' -> '/home/access.log_20171216041456'
