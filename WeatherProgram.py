import json
import requests
from Secret import OpenWeatherApi_Key
import pygame
import time
# Enter Your Country Name in country Variable, (Case Sensitive)
country = 'Sousse'
olddate = ''
date = ''
yMark = 0
xMark = 0

# this opens the city list we get download from the openweathermap website
# and puts the data in city_data
with open('city_list.json' ,'r+', encoding="UTF-8") as f:
    city_data = json.load(f)    

print("Look for Countries ... :\n")

# this looks for the country in the data and get the name, id and country
for data in city_data:
    if country in data['name']:
        print("name:{}\nid:{}\ncountry:{}".format(data['name'],data['id'],data['country']))
        print(data)
# Send request to the api to get your city weather information
# OpenWeatherApi_Key, you need to get plan to the api , beginner is free, then get your api key
# that you'll need to send requests and put it in secrets.py variable 
"""
r = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=Sousse,TN&mode=json&units=imperial&APPID=' + OpenWeatherApi_Key)
with open('HammamSousseWeatherData.json', 'w+') as f:
    f.write(r.text)
"""
# Load you city weather data into the variable HamamSousseData, HammamSousse being the city
# i chose to get data for
with open('HammamSousseWeatherData.json', 'r+', encoding="UTF-8") as f:
    HammamSousseData = json.load(f)


Count_dates = 0
Count_Hot_icon = 0
Count_VeryHot_icon = 0
Count_Cold_icon = 0
Count_freezing_cold_icon = 0
Count = 0
yMark = 0
xMark = 0

def CurrentdayInfo():
    global olddate
    olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(HammamSousseData['list'][0]['dt']))
    today_date = font_big.render("Time: " + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(HammamSousseData['list'][0]['dt'])), True, (255,255,255))
    Intermediate.blit(today_date,(0,0))
    Weather = font_medium.render("Weather in {}: ".format(country) , True, (255,255,255))
    Intermediate.blit(Weather,(10,50))
    temp = font_small.render("temperature: " + str(HammamSousseData['list'][0]['main']['temp']) + 'F', True, (255,255,255) )
    Intermediate.blit(temp,(30,100))
    if HammamSousseData['list'][0]['main']['temp'] <= 77 and HammamSousseData['list'][0]['main']['temp'] >= 68:
        Intermediate.blit(Hot_icon,(250,80))
    elif HammamSousseData['list'][0]['main']['temp'] > 77:
        Intermediate.blit(VeryHot_icon,(250,80))
    elif HammamSousseData['list'][0]['main']['temp'] <68 and HammamSousseData['list'][0]['main']['temp'] >50:
        Intermediate.blit(Cold_icon,(250,80))
    elif HammamSousseData['list'][0]['main']['temp'] <= 50:
        Intermediate.blit(freezing_cold,(250,80))

def DayAfterInfo(date):
    DayAfterInfoArray = []
    for data in HammamSousseData['list']:
        #print(data['dt_txt'].split('-')[2].split(' ')[0])
        #if int(data['dt_txt'].split('-')[2].split(' ')[0]) == int(olddate.split(' ')[1])+1:
        if time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt'])).split(' ')[1] == date.split(' ')[1]:
            DayAfterInfoArray.append(data)
            print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt'])))
            print(date)
        elif time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt'])).split(' ')[1] > date.split(' ')[1]:
            break
    print(DayAfterInfoArray)
    return DayAfterInfoArray
    
    #print("\nDayAfterInfoArray")
    #print(DayAfterInfoArray)
    #olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(DayAfterInfoArray[0]['dt']))
    #print(olddate)
