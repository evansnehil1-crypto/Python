print("=== Library Visit Planner ===")
print("Answer a few quick questions and I will plan your library visit!\n")

day = input("What day is it? (Monday to Sunday): ")
weather = input("What is the weather? (sunny / rainy / cloudy / snowy): ")
have_book = input("Do you have a book to return? (yes / no): ")
want_to_read = input("Do you want to browse for new books? (yes / no): ")

print()
print(f"=== Your Library Plan for {day} ===")
print("--" * 35)

if day in {"Saturday", "Sunday"}:
    print("Library hours: 10:00 AM - 5:00 PM (Weekend hours)")

elif day == "Monday":
    print("Library hours: 12:00 PM - 8:00 PM (Late opening)")

elif day == "Friday":
    print("Library hours: 9:00 AM - 6:00 PM (Early closing)")

if weather == "rainy" or weather == "snowy":
    print("Weather tip: Stay dry - the library is a perfect indoor activity today!")

elif weather == "cloudy":
    print("Weather tip: Good day for reading - bring a light jacket just in case.")

elif weather == "sunny":
    print("Weather tip: Beautiful day out! Enjoy the walk to the library.")

if have_book == "yes":
    print("Book return: Please return your book at the front desk.")
    print("Check your due date - you might have a late fee!")

elif have_book == "no" and want_to_read == "yes":
    print("Book return: No books to return - head straight to the browsing section!")

if want_to_read == "yes":
    print("Browsing: The new arrivals section has great books this week!")

    if have_book == "yes" and day in {"Saturday", "Sunday"}:
        print("Great plan: Return your book and browse the weekend special collection!")

elif want_to_read == "no" and have_book == "yes":
    print("Quick visit: Just return your book - you'll be in and out!")

if have_book == "yes" and day == "Monday":
    print("Reminder: Monday is the busiest day - expect a line at the return desk.")

elif have_book == "yes" and day in {"Saturday", "Sunday"}:
    print("Reminder: Weekend returns may take longer - plan for extra time.")

if weather in {"rainy", "snowy"} and want_to_read == "yes":
    print("Best plan: Cozy up in the library's reading corner with a new book today!")

elif weather == "sunny" and have_book == "yes" and want_to_read == "yes":
    print("Best plan: Return your book, pick a new one, and read in the sunny courtyard!")

elif have_book == "yes" and want_to_read == "no":
    print("Best plan: Quick drop-off - use the self-service return station!")

elif have_book == "no" and want_to_read == "yes" and day in {"Saturday", "Sunday"}:
    print("Best plan: Perfect weekend for browsing - bring the whole family!")

else:
    print("Best plan: Stop by the library and discover something new today!")

if have_book == "yes":
    print()
    print("Quick reminder: Check your book for any damage before returning!")

print()
print("Plan complete! Happy reading and enjoy your library visit!")