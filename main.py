import pyautogui


class BuyBackBot:
    BUY_BACK = True

    @classmethod
    def check_if_buy_now(cls, buy_back: bool) -> bool:
        return cls.BUY_BACK != buy_back
    
    @classmethod
    def check_market_name(cls, market_name):
        return market_name == 'wb'

    def __init__(
            self,
            buy_back,
            icon,
            log_in_tab,
            log_on_num,
            search_icon,
            search_tab,
            look_up_prod,
            delay,
            shop_picture,
            buy_now_tab,
            order_button,
            add_to_bin_pic,
            prod_name,
            prod_picture_name
            ):
        if self.check_if_buy_now(buy_back):
            self.BUY_BACK = False
        self.__icon = icon
        self.__log_in_tab = log_in_tab
        self.__log_on_num = log_on_num
        self.__search_icon = search_icon
        self.__search_tab = search_tab
        self.__look_up_prod = look_up_prod
        self.__delay = delay
        self.__shop_picture = shop_picture
        self.__buy_now_tab = buy_now_tab
        self.__order_button = order_button
        self.__add_to_bin_pic = add_to_bin_pic
        self.__prod_name = prod_name
        self.__prod_picture_name = prod_picture_name

    def __del__(self):
        print(f'Удаление экземпляра: {str(self)}')

    def turn_on(self, icon, log_in_tab, log_on_num):
        """
        Запускаем магаз и логинимся
        """
        pyautogui.click(icon)
        pyautogui.click(log_in_tab)
        pyautogui.click(log_on_num)

    def search_by_prod_name(self):
        """
        Выходим на вкладку поиска товара и находим списки с необходимым товаром
        """
        pyautogui.click(self.search_icon)
        pyautogui.click(self.search_tab)
        pyautogui.typewrite(self.look_up_prod, self.delay)
        pyautogui.press('enter')

    def locate_my_prod(self):
        """
        Находим необходимый продукт по картинке, либо скролим дальше
        """
        while True:
            try:
                pyautogui.click(self.shop_picture)
                break
            except:
                pyautogui.scroll(2)
    
    def buy_back_or_bin(self, prod_name, ):
        """Совершаем выкуп"""
        if self.buy_now == True:
            pyautogui.click(self.buy_now_tab)
            pyautogui.click(self.order_button)
        else:
            pyautogui.click(self.add_to_bin_pic)

    def set_buy(self, prod_name, prod_picture_name):
        self.__prod_name = prod_name
        self.__prod_picture_name = prod_picture_name
        

    def get_buy(self):
        self.turn_on
        self.search_by_prod_name
        self.locate_my_prod
        self.buy_back_or_bin
        return f''


if __name__ == '__main__':
    print_screens_for_bot = {}
    wb_bot = BuyBackBot()
