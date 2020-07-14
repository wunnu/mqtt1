import sys
class a:
    print("aa")
class b:
    print("dd")
class c(a,b):
    print("cc")
if __name__ == '__main__':
    d=c()