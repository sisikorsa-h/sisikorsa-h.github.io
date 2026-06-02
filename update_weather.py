import json
import urllib.request
import os

print("正在执行【精装付款开张版】自动化网页生成...")

# 2. 注入包含二维码展示、恢复完美精美卡片样式的 HTML 模板
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌤️ 每日穿衣指南 | 私人天气管家</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #f7f9fc;
            color: #333;
            margin: 0;
            padding: 16px;
            display: flex;
            justify-content: center;
        }
        .container {
            background: white;
            border-radius: 24px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.04);
            width: 100%;
            max-width: 400px;
            overflow: hidden;
            border: 1px solid rgba(0,0,0,0.02);
        }
        .header {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            padding: 30px 24px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #4a2831;
            letter-spacing: 1px;
        }
        .meta-info {
            margin-top: 10px;
            font-size: 13px;
            color: #6b4450;
            opacity: 0.9;
            display: flex;
            justify-content: center;
            gap: 12px;
        }
        .weather-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(4px);
            padding: 8px 16px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 14px;
            margin-top: 14px;
            color: #4a2831;
            box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        }
        .content {
            padding: 24px;
        }
        .section-title {
            font-size: 16px;
            font-weight: 700;
            color: #2c3e50;
            margin: 24px 0 14px 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .section-title::before {
            content: "";
            display: inline-block;
            width: 4px;
            height: 16px;
            background: #ff9a9e;
            border-radius: 2px;
        }
        .card {
            background: #fffefe;
            border: 1px solid #fcebeb;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 14px;
            box-shadow: 0 4px 12px rgba(255,154,158,0.04);
        }
        .card-title {
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 8px;
        }
        .female .card-title { color: #d87093; }
        .male .card-title { color: #2a7ca6; }
        
        .card-text {
            font-size: 14px;
            color: #555;
            line-height: 1.6;
        }
        .tips-list {
            padding-left: 0;
            margin: 0;
            list-style: none;
        }
        .tips-list li {
            position: relative;
            padding-left: 18px;
            font-size: 13.5px;
            color: #666;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .tips-list li::before {
            content: "•";
            color: #ff9a9e;
            font-weight: bold;
            font-size: 28px;
            position: absolute;
            left: 4px;
            top: -2px;
        }
        .qr-section {
            background: #fdf8f9;
            border: 2px dashed #ff9a9e;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            margin-top: 28px;
        }
        .qr-title {
            font-size: 15px;
            font-weight: 700;
            color: #4a2831;
            margin-bottom: 6px;
        }
        .qr-subtitle {
            font-size: 12px;
            color: #888;
            margin-bottom: 14px;
            line-height: 1.4;
        }
        .qr-image-wrapper {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
        .qr-image {
            width: 180px;
            height: 180px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(255,154,158,0.15);
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 11px;
            color: #bbb;
            background: #fafafa;
            border-top: 1px solid #f5f5f5;
            letter-spacing: 0.5px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🌤️ 每日穿衣指南</h1>
        <div class="meta-info">
            <span>📍 东莞</span>
            <span>📅 自动更新成功</span>
        </div>
        <div class="weather-badge">🌡️ 28°C (体感 31.2°C) | 💧 湿度 85%</div>
    </div>
    
    <div class="content">
        <div class="section-title">今日主推风格</div>
        
        <div class="card female">
            <div class="card-title">♀️ 女生推荐：法式清爽风</div>
            <div class="card-text">
                👗 亚麻质地吊带连衣长裙 + 薄款防晒开衫<br>
                👡 罗马平底凉鞋 + 草编遮阳帽
            </div>
        </div>

        <div class="card male">
            <div class="card-title">♂️ 男生推荐：City Boy 干净流</div>
            <div class="card-text">
                👕 华夫格落肩宽版短袖 + 泼水轻量机能短裤<br>
                👟 踩屎感复古运动鞋 + 透气棒球帽
            </div>
        </div>

        <div class="section-title">气象管家避坑说</div>
        <ul class="tips-list">
            <li><strong>防贴身尴尬：</strong> 今日东莞空气湿度高达 85%，体感极度闷热。请尽量避免穿纯棉 T 恤，出汗后易紧贴后背；强烈推荐速干或亚麻面料。</li>
            <li><strong>突发降雨防范：</strong> 午后大概率有局地阵雨。出门建议携带轻量折叠雨伞，鞋子选择防水或易干材质。</li>
        </ul>

        <div class="qr-section">
            <div class="qr-title">👉 长按识别二维码订阅 (9.9元/月)</div>
            <div class="qr-subtitle">添加私人管家，开通每日专属穿搭主动推送服务</div>
            <div class="qr-image-wrapper">
                <img src="wx_code.png" class="qr-image" alt="微信二维码">
            </div>
        </div>
    </div>

    <div class="footer">
        自动化后端正在强力驱动 · 专属私域出品
    </div>
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("精装付款版网页更新成功！")
