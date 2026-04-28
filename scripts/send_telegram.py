import os
import sys
import urllib.request
import urllib.parse
import json

def send_msg(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
    }).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

def main():
    token = os.environ.get("TG_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    date = os.environ.get("DATE")

    if not token or not chat_id:
        print("缺少 Telegram 配置，跳过")
        return

    file_path = f"docs/_posts/{date}-summary-zh.md"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"文件不存在: {file_path}")
        return

    # 提取概览行（带 ⭐️ 评分的条目列表）
    items = []
    for line in content.split("\n"):
        # 匹配 "1. [标题](#item-1) ⭐️ X.X/10" 这类行
        if "⭐️" in line and line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.", "15.")):
            # 清理：去掉 markdown 链接标记 [`xxx`] 和 (`#item-1`)
            clean = line
            # 去掉 [内容](链接) 变成 内容
            import re
            clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
            # 去掉链接
            clean = re.sub(r'\(https?://[^)]+\)', '', clean)
            # 去掉 <details> 标签
            clean = re.sub(r'<[^>]+>', '', clean)
            # 去多余空格
            clean = re.sub(r'\s+', ' ', clean).strip()
            items.append(clean)

    # 从文件头部提取统计信息
    stats_line = ""
    for line in content.split("\n"):
        if "从" in line and "条" in line and "筛选" in line:
            stats_line = line.strip()
            stats_line = re.sub(r'[<>]', '', stats_line)
            break

    # 组装消息
    msg = f"🌅 Horizon 日报 | {date}\n"
    if stats_line:
        msg += f"📊 {stats_line}\n"
    msg += "─" * 20 + "\n"

    for i, item in enumerate(items[:15], 1):
        msg += f"{item}\n"

    if len(items) > 15:
        msg += f"\n📎 共 {len(items)} 条，更多见 https://cunbin87.github.io/Horizon/"

    msg = msg.strip()

    if len(msg) > 4000:
        msg = msg[:3950] + "\n\n…"

    try:
        send_msg(token, chat_id, msg)
        print(f"✅ 已发送精简日报 ({len(msg)} chars, {len(items)} 条)")
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        # 尝试不带任何链接的纯文本版本
        msg_simple = msg.replace("https://", "")
        try:
            send_msg(token, chat_id, msg_simple)
            print("✅ 重试成功（纯文本版）")
        except Exception as e2:
            print(f"❌ 重试也失败: {e2}")

if __name__ == "__main__":
    main()
