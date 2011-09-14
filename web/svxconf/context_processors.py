#!/usr/bin/python
# -*- coding: utf-8 -*-

import comar
import svxlinkconf

def is_svxlink_running(request):
    # FIXME: Other distros will need different ways of checking the
    # service. Code this part so that it is flexible

    link = comar.Link()
    service = link.System.Service["svxlink"].info()

    # dbus.String() is returned from here, we get the actual value with
    # .title() function
    service_status = service[2].title()

    if service_status == "Off":
        return {"is_svxlink_running": False}
    else:
        return {"is_svxlink_running": True}

def total_remote_nodes(request):
    conf = svxlinkconf.SvxlinkConf("/home/eren/sourcebox/github/svxlinkconf/etc/svxlink.conf")

    return {"total_remote_nodes": len(conf.get_remote_nodes())}

