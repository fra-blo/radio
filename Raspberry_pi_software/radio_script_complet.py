import serial
import time
import os

current_lang = 0
current_radio = 0
current_mode = 0
current_volume = 0
memoire_volume = 0
previous_volume = 0
previous_radio = 0
previous_lang = 0
previous_mode = 0

#time.sleep(20)
ser = serial.Serial("/dev/ttyACM0", timeout=1)

# pour retrouver plein de radios, aller sur le site http://www.surfmusic.de/. Les liens sont dans le code source de la page

radios_fr = ["http://stream.virginradio.fr/virgin.mp3", "http://streaming.radio.funradio.fr/fun-1-44-64?listen=webCwsBCggNCQgLDQUGBAcGBg", "http://streaming.radio.rtl2.fr/rtl2-1-44-64?listen=webCwsBCggNCQgLDQUGBAcGBg", "http://stream.radiotime.com/listen.m3u?streamId=37709159", "http://cdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3?origine=fluxradios", "http://www.skyrock.fm/stream.php/tunein16_64mp3.mp3"]
radios_es = ["https://atlantisfm.radionetz.de/atlantisfm.mp3", "http://www.surfmusic.de/m3u/radio-4,7795.m3u", "http://www.surfmusic.de/m3u/dale-fm,21236.m3u", "https://alziraradiomob.streaming-pro.com:6172/alziraradio.mp3", "https://ssl1.viastreaming.net:7120/", "http://5.135.183.124:8207/stream"]
radios_de = ["http://80.237.156.8:4000", "https://stream.laut.fm/rap", "https://stream.laut.fm/kawedeoldiesradio", "https://stream.laut.fm/deutschrock", "https://stream.laut.fm/hitradio-deutschland-eins", "http://178.32.137.180:8731/;stream/1"]
radios_it = ["http://94.23.66.155:9200/;stream/1", "http://37.187.79.93:8634/;stream/1", "http://stream11.shoutcastsolutions.com:8017/autodj", "http://188.165.212.154:8048/;stream/1", "http://212.83.138.48:8324/;stream/1", "https://stream.laut.fm/radioazzurra"]
radios_en = ["http://www.surfmusic.de/m3u/solar-fm,1965.m3u", "http://www.surfmusic.de/m3u/pirate-fm,9387.m3u", "http://www.surfmusic.de/m3u/jack-radio-uk,19935.m3u", "http://www.surfmusic.de/m3u/key-103,1061.m3u", "http://www.surfmusic.de/m3u/desi-radio,11932.m3u", "http://www.surfmusic.de/m3u/cheesy-fm,19021.m3u"]

while True:
    
    ser.write(b"status\n")
    time.sleep(0.5)
    retours = []
    retours.append(ser.readline().decode("utf-8")[:-2])
    retours.append(ser.readline().decode("utf-8")[:-2])
    retours.append(ser.readline().decode("utf-8")[:-2])
    retours.append(ser.readline().decode("utf-8")[:-2])
    #print(retours)
    

    for retour in retours:
        if "lan" in retour:
            current_lang = int(retour[-1])
        if "rad" in retour:
            current_radio = int(retour[-1])
        if "typ" in retour:
            current_mode = int(retour[-1])
        if "vol" in retour:
            try:
                current_volume = 1023 - int(retour[4:])
                print(current_volume)
#                 if previous_volume == 0:
#                     previous_volume = current_volume
#                 if (current_volume < (previous_volume - 50)) | (current_volume > (previous_volume + 50)):
#                     current_volume = previous_volume
#                 else:
#                     previous_volume = current_volume
#                 print(current_volume)
            except:
                pass
            
    #ser.flush()
    #time.sleep(0.5)
            
    #ser.write(b"volume\n")
    #time.sleep(0.1)
    #volume_b = ser.readline()
    #print(volume_b)
    #current_volume = 1023 - int(volume_b.decode("utf-8")[:-2][4:])


    # application du nouveau volume
    os.system("pactl set-sink-volume @DEFAULT_SINK@ " + str(int(0.1 * current_volume + 30)) + "%")
            
    # mode 2 = radio
    if current_mode == 2:
        if (current_radio != previous_radio) | (current_lang!= previous_lang) | (previous_mode != current_mode):
            #print("mode_radio")
            ser.write(b"lumiere\n")
            os.system("cvlc --one-instance /home/pi/Downloads/transition.mp3 &")
            time.sleep(2)
            previous_radio = current_radio
            previous_lang = current_lang
            previous_mode = current_mode
            if current_lang == 1:
                os.system("cvlc --one-instance " + radios_fr[current_radio-1] + " &")
            if current_lang == 2:
                os.system("cvlc --one-instance " + radios_es[current_radio-1] + " &")
            if current_lang == 3:
                os.system("cvlc --one-instance " + radios_de[current_radio-1] + " &")
            if current_lang == 4:
                os.system("cvlc --one-instance " + radios_it[current_radio-1] + " &")
            if current_lang == 5:
                os.system("cvlc --one-instance " + radios_en[current_radio-1] + " &")

    if current_mode == 3:
        #print("mode_bluetooth")
        previous_mode = current_mode
        os.system("killall vlc")
        #os.system("kill -9 $(pgrep vlc)")
        time.sleep(0.5)
