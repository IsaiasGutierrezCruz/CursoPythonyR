from helper import gsheet_helper
from telegram.ext import Updater, CommandHandler, updater
from cfg import TOKEN

gsconn = gsheet_helper()

def start(update, context):
    user_dic = {
            'id': update.message.from_user.id,
            'first_name': update.message.from_user.first_name,
            'is_bot': update.message.from_user.is_bot,
            'last_name': update.message.from_user.last_name,
            'username': update.message.from_user.username,
            'language_code': update.message.from_user.language_code
    }

    gsconn.store_user(user_dic)

    saludos = f"""
    Hola {user_dic["username"]}! Esta es tu tienda de electronicos preferida!
    /stock te dice el stock actual de la tienda!
    """

    update.message.reply_text(saludos)

def stock(update, context):
    items = gsconn.get_items()
    update.message.reply_text(f"{items}")

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("stock", stock))

    # iniciar el bot
    updater.start_polling()

    # para que se quede esperando 
    updater.idle()

if __name__ == "__main__":
    main()

