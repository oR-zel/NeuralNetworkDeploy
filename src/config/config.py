import os
import pathlib

NUM_LAYERS = 3
NUM_INPUTS = 2
P = [NUM_INPUTS,2,1]

f = [None, "Linear", "Sigmoid"]

LOSS_FUNCTION = "Mean Squared Error"
MINI_BATCH_SIZE = 1

PACKAGE_ROOT = pathlib.Path(src.__file__).resolve().parent#Src ko root (parent) dir banane ke liye
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")
#Datapath variable ke andar training data ka location as a path yaha hai: "/src/datasets"
SAVED_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")
#Output same as above: "/src/trained_models"
