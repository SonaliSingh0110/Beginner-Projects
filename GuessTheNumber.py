import random                   
number = random.randint(1,10)          //chooses numbers from 1 to 10
for i in range(0,3):                   // gives user 3 tries
  user = int(input("Guess the number"))        
  if user == number:
    print("HURRAYYYY!!!")
    print(f"you guessed it right,the number is {number}")
    break
  if user != number:
  
      print(f"Your guess is wrong,the number is {number}!")
 
