#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <bitbar.title>Zoom</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Andras Helyes</bitbar.author>
# <bitbar.author.github>helyes</bitbar.author.github>
# <bitbar.desc>Join zoom meeting</bitbar.desc>
# <bitbar.image>https://github.com/helyes/bitbar-plugins/raw/master/aws-opsworks-ssh/bitbar-image-aws-opsworks-ssh.py.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/helyes/bitbar-plugins/blob/master/aws-opsworks-ssh/aws-opsworks-ssh.py</bitbar.abouturl>
# ./aws-opsworks-ssh/aws-opsworks-ssh.py

import json
import os

# 32X32 dpi144
MENUBAR_IMAGE="| templateImage=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"

CONFIG_FILE=os.getenv("HOME") + "/.config/bitbar/zoom/zoom.json"

# static menu - print here, show it regardless if error raised below
print MENUBAR_IMAGE
print "---"

def initConfig():
  configExample="""{
  "config" : {
    "zoomexecutable" : "/Users/john/zoom.applescript",
    "editor" : "/usr/local/bin/code",
    "editor_app_example": "open -a TextEdit"
  },
  "rooms" : [
    {
      "name": "Standup",
      "id": "1234567890",
      "WARNING": "Space is not supported in user name",
      "user": "John",
      "password": "123456"
    },
    {
      "name": "Planning",
      "id": "1234567890",
      "user": "John",
      "password": "123456"
    } 
  ]
  }"""
  try:
    configFolder=os.path.dirname(CONFIG_FILE)
    if not os.path.exists(configFolder):
      os.makedirs(configFolder)
  except OSError:
    print ("Could not create directory %s" % configFolder)
  configFile = open(CONFIG_FILE, "at")
  configFile.write(configExample)
  configFile.close()

if not os.path.exists(CONFIG_FILE):
  initConfig()

def loadConfig():
  try:
    with open(CONFIG_FILE, 'r') as f:
      content =f.read()
      return json.loads(content)
  except IOError:
      print 'Cannot open config file: ' + CONFIG_FILE
  except ValueError:
      print 'Cannot parse config file: ' + CONFIG_FILE

CONFIG=loadConfig()
EDIT_CONFIG_COMMAND=CONFIG["config"]["editor"] + " " + CONFIG_FILE

for roomConfig in CONFIG["rooms"]:
  command = "%s --room=%s --user=%s --password=%s" % (CONFIG["config"]["zoomexecutable"], roomConfig["id"], roomConfig["user"], roomConfig["password"])
  print roomConfig["name"] + " | bash='/bin/bash' param1='-c' param2='%s' terminal=false" % (command)

print "---"
print "Edit config | bash='/bin/bash' param1='-c' param2='%s' terminal=false" % (EDIT_CONFIG_COMMAND)
print "Reload config | terminal=false refresh=true"
