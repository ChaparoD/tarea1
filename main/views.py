from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import requests


# Create your views here.
#store diferente views and http request

def index(response):
    #return HttpResponse(" <h1> Funciona la raaja </h1>")
    item = {"name": "gustavo",
    "ide": "1"},{"name": "velociraptor",
    "ide": "2"},{"name": "cabroweno",
    "ide": "3"}

    return render(response, "main/base.html", {})

def home(response):
    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes").json()
    contador_bb = 0
    contador_bcs = 0
    #calculamos el numero de seasons
    for episode in appi:
        if episode["series"] == "Breaking Bad":
            if int(episode["season"]) > contador_bb:
                contador_bb = int(episode["season"])

        if episode["series"] == "Better Call Saul":
             if int(episode["season"]) > contador_bcs:
                contador_bcs = int(episode["season"])

    
    temporadas_bb =[]
    temporadas_bcs =[]
    for n_temp in range(contador_bb):
        temporadas_bb.append(n_temp + 1)

    for n_temp in range(contador_bcs):
        temporadas_bcs.append(n_temp + 1)
    temporadas = {"bb": temporadas_bb, "bcs":temporadas_bcs}

    return render(response, "main/home.html", {"temporadas":temporadas})

def breakingbad(response, id):
    episodes =[]

    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()

    for episode in appi:
        if int(episode["season"]) == id:
            episodes.append(episode)

    return render(response, "main/episodes.html", {"episodes":episodes, "temp": id})

def bettercallsaul(response, id):
    episodes =[]

    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()

    for episode in appi:
        if int(episode["season"]) == id:
            episodes.append(episode)

    return render(response, "main/episodes.html", {"episodes":episodes, "temp": id})
        

def episode(response, ide):
    
    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes/"+str(ide)).json()

    largo = len(appi[0]["characters"])
    result =[]
    for i in range(largo):
        result.append(i)
    new_characters = {}
    for i in result:
        new_characters[appi[0]["characters"][i]] = i
    print(new_characters)
    print("esto son los de la appi ")
    print(appi[0]["characters"])


    return render(response, "main/episode.html", {"item":appi[0], "names": new_characters} )

def character(response, eid, chr):
    
    print("buscado = "+ chr)
    all = []
    searching = True
    i = 0
    correct_id = 0
    while searching:    
        print("searching...")
        new_request = (requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/characters?limit=10&offset="+str(i)).json())
        i += 10
        for new in new_request:
            if new["name"] == chr:
                print(new["name"])
                print(str(new["char_id"]))
                correct_id =new["char_id"]
                searching = False
                print("ready")
        print("next..")
    
    correct_char = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/characters/"+str(correct_id)).json()

    quotes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/quote?author="+chr).json



    return render(response,"main/character.html" ,{"info": correct_char[0],"citas":quotes} )


def configbb(response, cid, sid):
    episodes =[]

    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()

    for episode in appi:
        if int(episode["season"]) == sid:
            episodes.append(episode)

    return render(response, "main/episodes.html", {"episodes":episodes, "temp": sid})

def configbcs(response, cid, sid):
    episodes =[]

    appi = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()

    for episode in appi:
        if int(episode["season"]) == sid:
            episodes.append(episode)

    return render(response, "main/episodes.html", {"episodes":episodes, "temp": sid})


    



