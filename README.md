# GrandPyBot
status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/GrandPyBot.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/GrandPyBot)

## La démarche
Le projet #7 de OC est un projet principalement axé sur le TDD, Ajax et Flask.<br>
Le brief est disponible [ici](https://openclassrooms.com/fr/paths/68/projects/158/assignment).<br>
Pour satisfaire l'exigence du TDD ce projet est branché sur le systeme d'integration Circle-ci. <br>
Un fichier requirements.txt installe le contexte pytest avec le package unittest et un jeu de test sur les fonctions principales pour vérifier que le principe est respecté<br>
<br>

Appli sur Heroku :
https://yagp.herokuapp.com/

Acces tableau Kanban :<br>
https://jcgibierscompany.atlassian.net/secure/RapidBoard.jspa?rapidView=3&projectKey=GRAN&selectedIssue=GRAN-14<br>
(autorisation necessaire: demandez moi)

Infos requetes / strategie :<br>
1 requête Google Place API pour récupérer la "fromatted adresse + latitide & longitude<br> 
Puis charger la MAP (cf script async defer avec  lat & long)<br>
Enfin recupérer la page wiki en fonction d'un ou de +ieurs mots clé constitués par la formated adress<br>
https://fr.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&namespace=0&format=json

## Usage
Question :
![Presentation question](doc/gdpy_ask.png)

Reponse :
![Presentation reponse](doc/gdpy_resp.png)
