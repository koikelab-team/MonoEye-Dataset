import json
from itertools import chain, product
from string import ascii_lowercase
try:
    import wget
except:
    print("Please install the python wget package first!")
    exit(1)

# cat test-set.* | tar xvzf -


base_link = "https://github.com/koikelab-team/MonoEye-Dataset/releases/download/v1/"
train_prefix = "train-set.part"
train_last_chunk = 'fw'
test_prefix = "test-set.part"
test_last_chunk = 'ab' 

if __name__ == "__main__":
    print("MonoEye-dataset Downloader")
    with open("./conf.ig", "r") as st_json:
        config = json.load(st_json)

    download_path = config['download_path']
    
    if config['agree_to_license'] == 0:
        print("Can't download the dataset without agreement for license.")
        exit(1)

    if config['download_trainset'] == 1:
        print("Download trainset.")
        for combo in chain(product(ascii_lowercase, repeat=2)):
            part_name = "".join(combo)
            url = base_link + train_prefix + part_name
            print("Downloading " + train_prefix + part_name)
            wget.download(url, out=download_path)

            if part_name == train_last_chunk:
                print("Finish to download trainset.")
                break        

    if config['download_testset'] == 1:
        print("Download testset.")
        for combo in chain(product(ascii_lowercase, repeat=2)):
            part_name = "".join(combo)
            url = base_link + test_prefix + part_name
            print("Downloading " + test_prefix + part_name)
            wget.download(url, out=download_path)

            if part_name == test_last_chunk:
                print("Finish to download testset.")
                break        
