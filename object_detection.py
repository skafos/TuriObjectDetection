import urllib.request
import tarfile
import turicreate as tc
from skafossdk import *
import common.save_models as sm
import coremltools

ska = Skafos()


data_url = "https://s3.amazonaws.com/skafos.example.data/ObjectDetection/ig02.sframe.tar.gz"
data_path = "ig02.sframe.tar.gz"

# Fetch training data from an AWS bucket publicly hosted by Metis Machine. This data was generated using load_object_data.ipynb
ska.log("Retrieving the images from online", labels = ['image_similarity'])
retrieve = urllib.request.urlretrieve(data_url, data_path)

## pull the compressed data and extract it
ska.log("Images downloaded, extracting the images", labels = ['image_similarity'])
tar = tarfile.open(data_path)
tar.extractall()
tar.close()

# Load the data into a Turi Create SFrame.
data =  tc.SFrame('ig02.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Train an object detection model. This will take approximately 1.5 days on Skafos with 6CPU's and 10GB of RAM.
model = tc.object_detector.create(train_data)

# Save the model for later use in Skafos
coreml_model_name = 'object_detection.mlmodel'
res = model.export_coreml(coreml_model_name)

# convert model weights to half-precision to save on model size
model_spec = coremltools.utils.load_spec(coreml_model_name)
model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
coremltools.utils.save_spec(model_fp16_spec, coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')