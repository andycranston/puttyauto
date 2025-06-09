#
# @(!--#) @(#) charmap-util.py, version 001, 08-june-2025
#
# read in a bit map with the following printable ASCCI characters:
#
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#
# and print on stdout the cmap array definitions     
# 

#########################################################################

import sys
import os
import argparse
from PIL import Image

#########################################################################

def validwideortall(s):
    if len(s) == 0:
        return False
    
    for c in s:
        if not c.isdigit():
            return False

    n = int(s)
    
    if (n < 4) or (n > 99):
        return False
    
    return True

#########################################################################

def checkbitmapfilename(bitmapfilename):
    global progname
    
    if len(bitmapfilename) < 5:
        print('{}: bitmap filename "{}" is too short'.format(progname, bitmapfilename), file=sys.stderr)
        sys.exit(2)
        
    if not bitmapfilename.lower().endswith('.bmp'):
        print('{}: bitmap filename "{}" does not end with a .bmp suffix'.format(progname, bitmapfilename), file=sys.stderr)
        sys.exit(2)
    
    basename = bitmapfilename[:-4]
    
    pieces = basename.split('_')
    
    if len(pieces) < 3:
        print('{}: bitmap filename "{}" does not have width and tall values between underscore ("_") characters'.format(progname, bitmapfilename), file=sys.stderr)
        sys.exit(2)
    
    widepiece = pieces[-2]
    tallpiece = pieces[-1]

    if not validwideortall(widepiece):
        print('{}: bitmap filename "{}" has an invalid width value "{}"'.format(progname, bitmapfilename, widepiece), file=sys.stderr)
        sys.exit(2)
        
    if not validwideortall(tallpiece):
        print('{}: bitmap filename "{}" has an invalid tall value "{}"'.format(progname, bitmapfilename, tallpiece), file=sys.stderr)
        sys.exit(2)
    
    return int(widepiece), int(tallpiece)

#########################################################################

def main():
    global progname
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('bitmap', help='bitmap filename')
    
    args = parser.parse_args()
    
    bitmapfilename = args.bitmap
    
    widevalue, tallvalue = checkbitmapfilename(bitmapfilename)
    
    try:
        bitmap = Image.open(bitmapfilename)
    except FileNotFoundError:
        print('{}: cannot open file "{}" for reading'.format(progname, bitmapfilename), file=sys.stderr)
        sys.exit(2)
    
    
    print('')
    print('cmap = {}')
    print('')
    
    cmap = {}
    
    for c in range(32, 127):
        s = ''
        
        for tall in range(0, tallvalue):
            for wide in range(0, widevalue):
                x = ((c - 32) * widevalue) + wide
                y = tall
                rgb = bitmap.getpixel((x, y))
                if rgb == 0:
                    s += '0'
                else:
                    s += '1'

        if (s in cmap):
            print('ERROR: duplicate "{}"'.format(s), file=sys.stderr)
            sys.exit(1)

        cmap[s] = c

        print('cmap[\'{}\'] = {}'.format(s, c))
        
    print('')

    return 0

##########################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file: charmap-util.py