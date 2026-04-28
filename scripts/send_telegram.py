import os
import sys
import urllib.request
import urllib.parse
import json

def send_msg(token, chat_id, text):
    """发送消息到 Telegram"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
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

    lines = content.split("\n")
    overview = []
    item_sections = []
    current_item = []
    in_item = False

    for line in lines:
        if line.startswith("## "):
            if current_item:
                item_sections.append("\n".join(current_item))
            current_item = [line]
            in_item = True
        elif not in_item and line.strip():
            overview.append(line)
        elif in_item:
            current_item.append(line)

    if current_item:
        item_sections.append("\n".join(current_item))

    # 发送概览
    overview_text = "\n".join(overview)
    if len(overview_text) > 3800:
        overview_text = overview_text[:3800] + "\n\n..."
    send_msg(token, chat_id, overview_text)
    print(f"✓ 概览已发送 ({len(overview_text)} chars)")

    # 发送前 10 条详情
    sent = 0
    for section in item_sections:
        if sent >= 10:
            break
        if len(section) > 3800:
            section = section[:3800] + "\n\n..."
        try:
            send_msg(token, chat_id, section)
            sent += 1
            print(f"✓ 第 {sent} 条已发送")
        except Exception as e:
            print(f"✗ 第 {sent} 条发送失败: {e}")

    print(f"✅ 完成，共发送 1 条概览 + {sent} 条详情")

if __name__ == "__main__":
    main()
