library(telegram.bot)

updater <- Updater(token = bot_token("botprueba"))

# declarar un comando llamado start
start <- function(bot, update){
    bot$sendMessage(chat_id = update$message$chat_id,
                    text = sprintf("Hola %s!", update$message$from$first_name))
}

start_handler <- CommandHandler("start", start)
updater <- updater + start_handler

# Contestar texto que no es un comando 
echo <- function(bot, update){
    bot$sendMessage(chat_id = update$message$chat_id, text = update$message$text)
}

updater <- updater + MessageHandler(echo, MessageFilters$text)

# agregar un comandos llamado caps para convertir el mensaje del ususario a mayusculas
caps <- function(bot, update, args){
    if (length(args > 0L)){
        text_caps <- toupper(paste(args, collapse = " "))
        bot$sendMessage(chat_id = update$message$chat_id, 
                        text = text_caps)
    }
}

updater <- updater + CommandHandler("caps", caps, pass_args = TRUE)

# contestar a comandos no conocidos 
unknown <- function(bot, update){
    bot$sendMessage(chat_id = update$message$chat_id, 
                    text = "Lo siento, no puedo entender tu comando.")
}

updater <- updater + MessageHandler(unknown, MessageFilters$command)

updater$start_polling()