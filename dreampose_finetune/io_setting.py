import os
import sys
from os.path import join

# Add submodule path into import paths
# is there a better way to handle the sub module path append problem?
PROJECT_FOLDER = os.path.dirname(__file__)
print('Project folder = {}'.format(PROJECT_FOLDER))
sys.path.append(join(PROJECT_FOLDER))

# Define the dataset folder and model folder based on environment
HOME_DATA_FOLDER = join(PROJECT_FOLDER, 'data')
DATASET_FOLDER = join(HOME_DATA_FOLDER, 'dataset')
MODEL_FOLDER = join(HOME_DATA_FOLDER, 'models')
OUTPUT_FOLDER = join(HOME_DATA_FOLDER, 'outputs')
PRETRAINED_MODEL_FOLDER = join(HOME_DATA_FOLDER, 'models/pretrained')
print('*' * 35, ' path_infor ', '*' * 35)
print('Data folder = {}'.format(HOME_DATA_FOLDER))
print('Dataset folder = {}'.format(DATASET_FOLDER))
print('Pretrained model folder = {}'.format(MODEL_FOLDER))
print('Output result folder = {}'.format(OUTPUT_FOLDER))
print('Pretrained model with finetuned folder = {}'.format(PRETRAINED_MODEL_FOLDER))
print('*' * 85)
os.environ['PYTORCH_PRETRAINED_BERT_CACHE'] = PRETRAINED_MODEL_FOLDER