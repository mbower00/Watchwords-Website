# Overview

This is a web app version of the popular game: Codenames ([Rules](https://czechgames.com/files/rules/codenames-rules-en.pdf)).

To run:
* run command: py manage.py runserver
* go to http://127.0.0.1:8000/ for the **Home Page**

To play:
* select word pack(s)
* enter email(s)
    * the answers will be sent to these addresses
* click PLAY
* wait for the **Game Page** to show up
* click the game words to reveal their colors
* click RUN BACK to play again
* click HOME to go to the **Home Page**


One purpose in working on this was to grow my skills in Django. I also love the game [Codenames](https://czechgames.com/files/rules/codenames-rules-en.pdf) and wanted to have a digital version to play with friends.

[Software Demo Video](https://youtu.be/6RsB65yzDz8)

# Web Pages

## Home Page
* header
* links to selected different word packs to use
    * colored a color set decided by Python code when activated
* email address input field
* a field that shows the email addresses to use
    * contents come from a global Python list
* a link to reset the email addresses to use
* a link to go to the **Game Page**

## Game Page
* header
    * colored according to the which color team starts the game
* buttons that show the game words
    * words pulled from a cloud database
    * when clicked, the background becomes the color decied by the Python code
* a link to restart the game (words will be pulled from the cloud database again)
* a link to go to the **Home Page**

# Development Environment

I used Visual Studio Code (code editor) with some extensions. I also used Firefox and Google Chrome (web browsers). I also used wireframe.cc for the creation of some wireframes. I used coolors.co for my color palette.

Languages:
* Python (Django uses this)
* HTML (for the pages)
* CSS (for style in the page)
* Javascript (used a very small amount for some logic in changing color of buttons)

Some (not all) of the Libraries used: 
* For the framework:
    * django
* For benefits of getting numbers and scrambling
    * random
* For using a firestore database
    * firebase_admin
* For email
    * ssl
    * smtplib
    * email.mime.text
    * email.mime.multipart


# Useful Websites

* [wireframe|cc](https://wireframe.cc/)
* [firebase](https://console.firebase.google.com/)
* [firebase](https://firebase.google.com/)
* [coolors](https://coolors.co)
* [w3schools](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table3)
* [w3schools](https://www.w3schools.com/html/html_tables.asp)
* [w3schools](https://www.w3schools.com/html/)
* [w3schools](https://www.w3schools.com/css/)
* [w3schools](https://www.w3schools.com/jsref/event_onclick.asp)
* [w3schools](https://www.w3schools.com/jsref/prop_style_backgroundcolor.asp)
* [w3schools](https://www.w3schools.com/tags/tag_button.asp)
* [w3schools](https://www.w3schools.com/js/js_if_else.asp)
* [w3schools](https://www.w3schools.com/django/)
* [w3schools](https://www.w3schools.com/django/django_add_record.php)
* [realpython](https://realpython.com/courses/django-portfolio-project/)
* [realpython](https://realpython.com/get-started-with-django-1/)
* [realpython](https://realpython.com/python-send-email/)
* [django](https://docs.djangoproject.com/en/4.0/)
* [django](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.POST)
* [django](https://docs.djangoproject.com/en/4.0/ref/csrf/)
* [youtube](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
* [youtube](https://www.youtube.com/watch?v=QLL4KzFMfVw)
* [django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
* [sebhastian](https://sebhastian.com/css-not-linking-html/)
* [careerkarma](https://careerkarma.com/blog/python-builtin-function-or-method-is-not-subscriptable/)
* [stackhawk](https://www.stackhawk.com/blog/django-csrf-protection-guide/)
* [portswigger](https://portswigger.net/web-security/csrf)
* [codegrepper](https://www.codegrepper.com/code-examples/python/django+import+file+from+another+directory)
* [git](https://git-scm.com/docs/gitignore)
* [tutorialspoint (maybe)](https://www.tutorialspoint.com/django/index.htm)

# Future Work (More of a Wishlist)

* Add better handling, so that it can handle PLAY getting clicked when there are no word packs selected
* Get the app publicly hosted
* Add more word packs