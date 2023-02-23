try:
    list=('s','d','f')
    x=list.count(list)
    if len(list)==0:
        print("your list is empty")
    else:
        print(x)
except Exception as er:
    print(er)        