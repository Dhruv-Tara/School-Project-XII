# License

"""
        Copyright [2022] [Yash-Sharma-1807]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""




"""
City Management in Python using 
// sys library (BY DEFAULT AVAILAIBLE IN PYTHON)
// mysql-python-connector library (https://pypi.org/project/mysql-connector-python/)
// pandas library (https://pypi.org/project/pandas/)
// datetime (BY DEFAULT AVAILAIBLE IN PYTHON)
// SQLAlchemy (https://pypi.org/project/SQLAlchemy/)
"""
# // IMPORTS

import pandas as pd
import sys
import mysql.connector as con
import datetime
from sqlalchemy import create_engine

# // DB Connection



# // PASSWORD 
x = input("Enter your id : ")
y = input("Enter your password : ")

now = datetime.datetime.now()
today = now.date()

if x == "Yash" and y == "123456":
    DB = con.connect(user="root",password="root",database="city") # /* in localhost no need to add a host */
    if DB.is_connected():
        print("Logged in Sucessfully\n")
    myc = DB.cursor()
    alchemy = create_engine("mysql+mysqlconnector://root:root@localhost/city")

# // MAIN CODE
    
    
    print("Hello {}".format(x))
    print("Welcome to Nashik SmartCity AREA Management System")
    print("======== MAIN MENU ========")       
    print("Select : ")                    
    print("1 to add new record.")         
    print("2 to update a record.")     
    print("3 to delete a record.")    
    print("4 to show all records")    
    print("5 to get a BAR-GRAPH.")
    print("===========================")
    
    inp = int(input("Enter Your value : "))
    
    
    if inp == 1:
        _query = "Select * from Nashik"
        _table = pd.read_sql(_query,alchemy,index_col="pin")
        print("\n\n")
        print("=========================== MAIN TABLE ===================================")
        print(_table)
        print("==========================================================================")
        print("\n\nPrinted Main Table for Your reference")
        pin = int(input("Enter the PIN CODE of area : "))
        name = input("Enter The name of area [PLEASE USE (_) INSTEAD OF SPACES (  )] : ")
        area = float(input("Enter Total area of {} in km² [EXAMPLE :- 13] : ".format(name)))
        population = float(input("Enter total population of {} : ".format(name)))
        water = float(input("Enter total usage of water for {} in Litres : ".format(name)))
        elec = float(input("Total usage of electricity for {} in units/kWh : ".format(name)))
        from_date = input("Enter the date of day from which all these information were recorded in format [YYYY-MM-DD] : ")
        last_updated = today
        # SQL QUERY 
        query = "insert into nashik values({},'{}',{},{},{},{},'{}','{}')".format(pin,name,area,population,water,elec,from_date,last_updated)
        myc.execute(query)
        DB.commit()
        sys.exit("Successfully Added {} \n[NOTE :- area population water and electricity are stored in approx values i.e. \nif you types 13.28 it will be converted to 13]\n\nRE-RUN THE CODE IF YOU WANT TO EXECUTE OTHER OPTIONS OF MAIN MENU".format(pin))
    
    elif inp == 2:
        print("========================================")
        print("\nSelect ONE OF the following :")
        print("1 If you want to Update name")
        print("2 If you want to Update Area")
        print("3 If you want to Update Population")
        print("4 If you want to Update Water Usage")
        print("5 If you want to Update Electricity Usage\n")
        print("=========================================")
        _query = "Select * from Nashik"
        _table = pd.read_sql(_query,alchemy,index_col="pin")
        print("\n\n")
        print("=========================== MAIN TABLE ===================================")
        print(_table)
        print("==========================================================================")
        print("\n\nPrinted Main Table for Your reference")
        inp_1 = int(input("\nEnter Your Query : "))

        if inp_1 == 1:
            pin = int(input("\nEnter Pin Code of Area : "))
            query = "select name from nashik where pin = {}".format(pin)
            myc.execute(query)
            for x in myc.fetchall():
                name = x[0]
            NEW = input("Enter New Name for {} [PLEASE USE (_) INSTEAD OF SPACES (  )] : ".format(name))
            query_ = "update nashik set name = '{}' where pin = {}".format(NEW,pin)
            myc.execute(query_)
            DB.commit()
            update_date = "update nashik set last_updated = '{}' where pin = {}".format(today,pin)
            myc.execute(update_date)
            DB.commit()
            sys.exit("\nSuccesfully Changed name of {} to {}. \n\nRE-RUN THE CODE IF YOU WANT TO EXECUTE OTHER OPTIONS OF MAIN MENU".format(name,NEW))
        
        
        elif inp_1 == 2:
            pin = int(input("\nEnter Pin Code of Area : "))
            query = "select name,area from nashik where pin = {}".format(pin)
            myc.execute(query)
            for x in myc.fetchall():
                name = x[0]
                area = x[1]
            NEW = float(input("Enter New Area For {} OLD AREA is {}km² : ".format(name,area)))
            query_ = "update nashik set area = {} where pin = {}".format(NEW,pin)
            myc.execute(query_)
            DB.commit()
            update_date = "update nashik set last_updated = '{}' where pin = {}".format(today,pin)
            myc.execute(update_date)
            DB.commit()
            sys.exit("Sucessfully changed Area of {} from {}km² to {}km². \n\nRE-RUN THE CODE IF YOU WANT TO EXECUTE OTHER OPTIONS OF MAIN MENU".format(name,area,NEW))


        elif inp_1 == 3:
            pin = int(input("Enter Pin of Area : "))
            query = "select name , population from nashik where pin = {}".format(pin)
            myc.execute(query)
            for x in myc.fetchall():
                name = x[0]
                population = x[1]
            NEW = float(input("Enter new Population for {} old population was {} : ".format(name,population)))
            query_ = "update nashik set population = {} where pin = {}".format(NEW,pin)
            myc.execute(query_)
            DB.commit()
            update_date = "update nashik set last_updated = '{}' where pin = {}".format(today,pin)
            myc.execute(update_date)
            DB.commit()
            sys.exit("Sucessfully Changed Population of {} from {} to {}.\n\nRE-RUN THE CODE IF YOU WANT TO EXECUTE OTHER OPTIONS OF MAIN MENU".format(name,population,NEW))


        elif inp_1 == 4:
            pin = int(input("Enter Pin of Area : "))
            query = "select name , water from nashik where pin = {}".format(pin)
            myc.execute(query)
            for x in myc.fetchall():
                name = x[0]
                water = x[1]
            NEW = float(input("Enter new Water Usage for {} old is {} L : ".format(name,water)))
            query_ = "update nashik set water = {} where pin = {}".format(NEW,pin)
            myc.execute(query_)
            DB.commit()
            update_date = "update nashik set last_updated = '{}' where pin = {}".format(today,pin)
            myc.execute(update_date)
            DB.commit()
            sys.exit("Successfully changed Water Usage for {} from {}L to {}L.\n\nRE-RUN THE CODE IF YOU WANT TO EXECUTE OTHER OPTIONS OF MAIN MENU".format(name,water,NEW))

        elif inp_1 == 5:
            pin = int(input("Enter Pin of Area : "))
            query = "select name,elec from nashik where pin = {}".format(pin)
            myc.execute(query)
            for x in myc.fetchall():
                name = x[0]
                elec = x[1]
            NEW = float(input("Enter new Electricity usage for {} old was {}units : ".format(name,elec)))
            query_ = "update nashik set elec = {} where pin = {}".format(NEW,pin)
            myc.execute(query_)
            DB.commit()
            update_date = "update nashik set last_updated = '{}' where pin = {}".format(today,pin)
            myc.execute(update_date)
            DB.commit()
            print("Successfully changed Electricity usage for {} from {}units to {}units".format(name,elec,NEW))


        else:
            sys.exit("RE-RUN the code and write proper query.")
    

    elif inp == 3:
        pin = int(input("Enter the pincode for area you want to delete from database : "))
        print("\nFor Security Measures Please Type Your ID and PASS AGAIN.")
        i_d = input("\nENTER YOUR ID : ")
        pa_ss = int(input("ENTER YOUR PASS : "))
        if i_d == "Yash" and pa_ss == 123456 :
            name = "select name from nashik where pin = {}".format(pin)
            myc.execute(name)
            for x in myc.fetchall():
                name_ = x[0]

            query = "DELETE FROM nashik WHERE pin = {}".format(pin)
            myc.execute(query)
            DB.commit()
            sys.exit("SUCCESSFULLY DELETED {} FROM DATABASE".format(name_))
        else:
            sys.exit("WRONG CREDENTIALS.")


    elif inp == 4:
        query = "select * from nashik"
        table = pd.read_sql(query,alchemy,index_col="pin")
        print("\n\n")
        print("=========================== MAIN TABLE ===================================")
        print(table)
        print("==========================================================================")
        sys.exit("\n\nRE-RUN THE CODE TO RUN OTHER QUERIES OF MAIN MENU")


    elif inp == 5:
        print("==================== MENU ====================")
        print("\nType 1 to get a Bar Graph of whole Database.")
        print("Type 2 to select the fields you want.")
        print("================ SELECT ONE : ================")
        _query = "Select * from Nashik"
        _table = pd.read_sql(_query,alchemy,index_col="pin")
        print("\n\n")
        print("=========================== MAIN TABLE ===================================")
        print(_table)
        print("==========================================================================")
        print("\n\nPrinted Main Table for Your reference")
        inp_2 = int(input("Enter Your Query : "))

        if inp_2 == 1:
            query = "Select name,area,population,water,elec from nashik"
            df = pd.read_sql(query,alchemy)
            df.plot(kind="bar")
        elif inp_2 == 2:
            print("\nTotal parameters availaible are (area,population,water,elec)")
            para = input("Enter the fields of which you want a bar graph [SEPARATE EACH BY (,)]: ")
            query = "select name,{} from nashik".format(para)
            df = pd.read_sql(query,alchemy)
            df.plot(kind="bar")
        else:
            sys.exit("\nWRONG QUERY\n\nRE-RUN THE CODE.")
            
    else:
        sys.exit("\nWRONG QUERY\n\nRE-RUN THE CODE.")

else:
    sys.exit("Wrong Credentials..")  # // USING SYS FOR PROPER EXIT [EXPLANED HERE (https://bit.ly/3EfabLp)]