# -*- coding: utf-8 -*-
import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_location(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)

        location = geocoder.description_for_number(parsed_number, 'en')
        service_provider = carrier.name_for_number(parsed_number, 'en')

        return location, service_provider
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error:", e)
        return None, None

def get_name_from_phone_number(phone_number):
    # Simüle edilmiş bir veritabanı / bilgi tabanı
    phonebook = {
        "+905378286585": "Berkay Sanal"
        # Buraya istediğiniz başka telefon numaraları ve ad-soyad bilgileri ekleyebilirsiniz
    }

    # Telefon numarasını temizle
    parsed_number = phonenumbers.parse(phone_number, None)
    cleaned_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    # Telefon numarasına göre ad-soyad bilgisini kontrol et
    if cleaned_number in phonebook:
        return phonebook[cleaned_number]
    else:
        return "not found"

# Kullanıcıdan telefon numarasını al
phone_number = input("Enter the phone number with country code: ")

# Telefon numarasıyla ilgili bilgileri al
location, service_provider = get_phone_location(phone_number)
name = get_name_from_phone_number(phone_number)

# Sonuçları göster
print(f"Location: {location}")
print(f"Service Provider: {service_provider}")
print(f"Name: {name}")
