import json
f = open("pattern")
lines = f.readlines()
total = {}

# category
total["categories"] = [{"id": 1, "name": "red"},
                       {"id": 2, "name": "green"},
                       {"id": 3, "name": "yellow"}]

# trivia
total["licenses"] = []
total["info"] = [{}]

# image
images = []
for i in range(5):
    d = {}
    d["id"] = i+1
    d["file_name"] = ("data%i.jpg" % (i+1))
    d["width"] = 640
    d["height"] = 320
    d["has_annots"] = True
    images.append(d)
total["images"] = images

anno_id = 0
image_id = 0
annotation = []

for line in lines:
    # print(line)
    if len(line.strip()) == 0:
        image_id += 1
    else:
        anno_id +=1
        data = line.split()
        d = {}
        d["id"] = anno_id
        d["image_id"] = image_id
        d["category_id"] = int(data[0])
        d["bbox"] = [float(data[i]) for i in range(1, 5)]
        d["area"] = float(data[5])
        d["roi_shape"] = "bbox"
        d["segmentation"] = []
        d["iscrowd"] = 0
        print(d)
        annotation.append(d)
total["annotations"] = annotation

f = open("output.json", "w")
aa = json.dump(total, f, indent=4, separators=(',', ":"))