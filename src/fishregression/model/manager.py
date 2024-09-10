import os

def get_model_path():
	my_path = __file__
	file_name = 'model.pkl'
	dir_name = os.path.dirname(my_path)
	model_path = os.path.join(dir_name, file_name)
	return model_path
