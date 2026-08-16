import data


BOOKINGS = {
    "1":{
        "title":"Testing movie 1",
        "price":"",
    }
            

            }

def modify_booking():
    print()
    if not BOOKINGS:
        print("No active bookings found.")
        return
    
    ticket_id = input("Enter your Ticket ID (e.g., 1)")
    if ticket_id not in BOOKINGS:
        print("Booking not found!")
        return

    booking = BOOKINGS[ticket_id]
    print(f"Current Booking: {booking["title"]}")
    print("")
    print("")
    print("")



modify_booking()
    