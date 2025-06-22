#Travel Agency
import mysql.connector
print('''---------------------------------------------------------------------------------------------''
        'Travel Agency Management System'
''-------------------------------------------------------------------------------------''')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)
mycursor=mydb.cursor()
mycursor.execute('create database if not exists travel')
mycursor.execute('use travel')
mycursor.execute('''create table if not exists destination(name varchar(24) not null, email varchar(40), location1 varchar(20) not null, location2 varchar(20) not null, people int(20), cost int(10))''')

#to add new Bookings
def add_destination():
    name=input('Enter Your Name: ')
    email=input('Enter Your Email: ')
    location1=input('From State: ')
    location2=input('To: ') 
    language=input('Preffered Language: ')
    people=int(input('Number of Travelers: '))

    query=f"INSERT INTO destination(name,email,location1,location2,language,people)"
    mycursor.execute('''create table if not exists destination(
        name varchar(24) not null, 
        email varchar(40), 
        location1 varchar(20) not null, 
        location2 varchar(20) not null, 
        language varchar(20), 
        people int(20), 
        cost int(10))''')
    mydb.commit()
    print('''--------------------------------------------------------------------------------------------------------------------------------''
                'Booking Added Successfully'
                ''--------------------------------------------------------------------------------------------------------------------------------''')
    

    rcost = cost ()
    query=f"UPDATE destination SET cost={rcost} WHERE name='{name}'"
    mycursor.execute(query)
    mydb.commit()
    print("\nYour Total Estimated Budget is: ",rcost)
    print('''--------------------------------------------------------------------------------------------------------------------------------''
                        'Budget Updated Successfully'
                        ''--------------------------------------------------------------------------------------------------------------------------------''')
    

#Transportation
def transportation():
      print("Transportation Options:")
      print("1 ⊳ Bus")
      print("2 ⊳ Train")
      print("3 ⊳ Flight")
      print("4 ⊳ Car Rental")
      print("5 ⊳ Waterways")

      choice=input('How do you want to travel? ')
      if choice=='1':
           print('For Details About Bus Service Contact: 1234567890')
      elif choice=='2':
           print('For Details About Train Service Contact: 0987654321')
      elif choice=='3':
           print('For Details About Flight Service Contact: 1122334455')
      elif choice=='4':
           print('For Details About Car Rental Service Contact: 2233445566')
      elif choice=='5':
          print('For Details About Waterways Service Contact: 3344556677')
      else:
          print('Sorry This Service is Not Available!, Please Try Again!')
      print('''                                                                                                                                              
                                                                   ''')
      

#Funtion For Accomodation cost
def accomodation_cost():
    
    room=input('Enter the room type (single/double/suite): ')
    nights=int(input('Enter the number of nights you want to stay: '))
    print('''Prices for one night stay -->
          1. Single Room: $100,
          2. Double Room: $150,
          3. Suite: $200''')
    
    print("Accomodation Options:")
    print("1 ⊳ Hotel")
    print("2 ⊳ Resort")
    print("3 ⊳ Guest House")
    print("4 ⊳ Homestay")
    

    choice=input('Where do you want to stay? ') 
    if choice=='1':
        roomcost=27000*nights 
    elif choice=='2':
        roomcost=32000*nights
    elif choice=='3':
        roomcost=20000*nights
    elif choice=='4':
        roomcost=38000*nights
    else:
        print('Sorry This Service is Not Available!, Please Choose From Above Options!')
        roomcost=0
    return roomcost

#func for cost
def cost():
    print('Details For Accomodation Cost')
    roomcost=accomodation_cost()
    print('''                                                                                      
                                                      ''')
    return roomcost
#func to view destination
def view_destination():
    mycursor.execute('select * from destination')
    result=mycursor.fetchall()
    if result:
        print('The list of Destinations')
        for row in result:
            print(f"name:{row[0]}")
            print(f"email:{row[1]}")
            print(f"location1:{row[2]}")
            print(f"location2:{row[3]}")
            print(f"language:{row[4]}")
            print(f"persons:{row[5]}")

            print("-"*40)
    else:
        print(" ")

def search_destination():
    location = input("Enter the Destination to Search: ")
    mycursor.execute(f"SELECT * FROM destination WHERE location2='{location}'")
    result=mycursor.fetchall()
    if result:
        print('The list of Destinations')
        for row in result:
            print(f"name:{row[0]}")
            print(f"email:{row[1]}")
            print(f"location1:{row[2]}")
            print(f"location2:{row[3]}")
            print(f"language:{row[4]}")
            print(f"persons:{row[5]}")       

            print("-"*40)
    else:
        print("No Match Found! ")
 
 # to delete a destination
def delete_destination():
    view_destination()
    print('''                                                                   
                              ''')
    print('Do you want to delete a Destination?')
    print('1-Yes')
    print('2-No')

    choice=int(input('Enter your choice: '))

    if choice==1:
        location2=input("Enter Your Destination To Be Deleted:")
        mycursor.execute(f"DELETE FROM destination WHERE location2='{location2}'")
        mydb.commit()

        print(f"Your Destination {location2} has been deleted successfully.")
    else:
        print('''*************************************
                            Thank You
              ***************************************************************''')
        
while True:
    print("Press 1-Add a New Destination")
    print("Press 2-View All Destinations")
    print("Press 3-Delete a Destination")
    print("Press 4-Search a Destination")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        add_destination()
        transportation()

    elif ch==2:
        view_destination()
    elif ch==3:
        delete_destination()
    elif ch==4:
        search_destination()
    else:
        break