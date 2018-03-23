import linecache
import sys

# Title Options
PROJECT_NAME = "MP3 Tag Automation"
VERSION = "v1.0"
PROJECT_FULL_NAME = PROJECT_NAME + " " + VERSION

# General parameters for usage
DEBUG = False
GUI = True

# Enum for options that can be received from GUI
FOLDER = 0
FILE = 1
ABOUT = 2

PROJECT_ABOUT_MSG = PROJECT_FULL_NAME + "\n" \
                    + "Created on May,2013 by techyE \n\n" \
                    + "Organize your MP3 files by editing the headers inside the file. " \
                    + "Requires predefined conventions: \n<Artist> - <SongName>.mp3 \nin order " \
                    + "to work properly. "


def decorate_header(header, pattern="*"):
    """ CLI function to decorate words with a 
    certain pattern.
    """
    decoration = ""

    for i in range(len(header)):
        decoration += pattern

    print(decoration)
    print(header)
    print(decoration)
    print()


def print_exception(debug_const):
    if debug_const:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        line_num = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, line_num, f.f_globals).split("#")[0]
        print('Exception In:\n Line:   {} \n Error:  {} \n Reason: {}'.format(line_num, line.strip(), exc_obj))
