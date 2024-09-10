import requests
import json

def lr_api(length):
	headers = { 'accept' : 'application/json' }
	params = { 'length' : length }

	response = request.get('http://127.0.0.1:8001/fish_ml_regression', params=params, headers=headers)
	data = json.loads(response.text)
	r = data['prediction']

	return r

def knn_api(length, weight, n_neighbors=5):
	headers = { 'accept' : 'application/json' }
	params = { 'n_neighbors' : n_neighbors, 'length' : length, 'weight' : weight }
	response = requests.get('http://127.0.0.1:8001/fish_ml_regression', params=params, headers=headers)
	data =  json.loads(response.text)
	r = data['prediction']

	return r
 
def predict():
	length = float(input("물고기 무게를 입력하세요: "))

	## weight 예측 선형회귀 API 호출
	weight = lr_api(length)

	## 물고기 분류 API 호출
	fish_class = knn_api(length, weight)

	print(f"length:{length} 물고기는 weight:{weight}으로 예측되며 종류는 {fish_class} 입니다.")
