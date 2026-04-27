// script.js
const userAvatar = new Image();
userAvatar.src = "bot.png";

window.onload = function () {

    updateTopBar();

    // 修改模型选择器的事件处理程序
    document.getElementById('model-selector').addEventListener('change', function () {
        updateTopBar();
    });

};

// 显示conversation框
document.getElementById('conversation').style.display = 'block';
appendMessage('bot', '你好，这里是deepin助手！\
    \n你可以询问我任何关于deepin系统的问题👌');

function appendMessage(who, text) {
    const conversation = document.getElementById('conversation');
    const message = document.createElement('div');
    message.className = 'message ' + who;

    // 创建气泡元素
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;
    bubble.style.whiteSpace = 'pre-line'; // 允许换行

    // 创建头像元素
    const avatar = document.createElement('div');
    avatar.className = 'avatar';

    // 如果是用户，先添加气泡，再添加头像
    if (who === 'user') {
        message.appendChild(bubble);
        message.appendChild(avatar);
    } else {
        // 如果是机器人，先添加头像，再添加气泡
        message.appendChild(avatar);
        message.appendChild(bubble);
    }

    conversation.appendChild(message);
    conversation.scrollTop = conversation.scrollHeight;
}




function submitQuestion() {
    const llm = 'ErnieBot';

    const query = document.getElementById('user-input').value;


    appendMessage('user', query);
    const xhr = new XMLHttpRequest();
    xhr.open("POST", ":8000/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const result = JSON.parse(xhr.responseText);
                // 使用机器人回答调用appendMessage函数
                appendMessage('bot', result.answer);
                console.log(result)
            }
        }
    };

    const data = JSON.stringify({llm, query});
    // 清空输入框
    document.getElementById('user-input').value = '';

    xhr.send(data);
}