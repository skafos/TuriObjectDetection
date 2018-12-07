# Turi Object Detection

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training an object detection model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's object detection example which can be found [here](https://apple.github.io/turicreate/docs/userguide/object_detection/). 

## What is here?

The two main components to this repo are:
- `object_detection.py` - a Skafos job that trains an object detection model and saves a core ml model
- `object_detection.ipynb` - a python notebook with the same code as the above `object_detection.py` job.

Additionallly, there exist:
- `metis.config.yml` - a file telling Skafos how to execute the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos
- `load_object_data.ipynb` - a helper notebook that saved the data in the proper format for this model. This was taken from [Turi Create's own data cleaning](https://apple.github.io/turicreate/docs/userguide/object_detection/data-preparation.html)

## Further notes:
- For retraining this object detection model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create object detection model takes about 60 minutes on a GPU and about 1.5 days on Skafos with 6 CPU's and 10G of memory. Training will take considerably more time locally using only CPU. GPU support on Skafos is currently in development and will be coming soon.
