# AI Attribute Identifier - will have more options than just race in the future!
AI Attribute Identifier can be used to identify race of a specific person on an image using fastai's wonderful deep learning library. It can be trained on any dataset - though I didn't even use a dataset as you will see if you look at the code; instead I used thispersondoesnotexist.com for my "dataset" because I couldn't find a good enough dataset. It works brilliantly though :) 

It's not capable of anything other than identifying a person's race at the moment but I'm sure it'll change in the future when I work on this project more.
Other attributes I'm gonna add in the future are things like emotion, age, eye color, bald/not bald, gender etc.

It can identify a total of 6 races:
- white
- black
- latino
- indian
- asian
- middle eastern

In the start it wasn't good at all but when I spent a solid 25 minutes gathering data, it was surprisingly good in the end.

You can test it out without training at all by using the example model called 'example.pkl' in the models folder.

# Installation
1. Git clone or download it
2. Use 'pip install -r requirements.txt'
3. Run setup.py
4. Make sure all the paths in the .py files are adjusted to you
4. Create data by using 'create_data.py' (manually takes a long time)
5. Transform the data into images using 'create_images.py'
6. Train the model using 'train.py'
7. Use the model with 'agent.py' by loading the .pkl file

# Credits
A huge thanks to ClarityCoders (https://github.com/ClarityCoders) for his FallGuysAI repo which is the whole foundation of this project. 
