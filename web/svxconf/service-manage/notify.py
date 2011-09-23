#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyinotify
import sys
import datetime
import os

import comar

SERVICE_MANAGE_DIR = "/home/eren/sourcebox/github/svxlinkconf/web/svxconf/service-manage"
SVXLINK_CONFIG_DIR = "/home/eren/sourcebox/github/svxlinkconf/etc"
SVXLINK_CONF = "svxlink.conf"

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if event.pathname == os.path.join(SVXLINK_CONFIG_DIR, SVXLINK_CONF):

            now = datetime.datetime.now()
            print "[%s] Restarting svxlink server..." % now.strftime("%Y-%m-%d %H:%M")

            link = comar.Link()
            link.System.Service["svxlink"].stop()
            link.System.Service["svxlink"].start()

    def process_IN_ATTRIB(self, event):
        path = event.pathname
        link = comar.Link()

        if path == os.path.join(SERVICE_MANAGE_DIR, "START"):
            print "Starting svxlink server..."
            link.System.Service["svxlink"].start()

        elif path == os.path.join(SERVICE_MANAGE_DIR, "STOP"):
            print "Stopping svxlink server..."
            link.System.Service["svxlink"].stop()

        elif path == os.path.join(SERVICE_MANAGE_DIR, "RESTART"):
            print "Restarting svxlink server..."
            link.System.Service["svxlink"].stop()
            link.System.Service["svxlink"].start()

def main():
    # The watch manager stores the watches and provides operations on watches
    wm = pyinotify.WatchManager()
    handler = EventHandler()
    mask = pyinotify.IN_ATTRIB | pyinotify.IN_MODIFY

    notifier = pyinotify.Notifier(wm, handler)
    wm.add_watch(SVXLINK_CONFIG_DIR, mask)
    wm.add_watch(SERVICE_MANAGE_DIR, mask)

    #notifier.loop(daemonize=True, pid_file="/tmp/notify.pid", stdout="/tmp/notify.stdout.txt")
    notifier.loop()

if __name__ == '__main__':
    main()
