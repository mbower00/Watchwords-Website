from django.shortcuts import render

# COLOR PALLETTE (From: https://coolors.co)
RED = "#C1292E"
# RED = "#e83151"
BLUE = "#235789"
# BLUE = "#387780"
YELLOW = "#F1D302"
# YELLOW = "#d2cca1"
WHITE = "#FDFFFC"
# OFFWHITE = "#dbd4d3"
BLACK = "#161925"
# BLACK = "#757780"
CARD_WHITE = "#dbd4d3"

#global list of word packs to be used
word_packs = []
#global list of email addresses to send the answers to
email_addresses = []

# global dict with data to pass to home.html
html_ready_home_info = {
    "css_ref": ".\static\home.css",
    "word_packs": word_packs,
    "email_addresses": " --- ",
    "classic_back": CARD_WHITE,
    "classic_text": BLACK,
    "pride_back": CARD_WHITE,
    "pride_text": BLACK,
    "pres_back": CARD_WHITE,
    "pres_text": BLACK,
    "lotr_back": CARD_WHITE,
    "lotr_text": BLACK,
    "dune_back": CARD_WHITE,
    "dune_text": BLACK,
    "star_back": CARD_WHITE,
    "star_text": BLACK,
    "more_words_back": CARD_WHITE,
    "more_words_text": BLACK,
    "famous_back": CARD_WHITE,
    "famous_text": BLACK,
}

# converts list of email addresses to a string of them concatenated together (e.g. " --- EMAIL@EMAIL.com --- EMAIL@EMAIL.com --- ")
def convert_email_list_to_string(email_addresses):
    result = " --- "
    if email_addresses:
        for i in email_addresses:
            result += i + " --- "
    return result

# converts a color string to the color from the palette
def convert_color_to_code(color:str):
    color = color.lower()
    color = color.strip()
    if color == "red":
        return RED
    elif color == "blue":
        return BLUE
    elif color == "yellow":
        return YELLOW
    elif color == "black":
        return BLACK


# gets the words from the data base, assigns colors, sends the answer email to the addresses (stored in a global), and loads up the game.htmt (passing data to it)
def start_game(request):
    global fireman
    global comissioner
    global word_packs
    global email_addresses
    comissioner.generate_watchwords(word_packs, fireman)
    for i in comissioner.color_word_key:
        starting_color = convert_color_to_code(comissioner.color_word_key[i])
        break
    html_ready_words_and_colors = {
        "startingColor":starting_color,
        "1c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[0]]), "1w":comissioner.watchwords[0],
        "2c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[1]]), "2w":comissioner.watchwords[1],
        "3c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[2]]), "3w":comissioner.watchwords[2],
        "4c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[3]]), "4w":comissioner.watchwords[3],
        "5c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[4]]), "5w":comissioner.watchwords[4],
        "6c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[5]]), "6w":comissioner.watchwords[5],
        "7c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[6]]), "7w":comissioner.watchwords[6],
        "8c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[7]]), "8w":comissioner.watchwords[7],
        "9c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[8]]), "9w":comissioner.watchwords[8],
        "10c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[9]]), "10w":comissioner.watchwords[9],
        "11c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[10]]), "11w":comissioner.watchwords[10],
        "12c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[11]]), "12w":comissioner.watchwords[11],
        "13c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[12]]), "13w":comissioner.watchwords[12],
        "14c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[13]]), "14w":comissioner.watchwords[13],
        "15c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[14]]), "15w":comissioner.watchwords[14],
        "16c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[15]]), "16w":comissioner.watchwords[15],
        "17c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[16]]), "17w":comissioner.watchwords[16],
        "18c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[17]]), "18w":comissioner.watchwords[17],
        "19c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[18]]), "19w":comissioner.watchwords[18],
        "20c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[19]]), "20w":comissioner.watchwords[19],
        "21c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[20]]), "21w":comissioner.watchwords[20],
        "22c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[21]]), "22w":comissioner.watchwords[21],
        "23c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[22]]), "23w":comissioner.watchwords[22],
        "24c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[23]]), "24w":comissioner.watchwords[23],
        "25c":convert_color_to_code(comissioner.color_word_key[comissioner.watchwords[24]]), "25w":comissioner.watchwords[24],
    }
    global password
    if email_addresses:
        for i in email_addresses:
            email_file(html_ready_words_and_colors, comissioner.color_word_key, i, password)
    starting_color = ""
    return render(request, "game.html", html_ready_words_and_colors)

