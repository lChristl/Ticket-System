import Add
import view
#import update

def main():
    while True:
        print("==== CINEMA TICKETING SYSTEM ====")
        print("1. Order Ticket ") #add
        print("2. View Tickets") #view
        print("3. Update") #update
        print("4. Exit\n")

        choice = input("Input choice here [1-4]: ")
        print()
        if choice == "1": #add
            Add.buy()
        elif choice == "2": #view
            view.view_tickets()
        elif choice == "3": #update
            print()
        elif choice == "4": #exit
            print("Exiting program..")
            break
        else:
            print("Input only numbers [1]-[4]\n")

if __name__ == "__main__":
    main()
# view()
# add()
# update()