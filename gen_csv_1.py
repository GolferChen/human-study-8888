
# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/human-study-8888"
# info = dict()
# info["gt_audio_url"] = []
# info["audio_url"] = []

# root = '1/audio'
# for pair_flag in sorted(os.listdir(root)):
#     pair_dir = os.path.join(root, pair_flag)
#     wav_names = os.listdir(pair_dir)
#     wav_names = sorted(wav_names, key=lambda x: len(x)) 
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[0])
#     info["gt_audio_url"].append(url)
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[1])
#     info["audio_url"].append(url)

# df = pd.DataFrame(info)
# df.to_csv("1-unshuffle.csv", index=False)
# print(df)
# df = df.sample(frac=1, random_state=666)
# print(df)
# df.to_csv("1.csv", index=False)



# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/human-study-8888"
# info = dict()
# info["gt_audio_url"] = []
# info["audio_url"] = []

# root = '2/audio'
# for pair_flag in sorted(os.listdir(root)):
#     pair_dir = os.path.join(root, pair_flag)
#     wav_names = os.listdir(pair_dir)
#     wav_names = sorted(wav_names, key=lambda x: len(x)) 
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[0])
#     info["gt_audio_url"].append(url)
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[1])
#     info["audio_url"].append(url)

# df = pd.DataFrame(info)
# df.to_csv("2-unshuffle.csv", index=False)
# print(df)
# df = df.sample(frac=1, random_state=666)
# print(df)
# df.to_csv("2.csv", index=False)




# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/human-study-8888"
# info = dict()
# info["audio_url"] = []

# root = '3/audio-partial'
# for wav_name in sorted(os.listdir(root)):
#     url = "{}/{}/{}".format(url_predix, root, wav_name)
#     info["audio_url"].append(url)

# df = pd.DataFrame(info)
# df.to_csv("3-unshuffle.csv", index=False)
# print(df)
# df = df.sample(frac=1, random_state=666)
# print(df)
# df.to_csv("3.csv", index=False)



# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/human-study-8888"
# info = dict()
# info["gt_audio_url"] = []
# info["audio_url"] = []

# root = '1/audio'
# for pair_flag in sorted(os.listdir(root)):
#     pair_dir = os.path.join(root, pair_flag)
#     wav_names = os.listdir(pair_dir)
#     wav_names = sorted(wav_names, key=lambda x: len(x)) 
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[0])
#     url = f'<iframe src={url} scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
#     info["gt_audio_url"].append(url)
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[1])
#     url = f'<iframe src={url} scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
#     info["audio_url"].append(url)

# df = pd.DataFrame(info)
# df.to_csv("1-unshuffle-html.csv", index=False)
# print(df)
# df = df.sample(frac=1, random_state=666)
# print(df)
# df.to_csv("1-html.csv", index=False)



# import numpy as np
# import pandas as pd
# import os

# url_predix = "https://golferchen.github.io/human-study-8888"
# info = dict()
# info["gt_audio_url"] = []
# info["audio_url"] = []

# root = '2/audio'
# for pair_flag in sorted(os.listdir(root)):
#     pair_dir = os.path.join(root, pair_flag)
#     wav_names = os.listdir(pair_dir)
#     wav_names = sorted(wav_names, key=lambda x: len(x)) 
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[0])
#     url = f'<iframe src={url} scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
#     info["gt_audio_url"].append(url)
#     url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_names[1])
#     url = f'<iframe src={url} scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
#     info["audio_url"].append(url)

# df = pd.DataFrame(info)
# df.to_csv("2-unshuffle-html.csv", index=False)
# print(df)
# df = df.sample(frac=1, random_state=666)
# print(df)
# df.to_csv("2-html.csv", index=False)


import numpy as np
import pandas as pd
import os

url_predix = "https://golferchen.github.io/human-study-8888"
info = dict()
info["audio_url"] = []

root = '3/audio-partial'
for wav_name in sorted(os.listdir(root)):
    url = "{}/{}/{}".format(url_predix, root, wav_name)
    url = f'<iframe src={url} scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
    info["audio_url"].append(url)

df = pd.DataFrame(info)
df.to_csv("3-unshuffle-html.csv", index=False)
print(df)
df = df.sample(frac=1, random_state=666)
print(df)
df.to_csv("3-html.csv", index=False)