import sys
a=[]
print(sys.getrefcount(a))
b=a
print(sys.getrefcount(a))
c=b
print(sys.getrefcount(a))#sys.getrefcount用于引用计数