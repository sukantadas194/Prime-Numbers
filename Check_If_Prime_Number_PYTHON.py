

#Find a number is Prime or not.
#(so basically prime number is a number which is only divisible by '1' & itself)
#examples : 2, 3, 5, 7, 11, 13,...

try:
    n = int(input("Enter number : "))
    for i in range(2,n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("It's a Prime Number")
except:
    print("Not a number")
    print("Enter Input Correctly")

