# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import time
import webbrowser
from PyQt4 import QtCore
import urllib2

import config

#output

def get_item(the_page, name):
    s = the_page.find(name+":")
    if s != -1:
        s = s + len(name)+1
        e = the_page.find("<br/>", s)
        if e != -1:
            return the_page[s: e]
    return ''

def checkup():
    has_update = False
    try:
        req = urllib2.Request(config.check_update_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
    except:
        return (has_update, '', '', '', '', '', '')

    sns = get_item(the_page, "sn")
    if sns:
        sn_set = set()
        sn_set.update(sns.split(';'))
        try:
            f = open(config.check_update_file)
            old_sns = f.read()
            sn_set.update(old_sns.split(';'))
        except IOError:
            pass
        f = open(config.check_update_file, "w")
        f.write(';'.join(list(sn_set)))
        f.close()

    prog_name = get_item(the_page, "prog_name")

    if prog_name == config.program_full_name:
        revision = int(get_item(the_page, "revision"))
        version = get_item(the_page, "version")
        required_mini_revision = int(get_item(the_page, "required_mini_revision"))
        url = get_item(the_page, "url")
        download_url = get_item(the_page, "download_url")
        if required_mini_revision <= config.revision < revision:
            has_update = True
    return (has_update, prog_name, version, revision, required_mini_revision, url, download_url)

class CheckupThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        has_update, prog_name, version, revision, required_mini_revision, url, download_url = checkup()
        if has_update:
            self.emit(QtCore.SIGNAL("newversion"), prog_name, version, revision, required_mini_revision, url, download_url)

# ----------------------------------------------------------------------------
# subprocess.terminate is not implemented on some Windows python versions.
# This workaround works on both POSIX and Windows.

if __name__ == "__main__":
    the_page = """<html>
        <head>
            <title>Hibosoft Batch Image Resizer Update Configuration</title>
        </head>
        <body>
            prog_name:Hibosoft Batch Image Resizer<br/>
            version:3.1.4.290<br/>
            revision:290<br/>
            url:http://www.hibosoft/product/hibosoft-batch-image-resizer/<br/>
            download_url:http://www.hibosoft/download/hibosoft-batch-image-resizer/<br/>
            required_mini_revision:200<br/>
            sn:aaa;aaa;aaa;<br/>
        </body>
    </html>
    """

    for name in ("prog_name", "version", "revision", "url", "download_url", "required_mini_revision", "sn",):
        value = get_item(the_page, name)
        print 'name, value=', name, ',', value
