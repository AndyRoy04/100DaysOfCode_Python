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
        # Loop through each column in the data record
        dictionary = {}     
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/random")
def get_random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())
   
@app.route('/all')
def all_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search/<location>")
def search(location):
    location = location.capitalize()    
    our_cafes = db.session.execute(db.select(Cafe).where(Cafe.location==location)).scalars().all()
    
    if our_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in our_cafes])
    else:
        error = {
            "error" : {
                "Not Found": "Sorry, No cafe found at that location."
            }
        }
        return jsonify(error)
            
      
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def patch_cafe(cafe_id):
    price = request.args.get('new_price')
    cafe_to_edit = db.session.get(Cafe, cafe_id)
    
    if cafe_to_edit:
        cafe_to_edit.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated Cafe price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, No cafe found at that location."}), 404
    
# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    secrete_code = 'TopSecretAPIKey'
    secrete_key = request.args.get('api_key')
    cafe_to_delete = db.session.get(Cafe, cafe_id)
    
    if cafe_to_delete:
        if secrete_key == secrete_code:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Cafe Successfully deleted."}), 200
        else:
            return jsonify(error={"error": "Sorry, you can't delete this field without the correct API Key."}), 403
    else:
        return jsonify(error={"Not Found": "Sorry, No cafe found with that id."}), 404
   

if __name__ == '__main__':
    app.run(debug=True)
