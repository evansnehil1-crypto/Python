def calculate_change(paid, price):
    change = paid - price
    return change

print("===== PARKING TICKET PAYMENT HELPER =====")

customers_served = 0
total_collected = 0

while True:
    print("\n===== NEW CUSTOMER =====")

    print("Vehicle types:")
    print("1. Motorcycle - 5 units per hour")
    print("2. Car - 10 units per hour")
    print("3. Bus - 20 units per hour")

    vehicle = int(input("Enter vehicle type (1, 2, or 3): "))
    hours = int(input("Enter number of hours: "))

    if vehicle == 1:
        price_per_hour = 5
    elif vehicle == 2:
        price_per_hour = 10
    elif vehicle == 3:
        price_per_hour = 20

    ticket_price = price_per_hour * hours

    print(f"Your parking ticket costs {ticket_price} units.")
    print("Accepted coins: 1, 5, 10, 25\n")

    total_inserted = 0
    coins_inserted = 0

    while True:
        coin = int(input("Insert a coin (1, 5, 10, or 25): "))

        if coin != 1 and coin != 5 and coin != 10 and coin != 25:
            continue

        total_inserted += coin
        coins_inserted += 1
        print(f"Inserted {coin}. Total so far: {total_inserted}\n")

        if total_inserted >= ticket_price:
            print("Enough money inserted!\n")
            break

    change_due = calculate_change(total_inserted, ticket_price)

    customers_served += 1
    total_collected += ticket_price

    print("Payment complete.")

    if change_due == 0:
        pass
    else:
        print(f"Here is your change: {change_due} units")

    print("\n===== CUSTOMER SUMMARY =====")
    print("Parking Price:", ticket_price)
    print("Hours Parked:", hours)
    print("Coins Inserted:", coins_inserted)
    print("Total Paid:", total_inserted)
    print("Change Given:", change_due)
    print("============================")

    another = input("\nServe another customer? (yes/no): ")

    if another != "yes":
        break

print("\n===== FINAL SUMMARY =====")
print("Customers Served:", customers_served)
print("Total Collected:", total_collected)
print("=========================")
print("Thanks for using the parking helper!")