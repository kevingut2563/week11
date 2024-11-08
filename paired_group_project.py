#Problem 1 
score = 0   
exellent = 0 
good = 0 
pass_count = 0
fail=0 
while score >= 0:
    score = int(input("Plese enter a score! ")) # this asks you to put in a score and starts the while loop 
    if score >= 90: #If the score is greater than or equal to 90 the computer will print exellent and add a one to the exellent list
        print("Exelent!")
        exellent = exellent + 1
    elif 70<= score <= 89: #if the score inputed is in between 70 and 89 the system will print good 
        print("good")
        good = good + 1 #then it will add a one to the good scores list 
    elif 50<= score <= 69: #if the score is in between 50 to 69 then the system will print pass 
        print("pass") 
        pass_count = pass_count + 1 #then it will add a one to the pass list #We used pass_count because pass was already an input 
    elif 0 <= score < 50:# finally if the score is between 0-50 then the system will print Fail 
        print("Fail")
        fail = fail + 1 #then the system will add a one to the fail list 
    else:
        print("Error Cannot be a negative number!") #if you input a negative number then the system will print "Error Cannot be a negative number!"
        break #then the While loop will break and stop looping 

print(f"The amount of exellent scores are {exellent}")
print(f"The amount of good scores are {good}")
print(f"The amount of pass scores are {pass_count}") #the sytem will print the amount of scores that were exellent, good, pass, and fail 
print(f"The amount of Fail scores are {fail}") 


#Problem 2 

start = input("Enter a number 1-30")
for item in range (1, 31):
    if item %2==0 and item >= 10:
# #this is checking each num to see if its even or odd
        print("Special even")
    else: print("Special Odd")
#this will print whether its even or odd