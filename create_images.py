import cv2, numpy, os

path = "C:/Users/oliver/Desktop/race-identifier"

data = numpy.load(f"{path}/data/training_data.npy", allow_pickle=True)
targets = numpy.load(f"{path}/data/target_data.npy", allow_pickle=True)

# makes sure that images directory is available
if not os.path.isdir("images"):
    os.mkdir("images")

# this is used to not get duplicates when saving the images
whites = 0
asians = 0
blacks = 0
m_easterns = 0 # middle eastern
latinos = 0
indians = 0


# store both data and targets in a list.
holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

# saves images to the correct folder
print("Writing images")
for data in holder_list:
    key = data[1]
    image = data[0]
    if key == 'W':
        whites += 1
        cv2.imwrite(f"{path}/images/white/white_{whites}.png", image) 
    if key == 'A':
        asians += 1
        cv2.imwrite(f"{path}/images/asian/asian_{asians}.png", image) 
    if key == 'B':
        blacks += 1
        cv2.imwrite(f"{path}/images/black/black_{blacks}.png", image) 
    if key == 'M':
        m_easterns += 1
        cv2.imwrite(f"{path}/images/middle-eastern/middle_eastern_{m_easterns}.png", image) 
    if key == 'L':
        latinos += 1
        cv2.imwrite(f"{path}/images/latino/latino_{latinos}.png", image) 
    if key == 'I':
        indians += 1
        cv2.imwrite(f"{path}/images/indian/indian_{indians}.png", image) 

total = latinos + whites + blacks + asians + indians + m_easterns
print(f"Total images written: {total}")