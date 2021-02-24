import time
import getpass
#import requests
import json
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.add_argument('--user-data-dir=C:\\Users\\tk300\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 1')  #この行を省略するとDefaultフォルダが指定されます
driver = webdriver.Chrome(chrome_options=options)


subject = ["数ⅠB","化学Ⅰ","基礎工作実習","現代の社会Ⅰ","工学概論","国語ⅠA","国語ⅠＢ","数学ⅠA","数学ⅠＢ","音楽","保健体育Ⅰ","英語ⅠA(黒木暁人)","英語ⅠA(小林貢)"]
originalURL=["https://docs.google.com/forms/d/e/1FAIpQLSfQ8h6nF89ztbtuYgQh2Woz_6SMImw_fGsi5-rTXPxB4jqWlA/viewform","https://docs.google.com/forms/d/e/1FAIpQLSfgp9Pf7bYjYYbzEFQ_qtx09nqgaYpQEIxJMY0-qFEG3CJlSg/viewform","https://docs.google.com/forms/d/e/1FAIpQLSck0lr3ItsvLZ-Ewpelo0Z_8mobxCrAcD6R_0Bv_WIvq6El-A/viewform","https://docs.google.com/forms/d/e/1FAIpQLSdi542KigwVJkAuxVy9VugBGwMO5iy_u1APHQ6Zz6k4g73tEw/viewform","https://docs.google.com/forms/d/e/1FAIpQLSd1iVt34cfulGb3_H7wfxGw_bnhFA2nkZoz-KwXAtWPvbQQSA/viewform","https://docs.google.com/forms/d/e/1FAIpQLSdAkt7TfaN-PUzbAsdhWkayBN4NZ3sI_iybyroVGWBPwuHdvg/viewform","https://docs.google.com/forms/d/e/1FAIpQLSciGNhyzUb2KDN721ioWtGmAW0cmbGjX1-xXK1KPaaAIK5hQQ/viewform","https://docs.google.com/forms/d/e/1FAIpQLSfrkqLgfDJbGBTvA2qlqcAJb8DAo6KIxTKXmolOvkxk51mFkg/viewform","https://docs.google.com/forms/d/e/1FAIpQLScXRCEDMIJOMz91Y7-oAknja8IdV_Fy9JXMZLB67ng3A7UC4g/viewform","https://docs.google.com/forms/d/e/1FAIpQLSc2D3Gd7Tw5N_fZlIqy-Mp8jZM2hSrXvWd2D_taMLqUjROBgQ/viewform","https://docs.google.com/forms/d/e/1FAIpQLSdT1yAdJ8YFdyt3XjtJdP_eqL6FFwOa2edId3GVMoGYy07cTA/viewform","https://docs.google.com/forms/d/e/1FAIpQLSfDsHVh5CJuiWbY4d-Ihb_mkV8sz8iltEVX127h5DeDJksaOw/viewform","https://docs.google.com/forms/d/e/1FAIpQLSf24lyDeRXUJl7Cqc0wFO6FZvT1yD2nO21M86t1vi09eY156A/viewform"]
answerURL1="?usp=pp_url&entry.626999884=1年&entry.1349777871=3組&entry.864066051="
answerURL2="&entry.1108179623=とてもそう思う&entry.126214635=とてもそう思う&entry.1067919537=とてもそう思う&entry.2000175824=とてもそう思う&entry.1895321897=とてもそう思う&entry.1653792532=とてもそう思う&entry.927939617=とてもそう思う&entry.1287598591=とてもそう思う&entry.657401875=とてもそう思う&entry.496882569=とてもそう思う&entry.185693913=とてもそう思う&entry.817792292=とてもそう思う&entry.1051536298=とてもそう思う&entry.1303375600=とてもそう思う&entry.39137056=とてもそう思う"
count=-1

