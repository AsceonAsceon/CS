# CS
First few programs :D
this is written as one of the prereqs in our subject CS 11 (o u o)
We don't know how to create buttons using pyglet sa we just stuck with making each pixel of the interface somewhat like a button
e.g.: if button == mouse.LEFT:
        if x > 0 and x < 300:
            if y > 540 - 36*(len(listvoiceclips)):
                for i in range(len(listvoiceclips)):
                    if y < 540 - 36*i and y > 540 - 36*(i+1):
                        engine.play_sound(listvoiceclips[i])
