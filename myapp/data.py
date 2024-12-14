import requests

# Create a session to persist cookies (including CSRF token)
session = requests.Session()

# URL of your API endpoint
url = "http://127.0.0.1:8000/api/transfer/?user_id=46"

# Perform a GET request to obtain the CSRF token
get_response = session.get(url)  # This will set the CSRF token in the session cookies

# Print the response from the GET request for debugging
print("GET response status:", get_response.status_code)
print("GET response cookies:", session.cookies)  # Check all cookies

# Prepare your payload
payload = {
    "target_phone": "1234567890",
    "amount": "100"
}

# Get the CSRF token from the session cookies
csrf_token = session.cookies.get('csrftoken')
print("CSRF Token:", csrf_token)  # Print CSRF token for debugging

# Prepare headers with the CSRF token
headers = {'X-CSRFToken': csrf_token}

# Send the POST request
response = session.post(url, data=payload, headers=headers)

# Print the response from the server
print("POST response status:", response.status_code)
print("POST response text:", response.text)
