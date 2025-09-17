import os.path
from plyer import notification # Import the new library

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
IMPORTANT_KEYWORDS = ["interview", "deadline", "urgent", "security", "alert", "verification", "offer", "application", "google meet" "congratulations"]

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me", maxResults=10).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No new messages found.")
            return
        
        print("Scanning recent emails for important keywords...")
        found_important_email = False
        for message in messages:
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()
            headers = msg["payload"]["headers"]
            subject = next((d['value'] for d in headers if d['name'] == 'Subject'), None)

            if subject:
                if any(keyword in subject.lower() for keyword in IMPORTANT_KEYWORDS):
                    print(f"\n!!! IMPORTANT EMAIL FOUND !!!")
                    print(f"Subject: {subject}")
                    
                    # --- THIS IS THE NEW CODE FOR THE NOTIFICATION ---
                    notification.notify(
                        title='Important Email Found!',
                        message=f'Subject: {subject}',
                        app_name='Sentinel',
                        timeout=10  # Notification will stay for 10 seconds
                    )
                    # --------------------------------------------------
                    
                    found_important_email = True
        
        if not found_important_email:
            print("No important emails found in the last 10 messages.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()