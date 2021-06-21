# SublimeText Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restrart Nautilus, and enjoy :)
#
# This script was initially written by cra0zy for VsCode and is released to the public domain
# It has been adapted by atutorme for SublimeText

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to subl
SUBL = 'subl'

# what name do you want to see in the context menu?
SUBLNAME = 'SublimeText'

# always create new window?
NEWWINDOW = False


class SublimeTextExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_subl(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of subl
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(SUBL + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name='SublimeTextOpen',
            label='Open In ' + SUBLNAME,
            tip='Opens the selected files with SublimeText'
        )
        item.connect('activate', self.launch_subl, files)

        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name='SublimeTextOpenBackground',
            label='Open in ' + SUBLNAME,
            tip='Opens SublimeText in the current directory'
        )
        item.connect('activate', self.launch_subl, [file_])

        return [item]
