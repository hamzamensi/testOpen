# testOpenPython
Exercice 1:
* Exercice1.py: c'est le code demandé par l'enoncé. pour y tester vous pouvez lancer la commande : python exercice1.py [list des chaines de caracteres] Exemple: python exercice1.py Ceci est un test
* exercice1_test.py: c'est le fichier où il y a les tests unitaires de 2 fonctions demandées. pour y lancer il faut installer pytest apres lancer la commande pytest.

Exercice 2:
* Excercice2.py : c'est le code de l'exercice 2
pour tester il faut ecrire cette commande python exercice2.py [action] [args]
les actions disponibles: add_user, get_users, get_one, add_users, search
- Exemples: 
python exercice2.py search first_name Hamza : pour chercher dans la base de données un user avec prénon Hamza
python exercice2.py get_users: vous trouverez les résultats dans users.json
python exercice2.py add_user 4 Hamza MENSI +336214382 : pour ajouter cet utilisateur avec ces données
python exercice2.py get_one
pyhton exercice2.py add_users users_to_add.json : pout ajouter des utilisateurs dans le fichier users_to_add.json

pour lancer les tests unitaires, on lance la commande pytes