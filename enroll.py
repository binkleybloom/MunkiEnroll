#!/usr/bin/env python

import cgitb, cgi, plistlib, os

repoPath = "/var/www/html"
f = open('template.plist', 'rb')
templatePlist = plistlib.readPlist(f)

cgitb.enable()

form = cgi.FieldStorage()
print "Content-Type: text/html"
print

def processSubmitted(getName):
   targetPlist = repoPath + "/manifests/" + getName + ".plist"
   if not os.path.isfile(targetPlist):
      f = open(targetPlist, 'wb')
      plistlib.writePlist(templatePlist, f)
      f.close
   else:
      print "Manifest already exists. Exiting."

if 'Name' in form.keys():
   getName = form.getfirst("Name")
   processSubmitted(getName)
else:
   print "Name was not specified. Exiting."
