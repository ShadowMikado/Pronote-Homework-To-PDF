# Documentation de récupération des devoirs sur Pronote

Ce programme Python vous permet de récupérer les devoirs sur Pronote et de les sauvegarder dans un fichier PDF, en utilisant les bibliothèques externe `pronotepy` et `fpdf`. Le fichier de configuration `config.json` est utilisé pour spécifier les informations d'identification et l'URL de l'ENT.

## Prérequis

Avant d'exécuter ce programme, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- Bibliothèque `pronotepy`
- Bibliothèque `pystyle`
- Bibliothèque `fpdf`

Pour installer les dépendances faites `pip install -r requirements.txt`.

## Configuration

Assurez-vous de remplir correctement le fichier `config.json` avec les informations suivantes :

- `Username` : Votre nom d'utilisateur Pronote
- `Password` : Votre mot de passe Pronote
- `ENT Url` : L'URL de l'ENT de votre établissement

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir les dépendances requises installées.
3. Configurez le fichier `config.json` avec vos informations d'identification.
4. Exécutez le programme en exécutant `python HomeworksToPDF.py`.

## Fonctionnement

Une fois le programme exécuté, il se connecte à Pronote en utilisant les informations d'identification fournies et récupère les devoirs à venir. Les devoirs sont ensuite sauvegardés dans un fichier PDF avec les informations suivantes pour chaque devoir :

- Date : La date à laquelle le devoir est prévu.
- Matière : Le nom de la matière pour laquelle le devoir est donné.
- Devoir : La description du devoir.

Le fichier PDF (`homeworks.pdf`) est enregistré dans le répertoire de travail actuel.

N'hésitez pas à apporter des modifications au code selon vos besoins ou à contribuer en soumettant des pull requests.

## Avertissement

Ce programme accède à Pronote en utilisant vos informations d'identification. Assurez-vous de ne pas partager le fichier `config.json` ou tout autre fichier contenant vos informations confidentielles.
