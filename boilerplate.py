'''
Quick utility to add a boilerplate to an existing file (from another template file).

$Python3 boilerplate.py [file name]

'''
import sys


def main():
        
    files = ['boiler.txt', sys.argv[1],'end_boiler.txt']
    text = []

    for i in files:
        with open(i, 'r') as fh:
                text.extend(fh.readlines())
    with open(sys.argv[1], 'w') as fh:
        for line in text:
            fh.write(line)
    print ("All Done!\n")


if __name__ == '__name__':
    main()