# loads the home.html file with the correct path to the home.css file passed in
def home_start(request):
    global html_ready_home_info
    html_ready_home_info["css_ref"] =  ".\static\home.css"
    return render(request, "home.html", html_ready_home_info)

# gives a random color pair from:
# [RED, WHITE]
# [YELLOW, BLACK]
# [BLUE, WHITE]
# or [CARD_WHITE, BLACK] if is_vanilla=False
def rand_color_pack(is_vanilla=False):
    if is_vanilla:
        return [CARD_WHITE, BLACK]
    rand = randint(1,3)
    if rand == 1:
        return [RED, WHITE]
    elif rand == 2:
        return [BLUE, WHITE]
    elif rand == 3:
        return [YELLOW, BLACK]

# toggles including the Classic pack, changes the color, gives home.html the correct path to the home.css file
def toggle_classic(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "classic" in word_packs:
        word_packs.remove("classic")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["classic_back"] = color_pack[0]
        html_ready_home_info["classic_text"] = color_pack[1]
    else:
        word_packs.append("classic")
        color_pack = rand_color_pack()
        html_ready_home_info["classic_back"] = color_pack[0]
        html_ready_home_info["classic_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Lord of the Rings pack, changes the color, gives home.html the correct path to the home.css file
def toggle_lotr(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "lotr" in word_packs:
        word_packs.remove("lotr")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["lotr_back"] = color_pack[0]
        html_ready_home_info["lotr_text"] = color_pack[1]
    else:
        word_packs.append("lotr")
        color_pack = rand_color_pack()
        html_ready_home_info["lotr_back"] = color_pack[0]
        html_ready_home_info["lotr_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Pride and Prejudice pack, changes the color, gives home.html the correct path to the home.css file
def toggle_pride(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "pride_and_prejudice" in word_packs:
        word_packs.remove("pride_and_prejudice")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["pride_back"] = color_pack[0]
        html_ready_home_info["pride_text"] = color_pack[1]
    else:
        word_packs.append("pride_and_prejudice")
        color_pack = rand_color_pack()
        html_ready_home_info["pride_back"] = color_pack[0]
        html_ready_home_info["pride_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Countries pack, changes the color, gives home.html the correct path to the home.css file
def toggle_countries(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "countries" in word_packs:
        word_packs.remove("countries")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["countries_back"] = color_pack[0]
        html_ready_home_info["countries_text"] = color_pack[1]
    else:
        word_packs.append("countries")
        color_pack = rand_color_pack()
        html_ready_home_info["countries_back"] = color_pack[0]
        html_ready_home_info["countries_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Presidents pack, changes the color, gives home.html the correct path to the home.css file
def toggle_presidents(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "presidents" in word_packs:
        word_packs.remove("presidents")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["presidents_back"] = color_pack[0]
        html_ready_home_info["presidents_text"] = color_pack[1]
    else:
        word_packs.append("presidents")
        color_pack = rand_color_pack()
        html_ready_home_info["presidents_back"] = color_pack[0]
        html_ready_home_info["presidents_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Star Wars pack, changes the color, gives home.html the correct path to the home.css file
def toggle_star(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "star_wars" in word_packs:
        word_packs.remove("star_wars")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["star_back"] = color_pack[0]
        html_ready_home_info["star_text"] = color_pack[1]
    else:
        word_packs.append("star_wars")
        color_pack = rand_color_pack()
        html_ready_home_info["star_back"] = color_pack[0]
        html_ready_home_info["star_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the Dune pack, changes the color, gives home.html the correct path to the home.css file
def toggle_dune(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "dune" in word_packs:
        word_packs.remove("dune")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["dune_back"] = color_pack[0]
        html_ready_home_info["dune_text"] = color_pack[1]
    else:
        word_packs.append("dune")
        color_pack = rand_color_pack()
        html_ready_home_info["dune_back"] = color_pack[0]
        html_ready_home_info["dune_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

# toggles including the More Words pack, changes the color, gives home.html the correct path to the home.css file
def toggle_more_words(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "more_words" in word_packs:
        word_packs.remove("more_words")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["more_words_back"] = color_pack[0]
        html_ready_home_info["more_words_text"] = color_pack[1]
    else:
        word_packs.append("more_words")
        color_pack = rand_color_pack()
        html_ready_home_info["more_words_back"] = color_pack[0]
        html_ready_home_info["more_words_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)

def toggle_famous(request):
    global html_ready_home_info
    global word_packs
    global calls
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    if "famous_people" in word_packs:
        word_packs.remove("famous_people")
        color_pack = rand_color_pack(is_vanilla=True)
        html_ready_home_info["famous_back"] = color_pack[0]
        html_ready_home_info["famous_text"] = color_pack[1]
    else:
        word_packs.append("famous_people")
        color_pack = rand_color_pack()
        html_ready_home_info["famous_back"] = color_pack[0]
        html_ready_home_info["famous_text"] = color_pack[1]
    return render(request, "home.html", html_ready_home_info)


def reset_emails(request):
    global html_ready_home_info
    global email_addresses
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    email_addresses.clear()
    html_ready_home_info["email_addresses"] = " --- "
    return render(request, "home.html", html_ready_home_info)

# used code from https://www.w3schools.com/django/django_add_record.php
def add_email(request):
    global html_ready_home_info
    global email_addresses
    html_ready_home_info["css_ref"] =  "..\static\home.css"
    email_addresses.append(request.POST["email_address"])
    html_ready_home_info["email_addresses"] = convert_email_list_to_string(email_addresses)
    return render(request, "home.html", html_ready_home_info)
























# EMAILING:

# used code from https://realpython.com/python-send-email/ and https://www.w3schools.com/html/html_tables.asp and https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table3
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def email_file(html_ready_words_and_colors, color_word_key, receiver_email_address, sender_password):
    """Sends an email to the specified address with the contents of the specified file

    Args:
        html_ready_words_and_colors (dict): the word+color dictionary ready to be sent to the html 
        color_word_key (dict): the color - words answers
        receiver_email_address (str): receiver's email address (also, the subject of the email, sans ".txt")
        sender_password (str): password for mitchbbowercode@gmail.com (depreciated)
        sender_password (str): password for mitchbbowercode@yahoo.com
    """
    global sender_email

    mail = MIMEMultipart("alternative")
    mail["Subject"] = "WATCHWORDS ANSWERS"
    mail["From"] = sender_email
    mail["To"] = receiver_email_address
    
    text_mail=""
    for i in color_word_key:
        text_mail += f"{i} | {color_word_key[i]}\n"

    # used code from https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table3
    html_mail = f"""\
        <html>
            <body>
                <table style="border: 2px solid black; width:100%;">
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['1c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['1w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['2c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['2w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['3c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['3w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['4c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['4w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['5c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['5w']}</td>
                    </tr>
                    <tr style="2px solid black; ">
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['6c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['6w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['7c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['7w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['8c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['8w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['9c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['9w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['10c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['10w']}</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['11c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['11w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['12c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['12w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['13c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['13w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['14c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['14w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['15c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['15w']}</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['16c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['16w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['17c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['17w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['18c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['18w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['19c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['19w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['20c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['20w']}</td>
                    </tr>
                    <tr style="border: 2px solid black; ">
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['21c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['21w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['22c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['22w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['23c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['23w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['24c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['24w']}</td>
                        <td style="border: 2px solid black; background-color:{html_ready_words_and_colors['25c']}; color:#FFFFFF; font-weight: bold; text-align: center;">{html_ready_words_and_colors['25w']}</td>
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






















#DATABASE CLASSES (constructed at the end):

# used code from https://firebase.google.com/docs/firestore/
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Fireman:
    """The Fireman is a firebase helper. He provides functionallity for
    for working with the database
    """
    def __init__(self):
        """constructs a new instance of Fireman
        """
        global fire_cert
        firebase_admin.initialize_app(credentials.Certificate(fire_cert))
        self.db = firestore.client()
        self.auto_increment_log = {}
    
    def set_data(self, collection, value, document="ai", key="word"):
        """set a record to the database. 
        If document="ai", it will auto increment according to the 'qty' value stored in the 'info' document.

        Args:
            collection (string): the collection to add to
            value (_type_): the value to set
            document (string): the document to add to. Defaults to "ai".
            key (string): the key for the value. Defaults to "word".
        """
        if document == "ai":
            document = self.auto_increment(collection)
        self.db.collection(collection).document(document).set({key : value})
    
    def add_to_data(self, collection, document, value, key="word"):
        """adds the value to the selected value in the database

        Args:
            collection (string): the collection to add to
            document (string): the document to add to.
            value (_type_): the value to add
            key (str, optional): the key of the value to add to. Defaults to "word".
        """
        added_value = self.get_data(collection, document, key=key) + value
        self.set_data(collection, added_value, document=document)

    def delete_document_and_shift(self, collection, document):
        """deletes a specified document and shifts to next documents' ID back one to fill in the space (by deleting and setting).
        Also, updates the 'qty' value stored in the 'info' document

        Args:
            collection (string): the collection 
            document (string): the document 
        """
        self._delete_single_document(collection, document)
        qty = int(self.get_data(collection, document="info", key="qty"))
        if str(qty) != document:
            for i in range(int(document)+1, qty+1):
                i = str(i) 
                value = self.get_data(collection, i)
                self._delete_single_document(collection, i)
                self.set_data(collection, value, document=str(int(i)-1))
        self.set_data(collection, str(qty-1), document="info", key="qty") #update the info document

    def _delete_single_document(self, collection, document):
        """deletes a single document.
        DOES NOT SHIFT IDS

        Args:
            collection (string): the collection 
            document (string): the document 
        """
        self.db.collection(collection).document(document).delete()

    def delete_collection(self, collection):
        """deletes a collection.
        Only will work if all documents are 1 through qty (the "info" document) plus the "info" document.

        Args:
            collection (string): the collection 
        """
        qty = int(self.get_data(collection, document="info", key="qty"))
        for i in range(1, qty+1):
            i = str(i)
            self._delete_single_document(collection, i)
        self._delete_single_document(collection, "info")

    def get_data(self, collection, document, key="word"):
        """get the value at location

        Args:
            collection (str): the collection from which to get data
            document (str): the document from which to get data
            key (str, optional): the key from which to get data. Defaults to "word".

        Returns:
            _type_: the value at the key
        """
        doc = self.db.collection(collection).document(document).get()
        if doc.exists:
            return doc.to_dict()[key]

    def get_all_words_from_collection(self, collection):
        """gets all the watchwords and their IDs from a collection

        Args:
            collection (str): the collection from which to get data

        Returns:
            dict{ID: watchword (NOTE: may be multiple words in one string)}: A dictionarry with all the watchwords and their IDs from a collection
        """
        result = {}
        qty = int(self.get_data(collection, document="info", key="qty"))
        for i in range(1, qty+1):
            result[str(i)] = self.get_data(collection, str(i))
        return result

    def auto_increment(self, collection):
        """gets an auto incremented value according to the passed collection

        Args:
            collection (string): the current collection

        Returns:
            int: an auto incremented number according to the current selection
        """
        doc = self.db.collection(collection).document("info").get()
        if doc.exists:
            new_value = str(int(self.get_data(collection, "info", key="qty")) + 1)
            self.set_data(collection, new_value, document="info", key="qty")
        else:
            new_value = "1"
            self.set_data(collection, new_value, document="info", key="qty")
        return new_value

from random import randint
from random import shuffle

class Comissioner:
    """The Comissioner provides functionallity for choosing watchwords from the database and assigning them colors for gameplay.
    """
    def __init__(self):
        """constructs a new instance of Comissioner
        """
        self.watchword_ids = {}
        self.watchwords = []
        self.color_word_key = {}
    
    def generate_watchwords(self, collections, fireman):
        """generates 25 watchwords for the game. It trys to get at least one from each collection and make no duplicates
        These are stored in the member list: watchwords. 
        Also, assigns color values to the watchwords. These are stored in the member dictionary: color_word_key.

        Args:
            collections (list): the collections from which to pull watchwords
            fireman (Fireman): the Fireman object
        """
        self.color_word_key = {}
        self.watchwords = [] # reset watchwords
        results = []
        self._decide_words(collections, fireman)
        for i in collections:
            for j in self.watchword_ids[i]:
                data = fireman.get_data(i, j)
                while data in results:
                    data = fireman.get_data(i, self._get_new_word_id(i, fireman))
                results.append(data)
        shuffle(results)
        self.watchwords = results
        self._generate_color_word_key()
        self.watchword_ids = {} # reset watchword_ids for future use

    def _decide_words(self, collections, fireman):
        """gets 25 watchwords IDs for the game. It trys to get at least one from each collection
        These are stored in the member dictionary: watchword_ids.

        Args:
            collections (list): the collections from which to pull watchwords
            fireman (Fireman): the Fireman object
        """
        qtys = []
        for i in collections:
            qtys.append(fireman.get_data(i, "info", key="qty"))
            self.watchword_ids[i] = []
        is_giving_each_collection_a_chance = True
        collection_counter_index = 0
        for _ in range(25):
            if collection_counter_index > len(collections)-1:
                is_giving_each_collection_a_chance = False
            if is_giving_each_collection_a_chance:
                collection_index = collection_counter_index
                document_id = randint(1, int(qtys[collection_index]))
                self.watchword_ids[collections[collection_index]].append(str(document_id))
                collection_counter_index += 1
            else:
                is_trying = True
                while is_trying:
                    collection_index = randint(0, len(collections)-1)
                    document_id = str(randint(1, int(qtys[collection_index])))
                    if not document_id in self.watchword_ids[collections[collection_index]]: #if it is not already in the watchword_ids dict
                        self.watchword_ids[collections[collection_index]].append(str(document_id))
                        is_trying = False
                    else:
                        is_trying = True
        
    def _get_new_word_id(self, collection, fireman):
        """gets a new watchword ID that is not already in the member list: watchword_ids[collection]

        Args:
            collection (str): the collection from which to get a new watchword ID
            fireman (Fireman): the Fireman object

        Returns:
            str: new watchword ID that is not already in the member list: watchword_ids[collection]
        """
        is_trying = True
        while is_trying:
            current_list = self.watchword_ids[collection]
            qty = fireman.get_data(collection, "info", key="qty")
            document_id = str(randint(1, int(qty)))
            if not document_id in current_list: #if it is not already in the watchword_ids dict
                return document_id
            else:
                is_trying = True
    
    def _generate_color_word_key(self):
        """assigns a color to each of the words. Also, decides who starts. There will be 8 reds, 8 blues, 7 yellows, 1 black, 
        and a extra red or blue according to who starts.
        """
        words = list(self.watchwords)
        starting_player_code = randint(1,2)
        if starting_player_code == 1:
            starting_player = "red"
            self.color_word_key[words.pop()] = "red"
            for _ in range(8):
                self.color_word_key[words.pop()] = "red"
            for _ in range(8):
                self.color_word_key[words.pop()] = "blue"
        else:
            starting_player = "blue"
            self.color_word_key[words.pop()] = "blue"
            for _ in range(8):
                self.color_word_key[words.pop()] = "blue"
            for _ in range(8):
                self.color_word_key[words.pop()] = "red"
        
        self.color_word_key[words.pop()] = "black"

        for _ in range(7):
            self.color_word_key[words.pop()] = "yellow"

        shuffle(self.watchwords) # shuffle at the end











# ===========================================================================
#                                   PRIVATE DATA:

# ===========================================================================










#MORE GLOBALS:

# construct the Fireman and Comissioner to be used as globals
fireman = Fireman()
comissioner = Comissioner()