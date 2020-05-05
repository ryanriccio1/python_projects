import keyboard
import sys
import os
import split_lines
import loading_animation
from time import sleep


def main():
    try:
        os.system("title Script Typer")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("By: Ryan Riccio")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("This program will write the words from a text file to another, separating by newlines.")
        print("Then, after 5 seconds, it will start to type each word, and then press enter after.")
        print('''Warning, it will remove all non-alphanumeric characters, minus "'".''')
        print("\nBe careful, 5 seconds after processing, it will start to type and the only way\n"
              "to exit is by closing this window or by pressing Ctrl(or Cmd on Mac) + C fast enough.")
        input("\nPress enter to continue...")
        print("REMEMBER! 5 SECONDS!!")
        sleep(2)
        success, filename = split_lines.split_file()
        time_input = 0.1
        if not success:
            print("ERROR: Some unknown error occurred and the words could not be split. Exiting...")
            sys.exit(1)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Files successfully processed.")
        loading_animation.load_escape(4, .3)
        valid = False
        while not valid:
            try:
                time_input = input("\rEnter the amount of time, in seconds, between keystrokes (default 0.1): ")
                if time_input == "":
                    time_input = 0.1
                    valid = True
                elif float(time_input) > 10:
                    print("ERROR: You may not enter a value greater than 10 seconds. Try again.")
                elif float(time_input) < 0.02:
                    print("ERROR: You may not enter a value less than 0.02 seconds. Try again.")
                else:
                    valid = True
                    float(time_input)
            except ValueError:
                print("ERROR: That is not a valid value. Try again.")
        loading_animation.load_ellipsis("CHANGE WINDOW! Writing keystroke in 5 seconds", 5, wait_time=1)
        with open(filename, "r") as file:
            for line in file:
                keyboard.write(line, delay=time_input)

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt triggered. Exiting...")
        input("Press enter to exit...")


if __name__ == "__main__":
    main()
