# initialize sum to 0
sum = 0

while True:
    # take input from user
    num = int(input("Enter a number:1,2,3 "))
    
    # check if number is negative
    if num < 0:
        break
    
    # add number to sum
    sum += num

# print final sum
print("The sum is:", sum)



