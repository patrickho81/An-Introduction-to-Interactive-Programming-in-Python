# template for "Stopwatch: The Game"
# try to stop the watch on a whole second
import simplegui

# define global variables
time = 0
success = 0
total = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    C = (t // 10) % 10
    B = t // 10 % 60 // 10
    A = t // 600
    return str(A)+":"+ str(B)+str(C)+"."+ str(D)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    global time, success, total
    if time % 10 == 0:
       success += 1
    total += 1
    

def reset():
    global time, success, total
    time = 0
    success = 0
    total = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global time, counter
    canvas.draw_text(format(time), [120,150], 28, "white") 
    canvas.draw_text(str(success)+'/'+str(total), [250,50], 28, "white")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 300)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

