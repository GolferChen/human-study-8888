
import pandas as pd
import numpy as np

def convert_answer(ori_answer):
    answer = []
    # print(answer)
    for x in ori_answer:
        if x == '相同':
            answer += [0]
        elif x == '部分相同':
            answer += [1]
        elif x == '不相同':
            answer += [2]
        elif '第一段' in x:
            answer += [3]
        elif '第二段' in x:
            answer += [4]
    return answer

# result_file_2 = '2-credamo.xlsx'
result_file_2 = '2-credamo-tol=30.xlsx'
df = pd.read_excel(result_file_2)
# print(df)

type_2_q_index = {}
type_2_q_index['adver_out'] =  [20, 21, 22, 29, 30]
type_2_q_index['adver_out_transfer'] = [6, 12, 18, 26, 32]
type_2_q_index['adver'] = [4, 8, 25, 28, 33]
type_2_q_index['adver_transfer'] = [10, 17, 19, 24, 27]
type_2_q_index['normal_out'] = [1, 2, 3, 5, 9, 13, 15, 16, 23, 31]

for type, q_index in type_2_q_index.items():
    type_2_q_index[type] = [f'Q{2*idx-1}' for idx in q_index]

type_2_answer = {}
for type in type_2_q_index.keys():
    type_2_answer[type] = []
    q_index = type_2_q_index[type]
    for idx in q_index:
        ori_answer = list(df[idx])
        answer = convert_answer(ori_answer)
        type_2_answer[type] += answer

# print(type_2_answer)

results = {'相同': [], '部分相同': [], '不相同': [], '模糊第一段': [], '模糊第二段': [], '模糊': [], '防御成功': []}
for type in type_2_answer.keys():
    answer = type_2_answer[type]
    p0 = np.argwhere(np.array(answer) == 0).flatten().size * 100 / len(answer)
    p1 = np.argwhere(np.array(answer) == 1).flatten().size * 100 / len(answer)
    p2 = np.argwhere(np.array(answer) == 2).flatten().size * 100 / len(answer)
    p3 = np.argwhere(np.array(answer) == 3).flatten().size * 100 / len(answer)
    p4 = np.argwhere(np.array(answer) == 4).flatten().size * 100 / len(answer)
    p_3_4 = (np.argwhere(np.array(answer) == 3).flatten().size +  np.argwhere(np.array(answer) == 4).flatten().size) * 100 / len(answer)
    p_d_s = (np.argwhere(np.array(answer) == 1).flatten().size +  np.argwhere(np.array(answer) == 2).flatten().size + np.argwhere(np.array(answer) == 4).flatten().size) * 100 / len(answer)
    results['相同'] += [round(p0, 2)]
    results['部分相同'] += [round(p1, 2)]
    results['不相同'] += [round(p2, 2)]
    results['模糊第一段'] += [round(p3, 2)]
    results['模糊第二段'] += [round(p4, 2)]
    results['模糊'] += [round(p_3_4, 2)]
    results['防御成功'] += [round(p_d_s, 2)]

r_df = pd.DataFrame(results, index=type_2_answer.keys())
print(r_df)
