web_app/
│
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── announcements.html
│   ├── maintenance.html
│   ├── lease.html
│ 
└── app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/announcements')
def announcements():
    announcements = [
        "Announcement 1: This is the first announcement.",
        "Announcement 2: This is the second announcement."
    ]
    return render_template('announcements.html', announcements=announcements)

@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():
    if request.method == 'POST':
        issue = request.form['issue']
        # Handle maintenance request submission
        print('Maintenance request submitted:', issue)
        return redirect(url_for('maintenance'))
    return render_template('maintenance.html')

@app.route('/lease', methods=['GET', 'POST'])
def lease():
    if request.method == 'POST':
        # Handle lease renewal
        print('Lease renewed')
        return redirect(url_for('lease'))
    return render_template('lease.html', lease_period="01/01/2024 - 12/31/2024")

@app.route('/community')
def community():
    return render_template('community.html')

if __name__ == '__main__':
    app.run(debug=True)
