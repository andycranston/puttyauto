#
# @(!--#) puttyauto.py, version 015, 09-june-2025
#
# automate a putty session
#
# Tested on:
#
#    Windows 10 Home - Version 2009 - OS Build 19045.5854
#    Python - version 3.9.13
#    PyAutoGUI - version 0.9.53
#    
#
# tested with PuTTY version 0.83 - download from:
#
#    https://www.chiark.greenend.org.uk/~sgtatham/putty/releases/0.83.html
#
# set the following settings:
#
# Window:   Columns: 80   Rows: 24
# Window:
#     Appearance:   Font: Fixedsys, 12-point
# Window:
#     Colours:   Default Background: RGB value: red 0 green 0 blue 0
#

########################################################################
# 3456789012345678901234567890123456789012345678901234567890123456789012
########################################################################

import os
import sys
import time
import datetime
import argparse
import pyautogui
from PIL import Image

########################################################################

CMAP_WIDE = 8
CMAP_TALL = 15

cmap = {}

cmap['000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'] = 32
cmap['000000000000000000000000000110000011110000111100001111000001100000011000000000000001100000011000000000000000000000000000'] = 33
cmap['000000000000000000000000011001100110011001100110000000000000000000000000000000000000000000000000000000000000000000000000'] = 34
cmap['000000000000000000000000001101100011011001111111001101100011011000110110011111110011011000110110000000000000000000000000'] = 35
cmap['000000000001100000011000001111000110011001100000001100000001100000001100000001100110011000111100000110000001100000000000'] = 36
cmap['000000000000000001110000110110001101101001110110000011000001100000110000011011100101101100011011000011100000000000000000'] = 37
cmap['000000000000000000000000001110000110110001101100001110000110000001101111011001100110011000111011000000000000000000000000'] = 38
cmap['000000000000000000000000000110000001100000011000000000000000000000000000000000000000000000000000000000000000000000000000'] = 39
cmap['000000000000000000000000000011000001100000011000001100000011000000110000001100000011000000011000000110000000110000000000'] = 40
cmap['000000000000000000000000001100000001100000011000000011000000110000001100000011000000110000011000000110000011000000000000'] = 41
cmap['000000000000000000000000000000000000000000110110000111000111111100011100001101100000000000000000000000000000000000000000'] = 42
cmap['000000000000000000000000000000000000000000011000000110000111111000011000000110000000000000000000000000000000000000000000'] = 43
cmap['000000000000000000000000000000000000000000000000000000000000000000000000000000000001110000011100000011000001100000000000'] = 44
cmap['000000000000000000000000000000000000000000000000000000000111111000000000000000000000000000000000000000000000000000000000'] = 45
cmap['000000000000000000000000000000000000000000000000000000000000000000000000000000000001110000011100000000000000000000000000'] = 46
cmap['000000000000000000000000000001100000011000001100000011000001100000011000001100000011000001100000011000000000000000000000'] = 47
cmap['000000000000000000000000000111100011001100110111001101110011001100111011001110110011001100011110000000000000000000000000'] = 48
cmap['000000000000000000000000000011000001110001111100000011000000110000001100000011000000110000001100000000000000000000000000'] = 49
cmap['000000000000000000000000001111000110011001100110000001100000110000011000001100000110000001111110000000000000000000000000'] = 50
cmap['000000000000000000000000001111000110011001100110000001100001110000000110011001100110011000111100000000000000000000000000'] = 51
cmap['000000000000000000000000001100000011000000110110001101100011011001100110011111110000011000000110000000000000000000000000'] = 52
cmap['000000000000000000000000011111100110000001100000011000000111110000000110000001100000110001111000000000000000000000000000'] = 53
cmap['000000000000000000000000000111000001100000110000011111000110011001100110011001100110011000111100000000000000000000000000'] = 54
cmap['000000000000000000000000011111100000011000001100000011000001100000011000001100000011000000110000000000000000000000000000'] = 55
cmap['000000000000000000000000001111000110011001100110011101100011110001101110011001100110011000111100000000000000000000000000'] = 56
cmap['000000000000000000000000001111000110011001100110011001100110011000111110000011000001100000111000000000000000000000000000'] = 57
cmap['000000000000000000000000000000000000000000011100000111000000000000000000000000000001110000011100000000000000000000000000'] = 58
cmap['000000000000000000000000000000000000000000011100000111000000000000000000000000000001110000011100000011000001100000000000'] = 59
cmap['000000000000000000000000000001100000110000011000001100000110000000110000000110000000110000000110000000000000000000000000'] = 60
cmap['000000000000000000000000000000000000000000000000011111100000000001111110000000000000000000000000000000000000000000000000'] = 61
cmap['000000000000000000000000011000000011000000011000000011000000011000001100000110000011000001100000000000000000000000000000'] = 62
cmap['000000000000000000000000001111000110011001100110000011000001100000011000000000000001100000011000000000000000000000000000'] = 63
cmap['000000000000000000000000011111101100001111000011110011111101101111011011110011111100000001111111000000000000000000000000'] = 64
cmap['000000000000000000000000000110000011110001100110011001100110011001111110011001100110011001100110000000000000000000000000'] = 65
cmap['000000000000000000000000011111000110011001100110011001100111110001100110011001100110011001111100000000000000000000000000'] = 66
cmap['000000000000000000000000001111000110011001100110011000000110000001100000011001100110011000111100000000000000000000000000'] = 67
cmap['000000000000000000000000011110000110110001100110011001100110011001100110011001100110110001111000000000000000000000000000'] = 68
cmap['000000000000000000000000011111100110000001100000011000000111110001100000011000000110000001111110000000000000000000000000'] = 69
cmap['000000000000000000000000011111100110000001100000011000000111110001100000011000000110000001100000000000000000000000000000'] = 70
cmap['000000000000000000000000001111000110011001100110011000000110000001101110011001100110011000111110000000000000000000000000'] = 71
cmap['000000000000000000000000011001100110011001100110011001100111111001100110011001100110011001100110000000000000000000000000'] = 72
cmap['000000000000000000000000001111000001100000011000000110000001100000011000000110000001100000111100000000000000000000000000'] = 73
cmap['000000000000000000000000000001100000011000000110000001100000011000000110011001100110011000111100000000000000000000000000'] = 74
cmap['000000000000000000000000011001100110011001101100011011000111100001101100011011000110011001100110000000000000000000000000'] = 75
cmap['000000000000000000000000011000000110000001100000011000000110000001100000011000000110000001111110000000000000000000000000'] = 76
cmap['000000000000000000000000011000110110001101110111011010110110101101101011011000110110001101100011000000000000000000000000'] = 77
cmap['000000000000000000000000011000110110001101110011011110110110111101100111011000110110001101100011000000000000000000000000'] = 78
cmap['000000000000000000000000001111000110011001100110011001100110011001100110011001100110011000111100000000000000000000000000'] = 79
cmap['000000000000000000000000011111000110011001100110011001100111110001100000011000000110000001100000000000000000000000000000'] = 80
cmap['000000000000000000000000001111000110011001100110011001100110011001100110011001100110011000111100000011000000011000000000'] = 81
cmap['000000000000000000000000011111000110011001100110011001100111110001101100011001100110011001100110000000000000000000000000'] = 82
cmap['000000000000000000000000001111000110011001100000001100000001100000001100000001100110011000111100000000000000000000000000'] = 83
cmap['000000000000000000000000011111100001100000011000000110000001100000011000000110000001100000011000000000000000000000000000'] = 84
cmap['000000000000000000000000011001100110011001100110011001100110011001100110011001100110011000111100000000000000000000000000'] = 85
cmap['000000000000000000000000011001100110011001100110011001100110011001100110011001100011110000011000000000000000000000000000'] = 86
cmap['000000000000000000000000011000110110001101100011011010110110101101101011001101100011011000110110000000000000000000000000'] = 87
cmap['000000000000000000000000011001100110011000110100000110000001100000101100011001100110011001100110000000000000000000000000'] = 88
cmap['000000000000000000000000011001100110011001100110011001100011110000011000000110000001100000011000000000000000000000000000'] = 89
cmap['000000000000000000000000011111100000011000000110000011000001100000110000011000000110000001111110000000000000000000000000'] = 90
cmap['000000000000000000000000001111000011000000110000001100000011000000110000001100000011000000110000001100000011000000111100'] = 91
cmap['000000000000000000000000011000000110000000110000001100000001100000011000000011000000110000000110000001100000000000000000'] = 92
cmap['000000000000000000000000001111000000110000001100000011000000110000001100000011000000110000001100000011000000110000111100'] = 93
cmap['000000000001100000111100011001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'] = 94
cmap['000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111111'] = 95
cmap['000000000011100000011000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'] = 96
cmap['000000000000000000000000000000000000000000111100000001100000011000111110011001100110011000111110000000000000000000000000'] = 97
cmap['000000000000000000000000011000000110000001111100011001100110011001100110011001100110011001111100000000000000000000000000'] = 98
cmap['000000000000000000000000000000000000000000111100011001100110000001100000011000000110011000111100000000000000000000000000'] = 99
cmap['000000000000000000000000000001100000011000111110011001100110011001100110011001100110011000111110000000000000000000000000'] = 100
cmap['000000000000000000000000000000000000000000111100011001100110011001111110011000000110000000111100000000000000000000000000'] = 101
cmap['000000000000000000000000000111100011000000110000001100000111111000110000001100000011000000110000000000000000000000000000'] = 102
cmap['000000000000000000000000000000000000000000111110011001100110011001100110011001100110011000111110000001100000011001111100'] = 103
cmap['000000000000000000000000011000000110000001111100011001100110011001100110011001100110011001100110000000000000000000000000'] = 104
cmap['000000000000000000011000000110000000000001111000000110000001100000011000000110000001100001111110000000000000000000000000'] = 105
cmap['000000000000000000001100000011000000000000111100000011000000110000001100000011000000110000001100000011000000110001111000'] = 106
cmap['000000000000000000000000011000000110000001100110011001100110110001111000011011000110011001100110000000000000000000000000'] = 107
cmap['000000000000000000000000011110000001100000011000000110000001100000011000000110000001100001111110000000000000000000000000'] = 108
cmap['000000000000000000000000000000000000000001111110011010110110101101101011011010110110101101100011000000000000000000000000'] = 109
cmap['000000000000000000000000000000000000000001111100011001100110011001100110011001100110011001100110000000000000000000000000'] = 110
cmap['000000000000000000000000000000000000000000111100011001100110011001100110011001100110011000111100000000000000000000000000'] = 111
cmap['000000000000000000000000000000000000000001111100011001100110011001100110011001100110011001111100011000000110000001100000'] = 112
cmap['000000000000000000000000000000000000000000111110011001100110011001100110011001100110011000111110000001100000011000000110'] = 113
cmap['000000000000000000000000000000000000000001100110011011100111000001100000011000000110000001100000000000000000000000000000'] = 114
cmap['000000000000000000000000000000000000000000111110011000000110000000111100000001100000011001111100000000000000000000000000'] = 115
cmap['000000000000000000000000001100000011000001111110001100000011000000110000001100000011000000011110000000000000000000000000'] = 116
cmap['000000000000000000000000000000000000000001100110011001100110011001100110011001100110011000111110000000000000000000000000'] = 117
cmap['000000000000000000000000000000000000000001100110011001100110011001100110011001100011110000011000000000000000000000000000'] = 118
cmap['000000000000000000000000000000000000000001100011011010110110101101101011011010110011011000110110000000000000000000000000'] = 119
cmap['000000000000000000000000000000000000000001100110011001100011110000011000001111000110011001100110000000000000000000000000'] = 120
cmap['000000000000000000000000000000000000000001100110011001100110011001100110011001100110011000111100000011000001100011110000'] = 121
cmap['000000000000000000000000000000000000000001111110000001100000110000011000001100000110000001111110000000000000000000000000'] = 122
cmap['000000000000000000000000000011000001100000011000000110000011000001100000001100000001100000011000000110000000110000000000'] = 123
cmap['000000000000000000000000000110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000'] = 124
cmap['000000000000000000000000001100000001100000011000000110000000110000000110000011000001100000011000000110000011000000000000'] = 125
cmap['000000000000000000000000011100011101101110001110000000000000000000000000000000000000000000000000000000000000000000000000'] = 126

