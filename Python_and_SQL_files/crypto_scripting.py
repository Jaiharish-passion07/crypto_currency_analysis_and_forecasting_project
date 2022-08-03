#Import libraires
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import date,timedelta,datetime
from sql_db import create_table,insert_table,check_table_exist

class Crypto_Data_extract:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument("--window-size=1920,1100")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

    def initialize_webdriver(self):
        # path = Service("/home/ubuntu/selenium_driver/chromedriver")
        self.path = Service("/home/ubuntu/selenium_webdriver/chromedriver")
        self.driver = webdriver.Chrome(service=self.path, options=self.options)
        # For maximizing window
        self.driver.maximize_window()
        # Implicit wait apply for all elements to wait for 5 seconds to load
        self.driver.implicitly_wait(5)

    def extract_top_100coins(self):
        try:
            self.initialize_webdriver()
            self.driver.get("https:/coinmarketcap.com/")
            self.top_100_coin_list = []
            for i in range(1, 15):

                #Main Script
                # Giving Elements path id to extract data
                self.flag = self.driver.find_element(by=By.XPATH,
                                           value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                               i) + "]/td[3]/div/a/div/div/p")

                # Accessing coin name, price,24 hr change, Mkt Cap directly

                coin_name = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                    i) + "]/td[3]/div/a/div/div/p")

                coin_symbol = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                      i) + "]/td[3]/div/a/div/div/div/p")

                coin_price = self.driver.find_element(by=By.XPATH,
                                                  value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                     i) + "]/td[4]/div/a/span")

                hr_24 = self.driver.find_element(by=By.XPATH,
                                             value="//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[" + str(
                                                i) + "]/td[5]/span")

                market_cap = self.driver.find_element(by=By.XPATH,
                                                  value="// *[ @ id = '__next'] / div / div[1] / div[2] / div / div / div[5] / table / tbody / tr[" + str(
                                                     i) + "] / td[8] / p / span[2]")
                volume_24hr = self.driver.find_element(by=By.XPATH,
                                                   value="// *[ @ id = '__next'] / div / div[1] / div[2] / div / div / div[5] / table / tbody / tr[" + str(
                                                      i) + "] / td[9] / div / a / p")

                self.driver.execute_script("arguments[0].scrollIntoView();", self.flag)

                # print(coin_name.text.replace("\n", "").strip(), coin_symbol.text.replace("\n", "").strip(),
                #       volume_24hr.text)

                #Appending data into list of tuples
                self.top_100_coin_list.append((coin_name.text.replace("\n", "").strip(),
                                          coin_symbol.text.replace("\n", "").strip(),
                                          coin_price.text.replace("\n", "").strip(),
                                          hr_24.text.replace("\n", "").strip(),
                                          market_cap.text,
                                          volume_24hr.text))
        except:
            time.sleep(3)
            self.driver.close()

        finally:
            #Create table into DB
            create_table('top_100_coins')
            #Insert data into table
            insert_table('top_100_coins', self.top_100_coin_list)
            time.sleep(3)
            self.driver.close()

    def history_coins_data(self,coin_name,start_date,end_date):
        try:

            start,end = datetime.strptime(start_date, "%d/%m/%Y"),datetime.strptime(end_date, "%d/%m/%Y")
            diff = (end.year - start.year) * 12 + (end.month - start.month)
            no_of_month = diff
            delta = end.date() - start.date()
            no_of_days = int(delta.days)
            #Assign a empty list
            self.history_data_list = []

            #Intialize Webdriver by calling function
            self.initialize_webdriver()
            url = "https://coinmarketcap.com/currencies/" + coin_name + "/historical-data/"
            self.driver.get(url)
            time.sleep(3)

            self.driver.find_element(by=By.XPATH, value="//*[@id='cmc-cookie-policy-banner']/div[2]").click()
            for j in range(1, no_of_month):
                time.sleep(3)
                self.driver.find_element(by=By.XPATH, value='//button[normalize-space()="Load More"]').click()

            for i in range(1, no_of_days + 2):

                #Main Script
                # Giving Elements path id to extract data
                price_date = self.driver.find_element(by=By.XPATH,
                                            value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                               i) + "]/td[1]")
                open_price = self.driver.find_element(by=By.XPATH,
                                                  value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                     i) + "]/td[2]")
                high_price = self.driver.find_element(by=By.XPATH,
                                                  value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                     i) + "]/td[3]")
                low_price = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                    i) + "]/td[4]")
                close_price = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                      i) + "]/td[5]")
                volume = self.driver.find_element(by=By.XPATH,
                                              value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                 i) + "]/td[6]")
                mak_cap = self.driver.find_element(by=By.XPATH,
                                               value="//*[@id='__next']/div[1]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table/tbody/tr[" + str(
                                                  i) + "]/td[7]")
                print(price_date.text.strip(), open_price.text.strip(), close_price.text.strip())

                #Appending data into list of tuples
                self.history_data_list.append((price_date.text.strip(),
                                          open_price.text.strip(),
                                          high_price.text.strip(),
                                          low_price.text.strip(),
                                          close_price.text.strip(),
                                          volume.text.strip(),
                                          mak_cap.text.strip()))

        except:
            # setting time to close after 3 sec
            time.sleep(3)
            self.driver.close()
        finally:
            #Insert data into table
            insert_table(table_name, self.history_data_list)
            # setting time to close after 3 sec
            time.sleep(3)
            self.driver.close()


if __name__ =="__main__":

    # Time period to extract data
    current_date = date.today()
    yesterday = current_date - timedelta(days=1)
    yesterday_ = str(datetime.strftime(yesterday, "%d/%m/%Y"))
    select_coins=['bitcoin','ethereum','bnb','solana','polkadot-new','cardano']

    #Top_coins
    top_100_coins=Crypto_Data_extract()
    top_100_coins.extract_top_100coins()

    #Historical coin data
    for coin in select_coins:
        table_name = "historical_" + coin + "_data"
        new_user=check_table_exist(table_name)
        print(new_user)
        if not new_user:
            #Create table into DB
            create_table(table_name)
            history_price=Crypto_Data_extract()
            history_price.history_coins_data(coin_name=coin,start_date="1/7/2022",end_date=yesterday_)
        else:
            history_price = Crypto_Data_extract()
            history_price.history_coins_data(coin_name=coin, start_date=yesterday_, end_date=yesterday_)






