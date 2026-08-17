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

    ticket_id= (f"Ticket{len(BOOKINGS) + 1}")
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




    
    # print("1. Spider-Man:Brand New Day : P285 : July 31, 2026")
    # print("2. The Odyssey  : P255 : July 15, 2026")
    # print("3. Blue-Lock Live Action : P250 : August 07, 2026")


    # if choice == 1:
    #     movie, price, date, time = movies[0]

    #     print("====CINEMA 1 - Time Available====")
    #     print("1. 12:30PM")
    #     print("2. 3:30PM")
    #     print("3. 6:30PM")

    # elif choice == 2:
    #     movie, price, date, time = movies[1]

    #     print("====CINEMA 2 - Time Available====")
    #     print("1. 1:10PM")
    #     print("2. 5:00PM")
    #     print("3. 9:00PM")
        
    # elif choice == 3:
    #     movie, price, date, time = movies[2]

    #     print("====CINEMA 3 - Time Available====")
    #     print("1. 11:00AM")
    #     print("2. 4:00PM")
    #     print("3. 9:00PM")
    # else:
    #     print("Invalid!!")
    #     return()

    # print()
    # showtime_choice = int(input("Time (Enter a Number): "))
    # if showtime_choice == 1:
    #     showtime = time[0]

    # elif showtime_choice == 2:
    #     showtime = time[1]

    # elif showtime_choice == 3:
    #     showtime = time[2]
    # else:
    #     print("Invalid!!")
    #     return()

    # print()
    # quantity = int(input("Number of Ticket: "))
    # total = price * quantity

    # ticket = {
    #     "movie": movie,
    #     "showtime": showtime,
    #     "date": date,
    #     "quantity": quantity,
    #     "total": total,
    # }
    # tickets.append(ticket)
    
    # print()
    # print(f"Total: P{total}")
    # print(f"Time: {showtime}")
    # print(" Ticket purchased successfully!")
    # print() 


buy()