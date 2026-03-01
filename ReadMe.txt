RÉCAPITULATIF DES LIVRABLES
Étudiant	Blueprint	Routes	Services	Templates
Étudiant 1	Auth	login, logout	(dans routes)	login.html
Étudiant 2	Students	list, create, delete	add, delete, get, list	list.html, create.html
Étudiant 3	Teachers	list, create, delete	add, delete, get, list	list.html, create.html
Étudiant 4	Courses	list, create, assign, delete	add, assign, get, list	list.html, create.html, assign.html
Étudiant 5	Dashboard	index	(utilise les autres)	index.html, base.html, partials

===Pourquoi utiliser Application Factory ?=======
L'Application Factory est un pattern de conception qui permet de créer plusieurs instances de l'application avec des configurations différentes.

Avantages :

Tests plus faciles : On peut créer une instance pour les tests avec une config spécifique

Configuration dynamique : On peut charger la config selon l'environnement (dev, prod, test)

Extensions retardées : On initialise les extensions après la création de l'app

Réutilisabilité : On peut créer plusieurs instances pour différents contextes

Sécurité : Pas de variables globales, tout est encapsulé

========Pourquoi séparer routes et services ?=======
La séparation des responsabilités (Separation of Concerns) est un principe fondamental en génie logiciel.

Avantages :

Maintenabilité : Le code est plus facile à maintenir et à modifier

Réutilisabilité : Les services peuvent être réutilisés dans différentes routes

Testabilité : On peut tester la logique métier indépendamment des routes

Clarté : Chaque fichier a une responsabilité unique

Évolutivité : Plus facile d'ajouter des fonctionnalités

=======Si un blueprint n'est pas enregistré dans create_app() :========

Routes inaccessibles : Aucune route du blueprint ne sera accessible

Erreur 404 : Les URLs retourneront "Page non trouvée"

Fonctionnalités manquantes : Toute la fonctionnalité du blueprint sera indisponible

url_for échoue : Les appels à url_for('blueprint.route') généreront des erreurs

Templates non chargés : Les templates spécifiques au blueprint ne seront pas trouvés

=====Pourquoi utiliser url_prefix ?============
url_prefix permet de définir un préfixe commun pour toutes les routes d'un blueprint.

Avantages :

Organisation : Toutes les routes d'un module commencent par le même préfixe

Évitement de conflits : Pas de collision entre des routes de noms identiques

Clarté : Les URLs sont plus lisibles et organisées

Flexibilité : On peut changer le préfixe sans modifier les routes individuelles

API RESTful : Facilite la création d'APIs structurées

========Où doit se trouver la logique métier ?========
La logique métier doit se trouver dans les services (couche service), pas dans les routes.

Principes :

Routes : Uniquement la gestion HTTP (requêtes, réponses, templates)

Services : Toute la logique métier (calculs, validations, accès données)

Modèles : Définition des structures de données

