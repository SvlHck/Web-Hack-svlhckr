## santet-online 08-03-2018 (12:12)
# -*- coding: utf-8 -*-
# BlackHole Security
##
import time
from core.misc import *
from core.onlen import *

clearscreen()
logo()
print """
Katagoriden Bölüm Seçin:
  01) Saldiri Listesi Olustur Sivil Hacker
  02) Facebook Grubu Hack le Sivil Hacker
  03) SMS Bombala SivilHacker
  04) SMS Bombalar v2 SivilHacker
  05) DDoS ATTACK SivilHacker
  
  00) Web Hack svlhck Tan Cikis Yap
"""
santet = raw_input("santet > ")

if santet == "01" or santet == "1":
	netcat_rat()
elif santet == "02" or santet == "2":
	facebookgroup_hijack()
elif santet == "03" or santet == "3":
	sms_bomber_jdid()
elif santet == "04" or santet == "4":
	sms_spoof_elk()
elif santet == "05" or santet == "5":
	denialofservice_attack()
else:
	print "\nERROR: Bu Katagori Bolumde Bulunamadi"
	time.sleep(2)
	restart_program()