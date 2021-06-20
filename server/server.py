from flask import Flask, send_from_directory, jsonify, request, make_response, after_this_request
from flask_cors import CORS, cross_origin
import random
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('./models')

from models import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
Session = sessionmaker(bind=engine)
session = Session()


# Path for our main Svelte page
@app.route("/")
@cross_origin()
def base():
    return jsonify('Hello')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/get_users", methods = ['GET'])
def get_users():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    users=[]
    for username, email, password in session.query(User.username, User.email, User.password):
        users.append({
            "username": username,
            "email":    email,
            "password": password
            }
        )
    response = make_response(
                    jsonify(
                        users
                    ),
                    200,
                )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/get_residents", methods = ['GET'])
def get_residents():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    residents=[]
    for resident in session.query(Resident):
        residents.append({
            "residentID": residentID,
            "firstName":    firstName,
            "lastName": lastName,
            "coinsBalance": coinsBalance,
            "cashBalance":    cashBalance,
            "energyValue":    energyValue,
            "energyUnits": energyUnits,
            "cashCurrency": cashCurrency
            }
        )
    response = make_response(
                    jsonify(
                        residents
                    ),
                    200,
                )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/get_banks", methods = ['GET'])
def get_banks():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    banks=[]
    for bank in session.query(Bank):
        banks.append({
            "bankID":        bank.bankID,
            "name":          bank.name,
            "coinsBalance":  bank.coinsBalance,
            "cashBalance ":  bank.cashBalance ,
            "cashCurrency":  bank.cashCurrency
            }
        )
    response = make_response(
                    jsonify(
                        banks
                    ),
                    200
                )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/get_utility", methods = ['GET'])
def get_utility():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    utilities=[]
    for utility in session.query(UtilityCompany):
        utilities.append({
            "utilityID":    utility.utilityID,
            "name":         utility.name,
            "coinsBalance": utility.coinsBalance,
            "energyValue":  utility.energyValue,
            "energyUnits":  utility.energyUnits
            }
        )
    response = make_response(
                    jsonify(
                        utilities
                    ),
                    200
                )
    response.headers["Content-Type"] = "application/json"
    return response

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/login_user", methods = ['GET'])
def login_user():
    arg2= request.args['email']
    query = session.query(User.email).filter_by(email=arg2).count()
    if(query==1):
        response = make_response(
                        jsonify(
                            {"message": "Logged in",
                             "data": str(arg2)
                            }
                        ),
                        200,
                    )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        response = make_response(
                        jsonify(
                            {"message": "Logged in",
                             "data": str(arg2)
                            }
                        ),
                        400,
                    )
        response.headers["Content-Type"] = "application/json"
        return response

@app.route("/register_user", methods = ['POST'])
def register_user():
    """Register"""
    if not request.is_json:
        response = make_response(
                jsonify(
                    {"message": "Wrong json format"}
                ),
                418,
            )
        return response
    else:
        registered_user = User(username=request.get_json()['username'], password=request.get_json()['password'], email=request.get_json()['email'])
        query = session.query(User.email).filter_by(email=request.get_json()['email']).count()
        if(query >= 1):
            response = make_response(
                jsonify(
                    {"message": "EMAIL ALREADY USED"}
                ),
                406,
            )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            session.add(registered_user)
            session.commit()
            response = make_response(
                    jsonify(
                        {"message": "Successfuly registered"}
                    ),
                    200,
                )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

@app.route("/register_resident", methods = ['POST'])
def register_resident():
    """Register"""
    if not request.is_json:
        response = make_response(
                jsonify(
                    {"message": "Wrong json format"}
                ),
                418,
            )
        return response
    else:
        registered_resident = Resident(
            residentID=request.get_json()['residentID'], 
            firstName=request.get_json()['firstName'], 
            lastName=request.get_json()['lastName'],
            coinsBalance=request.get_json()['coinsBalance'],
            cashBalance=request.get_json()['cashBalance'], 
            energyValue=request.get_json()['energyValue'], 
            energyUnits=request.get_json()['energyUnits'],
            cashCurrency=request.get_json()['cashCurrency'])
        query = session.query(Resident.residentID).filter_by(residentID=request.get_json()['residentID']).count()
        if(query >= 1):
            response = make_response(
                jsonify(
                    {"message": "name ALREADY USED"}
                ),
                406,
            )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            session.add(registered_resident)
            session.commit()
            response = make_response(
                    jsonify(
                        {"message": "Successfuly registered"}
                    ),
                    200,
                )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

@app.route("/register_bank", methods = ['POST'])
def register_bank():
    """Register"""
    if not request.is_json:
        response = make_response(
                jsonify(
                    {"message": "Wrong json format"}
                ),
                418,
            )
        return response
    else:
        registered_bank = Bank(
            name=request.get_json()['name'], 
            coinsBalance=request.get_json()['coinsBalance'], 
            cashBalance=request.get_json()['cashBalance'],
            cashCurrency=request.get_json()['cashCurrency'])
        query = session.query(Bank.name).filter_by(name=request.get_json()['name']).count()
        if(query >= 1):
            response = make_response(
                jsonify(
                    {"message": "name ALREADY USED"}
                ),
                406,
            )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            session.add(registered_bank)
            session.commit()
            response = make_response(
                    jsonify(
                        {"message": "Successfuly registered"}
                    ),
                    200,
                )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

@app.route("/register_utility", methods = ['POST'])
def register_utility():
    """Register"""
    if not request.is_json:
        response = make_response(
                jsonify(
                    {"message": "Wrong json format"}
                ),
                418,
            )
        return response
    else:
        registered_utility = UtilityCompany(
            name=request.get_json()['name'], 
            coinsBalance=request.get_json()['coinsBalance'], 
            energyValue=request.get_json()['energyValue'],
            energyUnits=request.get_json()['energyUnits'])
        query = session.query(UtilityCompany.name).filter_by(name=request.get_json()['name']).count()
        if(query >= 1):
            response = make_response(
                jsonify(
                    {"message": "name ALREADY USED"}
                ),
                406,
            )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            session.add(registered_utility)
            session.commit()
            response = make_response(
                    jsonify(
                        {"message": "Successfuly registered"}
                    ),
                    200,
                )
            response.headers["Content-Type"] = "application/json"
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

if __name__ == "__main__":
    app.run(debug=True, port=5001)

    #https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9