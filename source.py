from bs4 import BeautifulSoup
from urllib.request import urlopen
from pystyle import *
from threading import active_count
import time, os, threading, requests

def spammer(link):
    global z, x, start_time

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    try:
        if requests.get(link, headers=headers).status_code == 200:
            x += 1
            os.system(f'title Tekky (c) 2022 ^| Views sent: {x} ^| Failed: {z} ^| Speed: {x/(time.time() - start_time)}' if os.name == 'nt' else '')
        else:
            z += 1
            os.system(f'title Tekky (c) 2022 ^| Views sent: {x} ^| Failed: {z} ^| Speed: {x/(time.time() - start_time)}' if os.name == 'nt' else '')
    except:
        z += 1
        os.system(f'title Tekky (c) 2022 ^| Views sent: {x} ^| Failed: {z} ^| Speed: {x/(time.time() - start_time)}' if os.name == 'nt' else '')

def getlink(user):
    global link

    lss = []
    for link in BeautifulSoup(urlopen(f"https://github.com/{user}"), "lxml").findAll('a'):
        if "camo.githubusercontent" in link.get('href'):
            if len(link.get('href')) < 280:
                lss.append(link.get('href'))
    link =  lss[0]
    if len(lss) != 1:
        link = input("Couldn't find any or too much viewcounters, please input your own: ")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    txt = """
         ______ _____ _______ _     _ _     _ ______       _    _ _____ _______ _  _  _ _______ ______   _____  _______
        |  ____   |      |    |_____| |     | |_____]       \  /    |   |______ |  |  | |______ |_____] |     |    |   
        |_____| __|__    |    |     | |_____| |_____]        \/   __|__ |______ |__|__| ______| |_____] |_____|    |   
        
    """
    print(Colorate.Horizontal(Colors.blue_to_purple, txt, 1))
    
    user = Write.Input("        [?] Username > ", Colors.blue_to_purple, interval=0.001)
    print("")

    getlink(user)
    
    start_time = time.time()

    while True:
        while active_count() < 5000:
            threading.Thread(target=spammer, args=(link,)).start()
