
#Find the Prime Numbers in a given range with total count.
#(so basically prime number is a number which is only divisible by '1' & itself)
#examples : 2, 3, 5, 7, 11, 13,...



def error():
    try:

        #Finds the Prime Numbers in a given range:
        ip = int(input("Enter the range to find Prime Numbers: "))
        if ip <= 0:
            print("Wrong Input")
            print("Input must be a positive value")
            print("Start again..")
            error()

        print("Prime Numbers: ")

        for num in range(1, ip + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        i+=1
                        break

                else:
                    lst = list()
                    lst.append(num)
                    print(lst, end=" ")

        #Counts the Prime Numbers in a given range:
        def count_Prime_nums(n):
            count = 0

            for num in range(n):
                if num <= 1:
                    continue
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    count += 1

            return count

        print("\nTotal no. of Prime Numbers: ", count_Prime_nums(ip))

    except:
        #If there's an error, without giving a Traceback it prints a message
        #and also restarts the programme by itself using Recursion.
        print("Wrong Input")
        print("Start again..")
        error()
error()
















