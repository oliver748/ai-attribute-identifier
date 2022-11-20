# train all the data from images

from fastai.vision.all import *

def label_func(x): 
    return x.parent.name

def train():
    path = Path("C:/Users/oliver/Desktop/race-identifier/images/")
    fnames = get_image_files(path)
    print(f"Total Images: {len(fnames)}")

    dls = ImageDataLoaders.from_path_func(path, fnames, label_func, 
        bs=40, num_workers=0, weights=ResNet18_Weights.DEFAULT
    )
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    print("Loaded")
    # the higher number here (i use 8), the better it is with the same images
    learn.fine_tune(8, base_lr=1.0e-02) 

    #exports to images folder
    learn.export()


if __name__ == '__main__':
    train()