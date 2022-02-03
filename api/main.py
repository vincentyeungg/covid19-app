import requests
from flask import Flask, request, jsonify

_host = "127.0.0.1"
_port = 5050
app = Flask(__name__)

_url = "https://disease.sh/v3/covid-19"

# get worldwide covid 19 data
@app.route("/covid-19/all")
def get_worldwide_data():
    data = requests.get(f"{_url}/all").json()
    return jsonify({ "data": data })

# get covid 19 data for a specific country
@app.route("/covid-19/countries/<country>")
def get_data_for_country(country):
    data = requests.get(f"{_url}/countries/{country}").json()
    return jsonify({ "data": data })

# get covid 19 data for all countries
@app.route("/covid-19/countries/all")
def get_data_for_all_countries():
    data = requests.get(f"{_url}/countries").json()
    return jsonify({ "data": data })


# get covid 19 global vaccine doses administered
@app.route("/covid-19/vaccine/coverage")
def get_global_vaccine_coverage_stats():
    data = requests.get(f"{_url}/vaccine/coverage?lastdays=all&fullData=false").json()
    return jsonify({ "data": data })

# get covid 19 stats for vaccine doses administered for all countries
@app.route("/covid-19/vaccine/coverage/countries")
def get_vaccine_coverage_stats_for_all_country():
    data = requests.get(f"{_url}/vaccine/coverage/countries?lastdays=all&fullData=false").json()
    return jsonify({ "data": data })

# get covid 19 stats for vaccine doses administered for specific country
@app.route("/covid-19/vaccine/coverage/countries/<country>")
def get_vaccine_coverage_stats_for_country(country):
    data = requests.get(f"{_url}/vaccine/coverage/countries/{country}?lastdays=all&fullData=false").json()
    return jsonify({ "data": data })

if __name__ == "__main__":
    app.run(host=_host, port=_port)