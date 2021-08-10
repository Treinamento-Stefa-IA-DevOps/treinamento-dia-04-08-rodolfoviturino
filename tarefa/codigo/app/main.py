import pickle
import uvicorn
import sklearn
import pandas
from fastapi import FastAPI

result = 'asd'
app = FastAPI()
@app.post('/')
## Coloque seu codigo na função abaixo
def titanic(Sex:int,
            Age:float,
            Lifeboat:int,
            Pclass:int):
        with open('Titanic.pkl', 'rb') as fid: 
                titanic = pickle.load(fid)
                X_test = [[Sex, Age, Lifeboat, Pclass]]
                result = titanic.predict(X_test)

@app.get('/')
def get():
    global result
    return {'survived':result,
            'status':'int',
            'message':'string'}
