#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class NewNodeForm(forms.Form):
    node_name = forms.CharField(label="Uzak İstemci Adı",
                                max_length=30)

    ip_address = forms.IPAddressField(label="IP Adresi")

    port = forms.DecimalField(label="Port",
                              initial="5220")

    auth_key = forms.CharField(label="Kimlik Doğrulama Anahtarı")

