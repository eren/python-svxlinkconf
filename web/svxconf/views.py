#!/usr/bin/python
# -*- coding: utf-8 -*-

import svxlinkconf

from svxconf.wrapper import render_response
from svxconf.forms import NewNodeForm

def home(request):
    data = {"css_link_main": "active"}
    return render_response(request, "home.html", data)

def about(request):
    data = {"css_link_about": "active"}
    return render_response(request, "about.html", data)


def node_new(request):
    """A view that presents an interface for adding new remotetrx nodes

    """
    if request.method == "POST":
        form = NewNodeForm(request.POST)
        data = {"form": form,
                "css_link_client": "active"}

        if not form.is_valid():
            return render_response(request, "node_new.html", data)
        else:
            # FIXME: check if the node_name (section name) is already
            # present. If so, emit an error

            # form is valid, go on!
            node = svxlinkconf.SvxlinkTypeNet(form.cleaned_data["node_name"])
            node["host"] = form.cleaned_data["ip_address"]
            node["tcp_port"] = int(form.cleaned_data["port"])
            node["auth_key"] = '"%s"' % form.cleaned_data["auth_key"]

            # codec is default
            node["codec"] = "GSM"

            # does the user want to just check te node? Then check it
            if request.POST.get("control"):
                if node.is_online():
                    data.update({"node_access_ok": 1})
                    return render_response(request, "node_new.html",
                                           data)
                else:
                    data.update({"node_access_error": 1})
                    return render_response(request, "node_new.html",
                            data)
            else:
                # now user wants to add the node
                conf = svxlinkconf.SvxlinkConf("/etc/svxlink/svxlink.conf")
                conf.add_section(node)
                conf.write("sample.conf")

                data.update({"node_name": form.cleaned_data["node_name"]})

                return render_response(request, "node_new_ok.html",
                        data)
    else:
        # handling GET
        form = NewNodeForm()
        data = {"form": form,
                "css_link_client": "active"}

        return render_response(request, "node_new.html", data)
