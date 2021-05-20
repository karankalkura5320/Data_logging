'''
A receptionist is having the duty of noting the details of visitors walking -to the office.
She notes in the register their name, phone number, place, body temperature.
Using Python I created program to take the input and create a excel file and place all data in that excel file.
'''


import pandas as pd

name_list = []
phone_list = []
place_list = []
temp_list = []
while True:
    try:
        name = input("Name: ")                      # Input name
        if name == 'Done' or name == 'done':
            break
        phone = int(input("Phone Number: "))        # Input phone number
        place = input("Place: ")                    # Input place
        temp = int(input("Body temperature: "))     # Input body temperature
    except:
        print('Try again')                          # In case of error it will start again

    name_list.append(name)                          # append all values to the created list
    phone_list.append(phone)
    place_list.append(place)
    temp_list.append(temp)

# Input taken from receptionist will put in dictionary
data = {
    'Name': name_list,
    'Phone_number': phone_list,
    'Place': phone_list,
    'Temperature': temp_list
}

# Creating dataframe from the data
df = pd.DataFrame(data)

# Convert dataframe to .csv file
df.to_csv('Data.csv')