########################################################################

TIMEOUT = 10.0

SSH_PORT = "22"

POLL_INTERVAL = 0.5

PUTTY_EXECUTABLE_FILENAME = 'C:\\andyc\\projects\\puttyauto\\putty-0-83.exe'

PUTTY_CONFIG_ICON_FILENAME = 'puttyconfigicon.bmp'

PUTTY_LOGIN_ICON_FILENAME = 'puttyloginicon.bmp'

PUTTY_TERM_ICON_FILENAME = 'puttytermicon.bmp'

PUTTY_SECURITY_WARNING_FILENAME = 'puttysecuritywarning.bmp'

PUTTY_SECURITY_BUTTONS_FILENAME = 'puttysecuritybuttons.bmp'

PUTTY_STARTUP_DELAY = 2.0

########################################################################

def fatalerror(msg):
    global progname

    print('{}: {}'.format(progname, msg), file=sys.stderr)

    sys.exit(1)

########################################################################

def isassignment(line):
    lenline = len(line)

    if lenline < 3:
        return False

    equals = line.find('=')

    if equals == -1:
        return False

    if (equals < 1) or (equals >= (lenline -1)):
        return False

    return True    

########################################################################

def stripquotes(s):
    if len(s) >= 2:
        if (s[0] == '"') and (s[-1] == '"'):
            s = s[1:-1]
        elif (s[0] == "'") and (s[-1] == "'"):
            s = s[1:-1]

    return s
 
