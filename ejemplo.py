l=[1,2]
a=0
try:
    print(l[2])
except ZeroDivisionError as e:
    print("Ha habido un error dividiendo:",e)
except IndexError as ie:
    print("Ha habido un error:",ie)