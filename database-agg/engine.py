# Pandas
import datetime
import pandas as pd

# Initialize fireabase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('stocksmith.json')
firebase_admin.initialize_app(cred)
db = firestore.client()



a = pd.read_csv(filepath_or_buffer = "../datasets/a.csv")

for index, row in a.iterrows():
    try: 
        temp = {}
        datetime_object = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
        
        # Adding to temp json
        temp['date'] = datetime_object
        temp['volume'] = row['volume']
        temp['open'] = row['open']
        temp['close'] = row['close']
        temp['low'] = row['low']
        temp['high'] = row['high']
        temp['adjclose'] = temp['adjclose']
        
        tempId = str(index)
        doc_ref = db.collection(u'datasets').document(u'a')
        doc_ref.set({
            tempID : temp
        }, merge=True)


        
    except:
        print("An exception occurred")