#!/usr/bin/env python3

import eyed3    # MP3 Tag Lib
import os       # Operating System Lib
from tkinter import messagebox

from GuiClass import *
from general import *


def mp3_edit_dir(input_path):
    """
    Function that runs on directories and sub directories and executes MP3 Tag edits
    :param input_path: String - Path to a folder on which editing will be performed
    """
    for dir_path, dirs, files in os.walk(input_path):
        for file_path in files:
            mp3_tag_edit(os.path.join(dir_path, file_path))


def execute_cmd(gui, chosen_method):
    """
    Function that manages all options that can be received from GUI
    :param gui: GuiClass - Object
    :param chosen_method: int - value that represents the chosen action
    """
    # When Choosing a Folder
    if chosen_method == FOLDER:
        input_path = gui.open_folder("Select a MP3 music folder")
        debug_print(input_path, DEBUG)
        if input_path != "" and str(input_path) != "()":
            mp3_edit_dir(input_path)
            messagebox.showinfo(PROJECT_FULL_NAME, "Your files were fully edited.")
    # When Choosing a file
    elif chosen_method == FILE:
        input_path = gui.open_file("Select a MP3 music file")
        debug_print(input_path, DEBUG)
        # When Path is loaded, Edit MP3 Tag
        if input_path != "" and str(input_path) != "()":
            mp3_tag_edit(input_path)
            messagebox.showinfo(PROJECT_FULL_NAME, "Your file was fully edited.")
    elif chosen_method == ABOUT:
        messagebox.showinfo(PROJECT_FULL_NAME, PROJECT_ABOUT_MSG)
    else:
        sys.exit()


def lunch_gui():
    """
     Lunch program in using GUI
    """
    gui = GuiClass(True, PROJECT_FULL_NAME)
    gui.view_gui()

    while True:
        chosen_method = gui.get_chosen_val()
        execute_cmd(gui, chosen_method)


def lunch_cli():
    """
    Lunch program using CLI
    """
    decorate_header(PROJECT_FULL_NAME)
    input_path = input("Please enter a full path to the MP3 file / Folder you want to change:\n")

    file_match = input_path.find('.mp3')
    debug_print(file_match, DEBUG)
    # When editing a MP3 File
    if file_match != -1:
        mp3_tag_edit(input_path)
        print("Your file was fully edited.")
    # When editing a MP3 Folder
    else:
        debug_print(input_path, DEBUG)
        mp3_edit_dir(input_path)
        print("Your files were fully edited.")


def mp3_tag_edit(file_path):
    debug_print(file_path, DEBUG)
    file_name = os.path.basename(file_path)  # Get the string after the last "/"
    debug_print(file_name, DEBUG)
    try:
        id3info = eyed3.load(file_path)
        artist = file_name.split(" - ")[0]  # Splitting Artist
        debug_print(artist, DEBUG)
        title = file_name.split(" - ")[1]  # Splitting Title.MP3
        title = title[0:title.index('.mp3')]  # Splitting the title by searching the position of ".mp3"
        debug_print(title, DEBUG)
        id3info.tag.title = str(title)
        id3info.tag.artist = str(artist)
        id3info.tag.comment = u""
        id3info.tag.genre = u"Other"
        id3info.tag.lyrics.remove(u"")
        id3info.tag.images.remove(u"")
        id3info.tag.save(encoding="utf16")  # UTF 16 Enabled in order to edit songs which are not in English.
    except IndexError or ValueError:
        print_exception(DEBUG)
        print("Can not change file: " + file_name)


def debug_print(print_var, debug_constant):
    if debug_constant:
        print(print_var)


def main():
    if GUI:
        lunch_gui()
    else:
        lunch_cli()

if __name__ == "__main__":
    main()
