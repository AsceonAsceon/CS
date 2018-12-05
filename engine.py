import pyglet
player = pyglet.media.Player()
    
def listvc():
    listvoiceclips = ['amoyulamnabakayo', 'anghirapnitoeh', 'ewankosayoboy',
        'helloeverybody', '-laughs-', 'loveit',  'maygalitpa', 'mgakababayan',
        'kababayanamoyulam', 'mygod', 'mygodwatchagonnado',
        'nakakaloka', 'nananahimik', 'nocomment','noimnotpregnant', 'see',
        'sumasagotako', 'wagnayon', 'yes', '\'yon']
    return listvoiceclips

def generate_masterlist():
    file_stream=open('soundrecord.txt','r')
    data = file_stream.read()
    masterlist0 = str.split(data, ',')
    file_stream.close()
    masterlist = []
    for i in masterlist0:
        if i != '':
            temp = str.split(i)
            masterlist.append(temp)
    return masterlist

def record_to_txt(masterlist):
    file_stream=open('soundrecord.txt','w')
    for i in range(len(masterlist)):
        for j in range(len(masterlist[i])):
            if (masterlist[i])[j] != '':
                file_stream.write((masterlist[i])[j] + ' ')
        file_stream.write(',')
    file_stream.close()

class voiceclip:

    def __init__(self, filename):
        global audio
        self.audio = pyglet.media.load(str(filename) + '.wav', streaming=False)
        self.name = filename
        
def get(filename):
    global audio
    audio = pyglet.media.load(str(filename) + '.wav', streaming=False)
    return audio

def play_sound(sound):
    vc = voiceclip(sound)
    vc.audio.play()
    
def play_record(recordlist):
    for filename in recordlist:
        audio = get(filename)
        player.queue(audio)
    player.play()
