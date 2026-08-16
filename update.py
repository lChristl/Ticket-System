import data


BOOKINGS = {
    "1":{
        "title":"Testing movie 1",
        "price":100,
        "time":"12:00PM",
        "quantity":"2",
        "total": 200,
        "times_available": ("1:10PM","5:10PM","7:10PM")
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
    print("1. Change Showtime")
    print("2. Change Ticket Quantity")
    print("3. Cancel Booking")

    option = input("Choose an option: ")

    if option == "1":
        print("Available Showtimes: ")
        for index, time in enumerate(booking["times_available"], 1):
            print(f"{index}. {time}")

        t_choice = int(input("Select new showtime number: "))

modify_booking()
    