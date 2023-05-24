import random

class Random:

    def generer_nom_prenom_age():
        consonnes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        voyelles = ['a', 'e', 'i', 'o', 'u']
        syllabes = ['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu',
                    'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku',
                    'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
                    'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
                    'wa', 'we', 'wi', 'wo', 'wu', 'xa', 'xe', 'xi', 'xo', 'xu', 'ya', 'ye', 'yi', 'yo', 'yu', 'za', 'ze', 'zi', 'zo', 'zu']
        
        prenom = ''
        nom = ''
        
        # Générer le prénom
        nb_syllabes_prenom = random.randint(1, 2)
        for _ in range(nb_syllabes_prenom):
            syllabe = random.choice(syllabes)
            prenom += syllabe
        
        # Générer le nom
        nb_syllabes_nom = random.randint(1, 2)
        for _ in range(nb_syllabes_nom):
            syllabe = random.choice(syllabes)
            nom += syllabe
        
        # Générer l'âge
        age = random.randint(18, 80)
        
        return prenom.capitalize(), nom.capitalize(), age

    def generer_nom_ville():
        consonnes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        voyelles = ['a', 'e', 'i', 'o', 'u']
        syllabes = ['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu',
                    'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku',
                    'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
                    'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
                    'wa', 'we', 'wi', 'wo', 'wu', 'xa', 'xe', 'xi', 'xo', 'xu', 'ya', 'ye', 'yi', 'yo', 'yu', 'za', 'ze', 'zi', 'zo', 'zu']
        
        nom_ville = ''
        
        # Ajouter une ou deux syllabes au nom de ville
        nb_syllabes = random.randint(1, 2)
        for _ in range(nb_syllabes):
            syllabe = random.choice(syllabes)
            nom_ville += syllabe
        
        # Ajouter une consonne finale
        consonne_finale = random.choice(consonnes)
        nom_ville += consonne_finale
        
        # Ajouter une voyelle finale
        voyelle_finale = random.choice(voyelles)
        nom_ville += voyelle_finale
        
        return nom_ville.capitalize()