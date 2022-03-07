API
===

.. data:: download

Function Description : 
download SVHN dataset from `the original svhn dataset <http://ufldl.stanford.edu/housenumbers>`_
Optional features:
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


.. data:: ann_to_csv

Function Description :
convert .mat file into .json file
Optional features:
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

.. data:: ann_to_json

Function Description :
convert .mat file into .csv file
Optional features:
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


.. data:: gen_dataset


Function Description :
generate image dataset and related readily accessible annotation file
Optional features:
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

