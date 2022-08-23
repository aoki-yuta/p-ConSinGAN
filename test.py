# Input/Images/testの中身を一括実行

import subprocess
import os

path = "D:/dataset/place_v002/mask"
name_list = os.listdir(path)


print(name_list)

#python main_train.py --input_dir Input/Images/test --input_name colusseumm2.png --manualSeed 0 

cmd1 = ["python", "main_train.py", "--gpu", "0", "--train_mode", "inpainting", "--input_name", path, "--manualSeed", "0"]
# cmd2 = ["python", "random_samples_inpainting.py", "--input_dir", path, "--input_name", "images.png", "--mode", "random_samples_inpainting", "--gen_start_scale", "0", "--manualSeed", "0"]


for image_name in name_list:
    image_path = os.path.join(path, image_name)
    print(image_path)
    cmd1[7] = image_path
    print(cmd1)
    # cmd2[5] = image_name
    subprocess.run(cmd1, shell=True)
    # for i in range(11):
    #     cmd2[9] = str(i)
    #     subprocess.run(cmd2, shell=True)

