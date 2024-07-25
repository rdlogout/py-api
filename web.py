

from flask import Flask, jsonify, request, render_template,send_from_directory

from repo import FoodRepository
from db import save_email
food_repo = FoodRepository()
app = Flask(__name__)



 
@app.route('/', methods=['GET'])
def index(api=False):
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q', '', type=str)
    limit = request.args.get('limit', 24, type=int)
    offset = (page - 1) * limit
    zipcode = request.args.get('zipcode', '', type=str)
    items = food_repo.get_all_food(start=offset, limit=limit, q=q, zipcode=zipcode)
    pages = food_repo.get_items_length() // limit

    if api:
        return jsonify(items)
    return render_template('index.html', items=items, pages=pages, page=page, q=q, zipcode=zipcode)



@app.route('/<string:food_id>', methods=['GET'])
def detail(food_id, notify=False, api=False):
    data = food_repo.get_food_by_id(food_id)
    if api:
        return jsonify(data)
    return render_template('detail.html', food_id=food_id, data=data, notify=notify)

@app.route('/api', methods=['GET'])
def get_food():
    return index(api=True)

@app.route('/api/<string:food_id>', methods=['GET'])
def get_food_by_id(food_id):
    food = food_repo.get_food_by_id(food_id)
    if food:
        return jsonify(food)
    return jsonify({"error": "Food not found"}), 404

@app.route('/notify/<string:food_id>', methods=['POST'])
def notify(food_id):
    email = request.args.get('email', '', type=str)
    food = food_repo.get_food_by_id(food_id)
    if not food:
        return jsonify({"error": "Food not found"}), 404
    

    # store email in db or file

    save_email(email)
    return detail(food_id, notify=True)

 
 
if __name__ == '__main__':
    app.run(debug=True)