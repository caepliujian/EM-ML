"""Loads multiple chemprop models and make predictions on a dataset."""
from EMML_utils import *


if __name__ == '__main__':
    # make_predictions(args=PredictAllArgs().parse_args(predictAllArgsFromJson('predictArgs.json')))
    make_predictions(args=PredictAllArgs().parse_args(predictAllArgsFromParser()))
