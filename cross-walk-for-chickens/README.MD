---------------------------
create_training_data.py
---------------------------
Organizes data to use for finetuning.

This script takes data from an Excel file and converts it into JSON and XML data.
Then, it organizes this data into a JSONL file format that can be passed to OpenAI to fine tune an AI model.

To run, press the run button on your IDE.

---------------------------
create_json_for_testing.py
---------------------------
Creates JSON data for testing/verification purposes.

After training the AI model using fine tuning, we tested it by giving it JSON data and comparing it's XML format
response to the response we would expect.

This script takes in a second dataset Excel file and converts the data into JSON format in a file called run_model_with_json.json.

To run, press the run button on your IDE.

---------------------------
verification.py
---------------------------
Creates and compares AI-Generated and expected XML data.

This script tests our model by comparing generated output from our fine-tuned model to expected output.

To run, use the following command in the terminal
```python verification.py <OPENAI KEY>```
