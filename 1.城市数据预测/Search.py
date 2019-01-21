import re

import pandas as pd
import requests


def searchImage(ID, key):
    """

    :param ID: The searching ID specified by yourself
    :param key: Google API Key, In this example, it is ID[0]-City, ID[1]-Country provided by the .csv file.
    """

    print(ID[2])
    for i in [2, 3]:
        ID[i] = re.sub('/', '', ID[i])
        # use \\ to avoid dangling metacharacter
        ID[i] = re.sub('\\?', '', ID[i])
        ID[i] = re.sub(' ', '', ID[i])
        ID[i] = re.sub('\r', '', ID[i])
        ID[i] = re.sub('\n', '', ID[i])
    image_backgroud_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + ID[2] + ',' + ID[
        3] + '&zoom=10&format=png&maptype=roadmap&style=feature:road|visibility:off&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=' + key
    image_road_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + ID[2] + ',' + ID[
        3] + '&zoom=10&format=png&maptype=roadmap&style=visibility:off&style=feature:road|visibility:on&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=' + key
    image_roadmap_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + ID[2] + ',' + ID[
        3] + '&zoom=10&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=' + key
    image_satellite_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + ID[2] + ',' + ID[
        3] + '&zoom=10&format=png&maptype=satellite&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=' + key
    satellite = requests.get(image_satellite_url)
    backgroud = requests.get(image_backgroud_url)
    road = requests.get(image_road_url)
    roadmap = requests.get(image_roadmap_url)
    with open("./ImageSet/Background/" + str(ID[0]) + ".background_" + str(ID[2]) + ".png", "wb") as f:
        f.write(backgroud.content)
    with open("./ImageSet/Road/" + str(ID[0]) + ".road_" + str(ID[2]) + ".png", "wb") as f:
        f.write(road.content)
    with open("./ImageSet/RoadMap/" + str(ID[0]) + ".roadmap_" + str(ID[2]) + ".png", "wb") as f:
        f.write(roadmap.content)
    with open("./ImageSet/Satellite/" + str(ID[0]) + ".satellite_" + str(ID[2]) + ".png", "wb") as f:
        f.write(satellite.content)


def searchInRange(dataFile, idxS, idxE):
    for i in range(idxS, idxE):
        searchImage(dataFile[i])


# My Multi-threading
import threading


def threadAccelerate(datapath, operation, numThread):
    if operation == 'searchGoogle':
        data = pd.read_csv(datapath).values
        ThreadStart = True
        if ThreadStart:
            thread_size = numThread
            thread_length = len(data) // thread_size
            count = 0
            threadList = []
            print(thread_length)
            for i in range(thread_size + 1):
                newThread = threading.Thread(target=searchInRange,
                                             args=(data, count, min(count + thread_length, len(data)),))
                count += thread_length
                newThread.start()
                threadList.append(newThread)
            for i in range(thread_size):
                threadList[i].join()
            print("Done")


# 60 is ok for 16G memory and 4700K.
threadAccelerate('./Data/OldData/PopulationLatitudeLongitudeNoKorea.csv', 'searchGoogle', 60)
