from app.models import hotel, user
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
        return render_template("usuario.html", users=db.session.execute(db.select(user).order_by(user.id)).scalars())
    
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

    @app.route("/cad_usuario", methods=["GET", "POST"])
    def cad_usuario(): 
        if request.method == "POST":     
            _user = user()
            _user.email = request.form["email"]
            _user.nome = request.form["nome"]
            _user.data = request.form["data"]
            db.session.add(_user)
            db.session.commit()
            
            flash("Usuário criado com sucesso.")
            return redirect(url_for("cad_usuario"))
        return render_template("cad_usuario.html")     
    
    @app.route("/atualiza_user/<int:id>", methods=["GET", "POST"])
    def atualiza_user(id): 
        _hotel = hotel.query.filter_by(id=id).first()
        if request.method == "POST":
            nome_hotel = request.form["nome"] 
            local_hotel = request.form["local"] 
            preco_hotel = request.form["preco"]  
            
            flash("Hotel atualizado com sucesso.") 
            
            _hotel.query.filter_by(id=id).update({"nome": nome_hotel, "local": local_hotel, "preco": preco_hotel})
            db.session.commit()
            return redirect(url_for("inicio"))
            
        return render_template("atualiza_user.html", _hotel=_hotel)
    
    @app.route("/atualiza_usuario/<int:id>", methods=["GET", "POST"])
    def atualiza_usuario(id): 
        _user = user.query.filter_by(id=id).first()
        if request.method == "POST":
            email_user = request.form["email"] 
            nome_user = request.form["nome"] 
            data_user = request.form["data"]  
            
            flash("Usuário atualizado com sucesso.") 
            
            _user.query.filter_by(id=id).update({"email": email_user, "nome": nome_user, "data": data_user})
            db.session.commit()
            return redirect(url_for("usuario"))
            
        return render_template("atualiza_usuario.html", _user=_user)
    
    @app.route("/exclui_user/<int:id>")
    def exclui_user(id):  
        delete=hotel.query.filter_by(id=id).first()  
        db.session.delete(delete)
        db.session.commit()    
        return redirect(url_for("inicio"))
    
    @app.route("/exclui_usuario/<int:id>")
    def exclui_usuario(id):  
        delete=user.query.filter_by(id=id).first()  
        db.session.delete(delete)
        db.session.commit()    
        return redirect(url_for("usuario"))
    
    
    