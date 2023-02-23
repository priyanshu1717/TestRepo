# Write a Python program to read first n lines of a file.
fl = open('test.txt','r')
n =int(input("How many lines to  display")) 
if n < 0:
    print("Kindly enter the intger values")
else:
    for i in range(n):
        line = fl.readline()
        print(line)
 
