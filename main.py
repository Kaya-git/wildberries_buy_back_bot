import pyautogui
from abc import ABC, abstractmethod


if __name__ == '__main__':

    def click_on_wb_app(wildberies_icon):
        """Находим приложение вб по картинке"""
        pyautogui.click(wildberies_icon)
        # pyautogui.click(x, y)

    def click_on_wb_search_tab(wb_search_tab):
        """"Находим строку поиска"""
        pyautogui.click(wb_search_tab)
        # pyautogui.click(x, y)
    
    def go_to_searching_product_list(text: str, interval: float):
        """"Забиваем ключевое слово и осуществляем поиск"""
        pyautogui.typewrite(text, interval)
        pyautogui.press('enter')
    
    def locate_product(picture):
        """Находим необходимый продукт по картинке, либо скролим дальше"""
        while True:
            try:
                pyautogui.click(picture)
                break
            except:
                pyautogui.scroll(2)
    
    def add_to_bucket(bucket_picture):
        pyautogui.click(bucket_picture)

    def my_backet_tab_click(my_bucket_pic):
        pyautogui.click(my_bucket_pic)
    
    def get_in_my_acc(my_acc_tab):
        pyautogui.click(my_acc_tab)
    
    def log_in(log_in_tab):
        pyautogui.click(log_in_tab)
    
    def log_in_with_cellphone(cell_num_pic, cell_number):
        pyautogui.click(cell_num_pic)
        pyautogui.typewrite(cell_number)
        pyautogui.press('enter')

    def to_buy_order(buy_order_pic):
        pyautogui.click(buy_order_pic)