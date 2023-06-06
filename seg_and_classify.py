import numpy as np
import matplotlib.pyplot as plt
import cv2
import functions

#for detection/segmentation
from ultralytics import YOLO

#for classificatcion
import keras


seg_model = YOLO("yolov8l-seg.pt")
cla_model = keras.models.load_model("n_data_aug_92.h5")

def get_seg(image):
    seg_res = seg_model(image)[0]
    seg_res_boxes = seg_res.boxes.cls.numpy()
    banana_box_idx = np.where(seg_res_boxes == 46.)[0]
    if banana_box_idx.size == 0:
        print("no banana found")
        return 0
    if banana_box_idx.size > 1:
        print("more than one banana found, not handled yet")
        return 0
    mask = np.zeros_like(image)
    mask = cv2.drawContours(mask, [seg_res.masks.xy[0].astype(int)], 0, (255,255,255), -1)
    seg_image = mask & image
    plt.figure()
    plt.imshow(seg_image)
    plt.show()
    return seg_image

def seg_n_class(image):
    seg_image = get_seg(image)
    if type(seg_image) == int:
        return 0
    t_image = functions.transform(seg_image)
    cla_result = cla_model.predict(t_image.reshape(1, 64,64,3))[0]
    print(cla_result)
    print(np.dot(np.array([0,1,2,3]), np.array(cla_result)))
    return  np.dot(np.array([0,1,2,3]), np.array(cla_result))