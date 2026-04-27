from sentence_transformers import SentenceTransformer as ST
import json
from SBERT import Generate_Answer
from ErnieBot_turbo import ErnieBot


with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

def Natural_Language_Processing(Query):
    Model_Embed = ST(config['model_embed'])
    Model_LLM = ErnieBot
    Embed_Path, Data_Path = config['embedding_path'], config['data_path']
    # 加载数据集
    with open(Embed_Path, 'r', encoding="utf-8") as f:
        dict = json.load(f)
    File_Name, Sentence_Embedding_Array, url = [], [], []
    for i in dict:
        url.append(dict[i][0])
        File_Name.append(i)
        Sentence_Embedding_Array.append(dict[i][1])
    # 获取答案
    Answer = Generate_Answer(Query, url, File_Name, Sentence_Embedding_Array, Model_Embed, Model_LLM, Data_Path)
    return Answer
