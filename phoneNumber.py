import phonenumbers
from phonenumbers import timezone, geocoder, carrier
num=input("ENTER PHONE NUMBER PLEASE: ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
Carrier=carrier.name_for_number(phone,"en")
Location=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(Carrier)
print(Location)