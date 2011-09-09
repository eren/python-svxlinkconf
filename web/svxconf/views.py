#!/usr/bin/python
# -*- coding: utf-8 -*-

from svxconf.wrapper import render_response

import comar

def home(request):
    data = {"css_link_main": "active"}
    return render_response(request, "home.html", data)

def about(request):
    data = {"css_link_about": "active"}
    return render_response(request, "about.html", data)


def restart(request):
    print
