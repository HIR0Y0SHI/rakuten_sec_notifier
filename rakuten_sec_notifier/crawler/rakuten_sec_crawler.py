import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from rakuten_sec_notifier.original_logger import OriginalLogger

from rakuten_sec_notifier.original_logger import OriginalLogger

class RakutenSecCrawler:
    RAKUTEN_LOGIN_URL = 'https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html'
    
    def __init__(self):
        # 環境変数の取得
        self.login_id = os.environ['LOGIN_ID']
        self.login_pass = os.environ['LOGIN_PASS']
        
         # Loggerの生成
        self.logger = OriginalLogger()
        
        
    def crawl(self):
        # chromedriverの設定
        options = Options()
        options.add_argument('--headless')
        chrome_service = fs.Service(executable_path="./rakuten_sec_notifier/driver/chromedriver")
        driver = webdriver.Chrome(service=chrome_service, options=options)
        
        # ログイン画面を開く
        driver.get(RakutenSecCrawler.RAKUTEN_LOGIN_URL)
        sleep(0.3)
        
        # ログインフォームを取得
        login_id_form = driver.find_element(by=By.ID, value='form-login-id')
        login_pass_form = driver.find_element(by=By.ID, value='form-login-pass')
        login_btn = driver.find_element(by=By.ID, value='login-btn')

        # フォーム入力
        login_id_form.send_keys(self.login_id)
        login_pass_form.send_keys(self.login_pass)
        sleep(0.2)

        self.logger.info("Login completed!")

        # ログイン（クリック）
        login_btn.click()
        sleep(0.5)

        # 保有商品一覧へ遷移
        asset_total_btn = driver.find_element(by=By.ID, value='asset_total_possess_btn')
        asset_total_btn.click()

        self.logger.info("Transition to the Products Page is complete!")

        # 保有商品情報取得
        ## 資産合計
        total_assets_element = driver.find_element(by=By.XPATH, value='//*[@id="table_balance_data"]/div/table/tbody/tr[2]/td[2]/span').text
        ## 評価損益
        valuation_profit_element = driver.find_element(by=By.XPATH, value='//*[@id="table_balance_data"]/div/table/tbody/tr[2]/td[3]/span[3]/span').text

        self.logger.info("Analysis completed!")
        
        # chromedriverのclose
        # driverの操作を完全に終えてからcloseすること
        driver.close()
        driver.quit()
        
        return total_assets_element, valuation_profit_element