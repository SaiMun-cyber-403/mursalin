
from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python jan.py')
logo =                                          ("""   
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
┃    _____         _____ __  __  ____  _   _ ┃
┃  / ____|  /\   |_   _|  \/  |/ __ \| \ | | ┃
┃ | (___   /  \    | | | \  / | |  | |  \| | ┃
┃  \___ \ / /\ \   | | | |\/| | |  | | . ` | ┃
┃  ____) / ____ \ _| |_| |  | | |__| | |\  | ┃
┃ |_____/_/    \_\_____|_|  |_|\____/|_| \_|©┃
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
┌━━━━━━━━━━━━━━━━━ SAIMON ━━━━━━━━━━━━━━━━━━┑
┃   CREATED BY   :  SAIMON.CYBER            ┃
┃   FACEBOK      :  SAIMONk189              ┃
┃   GITHUB       :  SAIMUN.CYBER.403        ┃
┃   TOOL STATUS  :  TOOL IS FREE            ┃
┃   TOOL VIRSION :  0.3                     ┃
┃   TOOL NAME    :  DUMP FILE               ┃
└━━━━━━━━━━━━━━━━━ SAIMON ━━━━━━━━━━━━━━━━━━┘
""")
total = []
loop=0
ids = []
def xchker():
    pass

def login():
        os.system('clear')
        print(logo);xchker()
        cookie = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                ses = requests.Session()
                cookies = {'cookie':cookie}
                url = 'https://www.facebook.com/adsmanager/manage/campaigns'
                req = ses.get(url,cookies=cookies)
                set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
                nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
                roq = ses.get(nek,cookies=cookies)
                tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
                tokenw = open(".access_token.txt", "w").write(tok)
                cokiew = open(".fb_cookies.txt", "w").write(cookie)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python malang.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()
def create_file():
        os.system('clear')
        print(logo);xchker()
        print(' [1] Create File ')
        print(' [2] Remove Double Ids ')
        print(' [3] Seprate Ids ')
        print(' [0] Back')
        print(50*'-')
        create_ = input(' Select : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "2":
                double()
        elif create_ == "3":
                sep()
        elif create_ == "0":
                main()
        else:
                exit('invalid select')
                create_file() 

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('.fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('.access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        resss = requests.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":cok}).text
        if "mbasic_logout_button" in resss:
        	nama = re.findall('\<title\>(.*?)<\/title\>',str(resss))[0]
        else:
        	print('{m} INVALID COOKIE ')
        	login()
        print (f'welcome : {name}')
        print("[1] Create File Mix Ids")
        print("[2] Create File New Ids")
        print(44*"-")
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        for xd in range(1):
                idt = input(f' Put id: ')
                try:
                       # fd_url = 'https://graph.facebook.com/v2.0/'+idt+'?fields=friends.limit(5000)&access_token='+access_token)
                        xyz = requests.Session()
                        r = xyz.get('https://graph.facebook.com/v2.0/'+idt+'?fields=friends.limit(5000)&access_token='+access_token, cookies = cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                        
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/example.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        #fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get('https://graph.facebook.com/v2.0/'+idt+'?fields=friends.limit(5000)&access_token='+access_token, cookies = cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return new_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        for el in range(sl):
                sid1 = input(f' Put {el+1} link: ')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/example.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=50) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy1, exid,cookies,access_token,sf,sid1)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()
        


def new_file2(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        for el in range(sl):
                sid1 = input(f' Put {el+1} link: ')
        sid = "1"
       # os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('/storage/emulated/0/1900.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/example.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=50) as yaari:
                for exi6d in file:
                	exid = random.choice(file)
                	yaari.submit(iamBadBoy2, exid,cookies,access_token,sf,sid1)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()
def iamBadBoy(exid,cookies,access_token,sf):
        try:
                global total,loop
               # fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get('https://graph.facebook.com/v2.0/'+exid+'?fields=friends.limit(5000)&access_token='+access_token, cookies = cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                        
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass
def iamBadBoy1(exid,cookies,access_token,sf,sid1):
	try:
		global total,loop
		xyz = requests.Session()
		r = xyz.get('https://graph.facebook.com/v2.0/'+exid+'?fields=friends.limit(5000)&access_token='+access_token, cookies = cookies).text
		q = json.loads(r)
		for yaad in q['friends']['data']:
			iid = yaad['id']
			name = yaad['name']
			if sid1 in iid:
				if iid in total:
					pass 
				else:
					total.append(iid)
					open(sf,'a').write(iid+'|'+name+'\n')
			else:
				pass
		loop+=1
		sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
		time.sleep(15)
	except Exception as e:
		pass
		#print(e)
	except KeyError:
		pass
def iamBadBoy2(exid,cookies,access_token,sf,sid1):
	try:
		osf = open('/storage/emulated/0/9889.txt','r').read().splitlines()
		osf1 = open('/storage/emulated/0/mmkm.txt','r').read().splitlines()
		osf3 = ('/storage/emulated/0/mmkm.txt')
		global total,loop
		xyz = requests.Session()
		r = xyz.get('https://graph.facebook.com/v2.0/'+exid+'?fields=friends.limit(5000)&access_token='+access_token, cookies = cookies).text
		q = json.loads(r)
		for yaad in q['friends']['data']:
			iid = yaad['id']
			name = yaad['name']
			if iid in total:
				pass
			else:
				open(osf3,'a').write(iid+'|'+name+'\n')
				if sid1 in iid:
					if iid in osf:pass
					else:
						if iid in osf1:pass
						else:
							total.append(iid)
							open(sf,'a').write(iid+'|'+name+'\n')
				else:
					pass
		loop+=1
		sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
		time.sleep(15)
	except Exception as e:
		pass
		#print(e)
	except KeyError:
		pass
def sep():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\033[0m[Press enter to back] ')
        main()
        
def double():
	os.system('clear')
	print(logo);xchker()
	filepath = input("[->] Duplicate File Name  : ")
	newfile = input("[->] File Without Duplicate ID Save As : ")
	os.system('sort -r '+filepath+' | uniq > '+newfile)
	print (f' Your File Save As : {newfile}')
create_file()