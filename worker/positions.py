import os
import pyautogui


pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

print('Для выхода используйте <Ctrl+C>')

try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)

except:
    os.system('clear')
    print('программа завершена')