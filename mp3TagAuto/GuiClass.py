import tkinter
import tkinter.filedialog

from general import *


class GuiClass(object):
    """
    Class that encapsulates all the GUI processes required for mp3TagAuto
    """
    # Makes Sure that only the wanted GUI is open
    def __init__(self, view_main_block=False, block_title="Tk"):
        self.root = tkinter.Tk()
        self.root.title(block_title)
        if not view_main_block:
            self.root.withdraw()  # Eliminates the GUI Block.
        self.chosen_val = -1

    def close(self):
        """ Destroys the object """
        self.root.destroy()

    def open_folder(self, string):
        """ Open folder selection menu """
        return tkinter.filedialog.askdirectory(parent=self.root, initialdir=self.root, title=string)

    def open_file(self, string):
        """ Open file selection menu """
        return tkinter.filedialog.askopenfilename(initialdir=self.root, title=string)

    def view_gui(self):
        """
        Lunches GUI structure
        """

        def set_value(val):
            """
            Setting up the chosen value given from GUI
            :param val: int - representation of chosen value
            """
            self.chosen_val = val
            frame.quit()

        # create a menu
        menu = tkinter.Menu(self.root)
        self.root.config(menu=menu)
        help_menu = tkinter.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=lambda: set_value(ABOUT))

        # Creating Block Frame.
        frame = tkinter.Frame(self.root)
        frame.pack(padx=10, pady=10)

        gui_text = tkinter.Label(frame, text="Do you wish to edit a Music Folder or a single MP3 File?")
        gui_text.grid(row=0, column=0, columnspan=2, padx=15)

        folder_button = tkinter.Button(frame, text="Music Folder", fg="blue", command=lambda: set_value(FOLDER))
        folder_button.grid(row=1, column=0, pady=10)

        file_button = tkinter.Button(frame, text="MP3 File", fg="blue", command=lambda: set_value(FILE))
        file_button.grid(row=1, column=1, pady=10)

    def get_chosen_val(self):
        """
        Freeze GUI until option is being chosen
        :return: int - value of selected item
        """
        self.chosen_val = -1
        self.root.mainloop()
        return self.chosen_val
