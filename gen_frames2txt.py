#video, video_length, class
#1. read train_set -> video, class
#2. read each video dir and count frames -> #frame
#3. load to dict
#4. write dict to txt file

import os
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Dataset processor: Frames->txt")
parser.add_argument("dir_path", type=str, help="original dataset path")
parser.add_argument("dst_txt", type=str, help="dest path to save the txt")
parser.add_argument("target_txt", type=str, help="dest path to save the txt")
args = parser.parse_args()

if __name__ == "__main__":
    dir_path = args.dir_path
    dst_txt = args.dst_txt
    target_txt = args.target_txt

    targets = [x.strip() for x in open(target_txt).readlines()]
    dsts = [] 
    for target in tqdm(targets):
        video, anno = target.split(" ")
        video_path = os.path.join(dir_path, video)
        if os.path.exists(video_path):
            num_frames = len(os.listdir(video_path))
        else:
            print(f"no frames in {video}")
            continue

        summary = f"{video},{anno},{num_frames}"
        dsts.append(summary)
        
    with open(dst_txt, 'w') as f:
        for dst in dsts:
            f.write(dst)

    print("Done")


