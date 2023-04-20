import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASE_DIR = os.path.join(ROOT_DIR, 'database')
CONFIG_DIR = os.path.join(ROOT_DIR, 'configs')
SRC_DIR = os.path.join(ROOT_DIR, 'src')
MODEL_DIR = os.path.join(SRC_DIR, 'model')
MODEL_SCRIPTS_DIR = os.path.join(MODEL_DIR, 'scripts')
MODEL_WEIGHTS_DIR = os.path.join(MODEL_DIR, 'weights')
MODEL_INFERENCE_DIR = os.path.join(MODEL_DIR, 'inference')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
