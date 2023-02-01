from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import time
import pause
import warnings
import threading
import os
import logging
from telegram.ext import Updater, CommandHandler, run_async
from telegram import ChatAction
from config import Config
from os import execl
from sys import executable
import pickle

#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher
browser = driver

proxylist = [
    "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
   "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",
]
warnings.filterwarnings('ignore')

fake = [
'David Asir',
'Mohammed UAE',
'Victor Sam',
'SENTHILKUMAR DUBAI',
'Tamilarasan',
'NAWAZ KHALEEL',
'Samimii',
'PEER MOHAMMAD',
'L Krishnakumar',
'Yuvanathan',
'MANJU',
'Muthubabu',
'Christopher Asir Dass',
'KITTY',
'Prabhakar',]

MUTEX = threading.Lock()


def sync_print(text):
    with MUTEX:
        print(text)

def get_driver(proxy):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-infobars")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_argument("--start-maximized")
    if proxy is not None:
        options.add_argument(f"--proxy-server={proxy}")
    driver = webdriver.Chrome(options=options)
    return driver

browser = webdriver.Chrome(options=options)
logged_in=False
teams_in=False



@run_async
def restart(update, context):
    restart_message = context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
    # Save restart message object in order to reply to it after restarting
    browser.quit()
    context.bot.send_message(chat_id=update.message.chat_id,text="Restarted Your Bot👍.")
    logging.info("restarting bot!!")
    with open('restart.pickle', 'wb') as status:
        pickle.dump(restart_message, status)
    execl(executable, executable, "chromium.py")
    
def status(update, context):
	try:
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')
		logging.info("*enquired status*")
		time.sleep(10)
		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

	except:
		context.bot.send_message(chat_id=update.message.chat_id, text="please /restart your bot🤖 to get status")
		
def driver_wait(driver, locator, by, secs=1, condition=ec.element_to_be_clickable):
    wait = WebDriverWait(driver=driver, timeout=secs)
    element = wait.until(condition((by, locator)))
    return element
	
def zoom(update, context,name, proxy, user, wait_time):
	logging.info("DOING")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		
		usernameStr = Config.USERNAME
		passwordStr = Config.PASSWORD
		
		

		url_meet = update.message.text.split()[1]
		passStr = update.message.text.split()[2]
		user = 'alan'
	        

		browser.get('https://zoom.us/wc/join/'+ url_meet)

		time.sleep(5)
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid  = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), caption="Test", timeout = 120).message_id
		os.remove('ss.png')
		time.sleep(5)
		inp = driver.find_element(By.ID, 'inputname')
                time.sleep(1)
                inp.send_keys(f"{user}")
                btn2 = driver.find_element(By.ID, 'joinBtn')
   		btn2.click()
    		time.sleep(2)
    		inp2 = driver.find_element(By.ID, 'inputpasscode')
    		time.sleep(1)
    		inp2.send_keys(passcode)
    		btn3 = driver.find_element(By.ID, 'joinBtn')
    		time.sleep(1)
    		btn3.click()
    		sync_print(f"{name} sleep for {wait_time} seconds ...")
    		time.sleep(wait_time)
    		sync_print(f"{name} ended!")
		
		

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill ")
		context.bot.send_message(chat_id=update.message.chat_id,text="To exit click /exitmeet ")
		pause
		logging.info("STAAAAPH!!")

	
	except:
		browser.quit()
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occurred retry!please /restart")


def exitmeet(update,context):
	global logged_in
	if logged_in:
		try:
			logging.info("exiting meet!!!")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Exiting your meeting!!")
			browser.execute_script("window.open('');")
			browser.close()
			browser.switch_to.window(browser.window_handles[-1])
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Exited your meeting.")
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			time.sleep(10)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
			
		except:
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Some error occured!!!retry again.")
	else:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="No meeting is running to exit.")



def start(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text="Use following Commands to interact with bot :\nTo join zoom meeting - /zoom zoommeetingid password\nTo know Status of Bot - /status\nTo exit meet - /exitmeet\nTo restart Bot🤖 - /restart")
	
	
def __init__():
    wait_time = sec * 60
    workers = []
    for i in range(number):
        fakes = fake[i]
        try:
            proxy = proxylist[i]
        except IndexError:
            proxy = None
        try:
            user = fakes
        except IndexError:
            break
        wk = threading.Thread(target=start, args=(
            f'[Thread{i}]', proxy, user, wait_time))
        workers.append(wk)
    for wk in workers:
        wk.start()
    for wk in workers:
        wk.join()	

def main():
	import os
	# PORT = int(os.environ.get('PORT', 8000))
	dp.add_handler(CommandHandler("start",start))
	dp.add_handler(CommandHandler("zoom", zoom))
	
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("status", status))
	dp.add_handler(CommandHandler("exitmeet", exitmeet))
	
	
	logging.info("Bot started")
	# updater.start_webhook(listen="0.0.0.0",
 #                          port=int(PORT),
 #                          url_path=str(Config.BOT_TOKEN))
	# updater.bot.setWebhook('https://charanclassesbot.herokuapp.com/' + str(Config.BOT_TOKEN))
	updater.start_polling()

if __name__ == '__main__':
    main()
