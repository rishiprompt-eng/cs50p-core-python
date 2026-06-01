def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    new_dollars = dollars.replace("$", "")
    return float(new_dollars)

def percent_to_float(percent):
    new_percent = percent.replace("%", "")
    return float(new_percent)/100

main()
