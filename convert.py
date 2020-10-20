#~ Covert Decimal,Oktal,Hexadecimal,and Binary 
#~ Coded By Ario Bimo
#~ 20 Okt 2020
#~ Capek Oey :v

from colorama import Fore
import os
import sys

h = Fore.GREEN
m = Fore.RED
b = Fore.BLUE
k = Fore.YELLOW

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")


def bannereng():
    banner = ("""   
{}   _____                          _      __       _ _ {}
{}  / ____|                        | |    / _|     | | |{}
{} | |     ___  _ ____   _____ _ __| |_  | |_ _   _| | |{}
{} | |    / _ \| '_ \ \ / / _ \ '__| __| |  _| | | | | |{}
{} | |___| (_) | | | \ V /  __/ |  | |_  | | | |_| | | |{}
{}  \_____\___/|_| |_|\_/ \___|_|   \__| |_|  \__,_|_|_|{} 
{}                       _               {}
{}                      | |              {}
{} _ __  _   _ _ __ ___ | |__   ___ _ __ {}
{}| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|{}
{}| | | | |_| | | | | | | |_) |  __/ |   {}
{}|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   {}     

{}[{}{}# Coded By.Ario Bimo{}{}]{}
{}[{}{}# 20 Okt 2020{}{}]{}
    """)        
    print(banner.format(m,m,k,k,h,h,b,b,k,k,m,m,k,k,h,h,b,b,m,m,h,h,b,b,h,h,m,m,h,h,h,h,m,m,h,h))

def bannerind():
    banner = ("""
{} _    _ _           _       _     _ _                               {}
{}| |  | | |         | |     | |   (_) |                              {}
{}| |  | | |__   __ _| |__   | |__  _| | __ _ _ __   __ _  __ _ _ __  {}
{}| |  | | '_ \ / _` | '_ \  | '_ \| | |/ _` | '_ \ / _` |/ _` | '_ \ {}
{}| |__| | |_) | (_| | | | | | |_) | | | (_| | | | | (_| | (_| | | | |{}
{} \____/|_.__/ \__,_|_| |_| |_.__/|_|_|\__,_|_| |_|\__, |\__,_|_| |_|{}
{}                                                   __/ |            {}
{}                                                  |___/             {}
{} _                  _               {}
{}| |                | |              {}
{}| | ___ _ __   __ _| | ____ _ _ __  {}
{}| |/ _ \ '_ \ / _` | |/ / _` | '_ \ {}
{}| |  __/ | | | (_| |   < (_| | |_) |{}
{}|_|\___|_| |_|\__, |_|\_\__,_| .__/ {}
{}               __/ |         | |    {}
{}              |___/          |_|    {}

{}[{}{}# Coded By.Ario Bimo{}{}]{}
{}[{}{}# 20 Okt 2020{}{}]{}
    """)       
    print(banner.format(m,m,k,k,h,h,b,b,m,m,k,k,h,h,b,b,k,k,h,h,b,b,m,m,h,h,b,b,m,m,k,k,h,h,m,m,h,h,h,h,m,m,h,h))

selek = ("""

{}Language :{} 

{}[1.] English{}
{}[2.] Indonesian{}
{}[3.] Exit :({}

""")


print(selek.format(m,m,k,k,k,k,k,k))
tool = input(str(h + "["+m+"*"+h+"] Select a language : "))

