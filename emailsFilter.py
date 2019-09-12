#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: 12-09-2019 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% by Yassine Baghdadi %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


import os
import sys
import time

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("filtring Emails By domain-name !")
slowprint("Created at 12-09-2019")
slowprint(" by       YASSINE BAGHDADI ")



gmail = ("gmail.com\n")
yahoo = ('yahoo.com\n')
yahooo = ('yahoo.fr\n')
yah = ('yahoo.co.uk\n')
outlook = ('outlook.com\n')
outlok = ('outlook.fr\n')
web = ("web.com\n")
hotmail = ('hotmail.com\n')
hotmil = ('hotmail.fr\n')
hotml = ('hotmail.co.uk\n')
wanadoo = ("wanadoo.com\n")
gmx = ("gmx.com\n")
aol = ("aol.com\n")
msn = ("msn.com\n")
live = ("live.com\n")
yandex = ("yandex.ru\n")
bk = ("bk.ru\n")
inbox = ("inbox.ru\n")
mailru = ("mail.ru\n")
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def reStart():
    r = input("reStart ?? (y/n) : " )
    if r == "y":
        startFilter()
    else:
        print("Good Bay <3")
        slowprint("             YASSINE BAGHDADI ")
        exit()


def startFilter():
    # here script ask you to put your email list !
    global list
    ysne = input("\033[94m[?]\033[97m drag the \033[91memail-list \033[97m:")
    if len(ysne) == 0:
        print("enter the fucking list or go to hell (i'm just kidding <3 )")
        startFilter()

    # ysne="emails"
    try:
        list = open((ysne), "r")
    except:
        print("\033[91mthe \033[91mfile \033[91mwich \033[91myou \033[91mentred \033[91mnot \033[91mfound , \033[91mplease \033[91mtry \033[91magain .")
        reStart()
    # with slowprint script is COOL :V
    slowprint("\033[94m[!]\033[92m Filtering\033[97m:")
    # here the real work :3
    # script will read the email-list and he will filtering the email (gmail,outlook,hotmail...)
    # script will open new text and he will write all the email
    # ex : script will write all the gmail emails in text file : gmail.txt

    symboals = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':',
                ']']

    invalid_counter = 0
    gmail_counter = 0
    aol_counter = 0
    hotmail_counter = 0
    outlook_counter = 0
    msn_counter = 0
    yahoo_counter = 0
    other_counter = 0
    web_counter = 0
    live_counter = 0
    yandex_counter = 0
    mailru_counter = 0
    bk_counter = 0
    inbox_counter = 0
    u = 0
    for i in list.readlines():
        u+=1
        print(u)
        try:

            if (re.search(regex, i)):

                if i.endswith(gmail.upper()) or i.endswith(gmail):
                        file = open("outpute/gmail.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        gmail_counter += 1
                elif i.endswith(yahooo.upper()) or i.endswith(yahoo.upper()) \
                              or  i.endswith(yah.upper()) or i.endswith(yahooo) \
                              or i.endswith(yahoo) or  i.endswith(yah):
                        file = open("outpute/yahoo.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        yahoo_counter += 1
                elif i.endswith(outlook.upper()) or i.endswith(outlok.upper())or  i.endswith(outlook) or i.endswith(outlok):
                        file = open("outpute/outlook.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        outlook_counter +=1
                elif i.endswith(hotmail.upper()) or  i.endswith(hotmil.upper()) or  i.endswith(hotml.upper()) or\
                        i.endswith(hotmail) or  i.endswith(hotmil) or\
                        i.endswith(hotml) :
                        file = open("outpute/hotmail.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        hotmail_counter += 1
                elif i.endswith(web.upper()) or i.endswith(web):
                        file = open("outpute/web.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        web_counter +=1
                elif i.endswith(aol.upper()) or i.endswith(aol):
                        file = open("outpute/aol.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        aol_counter +=1
                elif i.endswith(msn.upper()) or  i.endswith(msn):
                        file = open("outpute/msn.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        msn_counter +=1
                elif i.endswith(live.upper()) or  i.endswith(live):
                        file = open("outpute/live.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        live_counter +=1
                elif i.endswith(yandex.upper()) or  i.endswith(yandex):
                        file = open("outpute/yandex.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        yandex_counter +=1
                elif i.endswith(mailru.upper()) or i.endswith(mailru):
                        file = open("outpute/mail.ru.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        mailru_counter +=1
                elif i.endswith(bk.upper()) or i.endswith(bk):
                        file = open("outpute/mail.ru.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        bk_counter +=1
                elif i.endswith(inbox.upper()) or i.endswith(inbox):
                        file = open("outpute/mail.ru.txt","a")
                        file.write((i)+"")
                        file.close()
                        print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
                        inbox_counter +=1
                else:

                    file = open("outpute/other.txt", "a")
                    file.write((i) + "")
                    file.close()
                    other_counter +=1
                    print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
            else:
                file = open("outpute/invalid.txt", "a")
                file.write((i) + "")
                file.close()
                invalid_counter += 1
                print("\033[1m{}".format(i), "\033[32mDone! added to {}".format(str(file.name)))
        except:
            print('some thing went wrong ')
            exit()

    os.system('clear')
    slowprint("\033[92mDone\033[97m , nice\033[91m phishing\033[97m !")
    slowprint("gmail   : {}".format(gmail_counter))
    slowprint("Yahoo   : {}".format(aol_counter))
    slowprint("outlook : {}".format(outlook_counter))
    slowprint("web     : {}".format(web_counter))
    slowprint("Hotmail : {}".format(hotmail_counter))
    slowprint("msn     : {}".format(msn_counter))
    slowprint("live    : {}".format(live_counter))
    slowprint("yandex  : {}".format(yandex_counter))
    slowprint("bk      : {}".format(bk_counter))
    slowprint("index   : {}".format(inbox_counter))
    slowprint("mail.ru : {}".format(mailru_counter))
    slowprint("Other   : {}".format(other_counter))
    slowprint("invalid : {}".format(invalid_counter))
    slowprint("Total   : {}".format(gmail_counter + aol_counter + outlook_counter +
                                  web_counter + hotmail_counter + msn_counter + live_counter +
                                  yandex_counter + bk_counter + inbox_counter
                                  + mailru_counter + other_counter))
    reStart()

startFilter()


