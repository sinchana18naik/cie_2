import sys

print(sys.argv)
if len(sys.argv) > 1:
    num= int(sys.argv[1])
    
    if num == 0:
        print("number is zero")
    elif num % 2 ==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("no number is provided")
