import os
import mat73
import json
import numpy as np
import pandas as pd
import cv2


def normalized2KITTI(box):
    """
    convert Bbox format
    :param box: [X, Y, width, height]
    :return: [xmin, ymin, xmax, ymax]
    """
    o_x, o_y, o_width, o_height = box
    xmin = int(o_x)
    ymin = int(o_y)
    xmax = int(o_x + o_width)
    ymax = int(o_y + o_height)
    return [xmin, ymin, xmax, ymax]


def getName(dSName, n):
    """getName returns the 'name' string for for the n(th) digitStruct. """
    return dSName[n]


def getBbox_json(dSBbox, n, kitti=False):
    """getBbox returns a dict of data for the n(th) bbox. """
    # print(n)
    bboxs = []
    elem = dSBbox[n]
    # print(elem['height'])
    if isinstance(elem['height'], list):
        l = len(elem['height'])
    else:
        l = 1
    for i in range(l):
        try:
            h, y, l, t, w = [float(max(k[i], 0)) for k in elem.values()]
        except:
            h, y, l, t, w = [float(max(k, 0)) for k in elem.values()]
        if kitti:
            xmin, ymin, xmax, ymax = normalized2KITTI([l, t, w, h])
            bbox = {
                'xmin': xmin,
                'ymin': ymin,
                'xmax': xmax,
                'ymax': ymax,
                'label': y
            }
        else:
            bbox = {
                'height': h,
                'width': w,
                'top': t,
                'left': l,
                'label': y
            }
        bboxs.append(bbox)
    return bboxs


def getDigitStructure_json(dSBbox, dSName, n, format_type):
    """get annotation for given index in dictionary format"""
    s = {}
    s['boxes'] = getBbox_json(dSBbox, n, format_type)
    s['name'] = getName(dSName, n)
    return s


def ann_to_json(file_path, save_path, bbox_type='normalize'):
    """convert .mat annotation file into .json file

    Args:
        file_path (str): .mat file path Ex : relative path '../data/digitStruct.mat' or complete path 'C:/usr/local/data/digitStruct.mat'
        save_path (str): .json file directory *Otherthan .json file complete folder directory must exists in the system Ex : '../data/train.json'
        bbox_type (str, optional): two type bounding box declaration format whether 'normalize' or 'kitti'. Defaults to 'normalize'.

    Returns:
        None : just save the .json file in the given dir.
    """
    data_dict = mat73.loadmat(file_path)
    dSName = data_dict['digitStruct']['name']
    dSBbox = data_dict['digitStruct']['bbox']
    if bbox_type == 'kitti':
        t = True
    else:
        t = False
    json_data = [getDigitStructure_json(
        dSBbox, dSName, i, t) for i in range(len(dSBbox))]

    with open(save_path, 'w', encoding='utf-8') as pf:
        json.dump(json_data, pf, ensure_ascii=True, indent=4)


def getBbox_csv(dSBbox, n, kitti=False):
    """getBbox returns a dict of data for the n(th) bbox. """
    # print(n)
    bboxs = []
    elem = dSBbox[n]
    # print(elem['height'])
    if isinstance(elem['height'], list):
        l = len(elem['height'])
    else:
        l = 1
    for i in range(l):
        # print(elem.values())
        try:
            h, y, l, t, w = [float(k[i]) for k in elem.values()]
        except:
            h, y, l, t, w = [float(k) for k in elem.values()]
        if kitti:
            xmin, ymin, xmax, ymax = normalized2KITTI([l, t, w, h])
            bbox = [xmin, ymin, xmax, ymax, y]
        else:
            bbox = [l, t, w, h]
        bboxs.append(bbox)
    return bboxs


def getDigitStructure_csv(dSBbox, dSName, n, format_type):
    """get annotation for given index in list of lists format"""
    s = getBbox_csv(dSBbox, n, format_type)
    filen = getName(dSName, n)
    for lis in s:
        lis.insert(0, filen)
    return s


