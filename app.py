from flask import flask

app =Flask(_name_)

@app.router('/')
def index():
    return '<h1>My Basic Details</h1><p>Name:Sankar</p><p>Email:austinsankar@gmail.com</p>'

    if _name_=='_main_':app.run(host='0.0.0.0',port=5000)
    