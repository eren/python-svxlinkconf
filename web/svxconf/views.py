#!/usr/bin/python
# -*- coding: utf-8 -*-

from svxlinkconf import SvxlinkConf, \
                        SvxlinkTypeNet

from svxconf.wrapper import render_response
from svxconf.forms import NewNodeForm

def home(request):
    conf = SvxlinkConf("/home/eren/sourcebox/github/svxlinkconf/etc/svxlink.conf")

    # FIXME: Use some kind of "get_voter()" function to select Voter
    # section. Hardcoding the section is not a good way.

    # FIXME: I assume that Voter and Multi TYPEs include only remote
    # nodes. Local sound devices can also be here. I'm omiting this fact
    # for now and treating all the nodes as TYPE=Net
    r = conf.get_section("MultiRx")
    receivers = map(lambda x: SvxlinkTypeNet(x, conf.config.items(x)), \
            r["RECEIVERS"].split(","))

    t = conf.get_section("MultiTx")
    transmitters = map(lambda x: SvxlinkTypeNet(x, conf.config.items(x)), \
            t["TRANSMITTERS"].split(","))

    rx_output = []
    # iterate over receivers, control if they are online and produce
    # output for the use of template
    for i in receivers:
        rx_output.append({"name": i.get_section_name(),
                            "is_online": i.is_online()})

    tx_output = []
    for i in transmitters:
        tx_output.append({"name": i.get_section_name(),
                            "is_online": i.is_online()})

    print rx_output

    data = {"css_link_main": "active",
            "receivers": rx_output,
            "transmitters": tx_output}




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
            node = SvxlinkTypeNet(form.cleaned_data["node_name"])
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
                conf = SvxlinkConf("/etc/svxlink/svxlink.conf")
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
