from flask import Flask, jsonify, make_response
import threading
from db.facades.AnonymousFacade import AnonymousFacade
from db.tables import AirlineCompanies, Tickets,Flights, Countries
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
anon_facade = AnonymousFacade()


@app.route('/countries', methods=['GET'])
def get_all_countries():
    countries: list[Countries] = anon_facade.get_all_countries()  # getting from facade list of countries
    countries_dict: list[dict] = [country.get_dict() for country in countries]  # parsing the countries objects to dict
    return make_response(jsonify(countries_dict), 200)


@app.route('/countries/<int:id_>', methods=['GET'])
def get_country_by_id(id_):
    country_to_get = anon_facade.get_country_by_id(id_)
    country_dict = country_to_get.get_dict()
    return make_response(jsonify(country_dict), 200)


@app.route('/flights', methods=['GET'])
def get_all_flights():
    flights: list[Flights] = anon_facade.get_all_flights()  # getting from facade list of flights
    flights_dict: list[dict] = [flight.as_dict() for flight in flights]  # parsing the flights objects to dict
    return make_response(jsonify(flights_dict), 200)

@app.route('/flights/<int:id_>', methods=['GET'])
def get_flight_by_id(id_):
    flight_to_get = anon_facade.get_flight_by_id(id_)
    flight_dict = flight_to_get.as_dict()
    return make_response(jsonify(flight_dict), 200)

@app.route('/tickets', methods=['GET'])
def get_all_tickets():
    tickets: list[Tickets] = anon_facade.get_all_tickets()  # getting from facade list of tickets
    tickets_dict: list[dict] = [ticket.get_dict() for ticket in tickets]  # parsing the tickets objects to dict
    return make_response(jsonify(tickets_dict), 200)

@app.route('/airlines', methods=['GET'])
def get_all_airlines():
    airlines: list[AirlineCompanies] = anon_facade.get_all_airline()  # getting from facade list of airlines
    airlines_dict: list[dict] = [airline_companies.as_dict() for airline_companies in airlines]  # parsing the airlines objects to dict
    return make_response(jsonify(airlines_dict), 200)

@app.route('/airlines/<int:id_>', methods=['GET'])
def get_airline_by_id(id_):
    airline_to_get = anon_facade.get_airline_by_id(id_)
    airline_to_get_dict = airline_to_get.as_dict()
    return make_response(jsonify(airline_to_get_dict), 200)

if __name__ == '__main__':
    app.run(debug=True)