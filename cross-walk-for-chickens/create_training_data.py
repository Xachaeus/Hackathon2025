"""
Organizes data to use for finetuning.

This script takes data from an Excel file and converts it into JSON and XML data.
Then, it organizes this data into a JSONL file format that can be passed to OpenAI to fine tune an AI model.
"""

import pandas as pd
import json

file_path = "C:/Users/u001m/Hen Street Hacks/mock_personal_info_revised.xlsx" # put data file path here

df = pd.read_excel(file_path,  engine="openpyxl")

with open("training_data.jsonl", "w", encoding="utf-8") as f:  # <-- open file here

    # declare fields to be populated
    line1 = ""
    line2 = ""
    city = ""
    region = ""
    zipcode = ""
    country = ""

    first_name = ""
    last_name = ""
    birth_date = ""
    phone_numbers = ""
    email = ""
    tax_id = ""

    full_record = []

    # iterate through each row of the excel data sheet and create a JSON and XML record for each row
    for index, row in df.iterrows():
        city = row.get("city", "")
        country = row.get("country_code", "")
        zipcode = row.get("postal_code", "")
        region = row.get("region_code", "")
        line1 = row.get("street_address", "")
        line2 = row.get("street_address_2", "")
        birth_date = row.get("birth_date", "")
        email = row.get("email", "")
        first_name = row.get("first_name", "")
        last_name = row.get("last_name", "")
        phone_numbers = row.get("phone_numbers", "")
        tax_id = row.get("tax_id", "")

        json_data = {
            "address": [
                {
                    "line1": str(line1),
                    "line2": str(line2),
                    "city": str(city),
                    "region": str(region),
                    "zipcode": str(zipcode),
                    "country": str(country)
                }
            ],
            "personal_details": [
                {
                    "first_name": str(first_name),
                    "last_name": str(last_name),
                    "birth_date": str(birth_date),
                    "phone_numbers": str(phone_numbers),
                    "email": str(email),
                    "tax_id": str(tax_id)
                }
            ]
        }

        json_string = json.dumps(json_data)

        xml_data = f"<address><line1>{line1}</line1><line2>{line2}</line2><city>{city}</city><region>{region}</region><zipcode>{zipcode}</zipcode><country>{country}</country></address><personal_details><first_name>{first_name}</first_name><last_name>{last_name}</last_name><birth_date>{birth_date}</birth_date><phone_numbers>{phone_numbers}</phone_numbers><email>{email}</email></personal_details>"

        # create a new record to add to the JSONL training data file
        new_record = {
            "messages": [
                {"role": "system", "content": "Your role is to convert JSON data to XML data."},
                {"role": "user", "content": f"Here is the JSON data input: {json_string}"},
                {"role": "assistant", "content": f"Here is the XML data output: {xml_data}"}
            ]
        }

        f.write(json.dumps(new_record) + "\n")

print("Training data created in training_data.jsonl file.")

