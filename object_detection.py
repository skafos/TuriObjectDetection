import urllib.request
import tarfile
import turicreate as tc
from skafossdk import *
import save_models as sm
import coremltools

ska = Skafos()


data_url = "https://s3.amazonaws.com/skafos.example.data/ObjectDetection/ig02.sframe.tar.gz"
data_path = "ig02.sframe.tar.gz"

# pull the tar
#ska.log("Retrieving the images from online", labels = ['image_similarity'])
retrieve = urllib.request.urlretrieve(data_url, data_path)

# extract the file
#ska.log("Images downloaded, extracting the images", labels = ['image_similarity'])
tar = tarfile.open(data_path)
tar.extractall()
tar.close()

# Load the data
data =  tc.SFrame('ig02.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data, max_iterations=900)

# Save the model for later use in Skafos
coreml_model_name = 'object_detection.mlmodel'
res = model.export_coreml(coreml_model_name)

# Convert to half-precision
model_spec = coremltools.utils.load_spec(coreml_model_name)
model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
coremltools.utils.save_spec(model_fp16_spec, coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')