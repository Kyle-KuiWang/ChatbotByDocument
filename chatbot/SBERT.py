# 导入scipy库，用于计算向量间的距离
import scipy
from LLM import LLM
def Match(Query, Sentence_Embedding_Array, Model_Embed_Vector):
    """
    根据查询和句子的嵌入表示，找到与查询最相似的句子。

    Args:
    - query: str, 用户输入的查询文本。
    - sentence_embedding: ndarray, 包含多个句子嵌入表示的二维数组。
    - model_embed_vector: EncoderModel, 用于生成文本嵌入表示的模型实例。

    Returns:
    - results: list, 包含句子索引和对应距离的元组列表，按距离升序排列。
    """
    # 使用模型将查询文本编码为嵌入表示
    Query_Embeddings = Model_Embed_Vector.encode(Query)
    # 计算查询嵌入与所有句子嵌入之间的余弦距离
    Distances = scipy.spatial.distance.cdist([Query_Embeddings], Sentence_Embedding_Array, "cosine")[0]
    # 将距离和对应的索引打包成元组列表
    Results = zip(range(len(Distances)), Distances)
    # 按距离升序排序结果
    Results = sorted(Results, key=lambda x: x[1])

    return Results


def Generate_Answer(Query, url, File_Name, Sentence_Embedding_Array, Model_Embed, Model_LLM, Data_Path):
    """
    根据查询，从多个文档中提取答案，并使用大型语言模型进行问答。

    Args:
    - query: str, 用户输入的查询文本。
    - url: list, 包含每个文档URL的列表。
    - file_name: list, 包含每个文档文件名的列表。
    - sentence_embedding_array: ndarray, 所有文档的句子嵌入表示的二维数组。
    - model_embed: EncoderModel, 用于生成文本嵌入表示的模型实例。
    - model_llm: LLM, 大型语言模型实例，用于处理问答任务。
    - data_path: str, 存储文档的文件路径前缀

    Returns:
    - ans_collections: str, 包含所有答案和参考链接的字符串。
    """
    # 初始化大型语言模型
    llm = LLM(Model_LLM)
    # 给初始化类LLM传入大语言模型ErnieBot
    # 找到与查询最相似的文档
    Results = Match(Query,Sentence_Embedding_Array, Model_Embed)
    Ans_Collections = ""  # 初始化答案列表

    # 遍历最相关的文档（这里只取第一个，但可以修改以处理多个）
    for idx, distance in Results[0:1]:  # 只取第一个结果
        # 读取对应文档的内容
        with open(Data_Path + File_Name[idx], "r", encoding='utf-8') as f:
            content = f.read()
            # 这一行代码的主要作用是从文档内容中抽取答案，并利用大型语言模型生成最终的回答。
        ans = llm.get_QA(Query, content.strip())
        # 拼接答案到答案列表中
        Ans_Collections += ans
        s = f'References: {url[idx]}'
        Ans_Collections += "\n" + s + "\n"
        print("_____________________________________________________")


    return Ans_Collections