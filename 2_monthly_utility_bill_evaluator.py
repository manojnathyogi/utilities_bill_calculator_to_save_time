import mysql.connector
dbms_name = "trial"
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234567890", database="{}".format(dbms_name))
mycursor = mydb.cursor()

# take month and year as input
calc_month = int(input("Hi, enter the month in 2 digit format (01: JAN, 04: APRIL, 11: NOV) : "))
calc_year = int(input("Now, enter the last two digit for the year( FOr example: type 22 for 2022): "))

# take this month units from user which user have collected from all the meter boxes
current_month_meter_units = []
for i in range(1, 12):
    current_meter_value = int(input("Enter the unit of meter number {}: ".format(i)))
    current_month_meter_units.append(current_meter_value)

# insert the rooms number and the FIRST Month unit in table
add_new_field = "ALTER TABLE rec_of_meter_units ADD {}_{} INTEGER(10)".format(calc_month, calc_year)
mycursor.execute(add_new_field)
mydb.commit()
for count in range(1, 12):
    meter_units = "UPDATE rec_of_meter_units SET {}_{} = {} WHERE rooms = 'room{}'".format(calc_month, calc_year, current_month_meter_units[count-1], count)
    mycursor.execute(meter_units)
    mydb.commit()

# read previous month's meter units of the rooms
if calc_month == 1:
    field_of_past_month_meter_units = "12_" + str(calc_year-1)
else:
    field_of_past_month_meter_units = str(calc_month-1) + "_" + str(calc_year)

prev_field_values = "SELECT {field_value} FROM rec_of_meter_units".format(field_value=field_of_past_month_meter_units)
mycursor.execute(prev_field_values)
# store previous month unit in the list
previous_month_meter_units_tuple = mycursor.fetchall()  # <--- important
print("prev month units tuple", previous_month_meter_units_tuple)

# convert previous month meter units to lists
prev_month_meter_units = []
for count in range(0, 11):
    convert_the_prev_month_meter_units = list(previous_month_meter_units_tuple[count])
    prev_month_meter_units = prev_month_meter_units + convert_the_prev_month_meter_units
print("prev _ month", prev_month_meter_units)

# calculate current monthly units
current_month_units = []
for count in range(0, 11):
    calc_this_month_units = current_month_meter_units[count] - prev_month_meter_units[count]
    current_month_units.append(calc_this_month_units)

# write the monthly units of the rooms in the file
add_new_field = "ALTER TABLE rec_of_monthly_units ADD {}_{} INTEGER(10)".format(calc_month, calc_year)
mycursor.execute(add_new_field)
mydb.commit()
for count in range(1, 12):
    monthly_units = "UPDATE REC_OF_MONTHLY_UNITS SET {}_{} = {} WHERE rooms = 'room{}'".format(calc_month, calc_year, current_month_units[count-1], count)
    mycursor.execute(monthly_units)
    mydb.commit()

# calculate the amount of electricity bill
current_month_elec_bills = []
rate_electricity = int(input("Enter the rate of electricity bill: "))
for count in range(0, 11):
    calc_this_month_elec_bill = current_month_units[count] * rate_electricity
    current_month_elec_bills.append(calc_this_month_elec_bill)

# write the amount of electricity bill in the file
add_new_field = "ALTER TABLE REC_OF_MONTHLY_ELEC_BILLS ADD {}_{} INTEGER(10)".format(calc_month, calc_year)
mycursor.execute(add_new_field)
mydb.commit()
for count in range(1, 12):
    monthly_elec_bills = "UPDATE REC_OF_MONTHLY_ELEC_BILLS SET {}_{} = {} WHERE rooms = 'room{}'".format(calc_month, calc_year, current_month_elec_bills[count-1], count)
    mycursor.execute(monthly_elec_bills)
    mydb.commit()

# calculate the units & multiply the rate to calculate the amount --> Store it in the list
current_month_total_bills = []
calc_water_amt = int(input("Hi there, Bill is almost ready! Please, provide the amount for water: "))
calc_cleanliness_amt = int(input("Please, provide the amount for cleanliness: "))
calc_gas_amt = int(input("Please, provide the amount for gas: "))
for count in range(0, 11):
    calc_total_amt = current_month_elec_bills[count] + calc_gas_amt + calc_water_amt + calc_cleanliness_amt
    current_month_total_bills.append(calc_total_amt)  # integer

# Write total monthly bills of this month in a table
add_new_field = "ALTER TABLE REC_OF_TOTAL_MONTHLY_AMT ADD {}_{} INTEGER(10)".format(calc_month, calc_year)
mycursor.execute(add_new_field)
mydb.commit()
for count in range(1, 12):
    total_monthly_bills = "UPDATE REC_OF_TOTAL_MONTHLY_AMT SET {}_{} = {} WHERE rooms = 'room{}'".format(calc_month, calc_year, current_month_total_bills[count-1], count)
    mycursor.execute(total_monthly_bills)
    mydb.commit()

if mydb.is_connected():
    mycursor.close()
    mydb.close()
    print("MySQL connection is closed.")

print("The code is executed!!")
