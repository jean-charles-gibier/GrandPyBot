# GrandPyBot
status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/GrandPyBot.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/GrandPyBot)

## La démarche
C'est un projet axé sur le TDD principalement, donc dans un premier temps on va brancher Circle-ci sur ce projet. <br>
Avec un fichier requirements.txt issu du cours 'flask' qui installera le contexte <br>
pour une installation de pytest avec le package unittest et un jeu de test minimal "papa/maman" pour vérifier que le principe est ok<br>
Si ça marche, on rajoute le petit macaron "circle-ci" et on se lance dans le TDD à grands coups de "test cases"<br>
Appli sur Heroku :
https://yagp.herokuapp.com/

Acces tableau Kanban
https://jcgibierscompany.atlassian.net/secure/RapidBoard.jspa?rapidView=3&projectKey=GRAN&selectedIssue=GRAN-14
(autorisation necessaire demandez mmoi)

Infos requetes / strategie :
1 requête Google Place API pour récupérer + la "fromatted adresse + lat & long<br> 
Puis pour récupéerer la MAP (cf script async defer avec  lat & long)<br>
Et recupérer la page wiki en fonction d'un ou de +ieurs mots clé constitués par la formated adress 
https://fr.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&namespace=0&format=json
