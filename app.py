from flask import Flask, render_template, request

app = Flask(__name__)

categories = [
    {'id': 1, 'name': 'Catégorie 1', 'description': 'Description de la catégorie 1'},
    {'id': 2, 'name': 'Catégorie 2', 'description': 'Description de la catégorie 2'}
]

articles = [
    {'id': 1, 'name': 'Article 1', 'description': 'Description de l\'article 1', 'price': 10.0, 'quantity': 5, 'category_id': 1},
    {'id': 2, 'name': 'Article 2', 'description': 'Description de l\'article 2', 'price': 20.0, 'quantity': 10, 'category_id': 1},
    {'id': 3, 'name': 'Article 3', 'description': 'Description de l\'article 3', 'price': 30.0, 'quantity': 15, 'category_id': 2},
]

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/category/<int:category_id>/articles')
def category_articles(category_id):
    category_articles = [article for article in articles if article['category_id'] == category_id]
    return render_template('category_articles.html', category_articles=category_articles)

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    article_id = request.form['article_id']
    article_quantity = int(request.form['article_quantity'])
    article = next((article for article in articles if article['id'] == article_id), None)
    if article and article['quantity'] >= article_quantity:
        # Ajouter l'article au panier
        return f"L'article {article['name']} a été ajouté au panier."
    else:
        # Afficher un message d'erreur
        return f"L'article {article['name']} n'est pas disponible en quantité suffisante."

if __name__ == '__main__':
    app.run(debug=True)