from typing import Union
from fastapi import FastAPI
import pickle
from fishregression.model.manager import get_model_path

app = FastAPI()

#무게 예측 함수
def run_prediction(length:float):
	model_path = get_model_path()
	with open(model_path, "rb") as f:
		fish_model = pickle.load(f)
	prediction = fish_model.predict([[length ** 2, length]])
	return float(prediction[0])

@app.get("/")
def read_root():
	return{"hello": "fish"}

@app.get("/fish_ml_regression")
def lr_api(length: float):
	"""
	물고기의 무게를 예측하는 함수

	Args:
		length(float): 물고기 길이(cm)

	Returns:
		dict:
			weight(float): 물고기 무게(g)
			length(float): 물고기 길이(cm)
	"""

##예측 후 결과
	prediction = run_prediction(length)

	return { "length" : length, "prediction" : prediction }
