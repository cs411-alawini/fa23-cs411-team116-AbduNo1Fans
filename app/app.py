from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS
import os

from queries import execute_query
import logic

app = Flask(__name__)
CORS(app)

# Secret key for session management
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('map'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if logic.attempt_login(username, password):
            session['user'] = username
            return redirect(url_for('map'))
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/map')
def map():
    if 'user' not in session:
        return redirect(url_for('login'))
    crime_spots = logic.get_crimes(session['user'])
    return render_template('map.html', username=session['user'], crime_spots=crime_spots)

all_options = {
    'list1': [crime[0] for crime in execute_query("SELECT crime_desc FROM CrimeType")],
    'list2': [weapon[0] for weapon in execute_query("SELECT weapon_desc FROM WeaponType")],
    'list3': [premis[0] for premis in execute_query("SELECT premis_desc FROM PremisType")]
}

selected_options = {
    'list1': [],
    'list2': [],
    'list3': []
}

crime_dict = {}
res = execute_query("SELECT * FROM CrimeType")
for r in res:
    crime_dict[r[1]] = r[0]

weapon_dict = {}
res = execute_query("SELECT * FROM WeaponType")
for r in res:
    weapon_dict[r[1]] = r[0]
   
premis_dict = {} 
res = execute_query("SELECT * FROM PremisType")
for r in res:
    premis_dict[r[1]] = r[0]

def update_selected():
    op1 = execute_query(f"SELECT crime_desc FROM CrimeFilter NATURAL JOIN CrimeType WHERE Username = '{session["user"]}'")
    selected_options['list1'] = [o[0] for o in op1]
    
    op2 = execute_query(f"SELECT weapon_desc FROM WeaponFilter NATURAL JOIN WeaponType WHERE Username = '{session["user"]}'")
    selected_options['list2'] = [o[0] for o in op2]
    
    op3 = execute_query(f"SELECT premis_desc FROM PremisFilter NATURAL JOIN PremisType WHERE Username = '{session["user"]}'")
    selected_options['list3'] = [o[0] for o in op3]
    print(selected_options)

@app.route('/search')
def search():
    update_selected()
    return render_template('search.html', all_options=all_options, selected_options=selected_options)

@app.route('/add/<list_id>', methods=['POST'])
def add(list_id):
    option = request.json.get('option')
    if list_id in all_options and option in all_options[list_id]:
        if option not in selected_options[list_id]:
            if list_id == "list1":
                execute_query(f"INSERT INTO CrimeFilter VALUES ('{session['user']}', '{crime_dict[option]}')")
            if list_id == "list2":
                execute_query(f"INSERT INTO WeaponFilter VALUES ('{session['user']}', '{weapon_dict[option]}')")
            if list_id == "list3":
                execute_query(f"INSERT INTO PremisFilter VALUES ('{session['user']}', '{premis_dict[option]}')")
            update_selected()
            return jsonify({'status': 'success', 'selected_options': selected_options[list_id]})
    return jsonify({'status': 'failure'})

@app.route('/remove/<list_id>', methods=['POST'])
def remove(list_id):
    option = request.json.get('option')
    if option in selected_options[list_id]:
        if list_id == "list1":
            execute_query(f"DELETE FROM CrimeFilter WHERE Username = '{session['user']}' AND crime_code = {crime_dict[option]}")
        if list_id == "list2":
            execute_query(f"DELETE FROM WeaponFilter WHERE Username = '{session['user']}' AND weapon_code = {weapon_dict[option]}")
        if list_id == "list3":
            execute_query(f"DELETE FROM PremisFilter WHERE Username = '{session['user']}' AND premis_code = {premis_dict[option]}")
        update_selected()
        return jsonify({'status': 'success', 'selected_options': selected_options[list_id]})
    return jsonify({'status': 'failure'})

@app.route('/report')
def report():
    return "todo"

@app.route('/new_account')
def profile():
    return render_template('new_account.html', )

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

