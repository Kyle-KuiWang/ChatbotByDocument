from main_server import Natural_Language_Processing

# 初始化对话历史记录列表
Conversation_History = []  # 用于保存对话历史
while (True):

    Query = input("请输入问题（输入q结束对话）：")
    # 检查对话是否要结束
    if Query.lower() in ['q']:
        print("对话结束。")
        break

    # 将用户查询添加到对话历史中
    Conversation_History.append({"role": "user", "content": Query})
    # 生成答案
    Answer = Natural_Language_Processing(Query)
    Conversation_History.append({"role": "assistant", "content": Answer})
    # 输出回答结果
    print("机器人助手:", Answer)
