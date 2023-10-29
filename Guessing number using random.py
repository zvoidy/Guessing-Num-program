import random

print("Guessing Game!")
print("----------------------------------")
print("Think of a number between 1 to N")
print("----------------------------------")

a_list=[]
range=int(input("Enter a range: "))
start=1
end=range
Try=0

while True:
  Try+=1
  
  number=random.randint(start,end)

  if number not in a_list:
    print(number)
    answer=input("Is my guess correct (Y), your number is too high (H), or too low (L)?: ")
    
    if (answer == "Y"):
      print()
      print(f"I guessed the number {number} in {Try}tries")
      print("Thank you for playing!")
      print()
      break

    elif (answer == "H"):
      start=number
      a_list.append(number)

    elif (answer == "L"):
      end=number
      a_list.append(number)
      
  else:
    continue
