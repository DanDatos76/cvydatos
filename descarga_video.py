import pafy 
import os 
import msvcrt


#Para DOS/Windows
os.system ("cls")
print("    ")
print("-----------------------------------------------------")
print("*****************************************************")
print("*****************************************************")
print("    ")
print("     SOFTWARE PARA DESCARGA DE VIDEOS ")
print("         Apps de Terminal Dan   ")
print("*****************************************************")
print("*****************************************************")
print("-----------------------------------------------------")
print("    ") 
print("    ") 
print("    ") 






link = input("por favor ingrese el link de su descarga:    ")


#URL

download_url = input(link)
video = pafy.new(link)
print("    ")

print("    ")
print("")
print("")
print("    ") 
streams = video.streams
 
for i in streams:
        print(i)
print("")
print("")
print("    ") 
#Mejor resolucion
best = video.getbest()
print(best.resolution, best.extension)
print("")
#Descarga - Directorio

best.download(filepath="video5")

print("renombre el archivo agregando  el formato mp4")
print("Video descargado correctamente...") 
print("")
print("")
print("    ") 


print("Presione una tecla para continuar...")
msvcrt.getch()
print("")
print("-----------------------------------------------------")
print("*****************************************************")
print("GRACIAS POR UTILIZAR NUESTRO ASISTENTE")   
print("*****************************************************")
print("-----------------------------------------------------")
saySomething("gracias por utilizar nuestro asistente")


print("-----------------------------------------------------")



print("     ****   ****  "  )
print("    *****   ***** "  )
print("     ***** *****  "  )
print("      *********  "  )
print("         *** "  )
print("          * "  )
