from data import movies, BOOKINGS


def buy():
    print("====Buy Ticket====")
    print("Movie Showing!!")

    for key, info in movies.items():
        print(f"{key}. {info["title"]} : P{info["price"]} : {info["date"]}")
    print("")

    choice = input("Movie (Enter a number): ") #number for the movie to be selected
    if choice not in movies:
        print("Invalid input")
        return


    selected_movie = movies[choice]
    print(f"====CINEMA {choice} - Time Available====")
    for index, time_slot in enumerate(selected_movie["times_available"], 1):
        print(f"{index}. {time_slot}")

    print()
    showtime_choice = int(input(f"Time: "))

    if 1 <= showtime_choice <= len(selected_movie["times_available"]):
        showtime = selected_movie["times_available"][showtime_choice - 1]
    else:
        print("Invalid")
        return

    quantity = int(input("Number of Ticket: "))
    total = selected_movie["price"] * quantity

    ticket_id= str(len(BOOKINGS) + 1)
    BOOKINGS[ticket_id] = {
        "movie": selected_movie["title"],
        "price": selected_movie["price"],
        "showtime": showtime,
        "date": selected_movie["date"],
        "quantity": quantity,
        "total": total,
        "times_available": selected_movie["times_available"]
    }

    print()
    print(f"Ticket ID: {ticket_id}")
    print(f"Total: P{total}")
    print(f"Time: {showtime}")
    print("Ticket purchased successfully!")
    print()