import requests

def mostra_tela():
   print("+---------------------------+")
   print("|        Urna 2026          |")
   print("+---------------------------+")
   print("|        Candidatos         |")
   print("+---------------------------+")
   print("| 21 - Juvencio             |")
   print("| 42 - Isaquel              |")
   print("| 52 - Alanirio             |")
   print("+---------------------------+")

def entra_dados():
    candidatos_validos= ["21","42","52"]
    titulo= input(" informe seu titulo: ")
    candidato= input(" informe seu candidato: ")

    if candidatos_validos.count(candidato) > 0:
        registrar_voto(titulo,candidato, "2530")
        print("Seu voto foi registrado com sucesso!")
    else:
        print("Candidato não registrado")


def registrar_voto(titulo: str, candidato: str,  urna: str):
    url="http://127.0.0.1:8000/register_vote"
    headers={'content-type':'application/json','Accept-Charset':'UTF-8'}
    dados='{  "titulo": ' + titulo  + ',  "candidato": '  + candidato  + ',  "urna": ' + urna + '}'
    r = requests.post(url, headers = headers, data = dados)
    print("*********")
    print (r)

if __name__ == "__main__":
    mostra_tela()
    entra_dados()