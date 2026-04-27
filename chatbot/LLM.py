
class LLM:
    def __init__(self, model):
        self.model = model
    def get_QA(self, question, ref):
        prompt = f'''你是一个问答机器人，请根据<>中参考文档的内容回答问题；你的回答不用包括参考链接"；\
            如果你觉得文档中没有匹配的内容，直接输出"对不起，我没有从下面的文档中找到相关内容"；
            问题：<{question}>    参考文档：<{ref}>'''
        ans = self.model(prompt, "QA")
        return ans