def MakeUsableList(data_list):
    dates_list = []
    Weather_list = []
    temp_list = []
    Hot_icon_list = []
    Cold_icon_list = []
    VeryHot_icon_list = []
    freezing_cold_icon_list = []
    windSpeed_list = []
    Count = 0
    wind_icon_list = []
    humidity_list = []
    humidity_icon_list = []
    
    Weather_list.append(font_big.render("Weather in {}: ".format(country) , True, (000,153,153)))

    for data in data_list:
        dates_list.append(font_medium.render('Time: ' + time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(data_list[Count]['dt'])) + "GMT",True,(200,150,60)))
        temp_list.append(font_small.render("temperature: " + str(data_list[Count]['main']['temp']) + 'F', True, (0,254,254)))
        windSpeed_list.append(font_small.render("Wind Speed: " + str(data_list[Count]['wind']['speed'])+ ' ' + "Miles/h",True, (0,254,254)))
        wind_icon_list.append(pygame.image.load('wind.png'))
        humidity_list.append(font_small.render("Humidity: " + str(data_list[Count]['main']['humidity'])+ ' ' + "%",True, (0,254,254)))
        humidity_icon_list.append(pygame.image.load('humidity.png'))
        if data_list[Count]['main']['temp'] <= 77 and data_list[Count]['main']['temp'] >= 68:
            Hot_icon_list.append(pygame.image.load('hottemp.png'))
        elif data_list[Count]['main']['temp'] > 77:
            VeryHot_icon_list.append(pygame.image.load('veryhottemp.png'))
        elif data_list[Count]['main']['temp'] <68 and data_list[Count]['main']['temp'] >50:
            Cold_icon_list.append(pygame.image.load('cold.png'))
        elif data_list[Count]['main']['temp'] <= 50:
            freezing_cold_icon_list.append(pygame.image.load('freezingtemp.png'))
        Count += 1
    return (dates_list,Weather_list,temp_list,Hot_icon_list,VeryHot_icon_list,Cold_icon_list,freezing_cold_icon_list,windSpeed_list,wind_icon_list,humidity_list,humidity_icon_list)
def printdayAfter(data_to_use,data_list):
    Count_dates = 0
    Count_Hot_icon = 0
    Count_VeryHot_icon = 0
    Count_Cold_icon = 0
    Count_freezing_cold_icon = 0
    Count = 0
    yMark = 0
    xMark = 0
    for data in range(len(data_list[0])):
            yMark += 100
            screen.blit(data_list[0][Count_dates],(xMark,yMark))
            yMark += 100
            screen.blit(data_list[1][Count_dates],(10,yMark))
            yMark += 100
            screen.blit(data_list[2][Count_dates],(30,yMark))
            if data_to_use[Count]['main']['temp'] <= 77 and data_to_use[Count]['main']['temp'] >= 68:
                screen.blit(data_list[3][Count_Hot_icon],(250,yMark - 20))
                Count_Hot_icon += 1
            elif data_to_use[Count]['main']['temp'] > 77:
                screen.blit(data_list[4][Count_VeryHot_icon],(250,yMark - 20))
                Count_VeryHot_icon += 1
            elif data_to_use[Count]['main']['temp'] <68 and data_to_use[Count]['main']['temp'] >50:
                screen.blit(data_list[5][Count_Cold_icon],(250,yMark - 20))
                Count_Cold_icon += 1 
            elif data_to_use[Count]['main']['temp'] <= 50:
                screen.blit(data_list[6][Count_freezing_cold_icon],(250,yMark - 20))
                Count_freezing_cold_icon +=1
            Count_dates += 1
            Count += 1


def DayBeforeInfo():
    pass

#olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(HammamSousseData['list'][0]['dt']))

#DayAfterInfo()

# Initialize Pygame
pygame.init()

# Making the Screen
screen = pygame.display.set_mode((1260,700))
# Change Screen Title and Action
pygame.display.set_caption("Weather Stats")
# Making Intermediate
size_Intermediate = (1260,2000)
Intermediate = pygame.surface.Surface((1260,2000))
# Icon source : <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
screen_icon = pygame.image.load("sun.png")
pygame.display.set_icon(screen_icon)
# Getting Background image for Program
Background = pygame.image.load("bg.png")
# Choose Font
font_small = pygame.font.Font('freesansbold.ttf',20)
font_medium = pygame.font.Font('freesansbold.ttf', 25)
font_big = pygame.font.Font('freesansbold.ttf', 32)

'''
Icons Source
Hot_icon = <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
cold_icon = <div>Icons made by <a href="https://www.flaticon.com/authors/smalllikeart" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
'''



# Make Weather Icons
Hot_icon = pygame.image.load('Hottemp.png')
VeryHot_icon = pygame.image.load('veryhottemp.png')
Cold_icon = pygame.image.load('cold.png')
freezing_cold = pygame.image.load('freezingtemp.png')

