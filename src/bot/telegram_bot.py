from telegram.ext import Application
from core.config import ConfigLoader

class TelegramBot:
    def __init__(self):
        config = ConfigLoader()
        self.token = config.get("telegram_bot.token")
        self.app = Application.builder().token(self.token).build()
        # add handlers 
        self.app.add_handler(CommandHandler("start", self.start))
        
    async def start(self, update, context):
        user = update.effective_user
        await update.message.reply_text(f"Hello {user.first_name}! STARS Server is running.")
        
    def run(self):
        self.app.run_polling()