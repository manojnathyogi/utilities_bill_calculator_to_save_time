import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234567890", database="rec_unit") #establish connection with DBMS
mycursor = mydb.cursor()

first_time = input("Hi, are you using this program for the first time( Y / N: ").lower()
if first_time[0] == "y":
    mycursor.execute("CREATE DATABASE rec_unit")  # create database
    mycursor.execute("SHOW DATABASES")  # get the names of databases
    for db in mycursor:
        print(db)  # output names of databases

    # take this month units from user which user have collected from all the meter boxes
    current_month_meter_unit = []
    for i in range(1, 12):
        current_meter_value = int(input("Enter the unit of meter number {}: ".format(i)))
        current_month_meter_unit.append(current_meter_value)
    this_month_unit = current_month_meter_unit
    this_month_elec_bill = []
    rate_electricity = int(input("Enter the rate of electricity bill: "))
    for count in range(0, 11):
        calc_this_month_bill = this_month_unit[count] * rate_electricity
        this_month_elec_bill.append[calc_this_month_bill]
else:
    # take month and year as input
    calc_month = int(input("Hi, enter the month in 2 digit format (01: JAN, 04: APRIL, 11: NOV) : "))
    calc_month = calc_month.lower()
    calc_year = int(input("Now, enter the last two digit for the year( FOr example: type 22 for 2022): "))

    # read previous month value from the DBMS
    if calc_month == "01":
        prev_year = int(calc_year)
        field_of_past_month_meter_unit = "12_" + str(prev_year)
    else:
        prev_month = int(calc_month)
        field_of_past_month_meter_unit = str(prev_month) + "_" + str(calc_year)

    url = "SELECT {field_value} FROM rec_of_units".format(field_value=field_of_past_month_meter_unit)
    mycursor.execute(url)
    # store previous month unit in the list
    previous_month_meter_unit = mycursor.fetchall()  # <--- important

    # take this month units from user which user have collected from all the meter boxes
    current_month_meter_unit = []
    for i in range(1, 12):
        current_meter_value = int(input("Enter the unit of meter number {}: ".format(i)))
        current_month_meter_unit.append(current_meter_value)
    '''
    for row in previous_month_unit:
        print(row)
    '''




    # write total bill (unit value) of this month only in DBMS

    # calculate the amount of electricity bill
    this_month_elec_bill = []
    rate_electricity = int(input("Enter the rate of electricity bill: "))
    for count in range(0, 11):
        calc_this_month_bill = this_month_unit[0] * rate_electricity
        this_month_elec_bill.append[calc_this_month_unit]

# calculate the units & multiply the rate to calculate the amount --> Store it in the list
this_month_amount = []
calc_water_amt = int(input("Hi there, Bill is almost ready! Please, provide the amount for water: "))
calc_cleanliness_amt = int(input("Please, provide the amount for cleanliness: "))
calc_gas_amt = int(input("Please, provide the amount for gas: "))
for count in range(0,12):
    calc_total_amt = this_month_elec_bill[count] + calc_gas_amt + calc_water_amt + calc_cleanliness_amt
    this_month_amount.append(calc_total_amt) #integer
# Write total amount of this month in a DBMS



# Generate bill
bill_of = input("Please, type the room number (1,2,3,4,5,6,7,8,9,10,11: ")
# take necessary values from DBMS

print("|" + "-" * 40 + "|")
print(" " * 6, "Room Number = {}".format(bill_of))
print()
print("| Units = {}".fomrat(this_month_unit[bill_of - 1]))
print("| Rate of electricity = {}".format(rate_electricity))
print("| Electricity bill = {}".fomrat(this_month_elec_bill[bill_of - 1]))
print("| Water bill = {}".fomrat(calc_water_amt))
print("| Cleanliness bill = {}".fomrat(calc_cleanliness_amt))
print("| Kitchen Gas bill = {}".fomraat(calc_gas_amt))
print("|" + "-" * 40 + "|")
print("| Total monthly utility bill : {}".format(this_month_amount[bill_of - 1]), "|")
print("|" + "-" * 40 + "|")







# close file
