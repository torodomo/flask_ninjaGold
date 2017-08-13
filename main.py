from flask import Flask, render_template, request, url_for, redirect, session, flash
import random
import datetime

app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret'

# import the random module
# The random module has many useful functions. This is one that gives a random number in a range
# random.randrange(0, 101) 
# # random number between 0-100


# session['someKey'] = 50
# Remove something from session like so:
# session.pop('someKey')


@app.route('/')                                                                    
def index():
    # Initialise the counter, or increment it
    session['total_gold'] = 0
    print session['total_gold']
    session['message'] = []
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def ProcessMoney():
    # Every time hit the button
    if request.form['building'] == 'farm':
        sumGoldIncrease1()

    elif request.form['building'] == 'cave':   
        sumGoldIncrease2()
        
    elif request.form['building'] == 'house':
        sumGoldIncrease3()

    elif request.form['building'] == 'casino':
        sumGoldGainLose()
        
    return render_template('index.html') 

def sumGoldIncrease1():
    # Farm setting
    result1 = int(random.randrange(10, 21))
    session['total_gold'] += result1
    print session['total_gold']
    print "farm"
    session['message'].append ("Earned " + str(result1) + " gold from the farm!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return render_template('index.html')

def sumGoldIncrease2():
    # Cave setting
    result2 = int(random.randrange(5, 11))
    session['total_gold'] += result2
    print session['total_gold']
    print "cave"
    session['message'].append ("Earned " + str(result2) + " gold from the cave!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return render_template('index.html')

def sumGoldIncrease3():
    # House setting
    result3 = int(random.randrange(2, 6))
    session['total_gold'] += result3
    print session['total_gold']
    print "house"
    session['message'].append ("Earned " + str(result3) + " gold from the house!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return render_template('index.html')

def sumGoldGainLose():
    # Casino setting
    result4 = int(random.uniform(-50, 51))
    session['total_gold'] += result4
    print session['total_gold']
    print "casino"
    if result4 > 0:
        session['message'].append ("Entered a Casino and won " + str(result4) + " gold!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    elif result4 < 0:
        if session['total_gold'] > 0:
            session['message'].append ("Entered a Casino and lost " + str(result4) + " gold...(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
        if session['total_gold'] < 0:
            session['message'].append ("Good Job, you lost all of your money and now your'e a homeless ninja!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    elif result4 == 0:
        session['message'].append ("Entered a Casino and came out even!(" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
    return render_template('index.html')


# Reset the game
@app.route('/play_again',methods=['POST']) 
def return_route():
    session['total_gold'] = 0
    session['message'] = ''
    return redirect("/")

app.run(debug=True)