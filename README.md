GmailBackup
===========

A Gmail backup system in python.
Just' in case of Zombie Attack or Google explusion.

## Configuration
### File configuration
You need to change `username`, `password` and `directory` in `__configuration__.py`

### Command line
Or if you prefer, you can use with arguments (just remove the file `__configuration__.py`)
	> ```
	gmail.py username password directory
	```

### Crontab
Do not forget to add the script in a crontab task ;-)

	crontab -e

And add, for example :

	###################################################
	# GMAIL BACKUP
	###################################################
	0 */2 * * * python /home/you/.../gmail.py


## Protect your password
There isn't a good way to keep your password account secret. It's saved in clear text.
But I recommand to use a unique password for this application only and not your own password.
So you can revoque the password when you want.
See [Application-specific password required](https://support.google.com/mail/answer/117327) form Google pages
