from flask import Flask

# 建立 Flask 應用程式
app = Flask(__name__)


# 系統首頁測試
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Enterprise IT Helpdesk</title>
    </head>
    <body>
        <h1>Enterprise IT Helpdesk</h1>
        <h2>企業 IT 報修管理系統</h2>
        <p>Flask 後端已經成功回應請求。</p>
    </body>
    </html>
    """


# 啟動伺服器
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
 
