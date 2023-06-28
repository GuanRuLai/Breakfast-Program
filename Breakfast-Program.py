# program ask user's name
# how much cash does user have
# if user is hungry or not
# program checks if the user has more than or equal to $30

name = input("Enter your name: ")
money = input("Enter your cash amount: ")
hungry = input("Are you hungry? (Y/N)")

if hungry == "Y":
    if int(money) >= 30:
        print(f"{name} should go to eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to buy breakfast.")
elif hungry == "N":
    if int(money) >= 30:
        print(f"{name} has enough money but doesn't want to eat breakfast.")
    else:
        print(f"{name} neither has enough money nor wants to eat breakfast.")
else:
    print("Please make sure that you enter either Y or N.")

#%%
