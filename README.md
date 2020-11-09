# MonoEye-Dataset

This repository is for the dataset of ["MonoEye: Multimodal Human Motion Capture System Using A Single Ultra-Wide Fisheye Camera"](https://dl.acm.org/doi/abs/10.1145/3379337.3415856) (UIST 2020).

## Download Dataset [MacOS and Linux]
You need around 600GB of storage to download the dataset contains compressed and decompressed files.
Make sure wget is installed:
```
# on Mac OS
brew install wget
```

To download the dataset, you need to agree the license in LICENSE.md and set the flag and download path in conf.ig file. 
Then use the download.py python script:
```
python ./download.py
```
Decompress the dataset with following command:
```
cat ./DOWNLOAD_PATH/train-set.* | tar xvfz -
```

## Structure
### Path
The synthetic dataset is structured as follows (train, valid, and test sets.):

```
synthetic
├── train
│   ├── body
│   │   └── 00000000.png
│   │   └── ...
│   │   └── gt.csv
│   ├── head
│   │   └── 00000000.png
│   │   └── ...
│   │   └── gt.csv
│   ├── camera
│   │   └── 00000000.png
│   │   └── ...
│   │   └── gt.csv
│
├── valid
│   ├── body
│   ├── head
│   ├── camera
│
├── test
│   ├── body
│   ├── head
│   ├── camera
```
### Body
In gt.csv for body pose, for each line, the joint information is structured as follows:
```
x_2d_1, y_2d_1, x_2d_2, y_2d_2, ... x_2d_15, y_2d_15, x_3d_1, y_3d_1, z_3d_1, ..., x_3d_15, y_3d_15, z_3d_15
```
### Head
In gt.csv for head pose, for each line, the rotation information is structured as follos:
```
pitch, yaw, roll
```

### Camera
In gt.csv for camear pose, for each line, the rotation information is structured as follows (Please ignore the roll data.):
```
pitch, yaw, roll(dummy)
```

### 

## Citation
If you find our work useful in your research, please cite our paper.
```
@inproceedings{hwang20_uist,
    author = {Hwang, Dong-Hyun and Aso, Kohei and Yuan, Ye and Kitani, Kris and Koike, Hideki},
    title = {MonoEye: Multimodal Human Motion Capture System Using A Single Ultra-Wide Fisheye Camera},
    year = {2020},
    doi = {10.1145/3379337.3415856},
    booktitle = {Proceedings of the 33rd Annual ACM Symposium on User Interface Software and Technology},
    pages = {98–111},
    numpages = {14},
    location = {Virtual Event, USA},
    series = {UIST '20}
}
```
