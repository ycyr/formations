   from flask import Flask
   import pymysql

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "API Backend en Flask est fonctionnelle 🚀"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)