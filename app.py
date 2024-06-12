# app.py
from flask import Flask
import streamlit as st

# Test
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Making update!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)