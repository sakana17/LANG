import json


# with open('dataset/plans.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
    
# for one in data:
#     one['plan-zh'] = one['report-zh']
#     one['plan-en'] = one['report-en']
#     for d in ['source similarity', 'source-zh', 'source-en', 'ansers', 'tokens', 'report-en', 'report-zh']:
#         one.pop(d, None)  # 用 pop 避免 KeyError

# with open('dataset/plans.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)



# 读取原始大文件
with open('dataset/corpus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 拆分
split_index = 60000
data1 = data[:split_index]
data2 = data[split_index:]

# 写入第一个文件
with open('dataset/corpus-01.json', 'w', encoding='utf-8') as f:
    json.dump(data1, f, ensure_ascii=False, indent=4)

# 写入第二个文件
with open('dataset/corpus-02.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f, ensure_ascii=False, indent=4)