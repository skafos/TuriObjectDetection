# Turi Object Detection

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training an object detection model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/object_detection/). The example model is based on images of cars, bikes and people. Given a new image containing cars, bikes, and or people, the model will detect instances of each and classify each instance as one of the three classes above.

## What is here?
The components of this repo are:

-  `object_detection.ipynb` - a Python notebook that trains and saves an object detection model to use in your app. Start here.
-  `utilities/` - a directory that contains helper functions used by `object_detection.ipynb`.
-  `advanced_usage/` - a directory that contains additional information about this object detection model, how to incorporate your own data, advanced usage, and additional example models.
-  `requirements.txt` - a file describing all required Python dependencies.

## About the model
-  The object detection model is trained on [images of people, cars and bikes](https://lear.inrialpes.fr/people/marszalek/data/ig02/).
-  Once trained, you can give the model a new image, and if the image contains a person, car or bike, it will:
    -  Detect the object in the image by surrounding it with a "bounding box".
    -  Classify the object within the bounding box as either a person, car or bike. 
-  The model takes several days to train in the JupyterLab session on CPUs. To decrease this run time, you can deploy as a job [and request a GPU for training](https://docs.metismachine.io/v1.3.1/docs/using-a-gpu).

## Going beyond the example
- If you wish to incorporate your own data or try another type of object detection model, check out the `advanced_usage/` section.
- Turi Create has built-in model evaluation and prediction techniques. We use some of the functions  in the `advanced_usage/` section, but for more detailed description, refer to Turi Create's [documentation](https://apple.github.io/turicreate/docs/api/turicreate.toolkits.evaluation.html).

## Need Help?
Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/object_detection) on object detection basics.
