from pynput import mouse

def get_co (x,y):
    print("Now at: {}".format((x,y)))

with mouse.Listener (on_move = get_co) as listen:
    listen.join()