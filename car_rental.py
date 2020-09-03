print("Welcome to car rentals!")
user_input = ""
user_input = input("Would you like to continue (y/n)? ")

while user_input != "n":
    customer_code = input("Customer code (b or d): ")
    number_of_days = int(input("Number of days: "))
    odometer_start = int(input("Odometer reading at the start: "))
    odometer_end = int(input("Odometer reading at the end: "))
    miles_driven = odometer_end - odometer_start

    if customer_code == "d":
        daily_rate = 60
        mile_rate = 0.25
        day_charge = number_of_days * daily_rate
        mile_charge = 0   #In case total driven miles is lower than number_of_days*100, there should be no charge for driven miles. 
        if miles_driven > 100 * number_of_days:   #Customers with the d customer code get 100 free miles for every day they rent the car
            miles_over_cap = 0
            miles_over_cap = miles_driven - 100 * number_of_days
            mile_charge = miles_over_cap * mile_rate
    elif customer_code == "b":
        daily_rate = 40
        mile_rate = 0.25
        day_charge = daily_rate * number_of_days
        mile_charge = miles_driven * mile_rate

    amount_due = day_charge + mile_charge

    print("Miles driven: " + str(miles_driven))
    print("Amount due: " + str(round(amount_due, 1)))

    user_input = input("Would you like to continue (y/n)? ") # Chech input again to see if the while loop should run again



