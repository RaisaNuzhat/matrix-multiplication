import requests

url = "http://127.0.0.1:5000/multiply"

data = {
    "matrixA": [[1, 2], [3, 4]],
    "matrixB": [[5, 6], [7, 8]]
}

response = requests.post(url, json=data)

# Print status and raw response
print("Status code:", response.status_code)
print("Raw text:", response.text)

# Try JSON only if it's valid
try:
    print("JSON:", response.json())
except Exception as e:
    print("Could not decode JSON:", e)
