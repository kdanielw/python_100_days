from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
            #Method 1. 
            dictionary = {}
            # Loop through each column in the data record
            for column in self.__table__.columns:
                #Create a new dictionary entry;
                # where the key is the name of the column
                # and the value is the value of the column
                dictionary[column.name] = getattr(self, column.name)
            return dictionary
            
            #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    jsonify_text = jsonify(cafe = {"id" : random_cafe.id,
                    "name" : random_cafe.name,
                    "map_url" : random_cafe.map_url,
                    "img_url" : random_cafe.img_url,
                    "location" : random_cafe.location,
                    "seats" : random_cafe.seats,
                    "has_toilet" : random_cafe.has_toilet,
                    "has_wifi" : random_cafe.has_wifi,
                    "has_sockets" : random_cafe.has_sockets,
                    "can_take_calls" : random_cafe.can_take_calls,
                    "coffee_price" : random_cafe.coffee_price,
                    })
    return jsonify(cafe = random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search():
    search_loc = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == search_loc))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error = {
            "Not found": "Sorry, we don't have a cafe at that location."
        }), 404
    
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error = {
            "Not found": "Sorry, a cafe with that id was not found in the database."
        }), 404
    else:
        cafe_to_update.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


@app.route("/report_close/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    if request.args.get('api-key') == "IlluMiliKillAlluKalluto":
        try:
            cafe_to_delete = db.session.get(Cafe, cafe_id)
        except:
            return jsonify(error = {
                "Not found": "Sorry, a cafe with that id was not found in the database."
            }), 404
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe."}), 200
    else:
        return jsonify(response={"Forbidden": "Sorry, that is not allowed. Make sure you have de correct api-key."}), 403

if __name__ == '__main__':
    app.run(debug=True)

# Postman's Documentation = https://documenter.getpostman.com/view/47091578/2sB34oDdgr
