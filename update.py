from data import BOOKINGS

def modify_booking():
    print()
    if not BOOKINGS:
        print("No active bookings found.")
        return
    
    ticket_id = input("Enter your Ticket ID (e.g., 1): ").strip()
    if ticket_id not in BOOKINGS:
        print("Booking not found!")
        return

    booking = BOOKINGS[ticket_id]
    # FIXED: Single quotes used & changed 'title' to 'movie'
    print(f"Current Booking: {booking['movie']} | Showtime: {booking['showtime']}")
    print("1. Change Showtime")
    print("2. Change Ticket Quantity")
    print("3. Cancel Booking")

    option = input("Choose an option: ")

    if option == "1": # Change showtime
        print("Available Showtimes: ")
        for index, time in enumerate(booking["times_available"], 1):
            print(f"{index}. {time}")

        t_choice = int(input("Select new showtime number: "))
        if 1 <= t_choice <= len(booking["times_available"]):
            booking["showtime"] = booking["times_available"][t_choice - 1]
            print(f"Showtime updated to {booking["showtime"]}")
        else: 
            print("Invalid choice")

    elif option == "2": # Change ticket qty
        new_qty = int(input("Enter new quantity: "))
        if new_qty > 0:
            booking["quantity"] = new_qty
            booking["total"] = booking["price"] * new_qty
            print(f"Quantity updated. New Total: P{booking["total"]}")
        else:
            print("Quantity must be greater than 0.")

    elif option == "3": # Delete ticket
        del BOOKINGS[ticket_id]
        print(f"Booking {ticket_id} has been canceled.")

    else:
        print("Invalid option!")