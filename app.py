from flask import Flask, jsonify, request, render_template, redirect, url_for
from data.food_repository import FoodRepository

food_repo = FoodRepository()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(api=False):
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q', '', type=str)
    limit = request.args.get('limit', 24, type=int)
    offset = (page - 1) * limit
    items = food_repo.get_all_food(start=offset, limit=limit, q=q)
    pages = food_repo.get_items_length() // limit

    if api:
        return jsonify(items)

    return render_template('index.html', items=items, pages=pages, page=page, q=q)

@app.route('/<string:food_id>', methods=['GET'])
def detail(food_id, notify=False):
    data = food_repo.get_food_by_id(food_id)
    return render_template('detail.html', data=data, notify=notify)

@app.route('/api', methods=['GET'])
def get_food():
    return index(api=True)

@app.route('/food/<string:food_id>', methods=['GET'])
def get_food_by_id(food_id):
    food = food_repo.get_food_by_id(food_id)
    if food:
        return jsonify(food)
    return jsonify({"error": "Food not found"}), 404

def save_email(email):
    # save email in db or file
    pass

@app.route('/notify/<string:food_id>', methods=['POST'])
def notify(food_id):
    email = request.args.get('email', '', type=str)
    food = food_repo.get_food_by_id(food_id)
    # store email in db or file
    save_email(email)
    return detail(food_id, notify=True)

if __name__ == '__main__':
    app.run(debug=True)