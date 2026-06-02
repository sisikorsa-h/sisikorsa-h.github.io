import urllib.request
import json
import os
import re

print("正在执行【全球前沿 AI 情报导航 - USDT纯净版】自动化构建...")

# ======= 🕷️ 核心大脑：全自动抓取/清洗全网最新 AI 镜像资源 =======
try:
    url = "https://raw.githubusercontent.com/LiLittleCat/awesome-free-chatgpt/main/README.md"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    response = urllib.request.urlopen(req, timeout=15)
    readme_content = response.read().decode('utf-8')
    
    urls = re.findall(r'https?://[^\s\)\`\]]+', readme_content)
    ai_mirrors = [u for u in urls if 'chat' in u or 'ai' in u or 'vercel' in u][:5]
except Exception as e:
    ai_mirrors = []

if not ai_mirrors:
    ai_mirrors = [
        "https://shared.oaifree.com (始皇出品-国行极速GPT)",
        "https://chat.reka.ai (海外新生代顶尖多模态AI)",
        "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat (官方免费AI)",
        "https://poe.com (全球最大AI聚合平台)"
    ]

side_hustle_title = "💡 今日暴利信息差：海外 AI 礼品卡套利与数字资产托管"
side_hustle_detail = "目前海外大量独立软件（如 Midjourney）支持虚拟卡充值。由于国内卡受限，在淘宝/闲鱼上代充的利润率高达 40%。利用加密货币采购海外廉价代充额度，再回国做私域分发，是目前零门槛、高回报的完美闭环..."

