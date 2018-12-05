import pyglet
import engine
from pyglet.window import mouse
player = pyglet.media.Player()
import sys
import interface

window = pyglet.window.Window(width = 1000, height = 540)
recordlist = []
masterlist = engine.generate_masterlist()
listvoiceclips = engine.listvc()

@window.event
def on_draw():
    window.clear()
    interface.load_images()
    interface.dlabel2(listvoiceclips)
    interface.dlabel4(recordlist)
    interface.dlabel5()
    interface.dlabels()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global masterlist
    if button == mouse.LEFT:
        if x > 0 and x < 300:
            if y > 540 - 36*(len(listvoiceclips)):
                for i in range(len(listvoiceclips)):
                    if y < 540 - 36*i and y > 540 - 36*(i+1):
                        engine.play_sound(listvoiceclips[i])
                        
        elif x > 320 and x < 620: 
            if y > 540 - 36*(len(listvoiceclips)-14):
                for i in range(13, len(listvoiceclips)):
                    if y < 540 - 36*(i-14) and y > 540 - 36*(i-13):
                        engine.play_sound(listvoiceclips[i])
                        
        elif x > 620 and x < 855:
            if y > 540 - 24*(len(recordlist)):
                for i in range(len(recordlist)):
                    if y < 540 - 24*i and y > 540 - 24*(i+1):
                        engine.play_sound(recordlist[i])

        if x > 855:
            masterlist = engine.generate_masterlist()
            if y > 540 - 24*(len(masterlist)):
                for i in range(len(masterlist)):
                    if y < 540 - 24*i:
                        recordlist2 = masterlist[i]
                engine.play_record(recordlist2)
            elif y < 40:
                if x > 930:
                    sys.exit()
                else:
                    engine.play_record(recordlist)
            elif y < 60:
                if len(masterlist) < 16:
                    masterlist.append(recordlist)
                    engine.record_to_txt(masterlist)
                    interface.dlabel5()
                    recordlist.clear()
                
    elif button == mouse.RIGHT:
        if len(recordlist) < 22:
            if x > 0 and x < 300:
                if y > 540 - 36*(len(listvoiceclips)):
                    for i in range(len(listvoiceclips)):
                        if y < 540 - 36*i:
                            sound = listvoiceclips[i]
                    recordlist.append(sound)
                    interface.dlabel4(recordlist)
                
            elif x > 320 and x < 620:
                if y > 540 - 36*(len(listvoiceclips)-14):
                    for i in range(13, len(listvoiceclips)):
                        if y < 540 - 36*(i-14):
                            sound = listvoiceclips[i]
                    recordlist.append(sound)
                    interface.dlabel4(recordlist)            
                                
            elif x > 620 and x < 855:
                if y > 540 - 24*(len(recordlist)):
                    for i in range(len(recordlist)):
                        if y < 540 - 24*i:
                            index = i
                    del recordlist[index]
                    interface.dlabel4(recordlist)

            if x > 855:
                if y > 540 - 24*(len(masterlist)):
                    for i in range(len(masterlist)):
                        if y < 540 - 24*i:
                            index = i
                    del masterlist[index]
                    engine.record_to_txt(masterlist)
                    interface.dlabel5()
                    
pyglet.app.run()
