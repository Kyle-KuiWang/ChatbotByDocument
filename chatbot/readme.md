### Project-225:文档问答机器人

队伍名称：哥哥说的都队

团队成员：王奎、张红杰、苏杨杨

指导老师：付自建、刘少飞
#### 相关链接：

本项目参考了往届参赛作品：[参考代码仓库](https://gitlab.eduxiji.net/educg-group-17066-1466467/202310007111069-3733)

本项目的创新点：
1. 本项目旨在编写完成中文聊天机器人，而国产大模型Ernie 3.5版本在中文处理方面展现出了强大的性能，不仅在多项基准测试中超越了ChatGPT，还在中文环境中击败了GPT 4，故我们选择了国产大模型进行接入。
2. 将.js文件中的响应接口设置为相对URL':8000/',以满足不同服务器上的跨域访问，并可以将服务器运行在deepin虚拟机中，在宿主机进行web服务的访问。
3. 将存放参考文档嵌入后的向量存放在一个.json文件中，取消了繁琐地手动选择问题类别功能。
4. 将调用SBERT.py文件中multi_ans()函数的代码封装到main_server.py文件的nlp_gen()函数中,当cmd端或web端运行时均从main_server.py中导入并使用，解耦了代码的结构。


项目文档：仓库目录下 chatbot项目文档.pdf

博客发布：[CSDN博客链接](https://blog.csdn.net/qq_62805613/article/details/139269888)

演示视频：[戳这里获取](https://pan.baidu.com/s/1ahi69op1faTBL-vMGIUgHw?pwd=2609)
#### 项目部署：

按仓库的目录结构下载至本地，首先配置config.json文件（其中"API-KEY"所对应的token值需自行前往百度智能云申请）。

我们的问答机器人支持不同操作系统上的cmd命令行访问和web访问，可以部署至任何系统上。

需确保电脑已配置Python3的环境（推荐使用虚拟环境），并在命令行运行以下指令安装必需的第三方库：

```
pip install scipy
pip install sentence-transformers
```

当web访问时，首先进入项目所在的目录，运行server.py启动服务器；在浏览器访问127.0.0.1:8000、localhost:8000、192.168.x.x:8000三者任意端口即可。

当cmd访问时，首先进入项目所在的目录，直接运行main.py即可。

当需要实现将web服务部署在虚拟机上，在宿主本机进行访问时，需要进行虚拟网络配置，采用NAT模式链接直接网络，并设置端口转移。随后在虚拟机中运行server.py启动服务器，在宿主机浏览器输入主机IP加端口号即可访问。
#### 仓库目录和文件介绍：

data：               存放了deepin wiki和linglong.dev网站内容的所有文档，用于进行嵌入。

embedding.json：     存放文档嵌入后的向量表示

ErnieBot_turbo.py：  调用ErnieBot接口实现问答系统输出

LLM.py：             ErnieBot语言模型的接口，设置prompt

server.py：          启动web服务器，端口为8000

main.py：            cmd命令行访问时的程序入口

main_server.py：     web访问时的程序入口，由server调用以进入模型

sBERT.py：           实现sBERT架构，完成文档匹配

doc_embedding.py：   对文档进行嵌入，存储得到的向量信息

config.json：        配置文件

dataset.json：       问答测试集，包含30条基于deepin文档的问答。

index.html：         前端页面文档

style.css：          前端页面文档

script.js：          前端页面文档

send.png/bot.png/user.png:  前端页面插图

chatbot项目文档.pdf：   项目介绍文档

ch-BERT： 预训练后的中文BERT模型，因文件过大，源文件放置于[百度网盘](https://pan.baidu.com/s/1WSc9NfVLsVln0EOnogJdPQ?pwd=2609)中，提取码：2609，解压密码：53992609。
