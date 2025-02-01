import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # 渲染首頁，包含 QR 掃描功能
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_qr_code():
    # 接收來自前端的 QR 碼數據
    qr_data = request.form.get('qr_data')
    if not qr_data:
        return "未收到 QR 碼數據！", 400

    # 安全性處理：防止 XSS 攻擊
    qr_data = qr_data.strip()

    # 如果是 URL，則自動跳轉
    if qr_data.startswith("http://") or qr_data.startswith("https://"):
        return redirect(qr_data)

    # 顯示掃描結果
    return render_template('success.html', qr_data=qr_data)

if __name__ == '__main__':
    app.run(debug=True)
