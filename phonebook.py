

# Create the initial customer dictionary
customer = {'name': 'Orwell', 'address': '4 Church St', 'age': '46'}

# Find and print the customer's address
print(customer['address'])

#  Add a new key-value for birthday
customer['birthday'] = '25 June'

# Change the value associated with 'name'
customer['name'] = 'Orwell, George'

#  Print the updated customer dictionary
print(customer)


# If the dictionary is in the format of a nested dictionary
customer_nested = {
    1: {'name': 'Orwell', 'address': '4 Church St', 'age': '46'},
    2: {'name': 'Cicero', 'address': '11 Carmine St', 'age': '63'}
}

# You can still follow the same steps for Part A
customer_nested[1]['name'] = 'Orwell, George'
customer_nested[1]['birthday'] = '25 June'
print(customer_nested)


#  Create the initial phonebook dictionary
phonebook = {
    'Euclid': {'number': '212.479.2851'},
    'Pythagoras': {'number': '212.479.4653'},
    'Avicenna': {'number': '212.892.1234'},
    'Descartes': {'number': '917.372.1650'}
}

#  Use the get function to search for Newton in the phonebook
newton_number = phonebook.get('Newton', 'Name not found')
print(newton_number)

#  Add Newton to the phonebook if not found
if newton_number == 'Name not found':
    phonebook['Newton'] = {'number': '917.364.1727'}

#  Change Avicenna's phone number
phonebook['Avicenna']['number'] = '212.472.1037'

#  Remove Descartes from the phonebook
phonebook.pop('Descartes', None)

#  Print each name and number using a for loop
for name, details in phonebook.items():
    print(f'{name} {details["number"]}')


#  Add the area code for each person to the phonebook
for name, details in phonebook.items():
    area_code = details['number'][:3]
    details['areaCode'] = area_code

print(phonebook)

#  Reverse lookup for '212.479.4653'
for name, details in phonebook.items():
    if details['number'] == '212.479.4653':
        print(f"The name associated with 212.479.4653 is: {name}")
        break


#  Create a data frame from the phonebook dictionary
#df = pd.DataFrame(phonebook).T

#  Print the data frame
#print(df)
