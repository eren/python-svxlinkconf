Python SvxlinkConf
==================

A library on the top of INIPARSE to manipulate Svxlink.conf file.

Requirements:

- python-iniparse

The code is in alpha stage right now but it's useful. I haven't decided
on naming scheme but as most of the open source projects use 0.1 for
initial release, we can call it in that way. Once I think that it's
enough, I will tag a new version. New version will be tagged when it's
ready :)

Description
------------

I have written this library to easily manipulate svxlink.conf file. The
main motivation was to easily configure MultiTx and MultiRx sections
because of the project I am working on. However, I thought that it would
be more appropriate to make the library extendable instead of limiting
myself. Right now, the code is easily extendable, and it abstracts ini
sections as python objects.

All the sections which have TYPE are represented by corresponding
SvxlinkType{xx} classes where xx is the name of the TYPE. These classes
inherit SvxlinkTypeContainer() object in which I define common methods
for each class.

The main advantadge of using python classes for every TYPE is that it
allows us to define TYPE-specific operations. For example, is_online()
method in SvxlinkTypeNet() checks if the host defined in this section is
reachable or not.

You manipulate the options in the section via SvxlinkType objects. For
example, to add new Net section, you can use the following code:


    conf = SvxlinkConf("foo/svxlink.conf")

    new_node = SvxlinkTypeNet("ExampleNode")
    new_node["host"] = 127.0.0.1
    new_node["tcp_port"] = 5210
    new_node["auth_key"] = '"test"'

    conf.add_section(new_node)
    conf.write()

    # you can as well get an SvxlinkType object. Say we have a TYPE=Net node
    # with the name of "foobar" we can get this by
    node = conf.get_section("foobar")

    # we can list every option that it has
    print node.items()

    # we can access its values
    print node["host"]


For another example, you can get TYPE=Net objects with:

    conf.get_remote_nodes()

it returns a list of SvxlinkTypeNet objects. You can, as well, access
its options the way that was written previously.

The code is self-documented. You can read the code for further
description.

Contributing
------------

1. Fork it.
2. Create a branch
3. Commit your changes
4. Push to the branch
5. Create an [Issue][1] with a link to your branch
6. Enjoy a refreshing Diet Coke and wait

[1]: http://github.com/eren/python-svxlinkconf/issues

Contact
-------

Eren Türkay (TA1AET) <eren ·--·-· pardus.org.tr>
