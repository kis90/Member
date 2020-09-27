from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# database connection details below
app.config['MYSQL_HOST'] = 'database-3.c0iauj5up3v0.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Admin123'
app.config['MYSQL_DB'] = 'probedb1'

# Intialize MySQL
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM memberlogin WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account == None:
            return 'Account not exists'
        else:
            return redirect('/landing')
    msg = ''
    return render_template('index.html', msg='')


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        return redirect('/input1')
    return render_template('landingpage.html', msg='')


@app.route('/input1', methods=['GET', 'POST'])
def input1():
    if request.method == 'POST':
        # Create variables for easy access
        techpt = request.form['Technology Platfornm']
        ospt = request.form['OS Platform']
        cdb = request.form['Connect Database']
        hostn = request.form['DB Host name']
        usern = request.form['DB UserName']
        pwd = request.form['DB Password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO  memberdata (ct1,ct2,dbcon,hostn,usern,pass) VALUES (%s, %s, %s, %s, %s, %s)',
                       (techpt, ospt, cdb, hostn, usern, pwd))
        mysql.connection.commit()
        return redirect('/input2')
    return render_template('input1.html', msg='')


@app.route('/input2', methods=['GET', 'POST'])
def input2():
    if request.method == 'POST':
        # Create variables for easy access
        etlcon = request.form['Connect ETL']
        hostna = request.form['ETL Host name']
        userna = request.form['ETL UserName']
        passw = request.form['ETL Password']
        bitconn = request.form['Connect BiTool']
        hostnam = request.form['BI Host name']
        usernam = request.form['BI UserName']
        passwo = request.form['BI Password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO  memberdata (etlcon,hostna,userna,passw,bitconn,hostnam,usernam,passwo) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)',
            (etlcon, hostna, userna, passw, bitconn, hostnam, usernam, passwo))
        mysql.connection.commit()
        return redirect('/input3')
    return render_template('input2.html', msg='')


@app.route('/input3', methods=['GET', 'POST'])
def input3():
    if request.method == 'POST':
        # Create variables for easy access
        migsuc = request.form['Success Host name']
        growth = request.form['Growth Estimation']
        dataret = request.form['Data Retention']
        dataurch = request.form['Data Archival']
        drst = request.form['DR Strategy']
        prodcp = request.form['Product']
        tdlis = request.form['Teradata License']
        growthper = request.form['Expected Growth']
        etltool = request.form['ETL Tools']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO  memberdata (migsuc,growth,dataret,dataurch,drst,prodcp,tdlis,growthper,etltool) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s)',
            (migsuc, growth, dataret, dataurch, drst, prodcp, tdlis, growthper, etltool))
        mysql.connection.commit()

    return render_template('input3.html', msg='')


if __name__ == '__main__':
    app.run(Debug=True)
