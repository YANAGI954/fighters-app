
import json
import requests
import feedparser
from bs4 import BeautifulSoup

# ニュース取得
rss_url = "https://news.yahoo.co.jp/rss/topics/sports.xml"
feed = feedparser.parse(rss_url)

news_items = []
for entry in feed.entries:
    if "日本ハム" in entry.title or "ファイターズ" in entry.title:
        news_items.append({
            "title": entry.title,
            "link": entry.link
        })
    if len(news_items) >= 5:
        break

with open("fighters_news.json", "w", encoding="utf-8") as f:
    json.dump({"news": news_items}, f, ensure_ascii=False, indent=2)

# パ・リーグ順位表
url = "https://baseball.yahoo.co.jp/npb/standings/"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

standings = []
for row in soup.select("section:nth-of-type(2) table tbody tr"):
    cols = row.find_all("td")
    if len(cols) >= 6:
        standings.append({
            "team": cols[0].text.strip(),
            "wins": int(cols[1].text),
            "losses": int(cols[2].text),
            "draws": int(cols[3].text),
            "win_pct": cols[4].text
        })

with open("fighters_standings.json", "w", encoding="utf-8") as f:
    json.dump({"standings": standings}, f, ensure_ascii=False, indent=2)
