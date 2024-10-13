import requests
import time

# Function to generate a temporary email address
def generate_temporary_email():
    domain = "1secmail.com"
    username = f"user{int(time.time())}"  # Use a timestamp for uniqueness
    email = f"{username}@{domain}"
    return email, username

# Function to check for incoming emails
def check_inbox(username, domain="1secmail.com"):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Returns a list of emails
    return []

# Function to retrieve email content
def get_email_content(username, message_id, domain="1secmail.com"):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return {}

def create_email_wait_for_message():
    # Example Usage
    print("Creating a temporary email and waiting for message. You can exit anytime with Ctrl+C")
    email, username = generate_temporary_email()
    print(f"Temporary Email: {email}")

    seen_messages = set()  # Set to store IDs of seen messages

    while True:
        inbox = check_inbox(username)

        if inbox:
            for message in inbox:
                message_id = message['id']
                if message_id not in seen_messages:  # If message hasn't been seen
                    print(f"New email received: {message['subject']}")
                    email_content = get_email_content(username, message_id)
                    print(f"Email content: {email_content['textBody']}")
                    seen_messages.add(message_id)  # Add message ID to the set

        time.sleep(5)

