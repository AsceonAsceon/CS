import pyglet
window = pyglet.window.Window(width = 1000, height = 540)
import engine

def load_images():    
    bg  = pyglet.image.load('bg.png')
    bg1 = pyglet.sprite.Sprite(bg)
    bg1.position = (0 ,0)
    bg1.draw()

def dlabel2(listvoiceclips):
    for i in range(len(listvoiceclips)):
        if i < 14:
            label2 = pyglet.text.Label('',
                        font_name='Times New Roman', 
                        font_size=24,
                        color = (0,0,0,255),
                        x = window.width - 990, y=window.height - 36 - 36*i)
        else:
            label2 = pyglet.text.Label('',
                        font_name='Times New Roman', 
                        font_size=24,
                        color = (0,0,0,255),
                        x = window.width - 680, y=window.height - 36 - 36*(i-14))
        label2.text = '{}'.format(listvoiceclips[i])
        label2.draw()

def dlabel4(recordlist):
    for i in range(len(recordlist)):
        label4 = pyglet.text.Label('',
                        font_name = 'Times New Roman',
                        font_size = 16,
                        x = window.width - 360, y=window.height - 24 - 24*i)
        label4.text = '{}'.format(recordlist[i])
        label4.draw()
        
def dlabel5():
    masterlist = engine.generate_masterlist()
    for i in range(len(masterlist)):
        label5 = pyglet.text.Label('',
                        font_name = 'Times New Roman',
                        font_size = 16,
                        x = window.width - 120, y=window.height - 24 - 24*i)
        label5.text = 'record {}'.format(i + 1)
        label5.draw()

def dlabels():
    label6 = pyglet.text.Label('save to records',
                    font_name='Times New Roman', 
                    font_size=12,
                    bold = True,
                    color = (0,0,0,255),
                    x = window.width - 120, y = window.height - 500)

    label7 = pyglet.text.Label('exit',
                    font_name='Times New Roman', 
                    font_size=12,
                    bold = True,
                    color = (0,0,0,255),
                    x = window.width - 60, y = window.height - 520)

    label8 = pyglet.text.Label('  play',
                    font_name='Times New Roman', 
                    font_size=12,
                    bold = True,
                    color = (0,0,0,255),
                    x = window.width - 120, y = window.height - 520)
    label6.draw()
    label7.draw()
    label8.draw()
