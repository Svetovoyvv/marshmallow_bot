from imports import *
from commands import cmd_profile, cmd_order_select_shop, cmd_active_orders


keyboard_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='☕ Сделать заказ').set_event(cmd_order_select_shop),
        KeyboardButton(text='🍽 Активные заказы').set_event(cmd_active_orders)
    ],
    [
        KeyboardButton(text='🦔 Профиль 🦔').set_event(cmd_profile)
    ],
])