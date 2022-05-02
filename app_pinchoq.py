from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("Register.html")
    
@app.route("/profile", methods=["POST"])
def Profile():
    name = request.form.get("nombre")
    lastname = request.form.get("apellidos")
    correo = request.form.get("correo")
    contra = request.form.get("contra")
    usua = request.form.get("us")
    bday = request.form.get("fn")
    sex = request.form.get("sexo")
    return render_template(
		"Profile.html",name=name,lastname=lastname,correo=correo,usua=usua,bday=bday,sex=sex,
	)
