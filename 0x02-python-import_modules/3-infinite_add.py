#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0
    for i in args[1:]:
        sum += int(i)
    print(sum)
