'''import phonenumbers 

phone_number = phonenumbers.parse("+918639814270") 

valid = phonenumbers.is_valid_number(phone_number) 

possible = phonenumbers.is_possible_number(phone_number) 

print(valid) 

print(possible)'''



#user number jio/country

import phonenumbers 

from phonenumbers import geocoder, carrier 

phoneNumber = phonenumbers.parse("+916301702199") 


Carrier = carrier.name_for_number(phoneNumber, 'en') 

Region = geocoder.description_for_number(phoneNumber, 'en') 

print(Carrier) 

print(Region)


#Program to extract phone numbers from a text 

'''import phonenumbers 

text = "Contact us at +919876543210 or +14691234567"

numbers = phonenumbers.PhoneNumberMatcher(text, "IN") 

for number in numbers: 

    print(number)'''
    
    
    
    # Program to get timezone a phone number 

  

'''import phonenumbers 

from phonenumbers import timezone 


phoneNumber = phonenumbers.parse("+917013305818") 

timeZone = timezone.time_zones_for_number(phoneNumber) 

print(timeZone)'''