# Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building object detection models. 

## Tips and "Gotchas"

-  **Training Data**: In order for an object detection model to identify a particular type of image, it must have seen other images with the same label. For example, if a model was trained on cars, bikes and people, and it is shown a plant, it will detect that plant as either a car, bike or person. To build an object detection model that identifies plants or other types of objects, you would need to retrain the model, using bounded and labeled images of the type you want.
-  **Model Runtime**: The out-of-the box model takes a long time to train on CPU. Try limiting the amount of data used to train the model. Likely, you don't need all 1,096 images of cars, bikes and people to get something working. Also, set `max_iterations` lower (default value is 10) in the `turicreate.object_detection.create` function if you want something to train quickly (at the cost of reduced accuracy).
-  **Model Size**: In addition to the tips above, try converting the CoreML model's weights to half-precision. This doesn't mean you sacrifice half of your accuracy, it simply means it uses less floating points in the weights of the model. To read more about this, check out [Apple's article](https://developer.apple.com/documentation/coreml/reducing_the_size_of_your_core_ml_app) on this topic.

## Resources

-  `object_images_in_turicreate.ipynb`: Gives some tips on wrangling image data and bounding boxes in Turi Create, detailing proper formatting and several helper functions.
-  `load_object_data.ipynb`: another module to help with wrangling images and bounding boxes.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/object_detection/) on object detection basics.
