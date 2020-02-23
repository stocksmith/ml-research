from flask import Flask, jsonify
from flask import abort
import json

import yfinance as yf
import pandas as pd

app = Flask(__name__)

#API description
apiDescription = [
    {
        'title': u'Sotcksmith Relatime Data API',
        'description': u'An API to query stock data for real time data analysis', 
        'Author': u'Team Stocksmith'
    }
]

# Paths: 

# /dataset/{name}
# /stock-data/{time frame}
# /stock-info/{company-abbreviation}


@app.route('/stocksmith/api/dataset/<string:query>', methods=['GET'])
def get_dataset(query):
    return "hello"

@app.route('/stocksmith/api/stock-data/<string:query>', methods=['GET'])
def get_stock_data(query):
    return jsonify({'description': apiDescription[0]})


@app.route('/stocksmith/api/stock-info/<string:query>', methods=['GET'])
def get_stock_info(query):
    stock = yf.Ticker(query)
    return stock.info



# Helper Functions 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)