import json
import sys
import argparse
import os
import os.path as osp
import cv2
import xml.dom
import xml.dom.minidom
import numpy as np

from txtGenerator import generate_txt
from xmlGenerator import createRootNode, createObjectNode, writeXMLFile
from imgEnhance import enhance

def ArgumentParser():
    parser = argparse.ArgumentParser(description='Parse json annotations file and convert to VOC style')
    parser.add_argument('--output_path', default='/home/pwhuang/data/VOCdevkit')
    parser.add_argument('--anno_path', default='output.json')
    return parser.parse_args()

args = ArgumentParser()

DATASET = "VOC2007"
IMG_PATH = osp.join(args.output_path, DATASET, 'JPEGImages')
XML_PATH = osp.join(args.output_path, DATASET, 'Annotations')
if not os.path.exists(XML_PATH):
    os.mkdir(XML_PATH)

train_anno = args.anno_path
with open(train_anno) as f:
    data = json.load(f)
    category = [c['name'] for c in data['categories']]
    images = data['images']
    annotation = data['annotations']

# id to image mapping
imageDict = {}
for image in images:
    if image['has_annots'] == True:
        key = image['id']
        imageDict[key] = image['file_name']

img = imread(images[0])
mean = np.mean(img, (0,1))
print(mean)
height, width, channel = (320, 640, 3)

total_annotation = {}
category_count = [0 for i in range(len(category))] 
counter = 0

for a in annotation:
    image_name = imageDict[a['image_id']].replace('.jpg', '')
    idx = a['category_id']-1
    single_ann = []
    single_ann.append(image_name)
    single_ann.append(category[idx])
    single_ann.extend(a['bbox'])

    if single_ann[4] != 0 and single_ann[5] != 0 and single_ann[2] < width and single_ann[3] < height:
        if image_name not in total_annotation:
            total_annotation[image_name] = []
        category_count[idx] += 1      
        total_annotation[image_name].append(single_ann)
    else:
        counter += 1

print('\n==============[ {} json info ]=============='.format(DATASET))
print("Total Annotations: {}".format(len(annotation)))
print("Total Image: {} / {}".format(len(total_annotation), len(images)))
print("wrong size Image: {}".format(counter))
print("Image shape: ({}, {})".format(width, height))
print("Total Category: {}".format(len(category)))
print("{:^20}| count".format("class"))
print('----------------------------')
for c, cnt in zip(category, category_count):
    if cnt != 0:
        print("{:^20}| {}".format(c, cnt))
fnames = list(total_annotation.keys())

for fname in fnames:
    is_save = True
    saveName = os.path.join(XML_PATH, fname + '.xml')
    doc, root_node = createRootNode(DATASET, fname, width, height, channel)

    for anno in total_annotation[fname]:
        object_node = createObjectNode(doc, anno, width, height)
        root_node.appendChild(object_node)    
    if is_save:
        writeXMLFile(doc, saveName)

generate_txt(DATASET)
