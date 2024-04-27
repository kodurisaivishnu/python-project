import phonenumbers
from phonenumbers import geocoder,carrier
phone=input('ENTER YOUR PHONE NUMBER [must contain country code]: ')
int(phone)
number=phonenumbers.parse(phone)
carrier=carrier.name_for_number(number,'en')
region=geocoder.description_for_number(number,'en')

print(carrier)
print(region)