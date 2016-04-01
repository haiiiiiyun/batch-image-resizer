# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os,  sys

if sys.platform == 'darwin':
    #REF: http://stackoverflow.com/questions/3498313/how-to-trigger-from-python-playing-of-a-wav-or-mp3-audio-file-on-a-mac
    import subprocess
    #audio_file = "/full/path/to/audio.wav"
    play_sound_fun = lambda sound_full_path: subprocess.call(["afplay", sound_full_path])
    #def play_sound_fun(sound_full_path):
        #print '\a'

    #REF: http://patternbuffer.wordpress.com/2008/03/15/play-mp3-from-python-on-mac/ and 
    #     http://www.cocoabuilder.com/archive/cocoa/212226-nssound-won-play-wave-files.html
elif sys.platform.startswith('win'):
    import winsound as sound
    play_sound_fun = lambda sound_full_path: sound.PlaySound(sound_full_path, sound.SND_FILENAME|sound.SND_ALIAS)

if __name__ == '__main__':
    # We cannot rely on __file__, because __file__ is not there in the py2exed main-script.
    def we_are_frozen():
        """Returns whether we are frozen via py2exe.
        This will affect how we find out where we are located."""
        return hasattr(sys, "frozen")

    def module_path():
        """ This will get us the program's directory,
        even if we are frozen using py2exe"""

        if we_are_frozen():
            return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))

        return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

    path = module_path()
    sound_full_path = os.path.join(path, 'click.wav')
    play_sound_fun(sound_full_path)

