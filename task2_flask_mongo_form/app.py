from flask import Flask, render_template, request, redirect, url_for
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi
from pymongo.errors import PyMongoError

load_dotenv()

uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Create / use database and collection
db = client["flask_db"]  # Database name
collection = db["users"]  # Collection name

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except PyMongoError as e:
            return render_template('form.html', error=str(e))
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
