from flask import Flask, render_template, url_for, redirect, request
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.xlsx', mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'Here is Data: \nemail:{email} \nsubject:{subject} \nmessage: {message}\n\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong please try again"


