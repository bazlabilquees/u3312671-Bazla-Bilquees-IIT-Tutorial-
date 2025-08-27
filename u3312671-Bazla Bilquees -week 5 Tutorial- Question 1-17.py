# Question 1 
num = 5
while True:
    num = 2*num
    if num %4==0:
  break (exit from the loop)
   print(num)
    
# Question 2
num = 3
while num < 15:
    num +=5
    print(num)

  # Question 3 (bcz it is from the last to first )
  
oceans = ["Atlantic", "Pacific", "Indian", "Artic", "Antarctic"]
i = len(oceans)-1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
        
    i = i-1
    print(",".join(oceans))
   
#Question 4 (start is inclusive, stop is exclusive)
for i in range (3,7):
    print(2*i)

#Question 5

num = 5
for i in range(num, 2 * num - 2):
    print(i)

#Question 6 (-1 is the step) 
for countdown in range(10,0,-1):
    print(countdown)

#Question 7
numEvens = 0
sumOfEvens = 0
list1 = [2,9,6,7,12]
for num in list1:
    if num%2==0:
        numEvens += 1
        sumOfEvens += num
        print(numEvens, sumOfEvens)

# Question 10
for num in range(1,10,2):
    print(num)

#Question 10 B 
total = 0
count = 0
while count < 3:
    total = total +int(1)
    count = count + 1 
    print(total)

#Question 11
L = ["sentence", "contains", "five", "words."]
L.insert(0, "This")
print(" ".join(L))

del L[3]
L.insert(3, "six")
L.insert(4, "different")
print(" ".join(L))

#Question 12
name = input("Bazla Bilquees")
L = name.split()
print("{0:s}, {1:s}" . format(L[1], L[0]))
virtues = ("wisdom", "courage", "temperance", "justice")
print(virtues[3])

#Question 13
nums = [6,2,8,1]
print("Largest umber:", max(nums))
print("Legth:" , len(nums))
print("Total:" , sum(nums))

#Question 14
tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print(" ".join(tuple2))

#Identify All Errors
#Question 15
# The total Index number is 3 not 4 
virtues = ("wisdom", "courage", "temperance", "justice")
print(virtues[3])

#Question 16
# we have to add the map and string in the print statement
list1 = [1, "two", "three", 4]
print(" ".join(map(str,list1)))

#Question 17
## Display the numbers from 1 through 5.
num = 0
while True; (#missing of : in the end of the statement)
    num = 1
    print(num)
    num += 1