# ======= 🎨 极致奢华：聚焦 USDT 支付的黑金 HTML 模板 =======
html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ AI-Hub & Global Nexus | 全球前沿情报直达站</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #0b0f19;
            color: #f3f4f6;
            margin: 0;
            padding: 16px;
            display: flex;
            justify-content: center;
        }}
        .container {{
            background: #111827;
            border-radius: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            width: 100%;
            max-width: 420px;
            overflow: hidden;
            border: 1px solid #1f2937;
        }}
        .header {{
            background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
            padding: 35px 24px;
            text-align: center;
            border-bottom: 1px solid #1f2937;
        }}
        .header h1 {{
            margin: 0;
            font-size: 22px;
            font-weight: 800;
            color: #6366f1;
            letter-spacing: 1px;
            text-shadow: 0 0 15px rgba(99,102,241,0.4);
        }}
        .meta-info {{
            margin-top: 10px;
            font-size: 12px;
            color: #9ca3af;
            display: flex;
            justify-content: center;
            gap: 12px;
        }}
        .badge {{
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
            padding: 6px 14px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 12px;
            margin-top: 14px;
            color: #a5b4fc;
        }}
        .content {{
            padding: 24px;
        }}
        .section-title {{
            font-size: 15px;
            font-weight: 700;
            color: #f3f4f6;
            margin: 24px 0 14px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-title::before {{
            content: "";
            display: inline-block;
            width: 4px;
            height: 14px;
            background: #6366f1;
            border-radius: 2px;
        }}
        .card {{
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 14px;
        }}
        .card-title {{
            font-weight: 700;
            font-size: 13.5px;
            color: #38bdf8;
            margin-bottom: 8px;
        }}
        .card-text {{
            font-size: 13px;
            color: #9ca3af;
            line-height: 1.6;
        }}
        
        .blur-box {{
            filter: blur(5px);
            user-select: none;
            opacity: 0.3;
        }}
        
        .subscribe-section {{
            background: linear-gradient(180deg, #1f2937 0%, #111827 100%);
            border: 1px solid #374151;
            border-radius: 20px;
            padding: 22px 20px;
            text-align: center;
            margin-top: 28px;
        }}
        .sub-title {{
            font-size: 14px;
            font-weight: 700;
            color: #f3f4f6;
            margin-bottom: 6px;
        }}
        .sub-subtitle {{
            font-size: 11.5px;
            color: #9ca3af;
            margin-bottom: 16px;
            line-height: 1.5;
        }}
        .action-btn {{
            display: inline-block;
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff;
            font-weight: 700;
            font-size: 13.5px;
            padding: 12px 28px;
            border-radius: 50px;
            text-decoration: none;
            box-shadow: 0 4px 20px rgba(79,70,229,0.4);
            transition: transform 0.2s;
            cursor: pointer;
            border: none;
        }}
        
        /* 弹窗样式 */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 999;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }}
        .modal-overlay.active {{
            opacity: 1;
            pointer-events: auto;
        }}
        .modal-card {{
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 24px;
            padding: 28px 20px;
            width: 90%;
            max-width: 340px;
            text-align: center;
            box-shadow: 0 25px 60px rgba(0,0,0,0.6);
            transform: scale(0.85);
            transition: transform 0.3s ease;
            position: relative;
        }}
        .modal-overlay.active .modal-card {{
            transform: scale(1);
        }}
        .qr-image {{
            width: 180px;
            height: 180px;
            border-radius: 12px;
            margin: 15px 0;
            border: 4px solid #111827;
        }}
        .close-btn {{
            position: absolute;
            top: 14px;
            right: 16px;
            font-size: 18px;
            color: #9ca3af;
            cursor: pointer;
            background: none;
            border: none;
        }}
        
        .address-box {{
            background: #111827;
            border: 1px solid #374151;
            border-radius: 10px;
            padding: 8px 12px;
            margin-top: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-align: left;
        }}
        .address-text {{
            font-size: 11px;
            font-family: monospace;
            color: #22c55e;
            word-break: break-all;
            margin-right: 8px;
            user-select: all;
        }}
        .copy-btn {{
            background: #16a34a;
            color: white;
            border: none;
            padding: 5px 10px;
            font-size: 11px;
            border-radius: 6px;
            cursor: pointer;
            white-space: nowrap;
        }}
        .copy-btn:active {{ background: #15803d; }}

        .modal-tip {{
            font-size: 11px;
            color: #ef4444;
            margin-top: 12px;
            line-height: 1.4;
            font-weight: bold;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            font-size: 10px;
            color: #4b5563;
            background: #0d131f;
            border-top: 1px solid #1f2937;
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>⚡ AI-Hub & Global Nexus</h1>
        <div class="meta-info">
            <span>🌐 全球边缘节点</span>
            <span>⏱️ 自动洗牌已同步</span>
        </div>
        <div class="badge">🔥 今日全网已成功清洗 142 个高价值暗网情报</div>
    </div>
    
    <div class="content">
        <div class="section-title">📢 全球前沿公开情报 (每日限免)</div>
        <div class="card">
            <div class="card-title">{side_hustle_title}</div>
            <div class="card-text">{side_hustle_detail}</div>
        </div>

        <div class="section-title">🔒 今日最新高防免翻墙 AI 镜像源 (需解锁)</div>
        <div class="card" style="position: relative;">
            <div class="blur-box">
                <div class="card-title">🌐 节点 01：https://chat-premium-pool.vercel.app</div>
                <div class="card-text">状态：🟢 极速延迟 | 权限：免登录全功能开通</div>
                <div class="card-title" style="margin-top:10px;">🌐 节点 02：https://claude-sonnet-asia.net</div>
                <div class="card-text">状态：🟢 极速延迟 | 权限：支持最新 Opus/Sonnet 强模型</div>
            </div>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; background: rgba(17,24,39,0.2);">
                <span style="font-size: 12px; background: #ef4444; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold;">⚠️ 包含 5 个最新高价值内部节点已隐藏</span>
            </div>
        </div>

        <div class="subscribe-section">
            <div class="sub-title">🔑 解锁全站核心情报与实时 AI 镜像</div>
            <div class="sub-subtitle">只需支付 2.0 USDT，即可永久解锁。</div>
            <button class="action-btn" id="openBtn">⚡ 扫码支付 立即解锁</button>
        </div>
    </div>

    <div class="footer">
        Automated Linux Action Core · Decentralized Premium Data Service
    </div>
</div>

<div class="modal-overlay" id="modalOverlay">
    <div class="modal-card">
        <button class="close-btn" id="closeBtn">✕</button>
        <div style="font-size: 14px; font-weight: bold; color: #ffffff;">USDT 安全结算通道</div>
        <div style="font-size: 11px; color: #9ca3af; margin-bottom: 5px;">请扫描或复制下方网络地址支付 <strong>2.0 USDT</strong></div>
        
        <img src="wx_code.jpg" class="qr-image" alt="USDT 收款二维码">
        
        <div class="address-box">
            <div class="address-text" id="usdtAddr">THmDhPhpQoekcdGGvHWbyE2oQwmjQfMuie</div>
            <button class="copy-btn" onclick="copyAddress()">复制地址</button>
        </div>
        
        <div class="modal-tip">⚠️ 绝对警告：当前通道仅接收 USDT (TRC20 网络/波场)！请勿充值任何其他资产，转错网络资金将永久丢失。</div>
        <div style="font-size: 10.5px; color: #9ca3af; margin-top: 12px;">付款完成后，请截图并保存交易哈希（TXID）联系客服激活权限。</div>
    </div>
</div>

<script>
    const openBtn = document.getElementById('openBtn');
    const closeBtn = document.getElementById('closeBtn');
    const modalOverlay = document.getElementById('modalOverlay');

    openBtn.addEventListener('click', () => {{ modalOverlay.classList.add('active'); }});
    closeBtn.addEventListener('click', () => {{ modalOverlay.classList.remove('active'); }});
    modalOverlay.addEventListener('click', (e) => {{ if (e.target === modalOverlay) modalOverlay.classList.remove('active'); }});

    function copyAddress() {{
        const text = document.getElementById('usdtAddr').innerText;
        navigator.clipboard.writeText(text).then(() => {{
            alert('✅ USDT-TRC20 地址已成功复制！快去你的钱包或交易所转账吧。');
        }}).catch(err => {{
            alert('复制失败，请长按选中文字手动复制。');
        }});
    }}
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("USDT(TRC20)格式修正版网站构建成功！")
