API
===

.. data:: download

**Function Description** : 

Download SVHN dataset from `the original svhn dataset <http://ufldl.stanford.edu/housenumbers>`_ 

**Optional features** : 

* Extract the downloaded dataset.
* Delete the .tar.gz file after downloading.

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter
     - Default Value
     - Description
   * - dataset_type
     - 'train'
     - Dataset type. One of 'train', 'test' or 'extra'
   * - save_path
     - ''
     - Dataset download path / extraction path. **The path should not contains any trailing '/'**
   * - extract
     - True
     - Whether or not the downloaded .tar.gz file should be extracted
   * - force
     - False
     - Download and save the dataset even if it's already in the given directory
   * - del_zip
     - False
     - Whether or not the .tar.gz file should be deleted after extraction

**Output view** : 

| `../data/svhn/train` : params : ('train', '../data/svhn', extract=True)
| `../data/svhn/train.tar.gz` : params : ('train', '../data/svhn', extract=False)

.. data:: ann_to_csv

**Function Description** :

Convert .mat file to .json file

**Optional features** : 

* Set bbox format to KITTI / Normalilzed

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter
     - Default value
     - Description
   * - file_path
     - None
     - .mat file path. Ex: relative path '../data/digitStruct.mat' or absolute path 'C:/usr/local/data/digitStruct.mat'
   * - save_path
     - None
     - .json file path Ex : '../data/train.json'
   * - bbox_type
     - 'normalize'
     - Two types of bounding box declaration formats: 'normalize' or 'kitti'

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

.. data:: ann_to_json

**Function Description** :

Convert .mat file to .csv file

**Optional features** : 

* Set bbox format to KITTI / Normalilzed

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter
     - Default value
     - Description
   * - file_path
     - None
     - .mat file path. Ex: relative path '../data/digitStruct.mat' or absolute path 'C:/usr/local/data/digitStruct.mat'
   * - save_path
     - None
     - .json file path Ex : '../data/train.csv'
   * - bbox_type
     - 'normalize'
     - Two types of bounding box declaration formats: 'normalize' or 'kitti'

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

.. data:: gen_dataset


**Function Description** :

Generate the image dataset and associated, readily-accessible annotation file.

**Optional features** : 

* Convert the RGB image to Gray-scale
* Set the threshold for the minimum # of digits present
* Set the threshold for the maximum # of digits present
* Crop the image to only include the digits with minimal background
* Resize the images
* Generate the annonations in two ways; In the first way the resulting annotations are directly compatible with the fixed numbered MDR task.
  The second annotation type is in a more generalized form. The resulting .json file could be converted into any well known annotation type [PascalVOC, COCO, YOLO-darkNet]. 
  For further image annotation conversions, you could use the python library called `imgann <https://pypi.org/project/imgann/>`_

.. list-table:: Parameter Description
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter
     - Default Value
     - Description
   * - image_path
     - None
     - The image folder path (*not the .tar.gz path*) without trailing '/'. Ex : '../data/train'
   * - mat_path
     - None
     - .mat file path Ex : '../data/train/digitStruct.mat'
   * - rgb
     - True (bool)
     - Whether to convert to RGB format
   * - min_digits
     - 0
     - The minimum number of digits in the SVHN image
   * - max_digits
     - 6
     - The maximum number of digits in the SVHN image *inclusive value*
   * - crop
     - True
     - Whether to crop the digit containing part from the original image
   * - resize_shape
     - (64, 64)
     - Shape to resize the image to. Could be rectangular or square in shape
   * - only_labels
     - False
     - If true, outputs only the labels in a numpy.ndarray. Else, outputs the formal json annotation file
   * - save
     - False
     - Whether or not to save the returned files

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
         .
      ],
   }