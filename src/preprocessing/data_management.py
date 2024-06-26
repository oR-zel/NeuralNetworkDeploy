import os 
import pandas as pd
import pickle

from src.config import config

def load_dataset(file_name):
    file_path = os.path.join(config.DATAPATH, file_name)
    #file_path me file_name waala dataset jo src/datasets me hai uska path stored hai as "/src/datasets/file_name"

    data = pd.read_csv(file_path)
    return data

def save_model(theta0,theta):
    
    pkl_file_path = os.path.join(config.SAVED_MODEL_PATH,"two_input_xor_nn.pkl")
    
    with open(pkl_file_path,"wb") as file_handle:
        
        pickle.dump({"biases":theta0,"weights":theta,"activation_function":{"0":None,"1":"Linear","2":"relu"}},file_handle)
        

def load_model(file_name):
    
    pkl_file_path = os.path.join(config.SAVED_MODEL_PATH,file_name)
    
    with open(pkl_file_path,"rb") as file_handle:
        trained_params = pickle.load(file_handle)
        
    return trained_params["biases"], trained_params["weights"]