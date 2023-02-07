import pyautogui
from string import ascii_letters


class Buy:

    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

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

    def __set_name__(self, owner, name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_search_word(value)
        setattr(instance, self.name, value)


class BuyBackBot:
    
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

    search_word = Buy()
    prod_card_pic = Buy()

    def __init__(
            self,
            search_word,
            prod_card_pic,
            ):

        self.search_word = search_word
        self.prod_card_pic = prod_card_pic


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


if __name__ == '__main__':
    print_screens_for_bot = []
    wb_bot = BuyBackBot('фонарик', 'фонарик')
    print(wb_bot.search_word)