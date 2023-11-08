
import numpy as np
import pandas as pd
import os

url_predix = "https://golferchen.github.io/human-study-8888"
info = dict()
info["gt_audio_url"] = []
info["audio_url"] = []

root = '1/audio'
for pair_flag in sorted(os.listdir(root)):
    pair_dir = os.path.join(root, pair_flag)
    wav_names = os.listdir(pair_dir)
    wav_names = sorted(wav_names, key=lambda x: len(x)) 
    url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[0])
    info["gt_audio_url"].append(url)
    url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[1])
    info["audio_url"].append(url)

df = pd.DataFrame(info)
df.to_csv("1-unshuffle.csv", index=False)
print(df)
df = df.sample(frac=1)
print(df)
df.to_csv("1.csv", index=False)