#!/usr/bin/env python2
import os
import sys

from PIL import Image
import winfiletime

def process(**kwargs):
    src_file = kwargs.get("src_file")
    dest_file = kwargs.get("dest_file")
    width = kwargs.get("width")
    height = kwargs.get("height")
    mode = kwargs.get("mode")
    keep_datetime = kwargs.get("keep_datetime")

    im = Image.open(src_file)
    try:
        im.load() # the image missing some trailing bytes will raise IOError image file is truncated error, and we should call load again
    except IOError: # image file is truncated error
        im.load()
    if mode == "Set Width & Height in Pixels":
        w = int(width)
        h = int(height)
    elif mode == "Set Width in Pixels, Height Keep Ratio":
        (ow,oh) = im.size
        w = int(width)
        h = w*(oh*1.0/ow)
    elif mode == "Set Height in Pixels, Width Keep Ratio":
        (ow,oh) = im.size
        h = int(height)
        w = h*(ow*1.0/oh)
    elif mode == "Set Width & Height in Percentage":
        (ow,oh) = im.size
        w = ow*(float(width)/100.0)
        h = oh*(float(height)/100.0)
    elif mode == "Set Width in Percentage, Height Keep Ratio":
        (ow,oh) = im.size
        w = ow*(float(width)/100.0)
        h = oh*(float(width)/100.0)
    elif mode == "Set Height in Percentage, Width Keep Ratio":
        (w,h) = im.size
        h = oh*(float(height)/100.0)
        w = ow*(float(height)/100.0)
    else:
        return False

    w, h = int(w),int(h)
    try:
        iout = im.resize((w,h), Image.ANTIALIAS)
        iout.save(dest_file)
    except IOError: # image file is truncated error
        print 'w,h=', w, ', ', h, ' file ', src_file, ' truncated'
        return False

    if keep_datetime:
        if sys.platform == "darwin":
            pass
        else:
            winfiletime.setfiletime(dest_file, *winfiletime.getfiletime(src_file))
    return True

if __name__ == '__main__': 
    pass