if tool == "1":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    bannereng()

    info = ("""
{}[{}{}Info ?{}{}]{}

{}[{}{}Binary numbers starting with 0b{}{}]{}
{}[{}{}Hexadecimal numbers prefixed 0x{}{}]{}
{}[{}{}Octal numbers beginning 0o{}{}]{}
    """)
    print(info.format(h,h,m,m,h,h,h,h,m,m,h,h,h,h,m,m,h,h,h,h,m,m,h,h))

    select = ("""
{}[{}{}1.{}{}]{} {}for Decimal to Binary{}
{}[{}{}2.{}{}]{} {}for Decimal to Hexa{}
{}[{}{}3.{}{}]{} {}for Decimal to Octal{}
{}[{}{}4.{}{}]{} {}for Binary to Decimal{}
{}[{}{}5.{}{}]{} {}for Binary to Hexa{}
{}[{}{}6.{}{}]{} {}for Binary to Octal{}
{}[{}{}7.{}{}]{} {}for Hexa to Binary{}
{}[{}{}8.{}{}]{} {}for Hexa to Decimal{}
{}[{}{}9.{}{}]{} {}for Hexa to Octal{}
{}[{}{}10.{}{}]{} {}for octal to Binary{}
{}[{}{}11.{}{}]{} {}for octal to Decimal{}
{}[{}{}12.{}{}]{} {}for octal to Hexa{}

    """)

    print(select.format(h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k))

    i = int(input("Enter your choice : "))

    print("")

    if i == 1:
        x = int(input("Enter a Decimal number: "))        
        print()
        print ("Binary = " + bin(x))
    elif i == 2:
        x = int(input("Enter a Decimal number: "))
        print()
        print ("Hexadecimal = " + hex(x))
    elif i == 3:
        x = int(input("Enter a Decimal number: "))
        print()
        print ("Octal = " + oct(x))
    elif i == 4:
        x = int(input("Enter a Binary number: "),2)
        print()
        print ("Decimal = " + x)
    elif i == 5:
        x = int(input("Enter a Binary number: "),2)
        print()
        print ("Hexadecimal =" + hex(x))
    elif i == 6:
        x = int(input("Enter a Binary number: "),2)
        print()
        print ("Octal = " + oct(x))
    elif i == 7:
        x = int(input("Enter a Hexadecimal number: "),16)
        print()
        print ("Binary = " + bin(x))
    elif i == 8:
        x = int(input("Enter a Hexadecimal number: "),16)
        print()
        print ("Decimal = " + x)
    elif i == 9:
        x = int(input("Enter a Hexadecimal number: "),16)
        print()
        print ("Octal = " + oct(x))
    elif i == 10:
        x = int(input("Enter the Octal number: "),8)
        print()
        print ("Binary = " + bin(x))
    elif i == 11:
        x = int(input("Enter the Octal number: "),8)
        print()
        print ("Decimal = " + x)
    elif i == 12:
        x = int(input("Enter the Octal number: "),8)
        print()
        print ("Hexadecimal = " + hex(x))
    else:
        print("Your choice is wrong !")

elif tool == "2":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    bannerind()

    info = ("""
{}[{}{}Info ?{}{}]{} 

    {}[{}{}Angka Binary diawali (0b){}{}]{} 
    {}[{}{}Angka Hexa diawali (0x){}{}]{} 
    {}[{}{}Angka Oktal diawali (0o){}{}]{}\n""")
    print(info.format(h,h,m,m,h,h,h,h,m,m,h,h,h,h,m,m,h,h,h,h,m,m,h,h))

    select = ("""
{}[{}{}1.{}{}]{} {}untuk Desimal ke Binary{}
{}[{}{}2.{}{}]{} {}untuk Desimal ke Hexa{}
{}[{}{}3.{}{}]{} {}untuk Desimal ke Octal{}
{}[{}{}4.{}{}]{} {}untuk Binary ke Desimal{}
{}[{}{}5.{}{}]{} {}untuk Binary ke Hexa{}
{}[{}{}6.{}{}]{} {}untuk Binary ke Oktal{}
{}[{}{}7.{}{}]{} {}untuk Hexa ke Binary{}
{}[{}{}8.{}{}]{} {}untuk Hexa ke Desimal{}
{}[{}{}9.{}{}]{} {}untuk Hexa ke Octal{}
{}[{}{}10.{}{}]{} {}untuk octal ke Binary{}
{}[{}{}11.{}{}]{} {}untuk octal ke Desimal{}
{}[{}{}12.{}{}]{} {}untuk octal ke Hexa{}


    """)    
    print(select.format(h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h,h,m,m,h,h,k,k,h))

    i = int(input("Masukkan pilihan anda: "))

    print("")

    if i == 1:
        x = int(input("masukkan angka Desimal: "))
        print()
        print ("Biner = " + bin(x))
    elif i == 2:
        x = int(input("masukkan angka Desimal: "))
        print()
        print ("Hexadesimal = " + hex(x))
    elif i == 3:
        x = int(input("masukkan angka Desimal: "))
        print()
        print ("Oktal = " + oct(x))
    elif i == 4:
        x = int(input("masukkan angka Binary: "),2)
        print()
        print ("Desimal = " + x)
    elif i == 5:
        x = int(input("masukkan angka Binary: "),2)
        print()
        print ("Hexadesimal = " + hex(x))
    elif i == 6:
        x = int(input("masukkan angka Binary: "),2)
        print()
        print ("Oktal = " + oct(x))
    elif i == 7:
        x = int(input("masukkan angka hexadesimal: "),16)
        print()
        print ("Biner = " + bin(x))
    elif i == 8:
        x = int(input("masukkan angka hexadesimal: "),16)
        print()
        print ("Desimal = " + x)
    elif i == 9:
        x = int(input("masukkan angka hexadesimal: "),16)
        print()
        print ("Oktal = " + oct(x))
    elif i == 10:
        x = int(input("masukkan angka Octal: "),8)
        print()
        print ("Biner = " + bin(x))
    elif i == 11:
        x = int(input("masukkan angka Octal: "),8)
        print()
        print ("Desimal = " + x)
    elif i == 12:
        x = int(input("masukkan angka Octal: "),8)
        print()
        print ("Hexadesimal = " + hex(x))
    else:
        print("Pilihan kamu salah ! ")

else:
    sys.exit("Byee :)")

