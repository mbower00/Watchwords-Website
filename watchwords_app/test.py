import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(receiver_email_address, sender_password):
    """Sends an email to the specified address with the contents of the specified file

    Args:
    : the word+color dictionary ready to be sent to the html 
        color_word_key (dict): the color - words answers
        receiver_email_address (str): receiver's email address (also, the subject of the email, sans ".txt")
        sender_password (str): password for mitchbbowercode@gmail.com (depreciated)
        sender_password (str): password for mitchbbowercode@yahoo.com
    """
    sender_email = "watchwordsgame@gmail.com"

    mail = MIMEMultipart("alternative")
    mail["Subject"] = "WATCHWORDS ANSWERS"
    mail["From"] = sender_email
    # mail["From"] = "mitchbbowercode@yahoo.com"
    mail["To"] = receiver_email_address
    
    text_mail="foo"

    # used code from https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table3
    html_mail = f"""\
        <html>
            <body>
                <table style="border: 2px solid black; width:100%;">
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                    </tr>
                    <tr style="2px solid black; ">
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                        <td style="border: 2px solid black; color:#FFFFFF; font-weight: bold; text-align: center;">foo</td>
                    </tr>
                </table>
            </body>
        </html>
        """

    text_part = MIMEText(text_mail, "plain")
    html_part = MIMEText(html_mail, "html")
    
    mail.attach(text_part)
    mail.attach(html_part)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email_address, mail.as_string())


send_email("mitchbbower@gmail.com", "kfgpqsmyupviwdxm")