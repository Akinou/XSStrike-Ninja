import os

# Demander à l'utilisateur d'entrer l'URL du site à tester pour les failles XSS
site = input("Entrez l'URL du site à tester pour les failles XSS: ")

# Options disponibles avec description
options = {
    '1': 'Scanner le site pour les failles XSS avec une méthode standard',
    '2': 'Scanner le site pour les failles XSS avec une méthode avancée',
    '3': 'Scanner le site pour les failles XSS avec une méthode basée sur le temps',
    '4': 'Scanner le site pour les failles XSS avec une méthode de détection de WAF',
    '5': 'Scanner le site pour les failles XSS avec toutes les méthodes disponibles',
    '6': 'Utiliser des payloads personnalisés pour le scan',
    '7': 'Définir le nombre de threads utilisés pour le scan',
    '8': 'Définir le timeout pour les requêtes HTTP',
    '9': 'Définir le User-Agent pour les requêtes HTTP',
    '10': 'Définir le cookie pour les requêtes HTTP',
    '11': 'Activer le mode verbeux pour les messages de sortie',
    '12': 'Activer le mode silencieux pour les messages de sortie',
    '13': 'Spécifier le temps d\'attente avant chaque requête',
    '14': 'Activer le mode HEAD pour les requêtes HTTP',
    '15': 'Activer le mode HTTPS pour les requêtes HTTP',
    '16': 'Activer le mode surchauffe pour simuler une attaque plus importante',
    '17': 'Définir un proxy pour les requêtes HTTP',
    '18': 'Ignorer les erreurs de certificat SSL',
    '19': 'Ignorer les erreurs de vérification DNS',
    '20': 'Activer la recherche de vulnérabilités dans les URL et les formulaires',
    '21': 'Scanner les sous-domaines en utilisant la liste de sous-domaines fournie',
    '22': 'Scanner les sous-domaines en utilisant la résolution de DNS',
    '23': 'Scanner les sous-domaines en utilisant la recherche Google'
}

# Afficher les options disponibles avec description
print("Options disponibles:")
for key, value in options.items():
    print(key + ". " + value)

# Demander à l'utilisateur de choisir une option
option = input("Entrez le numéro de l'option à utiliser: ")

# Exécuter l'option sélectionnée
if option in options:
    command = f'python3 xsstrike.py -u "{site}" '
    if option == '1':
        os.system(command)
    elif option == '2':
        os.system(command + '-a')
    elif option == '3':
        os.system(command + '-t')
    elif option == '4':
        os.system(command + '-w')
    elif option == '5':
        os.system(command + '-a -t -w')
    elif option == '6':
        payload_file = input('Entrez le chemin du fichier contenant les payloads personnalisés: ')
        os.system(command + f'-p "{payload_file}"')
    elif option == '7':
        threads = input('Entrez le nombre de threads à utiliser: ')
        os.system(command + f'--threads {threads}')
    elif option == '8':
        timeout = input('Entrez le timeout pour les requêtes HTTP: ')
        os.system(command + f'--timeout {timeout}')
    elif option == '9':
        user_agent = input('Entrez le User-Agent pour les requêtes HTTP: ')
        os.system(command + f'-H "User-Agent: {user_agent}"')
    elif option == '10':
        cookie = input('Entrez le cookie pour les requêtes HTTP: ')
        os.system(command + f'--cookie "{cookie}"')
    elif option == '11':
        os.system(command + '-v')
    elif option == '12':
        os.system(command + '-s')
    elif option == '13':
        wait = input('Entrez le temps d\'attente avant chaque requête: ')
        os.system(command + f'-w {wait}')
    elif option == '14':
        os.system(command + '-H "Content-Type: text/html" -X HEAD')
    elif option == '15':
        os.system(command + '--https')
    elif option == '16':
        os.system(command + '--staging')
    elif option == '17':
        proxy = input('Entrez l\'URL du proxy: ')
        os.system(command + f'--proxy "{proxy}"')
    elif option == '18':
        os.system(command + '--ignore-ssl')
    elif option == '19':
        os.system(command + '--ignore-dns')
    elif option == '20':
        os.system(command + '-p')
    elif option == '21':
        subdomains_file = input('Entrez le chemin du fichier contenant la liste de sous-domaines: ')
        os.system(command + f'-l "{subdomains_file}"')
    elif option == '22':
        os.system(command + '-D')
    elif option == '23':
        os.system(command + '-G')
else:
    print("Option invalide")

