n = int(input("Enter a number: "))
number = 2
for i in range(n):
    if(number<n):
        if(n%number==0):
            print("Number is not prime")
            break
        else:
            number = number+1
        print("Number is prime")
        break