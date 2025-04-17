import imaplib
import email
from email.header import decode_header

# Login credentials
USERNAME = 'ashiqueat38@gmail.com'
PASSWORD = 'jnlb rcdl ihwb sace'  # Use App Password if 2FA is enabled

# Connect to the Gmail IMAP server
imap_server = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_server)

# Login to the server
mail.login(USERNAME, PASSWORD)

# Select the Spam folder (instead of inbox)
mail.select("inbox")

# Search for all emails in the Spam folder
status, messages = mail.search(None, 'ALL')
email_ids = messages[0].split()

# Number of emails to process
N = 10
for i in email_ids[-N:]:
    # Fetch the email by ID
    res, msg = mail.fetch(i, "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # Parse email bytes to message
            msg = email.message_from_bytes(response[1])

            # Decode subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            # Decode sender
            from_, encoding = decode_header(msg.get("From"))[0]
            if isinstance(from_, bytes):
                from_ = from_.decode(encoding or "utf-8")

            print("From:", from_)
            print("Subject:", subject)
            print("-" * 50)
status,folders=mail.list()
for folder in folders:
    print(folder.decode())

# Logout
mail.logout()
