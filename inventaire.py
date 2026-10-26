import os
import requests

DOCKER = os.environ.get("DOCKER_API_URL", "http://127.0.0.1:2375").rstrip("/")
TIMEOUT = 10


def inventaire_docker(session):
    reponse = session.get(f"{DOCKER}/containers/json?all=true", timeout=TIMEOUT)
    reponse.raise_for_status()
    resultat = []
    for c in reponse.json():
        resultat.append({
            "id": c["Id"][:12],
            "nom": c["Names"][0].lstrip("/"),
            "image": c["Image"],
            "etat": c["State"],
        })
    return resultat


def main():
    with requests.Session() as session:
        conteneurs = inventaire_docker(session)
    for c in conteneurs:
        print(c["nom"], c["image"], c["etat"])


if __name__ == "__main__":
    main()