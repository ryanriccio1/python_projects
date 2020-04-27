import re
import os
import tkinter as tk
import tkinter.filedialog as filedialog
from time import sleep
import loading_animation


def split_file():
    try:
        root = tk.Tk()
        root.withdraw()
        src_path = None
        destination_path = None

        valid = False
        while not valid:
            print("\nPlease select the source file.")
            sleep(1.5)
            src_path = filedialog.askopenfilename(initialdir=__file__, title="Select source file",
                                                  filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if src_path == "":
                print("You did not select a file. Try again.")
            else:
                print(f"You selected the file: '{os.path.basename(src_path)}'.")
                valid = True

        valid = False
        while not valid:
            print("\nPlease select the destination file.")
            sleep(1.5)
            destination_path = filedialog.askopenfilename(initialdir=__file__, title="Select destination file",
                                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if destination_path == "":
                print("You did not select a file. Try again.")
            elif destination_path == src_path:
                print("Destination file cannot be the same as source file. Try again.")
            else:
                print(f"You selected the file: '{os.path.basename(destination_path)}'.")
                valid = True

        loading_animation.load_escape(5, .2)
        loading_animation.load_ellipsis("Opening file", 5, wait_time=.25)
        sleep(.3)
        with open(src_path, "r") as src_file:
            with open(destination_path, "w") as destination_file:
                loading_animation.load_escape(3, .2)
                loading_animation.load_ellipsis("Reading files and formatting", 5, wait_time=.25)
                print("")
                file_contents = src_file.read().replace("\n", " ").split()
                loading_animation.load_ellipsis("Starting loop", 5, wait_time=.25)
                print("")
                loading_animation.loading_bar(30, .3)
                for i in file_contents:
                    i_searched = re.search(r"([a-zA-Z0-9']+)", i)
                    if i_searched:
                        destination_file.write(i_searched.group() + "\n")
    except FileNotFoundError:
        print("ERROR: The file has not been found. Exiting...")
        return False
    except IOError:
        print("ERROR: Some type of file error occurred. Exiting...")
        return False
    except ValueError:
        print("ERROR: Input data format incorrect. Exiting...")
        return False
    except TypeError:
        print("ERROR: Error stripping spaces and writing. Exiting...")
        return False
    else:
        return True, destination_path


if __name__ == "__main__":
    split_file()
