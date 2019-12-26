# Python program to print all
# prime number in an interval

start = int(input("Enter the start value"))
end = int(input("Enter the end value"))
sum = 0
for val in range(start, end + 1):

# If num is divisible by any number
# between 2 and val, it is not prime
    if(val > 1):
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            sum=sum+val

print(sum)

