GmailBackup
===========

A Gmail backup system in python.
Just' in case of Zombie Attack or Google explusion.

## Configuration
### File configuration
You need to change `username`, `password` and `directory` in `\_\_configuration\_\_.py`

### Command line
Or if you prefer, you can use with arguments (just remove the file `\_\_configuration\_\_.py`)
	> ```
	gmail.py username password directory
	```


## Protect your password
There isn't a good way to keep your password account secret. It's saved in clear text.
But I recommand to use a unique password for this application only and not your own password.
So you can revoque the password when you want.
See [Application-specific password required](https://support.google.com/mail/answer/117327) form Google pages
