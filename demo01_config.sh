#initialiser depo
git init
#configuration utilisateur
git config --global user.name = "Clement Raczek"
git config --global user.email = "clement.raczek@labom2iformation.fr"
#pour récupérer l'ensemble des éléments de configuration

git config --list
git config user.name
#permete de connaitre toutes les commandes disponibles
git help
#consulter de l'aide pour une commande
git help command
git config --help
git config -h
#permet de définir la branche par défaut comme étant'main' et non 'master"'
git config --global init.defaultBranch main

#créer des alias

git congig --global alias.st status