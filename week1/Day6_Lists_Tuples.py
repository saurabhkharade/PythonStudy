# conditional Statement
age = int(input("Enter your age: "))
if 18 <= age <= 45:
    print("Person is eligible to vote twice.")
elif age > 45:
    print("Person is eligible to vote ")
else:
    print("Person is ineligible to vote.")
print("\n")
print("----Menu----")
print("1. Green")
print("2. Red")
print("3. Yellow")
print("4. White")
choice = int(input("Enter your choice number:"))
if choice == 1:
    print("Your Color is Green. ")
elif choice == 2:
    print("Your Color is Red. ")
elif choice == 3:
    print("Your Color is Yellow. ")
elif choice == 4:
    print("Your Color is White. ")
else:
    print("Invalid Choice.")