def ann_to_csv(file_path, save_path, bbox_type='normalize'):
    """convert .mat annotation file into .csv file

    Args:
        file_path (str): .mat file path Ex : relative path '../data/digitStruct.mat' or complete path 'C:/usr/local/data/digitStruct.mat'
        save_path (str): .json file directory *Otherthan .json file complete folder directory must exists in the system Ex : '../data/train.json'
        bbox_type (str, optional): two type bounding box declaration format whether 'normalize' or 'kitti'. Defaults to 'normalize'.

    Returns:
        None : just save the .csv file in the given dir.
    """
    data_dict = mat73.loadmat(file_path)
    dSName = data_dict['digitStruct']['name']
    dSBbox = data_dict['digitStruct']['bbox']

    if bbox_type == 'kitti':
        t = True
    else:
        t = False

    data_arr = []
    for i in range(len(dSBbox)):
        data_arr.extend(getDigitStructure_csv(dSBbox, dSName, i, t))

    numpy_data = np.array(data_arr)
    if t:
        cols = ['filename', 'class', 'left', 'top', 'width', 'height']
    else:
        cols = ['filename', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    df = pd.DataFrame(data=numpy_data, columns=cols)
    df.to_csv(save_path, index=False)


def get_ann(img, bbox_data, img_name, i, e):
    """generate annotation according to formal .json file format from the .mat file"""
    bboxs = []
    images = []
    for b in bbox_data:
        e += 1
        point = {
            "id": e,
            "image_id": i,
            "category_id": b['label'],
            "area": (b['xmax']-b['xmin'])*(b['ymax']-b['ymin']),
            "bbox": [b['xmin'], b['ymin'], b['xmax'], b['ymax']],
            "ignore": 0,
            "iscrowd": 0
        }
        bboxs.append(point)

        im = {
            "file_name": img_name,
            "height": img.shape[0],
            "width": img.shape[1],
            "id": i,
        }
        images.append(im)
    return bboxs, im, e


def crop_image(image, bboxs, eps=3):
    """ crop only digit containing part from the image
    bboxs = [
        [xmin, ymin, xmax, ymax],
    ] <np.ndarray>"""
    crp_xmin = np.min(bboxs[:, 0])
    crp_ymin = np.min(bboxs[:, 1])
    crp_xmax = np.max(bboxs[:, 2])
    crp_ymax = np.max(bboxs[:, 3])
    crp_image = image[crp_ymin:crp_ymax, crp_xmin:crp_xmax, :]
    return crp_image


def gen_dataset(image_path, mat_path, rgb=True, min_digits=0, max_digits=6, crop=True, resize_shape=(64, 64), only_labels=False, save=False):
    """dataset generator that can be directly used in the MDR project

    Args:
        image_path (str): image containing folder path *not the .tar.gz path * without trailing '/' mark Ex : '../data/train'
        mat_path (str): .mat file path Ex : '../data/train/digitStruct.mat'
        rgb (bool, optional): whether or not convert to RGB format or GRAYscale. Defaults to True.
        min_digits (int, optional): minimum number of digits must included in the SVHN image. Defaults to 0.
        max_digits (int, optional): maximum number of digits that can contained in a image *inclusive value. Defaults to 6 [this is empirical maximum value].
        crop (bool, optional): whether to crop only digit containing part from the original image. Defaults to True.
        resize_shape (tuple, optional): image resize shape. Defaults to (64, 64).
        only_labels (bool, optional): if true outputs only labels in numpy.ndarray, if not outputs formal json annotation file. Defaults to False.
        save (bool, optional): whether or not save the returning files. Defaults to False.

    Returns:
        images: numpy ndarray object, with shape of [N, resize_shape, 1] <- if rgb=False, else [N, resize_shape, 3] ; where resize_shape == w,h
        annotation: numpy ndarray or python dictionary object
    """

    # load and filter num of labels
    data_dict = mat73.loadmat(mat_path)
    dSName = data_dict['digitStruct']['name']
    dSBbox = data_dict['digitStruct']['bbox']

    images = []
    if only_labels:
        annotation = []
    else:
        annotation = {
            "annotations": [],
            "image": [],
            "categories": [{"id": g, "name": g, "supercategory": "none"} for g in range(10)]
        }

    e = 0
    for i in range(len(dSBbox)):
        bbox_data = getDigitStructure_json(dSBbox, dSName, i, True)
        l = len(bbox_data['boxes'])
        if (l < max_digits) and (l > min_digits):
            img = cv2.imread(f"{image_path}/{bbox_data['name']}")
            if rgb:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            if only_labels:
                labels = [bbox_data['boxes']['label'] for _ in range(l)]
                annotation.append(labels)
            else:
                box_data, image_data, e = get_ann(
                    img, bbox_data['boxes'], bbox_data['name'], i, e)
                annotation['annotations'].append(box_data)
                annotation['image'].append(image_data)

            if crop:
                bboxs = np.array([list(b.values())[:-1]
                                 for b in bbox_data['boxes']])
                img = crop_image(img, bboxs, 5)
            try:
                img = cv2.resize(img, resize_shape,
                                 interpolation=cv2.INTER_AREA)
            except:
                print(img.shape, bbox_data['name'], bbox_data['boxes'])
            images.append(img)

    if save:
        with open('./image_dataset.npy', 'wb') as pf:
            np.save(pf, np.array(images))

        if only_labels:
            with open('./labels.npy', 'wb') as pf:
                np.save(pf, np.array(annotation))

        else:
            with open('./labels.json', 'w', encoding='utf-8'):
                json.dump(annotation, pf, ensure_ascii=True, indent=4)

    if only_labels:
        return np.array(images), np.array(annotation)
    else:
        return np.array(images), annotation
