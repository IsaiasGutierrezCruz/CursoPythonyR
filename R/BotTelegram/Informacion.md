# Bot de telegram 
## Creación del Bot de telegram 
- En primer lugar es necesario que tengas un cuenta en telegram. Posteriormente es necesario dirigirse al usuario "@BotFather". Una vez dentro del chat de este Bot Padre, envia el siguiente comando: `\newbot`
- Una vez ejecutado el paso anterior te pedirá ingresar el nombre que quieres colocar a ese bot
- Por ultimo será necesario que agregues un user name para el bot
- Como resultado obtendrás un mensaje en el cual esta contenido un TOKEN con la siguiente forma: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

## Interacción con el bot de telegram
Para nosotros interactuar con el bot de telegram haremos uso de peticiones HTTPS. Esto quiere decir que estaremos interactuando a través de el navegador. De acuerdo a diferentes URL's podremos hacer varias acciones que afecten a nuestro bot. Si ingresamos al siguiente enlace obtendremos información de nuestro chatbot: `https://api.telegram.org/bot<your-bot-token>/getMe`
La información obtenida se encuentra en un formato llamdo JSON. 

### Recibir un mensaje del bot 
Para recibir un mensaje que un usuario haya enviado a nuestro chatbot, podemos acceder a la siguiente dirección: `https://api.telegram.org/bot<your-bot-token>/getUpdates`
Para poder ver la información, antes de acceder al enlace tienes que enviar tu primer mensaje a tu bot. 

## El paquete telegram.bot
Este paquete se encarga de hacer las peticiones HTTPS de manera más sencilla, sin tener que interectuar directamente con las direcciones URL. 
Para usar este paquete es necesario instalarlo con la declaración `install.packages("telegram.bot")`

Cuando se cree el bot, es util colocar el token como una variable de ambiente en el archivo `.Renviron`. Para modificar este archivo es necesario ejectuar la siguiente linea en la terminal `file.edit(path.expand(file.path("~", ".Renviron")))`

Cuando abra este archivo, coloca lo siguiente: `R_TELEGRAM_BOT_<nombre de tu bot sin espacios>=<TOKEN>`
