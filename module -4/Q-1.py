#     Write a Python program to read an entire text file.
import os    
#open('test.txt','x')

fl = open('test.txt','a')

fl.write("hello python!")
fl.write('\none')
fl.write('\ntwo')
fl.write('\nthree')
fl.write('\nfour')
fl.write('\nfive')
fl.write('\nsix')
fl.write('\nseven')
fl.write('\neight')
fl.write('\nnine')
fl.close()


def fread(fname):
        txt = open(fname)
        print(txt.read())
fread('test.txt') 