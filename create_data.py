import numpy, cv2, os, time, keyboard
from utilities.fetch_face import download_face
from utilities.key_input import key_check
from deepface import DeepFace


class CreateData:
    def __init__(self):
        self.file_training_data = "data/training_data.npy"
        self.file_target_data = "data/target_data.npy"

        image_data, targets = self.get_data()

        input('Press ENTER to start\n\n')

        print("Press D when you're done\n")
        print("W for White")
        print("A for Asian")
        print("B for Black")
        print("M for Middle Eastern")
        print("L for Latino")
        print("I for Indian")
        print("S for Skip (if you're not sure or an error has happened)\n")

        """
        this is to manually enter the race of every person popping up
        using cv2 and thispersondoesnotexist.com
        """
        # count = 0
        # run = True
        # while run:
        #     face = download_face()
        #     while run:
        #         cv2.imshow("Face", face)
        #         cv2.waitKey(25)
        #         key_press = key_check()
        #         if key_press:
        #             if key_press == "S": # for Skip
        #                 print("[LOG] - Skipped")
        #             elif key_press == "D": # for Done
        #                 run = False
        #             else:
        #                 count += 1
        #                 targets.append(key_press)
                         
        #                 # change cv2 settings here if images are too big
        #                 image = cv2.resize(face, (150, 150))
        #                 image = numpy.array(image)
        #                 image_data.append(image)

        #                 print(f"[LOG] - Race: {key_press} <-> Count: {count}")

        #             break

        """
        code under this comment can be used to train the model with
        deepface analyze to make the process much quicker.
        results can still be achieved through manual work though
        so dont worry about that! :)
        """

        count = 0
        while True:
            try:
                face = download_face()
                cv2.imshow("Face", face)
                cv2.waitKey(150)
                obj = DeepFace.analyze(img_path=face, actions=['race'], prog_bar=True)
                race = max(obj['race'], key=obj['race'].get)

                if race == "indian":
                    key_press = "I"
                elif race == "asian":
                    key_press = "A"
                elif race == "black":
                    key_press = "B"
                elif race == "latino hispanic":
                    key_press = "L"
                elif race == "white":
                    key_press = "W"
                elif race == "middle eastern":
                    key_press = "M"

                targets.append(key_press)

                image = cv2.resize(face, (150, 150))
                image = numpy.array(image)
                image_data.append(image)

                count += 1
                print(f"[LOG] - Race: {key_press} <-> Count: {count}")
                time.sleep(0.5)
                
            except ValueError:
                pass
            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break

        """
        found a dataset with selfies containing the race and all sorts
        of interesting things - therefore i wrote some code to interprate this
        specific dataset since its valuable
        only using this to train race atm but it can definitely be used to 
        train all sorts of things
        the dataset only tells if the person is asian, white or black so
        if the person is latino then we wont know, so i made a backup using
        deepface analyze because its dumb not to do it ;)

        dataset link: https://www.crcv.ucf.edu/data/Selfie/
        46836 selfies taken in 2015
        """

        # count = 0
        # folder = os.listdir("selfies")
        # folder = sorted(folder)
        # for file_name in folder:
        #     with open("selfie_dataset.txt", "r") as f:
        #         f = f.read().splitlines()
        #         f = sorted(f)
        #         for line in f:
        #             filename = line.split(" ")[0]
        #             if filename == file_name.split('.')[0]:
        #                 white = line.split(" ")[10]
        #                 black = line.split(" ")[11]
        #                 asian = line.split(" ")[12]
        #                 if line.split(" ")[2] == "-1":
        #                     if white == "1":
        #                         key_press = "W"
        #                     elif black == "1":
        #                         key_press = "B"
        #                     elif asian == "1":
        #                         key_press = "A"
        #                     else:
        #                         try:
        #                             obj = DeepFace.analyze(img_path=face, actions=['race'], prog_bar=True)
        #                             race = max(obj['race'], key=obj['race'].get)
        #                             if race == "indian":
        #                                 key_press = "I"
        #                             elif race == "asian":
        #                                 key_press = "A"
        #                             elif race == "black":
        #                                 key_press = "B"
        #                             elif race == "latino hispanic":
        #                                 key_press = "L"
        #                             elif race == "white":
        #                                 key_press = "W"
        #                             elif race == "middle eastern":
        #                                 key_press = "M"
        #                         except:
        #                             break
        #                     face = cv2.imread(f"selfies/{file_name}")
        #                     targets.append(key_press)
        #                     image = cv2.resize(face, (150, 150))
        #                     image = numpy.array(image)
        #                     image_data.append(image)
                                

        #                     count += 1
        #                     print(f"[LOG] - Race: {key_press} <-> Count: {count}")
        #                     break
        #                 else:
        #                     break
        #     if keyboard.is_pressed("½"):
        #         break


        ##########################

        print("[LOG] - Saving data")
        self.save_data(image_data, targets)

    def get_data(self):
        if os.path.isfile(self.file_training_data):
            print('Data already exists - loading previous data!')
            image_data = list(numpy.load(self.file_training_data, allow_pickle=True))
            targets = list(numpy.load(self.file_target_data, allow_pickle=True))
        else:
            print('File does not exist, starting out fresh!')
            image_data = []
            targets = []
        return image_data, targets


    def save_data(self, image_data, targets):
        numpy.save(self.file_training_data, image_data)
        numpy.save(self.file_target_data, targets)
    

if __name__ == "__main__":
    app = CreateData()