# can be used to combine training data and target data

import numpy


# paths 
output_path = "C:/Users/oliver/Desktop/ai-attribute-identifier/data"
training_data_1 = "C:/Users/oliver/Desktop/ai-attribute-identifier/training_data.npy"
target_data_1 = "C:/Users/oliver/Desktop/ai-attribute-identifier/target_data.npy"
training_data_2 = "C:/Users/oliver/Desktop/ai-attribute-identifier/data/training_data.npy"
target_data_2 = "C:/Users/oliver/Desktop/ai-attribute-identifier/data/target_data.npy"


print("Combining data")
image_data = list(numpy.load(training_data_1, allow_pickle=True))
image_data += list(numpy.load(training_data_2, allow_pickle=True))

targets = list(numpy.load(target_data_1, allow_pickle=True))
targets += list(numpy.load(target_data_2, allow_pickle=True))



# !!! REMEMBER TO RENAME THEM AFTER SO TRAIN.PY INTERPRETES THE RIGHT DATA !!!
print("Saving data")
numpy.save(f"{output_path}/new_training_data", image_data)
numpy.save(f"{output_path}/new_target_data", targets)
print("Done")
