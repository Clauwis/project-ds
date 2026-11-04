# Projet Data Science MLOps

Projet réalisé dans le cadre du cours de Pr. Mohamed LAZAAR (2026/2027).

## Structure

* `src/` : code source
* `tests/` : tests automatisés (pytest)
* `data/` : données (non versionnées)
* `notebooks/` : exploration

## Installation

```bash
git clone [https://github.com/MGTxlab/projet-ds.git](https://github.com/MGTxlab/projet-ds.git)
cd projet-ds
python -m venv .venv
source .venv/bin/activate
# Sur Windows : source .venv/Scripts/activate
pip install -r requirements.txt

##Données
Jeu : UCI Breast Cancer Wisconsin (Diagnostic), 569 observations.
Cible : diagnosis (B=0, M=1), encodée par src/prepare.py.
Déclarer le stockage : dvc remote add --local -d storage <dossier>
Récupérer les données : dvc pull (ou les retélécharger depuis l'UCI via python scripts/get_data.py).
Rejouer la préparation : dvc repro
Version de référence : tag data-bc-v1