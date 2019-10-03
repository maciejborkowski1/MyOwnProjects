import email, smtplib, ssl
import os
import datetime
import zipfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Prepare files with specificated types, is always only two files to get
eligibleFiles = []
types = ['.dat','.inf']
# Get todays date and modify to get todays files
today = datetime.date.today()
today = str(today)
today = today.replace('-','')
today = today[4:]
# Get todays files, and add correct extension
for type in types:
    todayType = today + type  
    folder = "c:\\someDirectory"
    folderContent = os.listdir(folder)
    for file in folderContent:
        if file.endswith(todayType):  # add files to the files list
              eligibleFiles.append(file)
print(eligibleFiles)

# Now we check content of list, if is empty we dont have our report, so we send a info message
if eligibleFiles == []:
    port = 465
    smtp_server = "server"
    sender_email = "mail"
    receiver_email = ""
    password = ("")
    message = """\
    Subject: Brak raportu

    Nie odnotowano raportu Nielsena."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login('', password)
        server.sendmail(sender_email, receiver_email, message)
# if list is not empty we pack files to zip, and send it
else:    
    # Get files
    fileOne = eligibleFiles[0]
    fileTwo = eligibleFiles[1]

    # Packing to zip
    newZip = zipfile.ZipFile('DJ063.zip','w')
    newZip.write(fileOne, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

    newZip = zipfile.ZipFile('DJ063.zip','a')
    newZip.write(fileTwo, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

    # Give parameters to get connection
    subject = "Halo dzień dobry"
    body = "Raporcik Nielsena się kłania"
    sender_email = ""
    receiver_email = ""
    password = ""

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "DJ063.zip"  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("", 465, context=context) as server:
        server.login('', password)
        server.sendmail(sender_email, receiver_email, text)
