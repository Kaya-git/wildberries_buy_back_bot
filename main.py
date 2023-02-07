import pyautogui
from string import ascii_letters


class Buy:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value


class BuyBackBot:
    # WB = ['WB', 'wb', 'wildberries', 'ВБ', 'вб', 'валдбериз']
    # OZON = ['OZON', 'ОЗОН', 'ozon', 'озон']
    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()
    WBPICTURES = {
        "cell_icon": "cell_icon", # нужно прописать пути к картинкам
        "log_in_tab": "log_in_tab",
        "log_on_num": "log_on_num",
        "search_icon": "search_icon",
        "search_tab": "search_tab",
        "delay": "delay",
        "buy_now_tab": "buy_now_tab",
        "order_button": "order_button",
    }

    def __init__(
            self,
            search_word,
            prod_card_pic,
            # market_name
            ):

        self.buy = search_word, prod_card_pic
        # self.__market_name = market_name

    # @classmethod
    # def __check_market_name(cls, market_name):
    #     if market_name in cls.WB:
    #         cls.__market_name = 'wb'
    #     if market_name in cls.OZON:
    #         cls.__market_name = 'ozon'
    #     else:
    #         raise ValueError("Такого магазина нет в списке")

    @classmethod
    def verify_search_word(cls, search_word):
        if type(search_word) != str:
            raise TypeError("Поисковое слово должно быть строкой")
        
        words = search_word.split()
        if len(words) < 1:
            raise TypeError("неверный формат")
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for letter in words:
            if len(letter) < 1:
                raise TypeError("Должен быть хотя бы один символ")
            if len(letter.strip(letters)) != 0:
                raise TypeError("Можно использовать только буквенные символы и дефис")

    # Необходимо добавить загрузку картинок для проверки
    # @classmethod
    # def check_if_prod_card_pic_added(cls, prod_card_pic):
    #     if prod_card_pic not in 'папка с файлами':
    #         raise TypeError("Картинка не добавлена")

    def __del__(self):
        print(f'Удаление экземпляра: {str(self)}')

    def _turn_on(self):
        """
        Запускаем магаз и логинимся
        """
        pyautogui.click(self.WBPICTURES["cell_icon"])
        pyautogui.click(self.WBPICTURES["log_in_tab"])
        pyautogui.click(self.WBPICTURES["log_on_num"])

    def _search_by_word(self):
        """
        Выходим на вкладку поиска товара и находим списки с необходимым товаром
        """
        pyautogui.click(self.WBPICTURES["search_icon"])
        pyautogui.click(self.WBPICTURES["search_tab"])
        pyautogui.typewrite(self.__search_word, self.WBPICTURES["delay"])
        pyautogui.press('enter')

    def _locate_my_prod(self):
        """
        Находим необходимый продукт по картинке, либо скролим дальше
        """
        while True:
            try:
                pyautogui.click(self.__shop_picture)
                break
            except:
                pyautogui.scroll(2)
    
    def _buy_now(self):
        """Совершаем выкуп"""
        pyautogui.click(self.WBPICTURES["buy_now_tab"])
        pyautogui.click(self.WBPICTURES["order_button"])
  
    @property
    def buy(self):
        self._turn_on()
        self._search_by_word()
        self._locate_my_prod()
        self._buy_now()
        return f' успешно выкуплен'
    
    @buy.setter
    def buy(self, search_word, prod_card_pic):#market_name):
        self.verify_search_word(search_word)
        # self.__market_name = market_name
        self.__search_word = search_word
        self.__prod_card_pic = prod_card_pic

    @buy.deleter
    def buy(self):
        del self.__search_word
        # del self.__market_name
        del self.__prod_card_pic


if __name__ == '__main__':
    print_screens_for_bot = []
    wb_bot = BuyBackBot()
    wb_bot.buy(search_word='Print category name', prod_card_pic='Path to the product card pic')#, market_name='Print name of the market')
    print(wb_bot.buy)