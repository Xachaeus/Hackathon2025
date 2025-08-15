"""
Creates JSON data for testing/verification purposes.

After training the AI model using finetuning, we tested it by giving it JSON data and comparing it's XML format
response to the response we would expect.

This script takes in a second dataset Excel file and converts the data into JSON format in a file called run_model_with_json.json.
"""

import pandas as pd
import json

file_path = "C:/Users/u001m/Hen Street Hacks/mock_personal_info_2nd_set.xlsx"

df = pd.read_excel(file_path,  engine="openpyxl")

with open("run_model_with_json.json", "w", encoding="utf-8") as f:

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
    full_json = []

    full_record = []

    # iterate through each row of the excel data sheet and create a JSON record for each row
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

        full_json.append(json_data)

    json.dump(full_json, f)

print(full_json)


