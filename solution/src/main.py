# coding: utf-8
import sys
import os
# import time

"""
Test Machine Specification:
    OS: Windows 10
    Memory: 8 GB
    CPU: Core i5
    Python Ver.: 3.6.2

This program can manage an input file 
which contains 100 million rows, around 700 seconds. 
"""

def exercise(lines, X):

    """ Algorithm of the exercise. """
    cols = []
    for line in lines:
        tmp = line.split()
        col1 = tmp[0].strip()  # Unique record identifier
        col2 = int(tmp[1].strip())  # numeric value

        """ Update a list which contains X-largest value. """
        if len(cols) == X:
            cols_srt = sorted(cols)
            if cols_srt[0][0] < col2:
                cols_srt[0] = [col2, col1]
                cols = sorted(cols_srt)
        else:
            cols.append([col2, col1])

    """ Print output messages. """
    for vals in cols:
        print(vals[1])

    """ This is check code for output. """
    # for vals in cols:
    #     print(vals)


def main():
    # t1 = time.time()

    """ Read input file or stdin. """
    args = sys.argv
    if len(args) > 1:
        if os.path.exists(args[1]):
            with open(args[1], 'r') as f:
                lines = f.readlines()
        else:
            print('ERROR: The file is not existed.')
            sys.exit()
    else:
        lines = sys.stdin.readlines()
        # print(lines)

    """ Read parameter X from stdin. """
    while True:
        X = input('Please input a number as parameter X: ')
        if X.isdigit():
            X = int(X)
            break

    """ Call main function. """
    exercise(lines, X)
    # print('\n Process Time: %.1f sec' % (time.time() - t1))

if __name__ == '__main__':
    main()