########################################################################

def parsevalue(v):
    envvar = ''

    if len(v) >= 3:
        if (v[0] == '[') and (v[-1] == ']'):
            envvar = v[1:-1]

    if envvar == '':
        return stripquotes(v)

    try:
        s = os.environ[envvar]
    except KeyError:
        return stripquotes(v)

    return s

########################################################################

def wordstring(line):
    line = line.strip()

    lenline = len(line)

    if lenline == 0:
        return '', ''

    words = line.split()

    if len(words) == 0:
        return '', ''

    word = words[0]

    i = len(word)

    while i < lenline:
        if (line[i] == ' '):
            i += 1
        else:
            break

    string = line[i:]

    return word, string
    
########################################################################

def waitfor(imagelist):
    global TIMEOUT
    global POLL_INTERVAL

    time.sleep(POLL_INTERVAL)

    starttime = time.time()

    while True:
        timenow = time.time()

        if (timenow - starttime) >= TIMEOUT:
            return -1, None

        index = 0
        for image in imagelist:
            region = pyautogui.locateOnScreen(image)

            if region != None:
                return index, region

            index += 1

########################################################################

def dragwindowtopleft(region, offsetx, offsety, backx, backy):
    pyautogui.mouseDown(region[0] + offsetx, region[1] + offsety)

    pyautogui.dragTo(backx, backy, 1, button='left')

    pyautogui.mouseUp()

    return

