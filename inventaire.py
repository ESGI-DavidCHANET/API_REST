import os
import requests
import json
from datetime import datetime, timezone

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

    inventaire = {
        "date_releve": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "docker": {"url": DOCKER, "conteneurs": conteneurs},
    }
    with open("inventaire.json", "w", encoding="utf-8") as f:
        json.dump(inventaire, f, ensure_ascii=False, indent=2)

    print(f"Relevé du {inventaire['date_releve']}")
    print(f"  {'NOM':<28} {'IMAGE':<34} {'ÉTAT':<10} {'CPU %':>7} {'MÉM. Mo':>9}")
    for c in conteneurs:
        cpu = f"{c['cpu_pourcent']:.2f}" if "cpu_pourcent" in c else "-"
        mem = f"{c['memoire_mo']:.1f}" if "memoire_mo" in c else "-"
        print(f"  {c['nom']:<28} {c['image'][:34]:<34} {c['etat']:<10} {cpu:>7} {mem:>9}")
    print("\nInventaire écrit dans inventaire.json")


if __name__ == "__main__":
    main()