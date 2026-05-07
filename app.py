from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

#AOT DATA

url = "https://api.attackontitanapi.com/characters"

response = requests.get(url)
data = response.json()

#lagre data for færre API-calls
AOTCharacters = data


#Tilfedige bakgrunnsbilder API

bg_image = "https://picsum.photos/1200/800"


#HOME

@app.route("/")
def home():

    return render_template(
        "home.html",
        bg_image=bg_image
    )


#ANIME MENU

@app.route("/anime")
def anime():

    return render_template(
        "anime.html",
        bg_image=bg_image
    )


#AOT

@app.route("/aot")
def aot():

    search = request.args.get("search")

    #Søk funksjon:
    if search:

        found_character = None

        for character in AOTCharacters["results"]:

            if search.lower() in character["name"].lower():

                found_character = character
                break

        if found_character:

            return render_template(
                "aot.html",
                name=found_character.get("name"),
                image=found_character.get("img"),
                status=found_character.get("status"),
                gender=found_character.get("gender"),
                species=found_character.get("species"),
                bg_image=bg_image
            )

        else:

            return render_template(
                "aot.html",
                error="Character not found 😢",
                bg_image=bg_image
            )

    #tilfeldig AOT karakter
    random_id = random.randint(1, 200)

    url = f"https://api.attackontitanapi.com/characters/{random_id}"

    response = requests.get(url)
    data = response.json()

    return render_template(
        "aot.html",
        name=data.get("name"),
        image=data.get("img"),
        status=data.get("status"),
        gender=data.get("gender"),
        species=data.get("species"),
        bg_image=bg_image
    )


#Tilfedige Pokemon

@app.route("/pokemon")
def pokemon():

    random_id = random.randint(1, 151)

    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

    response = requests.get(url)
    data = response.json()

    return render_template(
        "pokemon.html",
        name=data["name"].title(),
        image=data["sprites"]["front_default"],
        bg_image=bg_image
    )


#ANIMALS MENU

@app.route("/animals")
def animals():

    return render_template(
        "animals.html",
        bg_image=bg_image
    )


#CATFACTS

@app.route("/cats")
def cats():

    url = "https://catfact.ninja/fact"

    response = requests.get(url)
    data = response.json()

    fact = data["fact"]

    if len(fact) > 100:
        message = "🧠 Long fact"
    else:
        message = "⚡ Short fact"

    return render_template(
        "cats.html",
        fact=fact,
        message=message,
        bg_image=bg_image
    )


#Tilfedige hundebilder

@app.route("/dogs")
def dogs():

    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)
    data = response.json()

    return render_template(
        "dogs.html",
        image=data["message"],
        bg_image=bg_image
    )


app.run(debug=True)