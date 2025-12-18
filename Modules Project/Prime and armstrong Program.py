from Modules import*

print('This program is for the prime number program') 
n=int(input("Enter the number: ")) 
result = f"{n} is a prime number" if isprime(n) else f"{n} is not a prime number" 
print(result) 
print() 
print() 
print('This program is for the armstrong number program') 
n=int(input("Enter the number: ")) 
result = f"{n} is a armstrong number" if isarmstrong(n) else f"{n} is not a armstrong number" 
print(result) 
print()
print()
print("Program execution Complete. Happy learning 😊")