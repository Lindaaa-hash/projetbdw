from model.model_pg import count_instances
from controleurs.includes import add_activity

add_activity(SESSION['HISTORIQUE'], "affichage des données")

# récupérer les pieces
REQUEST_VARS['piece'] = count_instances(SESSION['CONNEXION'], 'piece')

# récupérer les photos
REQUEST_VARS['photos'] = count_instances(SESSION['CONNEXION'], 'photos')

# récupérer les usines
REQUEST_VARS['usine'] = count_instances(SESSION['CONNEXION'], 'usine')

def get_fixed_grille():
    # Représentation d'une grille 9x8 : 1 pour case cible, 0 pour case vide
    grille = [
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
    ]
    return grille


def afficher_pioche() :
    pioche = get_random_pieces(4)  # Sélectionne 4 briques
    grille = get_fixed_grille()
    return render_template('afficher.html', grille=grille, pioche=pioche)

def selectionner_brique():
    brique_id = request.form['brique_id']
    brique = get_piece_details(brique_id)
    
    # Réinsérer une nouvelle brique dans la pioche
    nouvelle_brique = get_random_pieces(1)[0]
    return render_template('afficher.html', brique=brique, nouvelle_brique=nouvelle_brique)
