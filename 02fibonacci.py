n = int(input("Enter a number"))
fibo= 1
number = 1
for i in range(n):
    if(number<=n):
        fibo = fibo*number
        number = number+1
print(fibo)