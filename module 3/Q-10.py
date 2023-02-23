list1=[1,2,3,4]
list2=[1,3,4,5]
x= any(check in list1 for check in list2) # using any function check common number..
if x:
    print("true")
else:
    ("false")    