########################################################################

def dragconfigwindow(region):
    dragwindowtopleft(region, 50, 10, 59, 17)

    return

########################################################################

### def dragsecuritywarning(region):
###     dragwindowtopleft(region, 155, -52, 191, 13)
### 
###     return

########################################################################

def dragtermwindow(region):
    dragwindowtopleft(region, 350, -15, 352, 17)

    return

########################################################################

def fieldovertype(fieldx, fieldy, text):
    pyautogui.click(fieldx, fieldy, clicks=2)

    pyautogui.typewrite(text)
    
    return
    
########################################################################

def clickbutton(x, y):
    pyautogui.click(x, y)

    return

########################################################################

def clicksshbutton(region):
    clickbutton(region[0] + 173, region[1] + 162)

    return

########################################################################

def clickconfigopenbutton(region):
    clickbutton(region[0] + 313, region[1] + 424)

    return

########################################################################

def clickwarningnobutton(region):
    # 158   255
    clickbutton(region[0] - 150, region[1] + 10)

    return

########################################################################

def screenlines(includeblanks=True):
    global cmap

    puttyterm = pyautogui.screenshot(region = (2, 32, CMAP_WIDE * 80, CMAP_TALL * 24))
    
    width, height = puttyterm.size
    
    cols = width // CMAP_WIDE
    lines = height // CMAP_TALL

    asciilines = []
    
    for l in range(0, lines):
        asciichars = ''
        
        for c in range(0, cols):
            x = c * CMAP_WIDE
            y = l * CMAP_TALL
            
            ### print(x, y)
            
            s = ''
            
            for yy in range(0, CMAP_TALL):
                for xx in range(0, CMAP_WIDE):
                    rgb = puttyterm.getpixel( (x + xx, y + yy) )
                    
                    if rgb[0] == 0:
                        s += '0'
                    else:
                        s += '1'
                    
                    ### print(x + xx, y + yy, rgb)
            
            ### print(s)
            
            pchar = '?'
            
            if s in cmap:
                if (cmap[s] >= 32) and (cmap[s] <= 126):
                    pchar = chr(cmap[s])
            
            asciichars += pchar
        
        asciichars = asciichars.rstrip()

        if includeblanks == True:
            asciilines.append(asciichars)
        else:
            if asciichars != '':
                asciilines.append(asciichars)
            
    return asciilines

