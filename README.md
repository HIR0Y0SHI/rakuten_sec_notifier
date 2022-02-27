# Rakunten Crawl

楽天証券から「資産合計」と「評価損益」を取得します。

## 環境変数

| 環境変数名        | 内容                           | 
| --------------- | ------------------------------ | 
| LOGIN_ID        | 楽天証券にログインするためのID | 
| LOGIN_PASS      | 楽天証券のパスワード           | 
| SLACK_API_TOKEN | Slack APIで利用するTOKEN       | 
| SLACK_CHANEL    | Slack通知チャンネル      | 

```bash
export LOGIN_ID="ID"
export LOGIN_PASS="PASSWORD"
export SLACK_API_TOKEN="TOKEN"
export SLACK_CHANNEL="CHANNEL"
```

## 依存

* selenium
* slack-sdk

```bash
poetry install
```

## Howl to Run 

```bash
poetry run python main.py
```

### chromedriver

ChromeDriver 98.0.4758.102
https://chromedriver.chromium.org/downloads