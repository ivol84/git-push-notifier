#!/usr/bin/python

import json
import subprocess
import notify2


def loadConfig():
    "Loads config from file"
    with open('config.json') as config_file:
        return json.load(config_file)


def isRepositoryNotPushed(folder):
    "Check repository for not pushed modifications"
    p = subprocess.check_output(['git', 'status'], cwd=folder)
    return p.decode("utf-8").find("Your branch is ahead of ") != -1


def showNotification(roots):
    notify2.init("Git Notifier")
    n = notify2.Notification(
        "Not pushed branches",
        str.join('\n', roots),
        "notification-message-im"   # Icon name
    )
    n.show()


# Load config
config = loadConfig()
notPushedRoots = []
for folder in config["folders"]:
    if isRepositoryNotPushed(folder):
        notPushedRoots.append(folder)
showNotification(notPushedRoots)
