from data import tickets

def view_tickets():
    print("===== VIEW PURCHASED TICKET =====")

    if not tickets:
        print("No tickets purchased yet.\n")
    else:
        for index, ticket in enumerate(tickets, start=1):
            print(f"Ticket: {index}")
            print(f" Movie: {ticket['movie']}")
            print(f" Date: {ticket['date']}")
            print(f" Time: {ticket['showtime']}")
            print(f" Quantity: {ticket['quantity']}")
            print(f" Total: P{ticket['total']}")
            print("-" * 20)