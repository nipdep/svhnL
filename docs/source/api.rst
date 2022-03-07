API
===

.. data:: download

**Function Description** : 

download SVHN dataset from `the original svhn dataset <http://ufldl.stanford.edu/housenumbers>`_ 

**Optional features** : 

* extract downloaded dataset
* delete .tar.gz file after downloading

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - parameter
     - default value
     - description
   * - dataset_type
     - 'train'
     - dataset type from 'train', 'test' or 'extra'
   * - save_path
     - ''
     - dataset download path / extracting path, **path should not contains any training / **
   * - extract
     - True
     - whether or not extract the downloaded .tar.gz file
   * - force
     - False
     - download and save even the dataset already in the given directory
   * - del_zip
     - False
     - whether or not delete the .tar file after extraction

**Output view** : 

| `../data/svhn/train` : params : ('train', '../data/svhn', extract=True)
| `../data/svhn/train.tar.gz` : params : ('train', '../data/svhn', extract=False)

.. data:: ann_to_csv

**Function Description** :

convert .mat file into .json file

**Optional features** : 

* set bbox format to KITTI / Normalilzed

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - parameter
     - default value
     - description
   * - file_path
     - None
     - .mat file path Ex : relative path '../data/digitStruct.mat' or complete path 'C:/usr/local/data/digitStruct.mat'
   * - save_path
     - None
     - .json file directory *Otherthan .json file complete folder directory must exists in the system Ex : '../data/train.json'
   * - bbox_type
     - 'normalize'
     - two type bounding box declaration format whether 'normalize' or 'kitti'

**Output view** : 

.. list-table:: train.csv
   :widths: 25 25 25 25 25 25
   :header-rows: 1

   * - filename
     - class
     - left
     - top
     - width
     - height
   * - 1.png
     - 1
     - 81.0
     - 77.0
     - 246.0
     - 219.0
   * - 1.png
     - 9
     - 96.0
     - 81.0
     - 346.0
     - 119.0

.. data:: ann_to_json

**Function Description** :

convert .mat file into .csv file

**Optional features** : 

* set bbox format to KITTI / Normalilzed

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - parameter
     - default value
     - description
   * - file_path
     - None
     - .mat file path Ex : relative path '../data/digitStruct.mat' or complete path 'C:/usr/local/data/digitStruct.mat'
   * - save_path
     - None
     - .csv file directory *Other than .csv file complete folder directory must exists in the system Ex : '../data/train.json'
   * - bbox_type
     - 'normalize'
     - two type bounding box declaration format whether 'normalize' or 'kitti'

**Output view** : 

.. code-block:: JSON

   [
      {
         "boxes": [
         {
            "width": 81.0,
            "top": 77.0,
            "label": 1.0,
            "left": 246.0,
            "height": 219.0
         },
         {
            "width": 96.0,
            "top": 81.0,
            "label": 9.0,
            "left": 346.0,
            "height": 119.0
         }
         ],
         "filename": "1.png"
      },
      ...
   ]

.. data:: gen_dataset


**Function Description** :

generate image dataset and related readily accessible annotation file

**Optional features** : 

* convert RGB image to Gray-scale
* set min digits present threshold
* set max digits present threshold
* crop the image to only show digits with miinimum background
* resize the images
* generate annonation under two ways; in the first way the resulting annotation directly compatible with the fixed numbered MDR task.
  The sencond annotation type is more generalized form, actually the resulting .json file could convert into any wel-known annotation type [PascalVOC, COCO, YOLO-darkNet]. 
  For further image annotation conversion you could use python library called `imgann <https://pypi.org/project/imgann/>`_

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - parameter
     - default value
     - description
   * - image_path
     - None
     - image containing folder path *not the .tar.gz path * without trailing '/' mark Ex : '../data/train'
   * - mat_path
     - None
     - .mat file path Ex : '../data/train/digitStruct.mat'
   * - rgb
     - True (bool)
     - whether or not convert to RGB format or GRAYscale
   * - min_digits
     - 0
     - minimum number of digits must included in the SVHN image
   * - max_digits
     - 6
     - maximum number of digits that can contained in a image *inclusive value
   * - crop
     - True
     - whether to crop only digit containing part from the original image
   * - resize_shape
     - (64, 64)
     - image resize shape, could be rectangular or square in shape
   * - only_labels
     - False
     - if true outputs only labels in numpy.ndarray, if not outputs formal json annotation file
   * - save
     - False
     - whether or not save the returning files

**Output view** : 

.. code-block:: JSON

   {
      "annotations": [
         {
               "id": "1",
               "image_id": "1",
               "category_id": 1,
               "area": 22165,
               "bbox": [170, 114, 313, 269],
               "ignore": "0",
               "iscrowd": "0"
         },
         .
         .
         ],
      "images": [
         {
               "file_name": "1.jpg",
               "height": 413,
               "width": 413,
               "id": "1"
         },
         .
         .
         ],
      "categories": [
         {
               "id": 1,
               "name": 1,
               "supercategory": "none"
         },
         .
         ],
   }