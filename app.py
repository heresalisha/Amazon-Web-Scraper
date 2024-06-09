from flask import *
from scraper import scrape
import sqlite3
from sqlite3.dbapi2 import connect
import os

DATABASE_URL = os.getcwd().replace("\\","/") + '/products.db'

def connectDB(URL):
    connection = sqlite3.connect(URL)
    return connection

def queryDatabase():
    connection = connectDB(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute('SELECT * from urls')
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return records

def deleteRecord(id):
    connection = connectDB(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM urls where id={id}')
    connection.commit()
    cursor.close()
    connection.close()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        connection = connectDB(DATABASE_URL)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO urls (url) VALUES ('{url}')")
        connection.commit()
    return render_template('home.html')

@app.route('/view')
def view():
    PRODUCT_URLS = queryDatabase() 
    data = scrape(PRODUCT_URLS)
    return render_template('view.html',data=data)

@app.route('/urls',methods=['GET','POST'])
def urls():
    if request.method == 'POST':
        data = request.get_json()
        deleteRecord(data['id'])
        return redirect(url_for('view'))
    else:
        urls = queryDatabase() 
        return render_template('urls.html',data=urls,size=len(urls))


if __name__ == '__main__':
    app.run(debug=True)