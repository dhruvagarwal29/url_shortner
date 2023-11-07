from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

import string
import random

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = '*****.mysql.****.com'
app.config['MYSQL_USER'] = '******'
app.config['MYSQL_PASSWORD'] = '*****'
app.config['MYSQL_DB'] = '*****$url_shortner'

db = MySQL(app)



# Making short URLs
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(1))

# Create the 'url' table when the application starts
with app.app_context():
    cursor = db.connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS url (
        id INT AUTO_INCREMENT PRIMARY KEY,
        short_url VARCHAR(1) UNIQUE NOT NULL,
        original_url VARCHAR(2048) NOT NULL
    )
    """)
    cursor.close()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']

    cursor = db.connection.cursor()

    cursor.execute("SELECT short_url FROM url WHERE original_url = %s", (original_url,))
    existing_url = cursor.fetchone()

    if existing_url:
        short_url = existing_url[0]
    else:
        short_url = generate_short_url()
        cursor.execute("INSERT INTO url (short_url, original_url) VALUES (%s, %s)", (short_url, original_url))
        db.connection.commit()

    cursor.close()

    return render_template("shortened_url.html",
                           shortened_url=request.url_root + short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    cursor = db.connection.cursor()
    cursor.execute("SELECT original_url FROM url WHERE short_url = %s", (short_url,))
    url = cursor.fetchone()

    if url:
        original_url = url[0]
        cursor.close()
        return redirect(original_url)

    cursor.close()
    return "URL not found"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
