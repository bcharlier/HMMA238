# Ce programme calcule le périmètre d'un cercle dont
# le rayon a été demandé au clavier à l'utilisateur.

import math

def perimetre_cercle(un_rayon):
    """Calculer le périmètre d'un cercle à partir de son rayon.
	:param un_rayon: le rayon du cercle (positif)
	:return le périmètre d'un cercle de rayon un_rayon
    """
    diametre = 2 * un_rayon
    return math.pi * diametre


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    saisie = input("Rayon du cercle : ")    # une chaîne de caractères
    le_rayon = float(saisie)                # convertie en un nombre réel

    # calculer le périmètre
    perimetre = perimetre_cercle(le_rayon)

    # afficher le périmètre à l'utilisateur
    print("Le périmètre d'un cercle de rayon", le_rayon, "est", perimetre)

if __name__ == "__main__":
    main()