print("Guessing Game!")
print("----------------------------------")
print("Think of a number between 1 to N")
print("----------------------------------")

range=int(input("Enter the range: ))
low = 1
high = range
Try=0

while True:
    Try+=1
    mid=(low+high)//2
    print("Is it ",mid)
    response=input("Is my guess correct (Y), your number is too high (H), or too low (L)?: ")

    if response=="Y":
        print()
        print(f"I guessed the number {mid} in {Try}tries")
        print("Thank you for playing!")
        print()
        break
    elif response!="Y" and response=="H":
        low=mid
    elif response!="Y" and response=="L":
        high=mid
        
