
import pandas as pd

def supprimer_lignes_vides(df):
    """Supprime les lignes incomplètes."""
    return df.dropna().reset_index(drop=True)

#ceci est un commentaire simple pour tester le commit