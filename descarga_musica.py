import pafy  
  
download_url = input("URL de la cancion: ")
video = pafy.new(download_url) 
  
audiostreams = video.audiostreams 
for i in audiostreams: 
    print(i.bitrate, i.extension, i.get_filesize()) 
  
audiostreams[1].download() 