# flask-projet
dans le code ajouter .py, nous avons créé deux classes ArticleList et Article correspondant aux routes /articles (pour la consultation de tous les articles et l’ajout d’article) et /articles/<int:id> (pour la consultation, la modification et la suppression d'un article par son ID) respectivement. 
Nous avons également défini deux méthodes GET pour récupérer tous les articles ou chercher un article par mot clé.
Dans le code app.py , nous avons défini deux listes : categories et articles, qui représentent respectivement les catégories et les articles de notre application. Nous avons également défini trois routes :

La route / qui affiche la page d'accueil de l'application et la liste des catégories.
La route /category/<int:category_id>/articles qui affiche la liste des articles d'une catégorie donnée.
La route /add-to-cart qui permet d'ajouter un article au panier.
