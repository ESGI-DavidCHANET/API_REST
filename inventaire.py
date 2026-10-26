import os
import requests

DOCKER = os.environ.get("DOCKER_API_URL", "http://127.0.0.1:2375").rstrip("/")
TIMEOUT = 10

def calculer_cpu(stats):
    cpu, avant = stats["cpu_stats"], stats["precpu_stats"]
    delta_cpu = cpu["cpu_usage"]["total_usage"] - avant["cpu_usage"]["total_usage"]
    delta_systeme = cpu.get("system_cpu_usage", 0) - avant.get("system_cpu_usage", 0)
    nb_cpus = cpu.get("online_cpus") or 1
    return delta_cpu / delta_systeme * nb_cpus * 100 if delta_systeme else 0.0

def inventaire_docker(session):
    reponse = session.get(f"{DOCKER}/containers/json?all=true", timeout=TIMEOUT)
    reponse.raise_for_status()
    resultat = []
    for c in reponse.json():
        fiche = {
            "id": c["Id"][:12],
            "nom": c["Names"][0].lstrip("/"),
            "image": c["Image"],
            "etat": c["State"],
        }
        if c["State"] == "running":
            r = session.get(f"{DOCKER}/containers/{c['Id']}/stats?stream=false", timeout=TIMEOUT)
            r.raise_for_status()
            stats = r.json()
            fiche["cpu_pourcent"] = round(calculer_cpu(stats), 2)
            fiche["memoire_mo"] = round(stats["memory_stats"].get("usage", 0) / 1024 / 1024, 1)
        resultat.append(fiche)
    return resultat


def main():
    with requests.Session() as session:
        conteneurs = inventaire_docker(session)
    for c in conteneurs:
        print(c)


if __name__ == "__main__":
    main()