"""
Creates and compares AI-Generated and expected XML data.

This script tests our model by comparing generated output from our fine-tuned model to expected output.
"""

from openai import OpenAI
import sys
import pandas as pd
import json

# GET AI GENERATED XML CODE

if len(sys.argv) < 2:
    print("Usage: python myscript.py <your_argument>")
    sys.exit(1)

# pass api_key in command line
key = sys.argv[1]

# get JSON data inputs from file
with open("run_model_with_json.json", "r", encoding="utf-8") as f:
    json_data_inputs = json.load(f)

client = OpenAI(api_key=key)

ai_xml_list = []

# call the AI model for JSON records and record its outputs
for i, record in enumerate(json_data_inputs, start=1):
    response = client.responses.create(
        model="ft:gpt-4.1-nano-2025-04-14:ah-personal-testing::C4XtP2oh",
        temperature=0,
        input=[
            {
                "role": "system",
                "content": "Your role is to convert JSON data to XML data."
            },
            {
                "role": "user",
                "content": f"Here is the JSON data input: {json.dumps(record)}"
            }
        ]

    )

    ai_response = response.output[0].content[0].text

    # parse ai-generated xml code
    ai_xml = ai_response[29:]

    ai_xml_list.append(ai_xml)


# GET EXPECTED XML CODE

file_path = "C:/Users/u001m/Hen Street Hacks/mock_personal_info_2nd_set.xlsx"

df = pd.read_excel(file_path,  engine="openpyxl")


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

expected_xml = ""

expected_xml_list = []

for index, row in df.iterrows():
    # Collect all fields from the row
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


    expected_xml = f"<address><line1>{line1}</line1><line2>{line2}</line2><city>{city}</city><region>{region}</region><zipcode>{zipcode}</zipcode><country>{country}</country></address><personal_details><first_name>{first_name}</first_name><last_name>{last_name}</last_name><birth_date>{birth_date}</birth_date><phone_numbers>{phone_numbers}</phone_numbers><email>{email}</email></personal_details>"

    expected_xml_list.append(expected_xml)

passing_count = 0
failing_count = 0

# compare AI-Generated and expected XML data produced
if len(expected_xml_list) == len(ai_xml_list):
    for index in range(len(expected_xml_list)):
        expected_xml = expected_xml_list[index]
        ai_xml = ai_xml_list[index]

        if ai_xml == expected_xml:
            passing_count += 1
            print("PASS: AI-Generated code matches Expected code.\n")
            print(f"Expected XML:\n{expected_xml}\n")
            print(f"AI-Generated XML:\n{ai_xml}\n")
            print("----------------------------------------------------------------\n")
        else:
            failing_count += 1
            print("FAIL: AI-Generated code does NOT match Expected code.\n")
            print(f"Expected XML:\n{expected_xml}\n")
            print(f"AI-Generated XML:\n{ai_xml}\n")
            print("----------------------------------------------------------------\n")


print(f"Passing Count = {passing_count}")
print(f"Failing Count = {failing_count}")