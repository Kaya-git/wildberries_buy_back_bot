from aiogram.types import CallbackQuery


async def go_to_balance(callback: CallbackQuery) -> None:
    """
    Обрабатываем команду просмотра баланса
    """

    await callback.answer(
        show_alert=True,
        text='Твой баланс на текущий момент равено 0.'
    )


async def go_to_stat(callback: CallbackQuery) -> None:
    """
    Обрабатываем команду статистики
    """

    await callback.answer(
        show_alert=True,
        text='Тут мы выведем таблицу с историей твоих выкупов.'
    )


async def go_to_prices(callback: CallbackQuery) -> None:
    """
    Вывести цены
    """

    await callback.answer(
        show_alert=True,
        text='Цена одного выкупа составляет 70 руб'
    )
