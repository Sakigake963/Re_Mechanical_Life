"""
Recognize food: fruit, vegetable
"""

from camera import camera
from hsv import hsv
import io
import os
from datetime import datetime
import time
import requests as req
import sys
import cv2
import signal
from google.cloud import vision_v1p3beta1 as vision

# Setup google authen client key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

# Source path content all images
SOURCE_PATH = "/home/pi/mll/Re_Mechanical_Life/foodrecog/foods/"

FOOD_TYPE = 'Fruit'  #'Vegetable'


def load_food_name(food_type):
    """
    Load all known food type name.
    :param food_type: Fruit or Vegetable
    :return:
    """
    names = [line.rstrip('\n').lower() for line in open('dict/' + food_type + '.dict')]
    return names


def recognize_food(img_path, list_foods):
    start_time = datetime.now()
    
    # Read image with opencv
    img = cv2.imread(img_path)
    
    # Get image size
    height, width = img.shape[:2]
    
    # Scale image
    img = cv2.resize(img, (800, int((height * 800) / width)))

    # Save the image to temp file
    cv2.imwrite(SOURCE_PATH + "output.jpg", img)
    
    # Create new img path for google vision
    img_path = SOURCE_PATH + "output.jpg"
    
    # Create google vision client
    client = vision.ImageAnnotatorClient()

    # Read image file
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)

    # Recognize text
    response = client.object_localization(image=image)
    labels = response.localized_object_annotations

    for label in labels:
        #if len(text.description) == 10:
        cnt = 1
        desc = label.name.lower()
        score = round(label.score, 2)
        print("label: ", desc, "  score: ", score)
        #res = req.post("http://your-django-app.com/receive_data/"json={"food"+str(cnt):desc})
        cnt += 1
        if (desc in list_foods):
            #score = round(label.score, 3)
            #print(desc, 'score: ', score)

            # Put text license plate number to image
            cv2.putText(img, desc.upper() + " ???", (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 200), 2)
            cv2.imshow('Recognize & Draw', img)
            cv2.waitKey(0)
            
            # Get first fruit only
            break
        
    print('Total time: {}'.format(datetime.now() - start_time))


'''
def main():
    path = SOURCE_PATH + 'camera_1.jpg
    print('---------- Start FOOD Recognition --------')
    list_foods = load_food_name(FOOD_TYPE)
    #print(list_foods)
    while(1):
        camera('1')
        value = hsv()
        if(value >= 100):
            path = SOURCE_PATH + 'camera_1.jpg'
            recognize_food(path, list_foods)
            time.sleep(2)
        else:
            continue
        time.sleep(0.1)
        
    print('---------- End ----------')
'''

def main():
    path = SOURCE_PATH + 'camera_1.jpg'
    list_foods = load_food_name(FOOD_TYPE)
    while(1):
        camera('1')
        recognize_food(path, list_foods)
        time.sleep(0.1)  


try:
    main()
except KeyboardInterrupt:
    signal.signal(signal.SIGNAL, signal.SIG_DFL)
