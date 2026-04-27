from sentence_transformers import SentenceTransformer as ST
import os
import json

# 加载配置
with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
model = ST(config['model_embed'])

# 设置路径
path = "./data"
Embeddings_Dict = {}

# 遍历文件夹中的文件
try:
    files = os.listdir(path)
    for File_Name in files:
        File_Path = os.path.join(path, File_Name)
        with open(File_Path, "r", encoding="UTF-8") as f:
            url = f.readline().strip()  # 读取第一行并去除换行符
            Sentence = f.read()  # 读取剩余内容
            Sentence_Embedding = model.encode([Sentence]).tolist()[0]  # 对单个句子进行编码
            Embeddings_Dict[File_Name] = [url, Sentence_Embedding]

    # 转换为JSON并保存
    Json_String = json.dumps(Embeddings_Dict, indent=4)
    with open('embeddings.json', 'w', encoding='utf-8') as json_file:
        json_file.write(Json_String)

except FileNotFoundError:
    print(f"指定的路径 {path} 不存在。")
except Exception as e:
    print(f"发生错误: {e}")
