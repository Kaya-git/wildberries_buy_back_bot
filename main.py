import pyautogui
from abc import ABC, abstractmethod


if __name__ == '__main__':

    def click_on_wb_app(x: float, y: float):
        pyautogui.click(x, y)

    def click_on_wb_search_tab(x: float, y: float):
        pyautogui.click(x, y)
    
    def go_to_searching_product_list(text: str, interval: float):
        pyautogui.typewrite(text, interval)
        pyautogui.press('enter')
    
    def make_a_print_screen():
        