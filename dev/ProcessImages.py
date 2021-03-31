import os
import cv2
import numpy

class processImage:
    def __init__(self, parent):
        self.parent=parent
        self.load_images_from_folder()

    def load_images_from_folder(self):
        images = []
        folder = "C:/Users/gnest/Documents/GitHub/C61-ProjetSynthese/dev/img/"
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
        self.getPixels(images)

    def getPixels(self, images):
        for image in images:
            rows, cols, channels = image.shape

            for i in range(rows):
                for j in range(cols):
                    k = image[i,j]
                    print(k)