########################################################################

def waitlastline(matchlist):
    global TIMEOUT
    global POLL_INTERVAL

    if len(matchlist) == 0:
        return -1, None

    starttime = time.time()

    while True:
        time.sleep(POLL_INTERVAL)

        timenow = time.time()

        if (timenow - starttime) >= TIMEOUT:
            return -1, None

        lines = screenlines(includeblanks=False)

        if len(lines) > 0:
            lastline = lines[-1]

            index = 0

            while index < len(matchlist):
                tuple = matchlist[index]
                text = tuple[0]
                match = tuple[1]

                if match == 'match':
                    if lastline == text:
                        return index, text
                elif match == 'ends':
                    if lastline.endswith(text):
                        return index, text

                index += 1

########################################################################

def invokeputty(va):
    region = pyautogui.locateOnScreen(PUTTY_CONFIG_ICON_FILENAME)

    if region != None:
        fatalerror('one or more putty sessions appear to already be active')
        sys.exit(1)

    os.startfile(PUTTY_EXECUTABLE_FILENAME)

    index, region = waitfor([ PUTTY_CONFIG_ICON_FILENAME ])

    if index == -1:
        fatalerror('PuTTY session failed to start or is not visible on screen')

    # dragconfigwindow(region)
    
    portnumber = SSH_PORT
    
    if ':' in va['hostname']:
        hostandport = va['hostname'].split(':')
        va['hostname'] = hostandport[0]
        portnumber = hostandport[1]        

    fieldovertype(region[0] + 261, region[1] + 115, va['hostname'])

    fieldovertype(region[0] + 392, region[1] + 115, portnumber)

    clicksshbutton(region)

    clickconfigopenbutton(region)

    # pyautogui.moveTo(1, 1)

    index, region = waitfor([ PUTTY_LOGIN_ICON_FILENAME, PUTTY_SECURITY_WARNING_FILENAME ])

    # print(index)

    if index == -1:
        fatalerror('PuTTY terminal window or security warning window did not appear')

    # print(region)

    if index == 1:
        # pyautogui.moveTo(region[0], region[1])
        # dragsecuritywarning(region)
        clickwarningnobutton(region)

    # pyautogui.moveTo(1, 1)

    index, region = waitfor([ PUTTY_LOGIN_ICON_FILENAME ])

    if index == -1:
        fatalerror('PuTTY terminal window did not appear')

    dragtermwindow(region)

    usernamesent = False
    passwordsent = False

    while True:
        index, line = waitlastline([ ('login as:', 'ends'), (' password:', 'ends'), (va['prompt'], 'match') ])

        ### print(index)

        if index == -1:
            fatalerror('timeout related issue invoking putty')
        elif index == 0:
            if usernamesent:
                pass
            else:
                pyautogui.typewrite(va['username'])
                pyautogui.press('enter')
                usernamesent = True
        elif index == 1:
            if not 'password' in va:
                fatalerror('PuTTY asking for password when no password set in script file')
            if passwordsent:
                pass
            else:
                pyautogui.typewrite(va['password'])
                pyautogui.press('enter')
                passwordsent = True
        elif index == 2:
            break

    return

