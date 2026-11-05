# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Alinoé", nom="Quinquet",
                           loisirs=["Handball", "Nourriture", "Résoudre des problèmes"])


@app.get("/loisirs")
def loisirs():
    return "Mes loisirs sont le handball, la nourriture et de faire marcher ma tête pour résoudre des problèmes."

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "plus")
    if op == "plus":
        return f"{a} + {b} = {a + b}"
    if op == "moins":
        return f"{a} - {b} = {a - b}"
    if op == "fois":
        return f"{a} x {b} = {a * b}"
    if op == "divise":
        if b == 0:
            return "Division par zéro impossible"
        return f"{a} / {b} = {a / b}"
    return "Opération inconnue : utilisez plus, moins, fois ou divise"


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "black")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "black")
    return render_template("salut.html", prenom=prenom, ville=ville,
                           couleur=couleur, methode=request.method)


# 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")


# 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


# Une page d'erreur 403 personnalisée
@app.errorhandler(403)
def acces_interdit(erreur):
    return render_template("403.html"), 403


@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )


@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",
    })


@app.get("/horloge")
def horloge():
    return render_template("horloge.html")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
