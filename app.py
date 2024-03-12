import requests
import json

url = "http://localhost:11434/api/generate"  # Assuming your API endpoint is at this URL
prompt = "Write Python code to print a number less than 10"  # Clear and concise prompt

headers = {
    'Content-Type': 'application/json'  # Corrected typo in header key
}

def generate_response(prompt):
    data = {
        "model": "codeguru",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("response sucees") # Print full response for debugging

        data = json.loads(response.text)
        return data['response']
    else:
        print("Error:", response.text)  # Print error message for troubleshooting
        return None  # Indicate error by returning None

result = generate_response(prompt=prompt)

if result:
    print("Generated Python code:")
    print(result)
else:
    print("An error occurred while generating the code. Please check your API connection or prompt.")
