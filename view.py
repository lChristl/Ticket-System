from data import BOOKINGS

def view_tickets():
    print("===== VIEW PURCHASED TICKET =====")

    if not BOOKINGS:
        print("No tickets purchased yet.\n")
    else:
        for ticket_id, ticket in BOOKINGS.items():
            print(f"Ticket ID: {ticket_id}")
            print(f" Movie: {ticket['movie']}")
            print(f" Date: {ticket['date']}")
            print(f" Time: {ticket['showtime']}")
            print(f" Quantity: {ticket['quantity']}")
            print(f" Total: P{ticket['total']}")
            print("-" * 20)