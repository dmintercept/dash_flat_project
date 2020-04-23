This a my template for a multi page dash app with a flat file structure

Make sure you have virtualenv installed

Create a virtual environment for this directory

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python index.py

This should start the dash app and present a 404 when you visit the local host port

add /app/app1 or /app/app2 to the url pattern to visit the two pages