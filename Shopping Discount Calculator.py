valid = False
while not valid:
    try:
        bill = float(input("Enter shopping bill: "))
        discount = float(input("Enter discount percentage: "))

        discount_amount = bill*discount/100
        final_bill = bill - discount_amount

    except ValueError:
        print("Invalid input. Please enter numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Discount:", discount_amount)
        print("Final bill:", final_bill)

    finally:
        print("Calculation finished.")