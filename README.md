<h1 aling='center'>
    svhnL
</h1>
<p align='center'>
    SVHN dataset preprocessing and annotation file reading and converting python library
</p>

## Installation
> From PyPI : 
```
$ pip install svhnl
```

## Documentation
> From ReadtheDocs : [link](https://svhnl.readthedocs.io/en/latest/index.html)

## Functionalities

### _Dataset Download & extract_
To download the original SVHN dataset [train, test or extra] from their website and extract the downloaded .tar.gz file, use. \
Code Example : 
```
>>>> import svhnl
>>>> train_dt_filename = svhnl.download(extract=False)
'./data/train.tar.gz'
>>>> test_dt_folder_path = svhnl.download(dataset_type='test', save_path='../dataset/svhn', extract=True, force=False, del_zip=False)
'../dataset/svhn/test'
```

### _Convert Annotation file into JSON_
To read the .mat annotation file provided with the original svhn dataset and generate more flexible and light-weight .json annotation file, use. \
Code Example : 
```
import svhnl
svhnl.ann_to_json(file_path='./train/digitStruct.mat', save_path='./svhn_ann.json', bbox_type='normalize')
```

### _Convert Annotation file into csv_
To read the .mat annotation file provided with the original svhn dataset and generate more operatable and light-weight .csv annotation file, use. \
Code Example :
```
import svhnl
svhnl.ann_to_csv(file_path='./train/digitStruct.mat', save_path='./svhn_ann.csv', bbox_type='normalize')
```

### _Generate MDR dataset_
To easily use the SVHN dataset in any MDR task [defined number of digit recognition or without restrictions on object detection] with digit cropping, RGB to Gray-scale conversion, digit count limiting, etc.
Code Example :
```
import svhnl
image_np, ann_dict = svhnl.gen_dataset(image_path='../data/svhn/train', mat_path='../data/svhn/train/digitStruct.mat')
```


