# GrandPyBot
status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/GrandPyBot.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/GrandPyBot)

## La démarche
Bon ... C'est un projet axé sur le TDD principalement, donc dans un premier temps on va brancher Circle-ci sur ce projet. <br>
Avec un fichier requirements.txt issu du cours 'flask' qui installera le contexte <br>
pour une installation de pytest avec le package unittest et un test minimal "papa/maman" pour vérifier que le principe est ok<br>
Si ça marche, on rajoute le petit macaron "circle-ci" et on se lance dans le TDD à grands coups de "test cases"<br>
A tester <br>
https://developers.google.com/maps/documentation/javascript/geolocation?hl=fr

Appli sur Heroku (dev en cours version non fonctionnelle) :
https://yagp.herokuapp.com/


Infos requetes / strategie :
D'abbord Google pour récupérer + la "fromatted adresse + lat & long<br> 
Puis pour récupéerer la MAP cf script async defer avec  lat & long<br>
https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=openclassroom&key=XYZIUYIUYZIUZYIUZZYZUIZYUIZY&inputtype=textquery&fields=formatted_address,geometry

Et recupérer la page wiki en fonction d'un ou  de +ieurs mots clé constitués par la formated adress 
https://fr.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&namespace=0&format=json
