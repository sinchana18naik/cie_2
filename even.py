import sys

print(sys.argv)
if len(sys.argv) > 1:
    num= int(sys.argv[1])
    if num == 0:
        print("Number is Zero")
    elif num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("No number provided")
