import json
import urllib.request
import os

print("正在执行【方案一：点击弹窗安全付款版】自动化网页生成...")

# 2. 注入包含隐藏弹窗、点击触发、毛玻璃遮罩效果的 HTML 模板
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
            position: relative;
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
        
        /* 引导订阅触发区域 */
        .subscribe-section {
            background: #fdf8f9;
            border: 1px solid #fcebeb;
            border-radius: 20px;
            padding: 22px 20px;
            text-align: center;
            margin-top: 28px;
            box-shadow: 0 6px 18px rgba(255,154,158,0.05);
        }
        .sub-title {
            font-size: 15px;
            font-weight: 700;
            color: #4a2831;
            margin-bottom: 6px;
        }
        .sub-subtitle {
            font-size: 12px;
            color: #888;
            margin-bottom: 16px;
            line-height: 1.4;
        }
        .action-btn {
            display: inline-block;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            color: #4a2831;
            font-weight: 700;
            font-size: 14px;
            padding: 12px 32px;
            border-radius: 50px;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(255,154,158,0.3);
            transition: transform 0.2s;
            cursor: pointer;
            border: none;
        }
        .action-btn:active {
            transform: scale(0.96);
        }

        /* 隐藏的悬浮收款码弹窗遮罩层 */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(8px); /* 毛玻璃磨砂效果 */
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 999;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        /* 弹窗激活状态 */
        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }
        .modal-card {
            background: white;
            border-radius: 24px;
            padding: 28px 24px;
            width: 85%;
            max-width: 320px;
            text-align: center;
            box-shadow: 0 20px 50px rgba(0,0,0,0.15);
            transform: scale(0.85);
            transition: transform 0.3s ease;
            position: relative;
        }
        .modal-overlay.active .modal-card {
            transform: scale(1);
        }
        .qr-image {
            width: 200px;
            height: 200px;
            border-radius: 12px;
            margin: 15px 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
        }
        .close-btn {
            position: absolute;
            top: 14px;
            right: 16px;
            font-size: 20px;
            color: #aaa;
            cursor: pointer;
            background: none;
            border: none;
            padding: 5px;
        }
        .modal-tip {
            font-size: 12px;
            color: #999;
            margin-top: 8px;
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

        <div class="subscribe-section">
            <div class="sub-title">🌤️ 私人穿搭管家服务 (9.9元/月)</div>
            <div class="sub-subtitle">开通后可添加专属微信，每日主动推送精细化防晒、避雨及穿搭策略</div>
            <button class="action-btn" id="openBtn">👉 点击开通服务</button>
        </div>
    </div>

    <div class="footer">
        自动化后端正在强力驱动 · 专属私域出品
    </div>
</div>

<div class="modal-overlay" id="modalOverlay">
    <div class="modal-card">
        <button class="close-btn" id="closeBtn">✕</button>
        <div style="font-size: 15px; font-weight: bold; color: #4a2831; margin-bottom: 4px;">扫码开通私人订阅</div>
        <div style="font-size: 12px; color: #666;">微信长按识别二维码付款</div>
        
        <img src="wx_code.png" class="qr-image" alt="微信二维码">
        
        <div class="modal-tip">付款后请添加管家微信激活专属推送</div>
    </div>
</div>

<script>
    // 控制弹窗显示和关闭的极简安全脚本
    const openBtn = document.getElementById('openBtn');
    const closeBtn = document.getElementById('closeBtn');
    const modalOverlay = document.getElementById('modalOverlay');

    // 点击按钮打开弹窗
    openBtn.addEventListener('click', () => {
        modalOverlay.classList.add('active');
    });

    // 点击右上角叉叉关闭弹窗
    closeBtn.addEventListener('click', () => {
        modalOverlay.classList.remove('active');
    });

    // 点击弹窗外部空白区域也能自动关闭，极佳的用户体验
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            modalOverlay.classList.remove('active');
        }
    });
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("点击弹窗安全付款版网页更新成功！")
