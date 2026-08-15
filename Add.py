movie = (
    ("Spider-Man:Brand New Day", 285, "July 31, 2026",
    ("12:30PM", "3:30PM", "6:30PM")),
    ("The Odyssey", 255, "July 15, 2026",
    ("1:10PM", "7:00PM", "9:00PM")),
    ("Blue-Lock Live Action", 250, "August 07, 2026",
    ("11:00AM", "4:00PM", "9:00PM"))
)
print("====Buy Ticket====")
print("Movie Showing!!");
print("1. Spider-Man:Brand New Day : P285 : July 31, 2026");
print("2. The Odyssey  : P255 : July 15, 2026");
print("3. Blue-Lock Live Action : P250 : August 07, 2026");

choice = int(input("Movie (Enter a number): "))
if choice == 1:
    movie, price, date, time = movie[0]

    print("====CINEMA 1 - Time Available====")
    print("1. 12:30PM")
    print("2. 3:30PM")
    print("3. 6:30PM")

elif choice == 2:
    movie, price, date, time = movie[1]

    print("====CINEMA 2 - Time Available====")
    print("1. 1:10PM")
    print("2. 5:00PM")
    print("3. 9:00PM")
    
elif choice == 3:
    movie, price, date, time = movie[2]

    print("====CINEMA 3 - Time Available====")
    print("1. 11:00AM")
    print("2. 4:00PM")
    print("3. 9:00PM")
else:
    print("Invalid!!")

showtime_choice = int(input("Time (Enter a Number): "))
if showtime_choice == 1:
    showtime = time[0]

elif showtime_choice == 2:
    showtime = time[1]

elif showtime_choice == 3:
    showtime = time[2]
else:
    print("Invalid!!")

quantity = int(input("Number of Ticket: "))
total = price * quantity

print(f"Total: P{total}")
print(f"Time: {showtime}")
