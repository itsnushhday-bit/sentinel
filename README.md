# Sentinel: A Smart Email Notifier

## 1. Problem Statement
Professionals and job applicants receive a high volume of emails daily, creating a significant risk of missing critical, time-sensitive information like interview invitations and project deadlines. This leads to missed opportunities and increased stress.

## 2. Proposed Solution
Sentinel is a lightweight Python service that connects to a user's Gmail account. It intelligently scans incoming emails for keywords related to urgency and opportunity, sending instant desktop notifications for only the most important messages.

## 3. Demo
https://github.com/itsnushhday-bit/sentinel/blob/main/Screenshot%202025-09-17%20135351.png?raw=true

## 4. Key Features
* Securely authenticates with any Google Account using OAuth 2.0.
* Fetches recent emails in real-time via the Gmail API.
* Scans email subjects for a customizable list of keywords (e.g., "interview," "google meet," "link").
* Generates native desktop notifications for high-priority emails.

## 5. Technical Architecture
The MVP is built with Python and leverages the official Google Client Library. Key technologies include:
* **Backend:** Python
* **API:** Google Gmail API (OAuth 2.0)
* **Notifications:** Plyer, win10toast
