from flask import Flask, render_template, request

app = Flask(__name__)

# 聊天记录，用一个列表保存所有的消息
chat_history = []

# 表情包列表
emojis = [
    "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋",
    "😎", "😍", "😘", "🥰", "😗", "😙", "😚", "☺️", "🙂", "🤗", "🤔",
    "🤨", "😐", "😑", "😶", "🙄", "😏", "😣", "😥", "😮", "🤐", "😯",
    "😪", "😫", "😴", "😌", "😛", "😜", "😝", "🤤", "😒", "😓", "😔",
    "😕", "🙃", "🤑", "😲", "🙁", "😖", "😞", "😟", "😤", "😢", "😭",
    "😦", "😧", "😨", "😩", "🤯", "😬", "😰", "😱", "😳", "🤪", "😵"
]

# 主页面，显示聊天记录和发送消息表单
@app.route("/")
def index():
    return render_template("index.html", chat_history=chat_history, emojis=emojis)

# 处理发送消息的请求
@app.route("/send_message", methods=["POST"])
def send_message():
    # 获取用户发送的消息和用户名
    message = request.form["message"]
    username = request.form["username"]
    # 将消息添加到聊天记录中
    chat_history.append({"username": username, "message": message})
    # 返回主页面
    return render_template("index.html", chat_history=chat_history, emojis=emojis)

if __name__ == "__main__":
    app.run()
