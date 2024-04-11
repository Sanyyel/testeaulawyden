from app.models import hotel
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify 
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):
        
    #@app.route("/")
    #def principal():        
        #return render_template("seu_job/index.html")
    
    @app.route("/")
    def inicio():        
        return render_template("inicio.html", hotels=db.session.execute(db.select(hotel).order_by(hotel.id)).scalars())
    
    
    @app.route("/usuario")
    def usuario():        
        return render_template("usuario.html")   
    
    @app.route("/cad_user", methods=["GET", "POST"])
    def cad_user(): 
        if request.method == "POST":     
            _hotel = hotel()
            _hotel.nome = request.form["nome"]
            _hotel.local = request.form["local"]
            _hotel.preco = request.form["preco"]
            db.session.add(_hotel)
            db.session.commit()
            
            flash("Hotel criado com sucesso.")
            return redirect(url_for("cad_user"))
        return render_template("cad_user.html")     
    
    @app.route("/atualiza_user")
    def atualiza_user():        
        return render_template("atualiza_user.html")
    
    @app.route("/exclui_user/<int:id>")
    def exclui_user(id):  
        delete=hotel.query.filter_by(id=id).first()  
        db.session.delete(delete)
        db.session.commit()    
        return redirect(url_for("inicio"))
    
    
    