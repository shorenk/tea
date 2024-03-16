import csv
import random
import os
import time
import datetime
import glob


regions = []

regions.append(Region(Region(0,0,638,720)))

regions.append(Region(Region(640,0,640,720)))

base_path    = 'C:\\blast\\'
tt_stock     = base_path  + "link_tiktok.txt" 
tt_komen    = open(base_path  + "tiktokkomen.txt")

waktu_jeda_min = 5
waktu_jeda_max = 10
array_number = [i for i in range(waktu_jeda_min, waktu_jeda_max)]

### RANDOM NARASI START
komen = csv.reader(tt_komen, delimiter='|', quotechar='"')
array_tiktok = []
kata = ''
jumlah = -1
for row in komen:
    if(len(row)==1):
        if(row[0]=='---baru---'):
            array_tiktok.append(kata)
            kata=''
            jumlah = jumlah + 1
        else:
            kata = kata + row[0] + '\n'

array_tiktok.append(kata)
jumlah = jumlah + 1
### NARASI DONE

with open(tt_stock, "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    tiktok_link = []
    for row in reader:
        print(row)
        tiktok_link.append(row)


#Jumlah pengulangan refresh
ulang = 2

#Link Video
url = 'https://www.tiktok.com/@ganjarpranowo/video/7319476903847496961?is_from_webapp=1&sender_device=pc&web_id=7222143481829230082'

#Looping Here
for loop in range(ulang):
    for baca in range(len(tiktok_link)):
        current_link = tiktok_link[baca][0]
        layar_user = -1
        for layar in regions:
                layar_user  = layar_user  + 1
                if layar.exists(Pattern("1700514481093.png").similar(0.80)):
                    layar.click(Pattern("1700514481093.png").similar(0.80).targetOffset(100,-55))
                    layar.type(Key.BACKSPACE)
                    layar.type(Key.BACKSPACE)
                    layar.paste(current_link)
                    layar.type(Key.ENTER)
        #Jeda
        waktu_jeda = random.randint(waktu_jeda_min, waktu_jeda_max)
        random.shuffle(array_number)
        waktu_jeda = array_number[0]
        print(waktu_jeda)
        time.sleep(waktu_jeda)
        layar_user = -1
        for layar in regions:
            layar_user = layar_user + 1
            if layar.exists(Pattern("1700514481093-1.png").similar(0.80).targetOffset(100,-55)):
                layar.click(Pattern("1700514481093-1.png").similar(0.80).targetOffset(134,-2))
                while True:
                    if not layar.exists(Pattern("1701418443529.png").similar(0.80)):
                        Mouse.wheel(WHEEL_DOWN, 4)
                    else:
                        print("Image Found!")
                        time.sleep(1)
                        break
                if layar.exists(Pattern("1701418443529.png").similar(0.80)):
                    layar.click(Pattern("1701418443529.png").similar(0.80))
                    layar.click(Pattern("1701418443529.png").similar(0.80))
                    time.sleep(1)
                     #GANTI RANDOM
                    acak   = random.randint(0,jumlah)
                    narasi = array_tiktok[acak]
        
                    for satusatu in narasi:
                        layar.paste(satusatu)
                        sleep(0.05)
    
                    layar.wait(Pattern("1703230185508.png").similar(0.80),180)
                    if layar.exists(Pattern("1703230185508.png").similar(0.80)):
                        layar.click(Pattern("1703230185508.png").similar(0.80))
                    time.sleep(1)
                    Mouse.wheel(WHEEL_DOWN, 1)
                    #while True:
                        #if not exists(Pattern("1701419303092.png").similar(0.80)):
                           # Mouse.wheel(WHEEL_DOWN, 1)
                        #else:
                            #print("Image Found!")
                            #time.sleep(1)
                            #break
                    if layar.exists(Pattern("1701419303092.png").similar(0.80)):
                        layar.click(Pattern("1701419303092.png").similar(0.80))
                        time.sleep(3)
                    #if layar.exists(Pattern("1703219786917.png").similar(0.80)):
                        #layar.click(Pattern("1703219786917.png").similar(0.80).targetOffset(125,-61))
                        #time.sleep(2)
                    
                #if layar.exists(Pattern("1700514481093-1.png").similar(0.80).targetOffset(510,176)):
                    #layar.click(Pattern("1700514481093-1.png").similar(0.80).targetOffset(512,177))      