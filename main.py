import Add
#import view
#import update

print("Ticket System")
print("What would you like to do?")
print("1. Order tickets") #add
print("2. View purchased tickets") #view
print("3. Update current tickets") #update


print("Input choice here")
choice = input()

if choice == "1": #add
    Add.buy()
elif choice == "2": #view
    print()
elif choice == "3": #update
    print()
else:
    print("Input only numbers [1]-[3]")

# view()
# add()
# update()