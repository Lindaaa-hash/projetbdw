from model.model_pg import *
from controleurs.includes import add_activity


add_activity(SESSION['HISTORIQUE'], "affichage des données")

# récupérer les pieces
REQUEST_VARS['piece'] = count_instances(SESSION['CONNEXION'], 'piece')

# récupérer les photos
REQUEST_VARS['photos'] = count_instances(SESSION['CONNEXION'], 'photos')

# récupérer les usines
REQUEST_VARS['usine'] = count_instances(SESSION['CONNEXION'], 'usine')

#récupérer des briques aléatoires
REQUEST_VARS['piece'] = random_brique(SESSION['CONNEXION'], 'piece')