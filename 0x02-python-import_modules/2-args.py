#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv_len = len(argv)

    if argv_len > 2:
        print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{}: {}".format(i, argv[i]))
    elif argv_len == 2:
        print("1 argument:")
        print("{}: {}".format(1, argv[1]))
    else:
        print("0 arguments.")
