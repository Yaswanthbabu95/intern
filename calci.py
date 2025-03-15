print("BASIC CALCUL20ATOR")
f=int(input("enter numner:"))
print(f)
s=int(input("enter number:"))
print(s)
o=input("select operator:+,-,*,/,%:")
while True:
    if 'o':
        if o=='+':
            print(f+s)
        elif o=='-':
            print(f-s)
        elif o=='*':
            print(f*s)
        elif o=='/':
            print(f/s)
        elif o=='%':
            print(f%s)
        else:
                print("error")
    else :
            print(invalid)
