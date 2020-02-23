from flask import Flask, jsonify
from flask import abort
import json

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
    return jsonify({'description': apiDescription[0]})

@app.route('/stocksmith/api/dataset/<string:query>', methods=['GET'])
def get_dataset(query):
    return jsonify({'description': apiDescription[0]})


@app.route('/stocksmith/api/dataset/<string:query>', methods=['GET'])
def get_dataset(query):
    return jsonify({'description': apiDescription[0]})



# Helper Functions 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)