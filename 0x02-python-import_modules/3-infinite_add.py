#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    result = 0

    for i in range(1, num + 1):
        result = result + int(sys.argv[i])
    print(result)