for i in range(11):
    count=count+1
    url=originalURL[count] + answerURL1 + subject[count] + answerURL2
    driver.get(url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    print(element)
    element.click()
    time.sleep(3)

   

""" 
?usp=pp_url&entry.626999884=1年&entry.1349777871=3組&entry.864066051=□&entry.1108179623=とてもそう思う&entry.126214635=とてもそう思う&entry.1067919537=とてもそう思う&entry.2000175824=とてもそう思う&entry.1895321897=とてもそう思う&entry.1653792532=とてもそう思う&entry.927939617=とてもそう思う&entry.1287598591=とてもそう思う&entry.657401875=とてもそう思う&entry.496882569=とてもそう思う&entry.185693913=とてもそう思う&entry.817792292=とてもそう思う&entry.1051536298=とてもそう思う&entry.1303375600=とてもそう思う&entry.39137056=とてもそう思う
数B           https://docs.google.com/forms/d/e/1FAIpQLSfQ8h6nF89ztbtuYgQh2Woz_6SMImw_fGsi5-rTXPxB4jqWlA/viewform?usp=pp_url&entry.626999884=1年&entry.1349777871=3組&entry.864066051=□&entry.1108179623=とてもそう思う&entry.126214635=とてもそう思う&entry.1067919537=とてもそう思う&entry.2000175824=とてもそう思う&entry.1895321897=とてもそう思う&entry.1653792532=とてもそう思う&entry.927939617=とてもそう思う&entry.1287598591=とてもそう思う&entry.657401875=とてもそう思う&entry.496882569=とてもそう思う&entry.185693913=とてもそう思う&entry.817792292=とてもそう思う&entry.1051536298=とてもそう思う&entry.1303375600=とてもそう思う&entry.39137056=とてもそう思う
化学Ⅰ        https://docs.google.com/forms/d/e/1FAIpQLSfgp9Pf7bYjYYbzEFQ_qtx09nqgaYpQEIxJMY0-qFEG3CJlSg/viewform?usp=pp_url&entry.626999884=1年&entry.1349777871=3組&entry.864066051=□&entry.1108179623=とてもそう思う&entry.126214635=とてもそう思う&entry.1067919537=とてもそう思う&entry.2000175824=とてもそう思う&entry.1895321897=とてもそう思う&entry.1653792532=とてもそう思う&entry.927939617=とてもそう思う&entry.1287598591=とてもそう思う&entry.657401875=とてもそう思う&entry.496882569=とてもそう思う&entry.185693913=とてもそう思う&entry.817792292=とてもそう思う&entry.1051536298=とてもそう思う&entry.1303375600=とてもそう思う&entry.39137056=とてもそう思う
基礎工作実習  https://docs.google.com/forms/d/e/1FAIpQLSck0lr3ItsvLZ-Ewpelo0Z_8mobxCrAcD6R_0Bv_WIvq6El-A/viewform
現代の社会Ⅰ  https://docs.google.com/forms/d/e/1FAIpQLSdi542KigwVJkAuxVy9VugBGwMO5iy_u1APHQ6Zz6k4g73tEw/viewform
工学概論      https://docs.google.com/forms/d/e/1FAIpQLSd1iVt34cfulGb3_H7wfxGw_bnhFA2nkZoz-KwXAtWPvbQQSA/viewform
国語ⅠA       https://docs.google.com/forms/d/e/1FAIpQLSdAkt7TfaN-PUzbAsdhWkayBN4NZ3sI_iybyroVGWBPwuHdvg/viewform
国語ⅠＢ      https://docs.google.com/forms/d/e/1FAIpQLSciGNhyzUb2KDN721ioWtGmAW0cmbGjX1-xXK1KPaaAIK5hQQ/viewform
数学ⅠA       https://docs.google.com/forms/d/e/1FAIpQLSfrkqLgfDJbGBTvA2qlqcAJb8DAo6KIxTKXmolOvkxk51mFkg/viewform
数学ⅠＢ      https://docs.google.com/forms/d/e/1FAIpQLScXRCEDMIJOMz91Y7-oAknja8IdV_Fy9JXMZLB67ng3A7UC4g/viewform
音楽          https://docs.google.com/forms/d/e/1FAIpQLSc2D3Gd7Tw5N_fZlIqy-Mp8jZM2hSrXvWd2D_taMLqUjROBgQ/viewform
保健体育Ⅰ    https://docs.google.com/forms/d/e/1FAIpQLSdT1yAdJ8YFdyt3XjtJdP_eqL6FFwOa2edId3GVMoGYy07cTA/viewform
英語ⅠA（黒木暁人)https://docs.google.com/forms/d/e/1FAIpQLSfDsHVh5CJuiWbY4d-Ihb_mkV8sz8iltEVX127h5DeDJksaOw/viewform
英語ⅠA（小林貢） https://docs.google.com/forms/d/e/1FAIpQLSf24lyDeRXUJl7Cqc0wFO6FZvT1yD2nO21M86t1vi09eY156A/viewform
"""