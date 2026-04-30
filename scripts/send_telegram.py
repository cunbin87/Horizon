import os
import re
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

def truncate(text, max_chars=100):
    """截断文本到约max_chars个字符，保留完整词语"""
    if len(text) <= max_chars:
        return text
    # 找到最后一个完整词的位置
    truncated = text[:max_chars]
    # 向前查找最后一个空格/标点
    for i in range(max_chars - 1, max_chars - 50, -1):
        if truncated[i] in ' ，、。！；：' or truncated[i] == ' ':
            return truncated[:i + 1] + "…"
    return truncated + "…"

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

    # 提取统计行
    stats_line = ""
    for line in content.split("\n"):
        if "从" in line and "条" in line and "筛选" in line:
            stats_line = re.sub(r'[<>]', '', line.strip())
            break

    # 按 item-1, item-2 分割内容，提取每条的标题和正文
    sections = re.split(r'<a id="item-(\d+)"></a>', content)
    # sections[0] = 空或开头, sections[1] = id, sections[2] = 内容...

    items_data = []
    for i in range(1, len(sections), 2):
        item_id = sections[i]
        item_content = sections[i + 1] if i + 1 < len(sections) else ""

        # 提取标题行 (## [标题](url) ⭐️ X.X/10)
        title_match = re.search(r'## \[([^\]]+)\]\([^)]+\) ⭐️ ([\d.]+)/10', item_content)
        if not title_match:
            continue
        title = title_match.group(1)

        # 提取正文（标题之后、下一个 **来源之前的内容）
        body_match = re.search(
            r'⭐️ [\d.]+/10\s*\n+(.+?)\n\s*\n\s*\S+\s*·',
            item_content, re.DOTALL
        )
        if body_match:
            summary = body_match.group(1).strip()
            # 清理 markdown
            summary = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', summary)
            summary = re.sub(r'<[^>]+>', '', summary)
            summary = re.sub(r'\s+', ' ', summary).strip()
            summary = truncate(summary, 100)
        else:
            summary = ""

        items_data.append({
            "id": int(item_id),
            "title": title,
            "summary": summary
        })

    # 组装消息
    msg = f"🌅 Horizon 日报 | {date}\n"
    if stats_line:
        msg += f"📊 {stats_line}\n"
    msg += "─" * 20 + "\n"

    for item in items_data[:15]:
        msg += f"{item['id']}. {item['title']} ⭐️\n"
        if item['summary']:
            msg += f"   {item['summary']}\n"
        msg += "\n"

    if len(items_data) > 15:
        msg += f"📎 共 {len(items_data)} 条，更多见 https://cunbin87.github.io/Horizon/"

    msg = msg.strip()

    if len(msg) > 4000:
        msg = msg[:3950] + "\n\n…"

    try:
        send_msg(token, chat_id, msg)
        print(f"✅ 已发送精简日报 ({len(msg)} chars, {len(items_data)} 条)")
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        msg_simple = msg.replace("https://", "")
        try:
            send_msg(token, chat_id, msg_simple)
            print("✅ 重试成功（纯文本版）")
        except Exception as e2:
            print(f"❌ 重试也失败: {e2}")

if __name__ == "__main__":
    main()
