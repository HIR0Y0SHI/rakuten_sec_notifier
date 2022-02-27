# Rakunten Crawl

楽天証券から「資産合計」と「評価損益」を取得します。
GitHub Actions上で30分ごとに実行し結果をSlack通知します。

## 環境変数

Actions secrets に以下環境変数を設定すること。

| 環境変数名        | 内容                           | 
| --------------- | ------------------------------ | 
| LOGIN_ID        | 楽天証券にログインするためのID | 
| LOGIN_PASS      | 楽天証券のパスワード           | 
| SLACK_API_TOKEN | Slack APIで利用するTOKEN       | 
| SLACK_CHANEL    | Slack通知チャンネル      | 

ローカルで実行する場合は以下のように環境変数を設定。

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
poetry run python rakuten_sec_notifier/main.py
```

### chromedriver

ChromeDriver 98.0.4758.102

https://chromedriver.chromium.org/downloads