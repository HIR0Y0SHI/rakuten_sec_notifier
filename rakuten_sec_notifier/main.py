from cmath import log
import datetime, os
from time import sleep
from rakuten_sec_notifier.crawler.rakuten_sec_crawler import RakutenSecCrawler
from rakuten_sec_notifier.original_logger import OriginalLogger
from rakuten_sec_notifier.slack.slack_emoji import SlackEmoji
from rakuten_sec_notifier.slack.slack_util import SlackUtil


SLACK_CHANNEL  = os.environ['SLACK_CHANNEL']

logger = OriginalLogger()
logger.info("start")

# Crawl
crawler = RakutenSecCrawler()
total_assets_element, valuation_profit_element = crawler.crawl()

# 現在時刻取得
now = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')

# 投稿メッセージ作成
slack_message = SlackEmoji.CHART_UP.value + " " + SlackUtil.bold("楽天証券資産状況") + SlackUtil.SLACK_LF \
    + SlackUtil.code("資産合計: " + total_assets_element + SlackUtil.SLACK_LF + "評価損益: " + valuation_profit_element) \
    + now + " 時点"
    
# Slack投稿
slack_util = SlackUtil()
slack_util.postMessage(slack_message, SLACK_CHANNEL)

logger.info("Slack Post Completed!")

logger.info("end")




