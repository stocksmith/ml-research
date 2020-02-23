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

temp = {}
temp['date'] = 2018-12-28
temp['open'] = 65.45
testId = str(0)
doc_ref = db.collection(u'datasets').document(u'test')
doc_ref.set({
    testId : temp
}, merge=True)


# a = pd.read_csv(filepath_or_buffer = "../datasets/a.csv")

# for index, row in a.iterrows():
#     try: 
#         print(index)
#         datetime_object = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
#         print(datetime_object)
#     except:
#         print("An exception occurred")