from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

categories = [
    {'id': 1, 'name': 'Catégorie 1', 'description': 'Description de la catégorie 1'},
    {'id': 2, 'name': 'Catégorie 2', 'description': 'Description de la catégorie 2'}
]

articles = [
    {'id': 1, 'name': 'Article 1', 'description': 'Description de l\'article 1', 'price': 10.0, 'quantity': 5, 'category_id': 1},
    {'id': 2, 'name': 'Article 2', 'description': 'Description de l\'article 2', 'price': 20.0, 'quantity': 10, 'category_id': 1},
    {'id': 3, 'name': 'Article 3', 'description': 'Description de l\'article 3', 'price': 30.0, 'quantity': 15, 'category_id': 2},
]

class Article(Resource):
    def get(self, id):
        article = next((article for article in articles if article['id'] == id), None)
        if article:
            return article, 200
        else:
            return {'message': 'Article not found'}, 404

    def put(self, id):
        article = next((article for article in articles if article['id'] == id), None)
        if article:
            article['name'] = request.json.get('name', article['name'])
            article['description'] = request.json.get('description', article['description'])
            article['price'] = request.json.get('price', article['price'])
            article['quantity'] = request.json.get('quantity', article['quantity'])
            article['category_id'] = request.json.get('category_id', article['category_id'])
            return article, 200
        else:
            return {'message': 'Article not found'}, 404

    def delete(self, id):
        global articles
        articles = [article for article in articles if article['id'] != id]
        return '', 204

class ArticleList(Resource):
    def get(self):
        keyword = request.args.get('q')
        if keyword:
            filtered_articles = [article for article in articles if keyword in article['name'] or keyword in article['description']]
            return filtered_articles, 200
        else:
            return articles, 200

    def post(self):
        article = {
            'id': len(articles) + 1,
            'name': request.json['name'],
            'description': request.json['description'],
            'price': request.json['price'],
            'quantity': request.json['quantity'],
            'category_id': request.json['category_id']
        }
        articles.append(article)
        return article, 201

api.add_resource(ArticleList, '/articles')
api.add_resource(Article, '/articles/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)