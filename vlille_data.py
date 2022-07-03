import requests

def get_vlille_data():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    
    payload={}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    print(response.text)  

print('Début du script Python')

dt = get_vlille_data()

print('Fin du script Python')

