# -*- coding: utf-8 -*-
import os 
import msvcrt
import  wget



os.system ("cls")


#DESCARGA DEL ARCHIVO CSV

url = input("ingresa url del video")



wget.download(url, "video1")