import mysql.connector
# establish connection with DBMS
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234567890")
mycursor = mydb.cursor()

first_time = input("Hi, are you using this program for the first time(Y / N): ").upper()
if first_time[0] == "Y":
    # introduce about the program to the user
    print("Welcome! ")
    print("In summary, this program will help you calculate the electricity bills, \n and store it for future ")
    print()
    print("Hi, first we should create a Database! ")

    # Create and show database
    dbms_name = "trial"
    mycursor.execute("CREATE DATABASE {}".format(dbms_name))  # create database
    mycursor.execute("SHOW DATABASES")  # get the names of databases
    for db in mycursor:
        print(db)  # output names of databases
    print("The database is created!! The name of database is TRIAL.")

    # create the required tables
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234567890", database="{}".format(dbms_name))
    mycursor = mydb.cursor()
    # take month and year as input
    calc_month = int(input("Hi, enter the month in 2 digit format (01: JAN, 04: APRIL, 11: NOV) : "))
    calc_year = int(input("Now, enter the last two digit for the year( FOr example: type 22 for 2022): "))

    mycursor.execute("CREATE TABLE REC_OF_METER_UNITS (rooms VARCHAR(6), {month}_{year} INTEGER(10))".format(month=calc_month, year=calc_year))  # create a table in DB
    mycursor.execute("CREATE TABLE REC_OF_MONTHLY_UNITS (rooms VARCHAR(6), {month}_{year} INTEGER(10))".format(month=calc_month, year=calc_year))  # create a table in DB
    mycursor.execute("CREATE TABLE REC_OF_MONTHLY_ELEC_BILLS (rooms VARCHAR(6), {month}_{year} INTEGER(10))".format(month=calc_month, year=calc_year))  # create a table in DB
    mycursor.execute("CREATE TABLE REC_OF_TOTAL_MONTHLY_AMT (rooms VARCHAR(6), {month}_{year} INTEGER(10))".format(month=calc_month, year=calc_year))  # create a table in DB

    mycursor.execute("SHOW TABLES")  # get names of tables in DB
    for table_name in mycursor:  # print names of tables in DB
        print(table_name)
    print("The necessary tables are created. The REC_OF_METER_UNITS stores the value taken from meter box of the room. \n The REC_OF_MONTHLY_UNITS table stores the calculated monthly unit of the room. \n The REC_OF_MONTHLY_ELEC_BILLS table stores the calculated electricity bill's amount according to the room. \n And finally, the REC_OF_TOTAL_MONTHLY_AMT stores the total monthly bill including the water, cleanliness and the kitchen gas with the electricity bill. ")
    print("!!ALL THE BEST!!")

    # take this month units from user which user have collected from all the meter boxes
    first_month_meter_unit = []
    for i in range(1, 12):
        current_meter_value = int(input("Enter the unit of meter number {}: ".format(i)))
        first_month_meter_unit.append(current_meter_value)

    # insert the rooms number and the FIRST Month unit in table
    for i in range(1, 12):
        meter_unit = "INSERT INTO rec_of_meter_units (rooms, {}_{}) VALUES (%s, %s)".format(calc_month, calc_year)
        room_value = ("room{}".format(i), first_month_meter_unit[i-1])
        mycursor.execute(meter_unit, room_value)
        mydb.commit()

        monthly_unit = "INSERT INTO rec_of_monthly_units (rooms, {}_{}) VALUES (%s, %s)".format(calc_month, calc_year)
        room_value = ("room{}".format(i), first_month_meter_unit[i-1])
        mycursor.execute(monthly_unit, room_value)
        mydb.commit()

    # calculate the amount of electricity bill and total bill, with water, kitchen gas, and cleanliness
    first_month_elec_bills = []
    first_month_total_bills = []
    rate_electricity = int(input("Enter the rate of electricity bill: "))
    calc_water_amt = int(input("Hi there, Bill is almost ready! Please, provide the amount for water: "))
    calc_cleanliness_amt = int(input("Please, provide the amount for cleanliness: "))
    calc_gas_amt = int(input("Please, provide the amount for gas: "))
    for count in range(1, 12):
        calc_first_month_elec_bills = first_month_meter_unit[count-1] * rate_electricity
        first_month_elec_bills.append(calc_first_month_elec_bills)
        elec_bill = "INSERT INTO REC_OF_MONTHLY_ELEC_BILLS (rooms, {}_{}) VALUES (%s, %s)".format(calc_month, calc_year)
        room_value = ("room{}".format(count), first_month_elec_bills[count-1])
        mycursor.execute(elec_bill, room_value)
        mydb.commit()

        calc_total_monthly_bills = calc_first_month_elec_bills + calc_gas_amt + calc_water_amt + calc_cleanliness_amt
        first_month_total_bills.append(calc_total_monthly_bills)
        total_bill = "INSERT INTO REC_OF_TOTAL_MONTHLY_AMT (rooms, {}_{}) VALUES (%s, %s)".format(calc_month, calc_year)
        room_value = ("room{}".format(count), first_month_total_bills[count-1])
        mycursor.execute(total_bill, room_value)
        mydb.commit()
else:
    print("If you have already created the Database, tables and using the set of programs, \n GO THROUGH the regular_utility_bill_input to evaluate and generate this month bill.")

if mydb.is_connected():
    mycursor.close()
    mydb.close()
    print("MySQL connection is closed.")

print(" ** Thank You for being with us **")
