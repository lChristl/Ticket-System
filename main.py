import Add
#import view
#import update

print("Ticket System")
print("What would you like to do?")
print("1. View Movies") #view
print("2. Order ticket") #add
print("3. Update current tickets") #update


print("Input choice here")
choice = input()

if choice == "1": #view
    print()
elif choice == "2": #add
    Add.buy()
elif choice == "3": #update
    print()
else:
    print("Input only numbers [1]-[3]")

# view()
# add()
# update()