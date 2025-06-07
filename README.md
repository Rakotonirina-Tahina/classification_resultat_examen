# Projet de Prédiction de la Réussite des Étudiants

## Description
Ce projet est une application de classification binaire développée en Python pour prédire si un étudiant réussira ou échouera un cours en fonction de deux caractéristiques : 

Heures d'étude : le nombre d'heures passées à étudier.
Moyenne scolaire : la note moyenne de l'étudiant.

Le modèle utilise un réseau de neurones artificiel construit avec TensorFlow/Keras pour effectuer cette prédiction, en classant les résultats en "Réussir" (1) ou "Échoue" (0).
## Objectif
L'objectif est de construire et d'entraîner un modèle de machine learning capable de prédire la réussite ou l'échec d'un étudiant à un examen, en se basant sur un ensemble de données simulées.
## Prérequis
Pour exécuter ce projet, assurez-vous d'avoir installé les bibliothèques suivantes :

Python 3.x
TensorFlow (pip install tensorflow)
NumPy (pip install numpy)
Pandas (pip install pandas)
Scikit-learn (pip install scikit-learn)

## Données
Le jeu de données est généré manuellement et comprend trois colonnes :

heure_etude : Nombre d'heures d'étude (de 1 à 10).
moyenne_scolaire : Moyenne scolaire de l'étudiant (de 5 à 20).
reussite_examen : Résultat binaire (0 pour échec, 1 pour réussite).

Exemple de données :



heure_etude                 moyenne_scolaire                    reussite_examen

    1                              10                                   0

    2                              13                                   0

    3                              15                                   1

    ...                            ...                                 ...


## Structure du Modèle
Le modèle est un réseau de neurones séquentiel construit avec Keras, composé de :

Couche d'entrée : Accepte 2 caractéristiques (heures d'étude et moyenne scolaire).
Première couche cachée : 10 neurones avec activation ReLU.
Deuxième couche cachée : 5 neurones avec activation ReLU.
Couche de sortie : 1 neurone avec activation sigmoïde pour la classification binaire.

## Compilation

Optimiseur : Adam
Fonction de perte : Binary Crossentropy
Métrique : Précision (accuracy)

## Entraînement

Époques : 100
Taille du lot : 2
Données d'entraînement : 80% des données (après division aléatoire)
Données de test : 20% des données

## Prétraitement

Les données sont normalisées à l'aide de StandardScaler de Scikit-learn pour standardiser les caractéristiques (heures d'étude et moyenne scolaire).
Les données sont divisées en ensembles d'entraînement et de test avec un ratio 80/20.

## Utilisation

Exécuter le script :
Exécutez le fichier Python pour entraîner le modèle sur les données simulées.
Le script affiche la perte (loss) et la précision (accuracy) sur l'ensemble de test.


## Prédictions :
Un ensemble de données de test est créé pour 6 nouveaux étudiants.
Le modèle prédit la probabilité de réussite et la classe (Réussir ou Échoue) pour chaque étudiant.
Les résultats sont affichés dans un tableau formaté :

|----------------------------------------------------------------------------------|
|         Etudiant         |           Classe          |         Pourcentage       |
|----------------------------------------------------------------------------------|
|           1              |          Echoue           |             45%           |
|----------------------------------------------------------------------------------|
|           2              |          Réussir          |             78%           |
|----------------------------------------------------------------------------------|
...





## Résultats

Le modèle évalue sa performance sur l'ensemble de test, affichant la perte et la précision.
Pour les nouveaux étudiants, le script prédit :
La classe : "Réussir" si la probabilité est > 0.5, "Échoue" sinon.
Le pourcentage : La probabilité de réussite multipliée par 100.



## Exemple de Code
Le script principal est inclus dans le fichier Python du projet. Voici un aperçu :

Chargement et préparation des données avec Pandas et Scikit-learn.
Normalisation des caractéristiques avec StandardScaler.
Construction et entraînement du modèle avec TensorFlow/Keras.
Prédiction pour de nouveaux étudiants et affichage des résultats.

## Améliorations Possibles

Augmenter la taille du jeu de données pour améliorer la précision du modèle.
Ajuster l'architecture du réseau (nombre de couches, neurones, etc.).
Tester d'autres hyperparamètres (époques, taille du lot, optimiseur).
Ajouter une validation croisée pour une évaluation plus robuste.

## Auteur
Ce projet a été créé dans le cadre d'un devoir sur la classification binaire avec des réseaux de neurones.

## Licence
Ce projet est fourni à titre éducatif et peut être librement utilisé ou modifié pour des besoins d'apprentissage.
