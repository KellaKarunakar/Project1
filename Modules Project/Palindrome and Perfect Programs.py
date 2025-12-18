from Modules import* 

print("This program is for palindrome number") 
n=int(input("Enter the number: ")) 
result = f"{n} is a palindrome number" if ispalindrome(n) else f"{n} is not a palindrome number" 
print(result) 
print()
print() 
print("This program is for Perfect number") 
n=int(input("Enter the number: ")) 
result = f"{n} is a perfect number" if isperfect(n) else f"{n} is not a perfect number" 
print(result)
print() 
print() 
print("This program is completed. Happy Learning 😊")