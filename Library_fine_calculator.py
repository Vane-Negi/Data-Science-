def calculate_fine(days):
    fine = 0

    if days <= 15:
        fine = 0
    elif days <= 30:
        fine = (days - 15) * 2
    else:
        fine = (15 * 2) + ((days - 30) * 5)

    return fine

days = int(input("Enter number of overdue days: "))

if days < 0:
    print("Days cannot be negative.")
else:
    total_fine = calculate_fine(days)
    print("Total Library Fine: ₹", total_fine)
