from fastapi import FastAPI
import os
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cache_dir = os.path.join(base_dir, 'cache')
dataset = os.path.join(cache_dir, 'movies-boxoffice-dataset-cleaned.csv')

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello" : "World"}


@app.get("/box-office")
def read_box_office_numbers():
    df = pd.read_csv(dataset)
    return df.to_dict("Rank")