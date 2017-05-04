# About
This little home-made script allows to automate checking of not pushed changes. To run it you should execute `python3 notifier.py`. You can add it to scheduler to automate process.
# Pre-requirements
You need to have python3 and python3-notify2 installed in your system. Modify config.json to actual folders, that you plan to check.
I check it only in Linux Mint, so feel free to modify it for your OS.

# Run thrue cron
Add folowing line to your crontab (you can use `crontab -e` command):
```
* * * * * env DISPLAY=:0 /usr/bin/python3 /full/path/git_notifier/notifier.py
```
