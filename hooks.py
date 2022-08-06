from imports import KeyboardButton, dp, Text
from types import MethodType
def kb_set_event(self, event):
    dp.register_message_handler(event, Text(equals=self.text, ignore_case=True))
    return self
KeyboardButton.set_event = kb_set_event