########################################################################

def screenshot(va):
    lines = screenlines()

    if len(lines) == 0:
        return

    tstamp = "{:%Y%m%d-%H%M%S}".format(datetime.datetime.now())

    sshotfilename = 'screenshot-{}-{}.txt'.format(va['hostname'], tstamp)

    try:
        sshotfile = open(sshotfilename, 'w', encoding='utf-8')
    except IOError:
        return

    for line in lines:
        print(line, file=sshotfile)

    sshotfile.flush()
    sshotfile.close()

    return

########################################################################

def main():
    global progname

    filelist = [ PUTTY_EXECUTABLE_FILENAME,
                 PUTTY_CONFIG_ICON_FILENAME,
                 PUTTY_LOGIN_ICON_FILENAME,
                 PUTTY_TERM_ICON_FILENAME,
                 PUTTY_SECURITY_WARNING_FILENAME ]

    for file in filelist:
        if not os.path.exists(file):
            fatalerror('cannot find/open file "{}"'.format(file))

    parser = argparse.ArgumentParser()
        
    parser.add_argument('script', help='script filename')
    parser.add_argument('--host', help='host name override', nargs=1)

    args = parser.parse_args()

    scriptfilename = args.script

    try:
        scriptfile = open(scriptfilename, 'r', encoding='utf-8')
    except IOError:
        fatalerror('cannot open script file "{}" for reading'.format(scriptfilename))

    if args.host:
        hostoverride = args.host[0]
    else:
        hostoverride = ''

    va = {}    # 'va' is variable array

    linenum = 0

    for line in scriptfile:
        linenum += 1

        line = line.rstrip()

        if line == '':
            continue

        if line[0:2] == ';;':
            continue

        words = line.split()

        lenwords = len(words)

        if lenwords == 0:
            continue

        word, string = wordstring(line)

        ### print('[{}] [{}]'.format(word, string))

        if isassignment(line):
            equals = line.find('=')
            varname = line[0:equals].rstrip()
            varvalue = line[equals+1:].lstrip()
            if varname != 'hostname':
                va[varname] = parsevalue(varvalue)
            else:
                if hostoverride != '':
                    va[varname] = hostoverride
                else:
                    va[varname] = parsevalue(varvalue)
        elif line == 'putty':
            if not 'hostname' in va:
                fatalerror('hostname not defined before "putty" line in script file')
            if not 'username' in va:
                fatalerror('username not defined before "putty" line in script file')
            if not 'prompt' in va:
                fatalerror('prompt not defined before "putty" line in script file')
            invokeputty(va)
        elif words[0] == 'cr':
            pyautogui.press('enter')
        elif word == 'send':
            string = stripquotes(string)
            if string != '':
                pyautogui.typewrite(string)
            pyautogui.press('enter')
        elif word == 'sendnocr':
            string = stripquotes(string)
            if string != '':
                pyautogui.typewrite(string)
        elif words[0] == 'sendvar':
            if lenwords >= 2:
                if words[1] in va:
                    pyautogui.typewrite(va[words[1]])
        elif words[0] == 'wait':
            if lenwords >= 2:
                if words[1] in va:
                    if lenwords >= 3:
                        comparison = words[2]
                    else:
                        comparison = 'match'
                    index, line = waitlastline([ (va[words[1]], comparison) ])
                    if index == -1:
                        fatalerror('wait command on line {} has timed out'.format(linenum))
        elif words[0] == 'sleep':
            if lenwords >= 2:
                time.sleep(float(words[1]))
        elif word == 'screenshot':
            screenshot(va)
        else:
            print('{}: line {} in script file "{}" cannot be processed:'.format(progname, linenum, scriptfilename), file=sys.stderr)
            print('        {}'.format(line), file=sys.stderr)        

    return 0

########################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file
