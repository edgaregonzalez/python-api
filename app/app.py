import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from mysql.connector import Error

load_dotenv()

app = Flask(__name__)

# Database configuration


db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Utility function to connect to the database


def db_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
    except Error as e:
        print(e)
    return conn

# API endpoint to add a new item to the inventory


@app.route('/item', methods=['POST'])
def add_item():
    data = request.get_json()
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO inventory (item_name, quantity, price, description)
        VALUES (%s, %s, %s, %s)
    """, (data['item_name'],data['quantity'],
          data['price'],
          data['description']))
    conn.commit()
    return jsonify(data), 201

# API endpoint to get all items in the inventory


@app.route('/items', methods=['GET'])
def get_items():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    return jsonify(items), 200

# Start the Flask app


if __name__ == '__main__':
    app.run(debug=True)
