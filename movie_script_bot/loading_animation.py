from time import sleep


def load_ellipsis(text, number, *, wait_time):
    for i in range(number):
        print(f"\r{text}{'.'*i}", end="")
        sleep(wait_time)


def load_escape(number, wait_time):
    animation = "|/-\\"
    idx = 0
    print("")
    for i in range(number*4):
        print(f"\r{animation[idx % len(animation)]}", end="")
        idx += 1
        sleep(wait_time)
        if idx > 4:
            idx = 0


def loading_bar(length, wait_time):
    full_char = "\u2588"
    for i in range(length+1):
        print("\r[ " + full_char*i + '-'*(length-i) + " ]", sep="", end="")
        sleep(wait_time)