timetoday = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(1584997200))
#print(timetoday.split(' '))

pageNumber = 0
Intermediate_pos_y = 0
scroll_y = 0
Currentday = True
dayAfter = False
dayBefore = False
running = True

olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(HammamSousseData['list'][0]['dt']))
data_to_use = DayAfterInfo(olddate)
data_list = MakeUsableList(data_to_use)

while running:
    # Screen Fill (Pass 3 RGB Colors)
    screen.fill((0,0,0))
    # Screen Background
    screen.blit(Background,(0,0))
    Intermediate.blit(Background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if Intermediate_pos_y < 0:
                    scroll_y += 20
                    Intermediate_pos_y += 20
            if event.key == pygame.K_z:
                if Intermediate_pos_y > -500:
                    scroll_y -= 20
                    Intermediate_pos_y -= 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if pageNumber > 0 :
                    dayAfter = False
                    Currentday = False
                    dayBefore = True
                    for data in HammamSousseData['list']:
                        #print(data['dt_txt'].split('-')[2].split(' ')[0])
                        if int(data['dt_txt'].split('-')[2].split(' ')[0]) == int(olddate.split(' ')[1])-1:
                            #print(int(data['dt_txt'].split('-')[2].split(' ')[0]))
                            #print(int(olddate.split(' ')[1])+1)
                            #print(data['dt'])
                            #print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt'])))
                            olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt']))
                            print(olddate)
                            break
                    data_to_use = DayAfterInfo(olddate)
                    data_list = MakeUsableList(data_to_use)
                    pageNumber -= 1
            if event.key == pygame.K_DOWN:
                if pageNumber < 5 :
                    dayBefore = False
                    Currentday = False
                    dayAfter = True
                    for data in HammamSousseData['list']:
                        #print(data['dt_txt'].split('-')[2].split(' ')[0])
                        if int(data['dt_txt'].split('-')[2].split(' ')[0]) == int(olddate.split(' ')[1])+1:
                            #print(int(data['dt_txt'].split('-')[2].split(' ')[0]))
                            #print(int(olddate.split(' ')[1])+1)
                            #print(data['dt'])
                            #print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt'])))
                            olddate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(data['dt']))
                            print(olddate)
                            break
                    data_to_use = DayAfterInfo(olddate)
                    data_list = MakeUsableList(data_to_use)
                    pageNumber += 1

    if Currentday == True:
        Count_dates = 0
        Count_Hot_icon = 0
        Count_VeryHot_icon = 0
        Count_Cold_icon = 0
        Count_freezing_cold_icon = 0
        Count = 0
        xMark = 0
        yMark = 0
        Intermediate.blit(data_list[1][0],(10,yMark))
        yMark +=50
        #print("datalist[0]={}".format(len(data_list[0])))
        for data in range(len(data_list[0])):
            if Count >= 1:
                yMark += 50
            Intermediate.blit(data_list[0][Count_dates],(xMark,yMark))
            yMark += 50
            Intermediate.blit(data_list[2][Count_dates],(30,yMark))
            Intermediate.blit(data_list[7][Count_dates],(360,yMark))
            Intermediate.blit(data_list[8][Count_dates],(630,yMark - 20))
            Intermediate.blit(data_list[9][Count_dates],(780,yMark))
            Intermediate.blit(data_list[10][Count_dates],(960,yMark -20))
            if data_to_use[Count]['main']['temp'] <= 77 and data_to_use[Count]['main']['temp'] >= 68:
                Intermediate.blit(data_list[3][Count_Hot_icon],(250,yMark - 20))
                Count_Hot_icon += 1
            elif data_to_use[Count]['main']['temp'] > 77:
                Intermediate.blit(data_list[4][Count_VeryHot_icon],(250,yMark - 20))
                Count_VeryHot_icon += 1
            elif data_to_use[Count]['main']['temp'] <68 and data_to_use[Count]['main']['temp'] >50:
                Intermediate.blit(data_list[5][Count_Cold_icon],(250,yMark - 20))
                Count_Cold_icon += 1 
            elif data_to_use[Count]['main']['temp'] <= 50:
                Intermediate.blit(data_list[6][Count_freezing_cold_icon],(250,yMark - 20))
                Count_freezing_cold_icon +=1
            Count_dates += 1
            Count += 1
    if dayAfter == True:
        Count_dates = 0
        Count_Hot_icon = 0
        Count_VeryHot_icon = 0
        Count_Cold_icon = 0
        Count_freezing_cold_icon = 0
        Count = 0
        xMark = 0
        yMark = 0
        Intermediate.blit(data_list[1][0],(10,yMark))
        yMark +=50
        #print("datalist[0]={}".format(len(data_list[0])))
        for data in range(len(data_list[0])):
            if Count >= 1:
                yMark += 50
            Intermediate.blit(data_list[0][Count_dates],(xMark,yMark))
            yMark += 50
            Intermediate.blit(data_list[2][Count_dates],(30,yMark))
            Intermediate.blit(data_list[7][Count_dates],(360,yMark))
            Intermediate.blit(data_list[8][Count_dates],(630,yMark - 20))
            Intermediate.blit(data_list[9][Count_dates],(780,yMark))
            Intermediate.blit(data_list[10][Count_dates],(960,yMark -20))
            if data_to_use[Count]['main']['temp'] <= 77 and data_to_use[Count]['main']['temp'] >= 68:
                Intermediate.blit(data_list[3][Count_Hot_icon],(250,yMark - 20))
                Count_Hot_icon += 1
            elif data_to_use[Count]['main']['temp'] > 77:
                Intermediate.blit(data_list[4][Count_VeryHot_icon],(250,yMark - 20))
                Count_VeryHot_icon += 1
            elif data_to_use[Count]['main']['temp'] <68 and data_to_use[Count]['main']['temp'] >50:
                Intermediate.blit(data_list[5][Count_Cold_icon],(250,yMark - 20))
                Count_Cold_icon += 1 
            elif data_to_use[Count]['main']['temp'] <= 50:
                Intermediate.blit(data_list[6][Count_freezing_cold_icon],(250,yMark - 20))
                Count_freezing_cold_icon +=1
            Count_dates += 1
            Count += 1
    if dayBefore == True:
        Count_dates = 0
        Count_Hot_icon = 0
        Count_VeryHot_icon = 0
        Count_Cold_icon = 0
        Count_freezing_cold_icon = 0
        Count = 0
        xMark = 0
        yMark = 0
        Intermediate.blit(data_list[1][0],(10,yMark))
        yMark +=50
        #print("datalist[0]={}".format(len(data_list[0])))
        for data in range(len(data_list[0])):
            if Count >= 1:
                yMark += 50
            Intermediate.blit(data_list[0][Count_dates],(xMark,yMark))
            yMark += 50
            Intermediate.blit(data_list[2][Count_dates],(30,yMark))
            Intermediate.blit(data_list[7][Count_dates],(360,yMark))
            Intermediate.blit(data_list[8][Count_dates],(630,yMark-20))
            Intermediate.blit(data_list[9][Count_dates],(780,yMark))
            Intermediate.blit(data_list[10][Count_dates],(960,yMark -20))
            if data_to_use[Count]['main']['temp'] <= 77 and data_to_use[Count]['main']['temp'] >= 68:
                Intermediate.blit(data_list[3][Count_Hot_icon],(250,yMark - 20))
                Count_Hot_icon += 1
            elif data_to_use[Count]['main']['temp'] > 77:
                Intermediate.blit(data_list[4][Count_VeryHot_icon],(250,yMark - 20))
                Count_VeryHot_icon += 1
            elif data_to_use[Count]['main']['temp'] <68 and data_to_use[Count]['main']['temp'] >50:
                Intermediate.blit(data_list[5][Count_Cold_icon],(250,yMark - 20))
                Count_Cold_icon += 1 
            elif data_to_use[Count]['main']['temp'] <= 50:
                Intermediate.blit(data_list[6][Count_freezing_cold_icon],(250,yMark - 20))
                Count_freezing_cold_icon +=1
            Count_dates += 1
            Count += 1
    
    screen.blit(Intermediate,(0,scroll_y))



    pygame.display.update()
