from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/contacts/')
def contacts():
    developer_name = 'Ilon Mask'
    developer_adres = 'grib'
    return render_template(template_name_or_list='contacts.html',name = developer_name,adres = developer_adres)

if __name__ == "__main__":
    app.run(debug=True)

