from telegram.ext import Updater
from telegram.error import TimedOut
from telegram.ext import Updater

class Telegram:

    def __init__(
        self,
        chat_code: int, 
        token: str
        ) -> None:
        
        assert (chat_code != "TELEGRAM_CHAT_ID"), "Need the Chat code parameter." 
        assert (token != "TELEGRAM_TOKEN"), "Need the Token ID parameter."
        
        self.chat_code = chat_code 
        self.token = token 
        self.updater = Updater(self.token)

    def send_message(self, message: str) -> None:

        try:
            self.updater.bot.send_message(self.chat_code, text=message)
        except TimedOut as te:
            print(te.message)
    