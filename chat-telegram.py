from telegram.ext import  Application, CallbackQueryHandler,  Updater, CommandHandler, MessageHandler ,ContextTypes , filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, helpers
import joblib
import pandas as pd
import os
import shutil

archivo_a_copiar = os.path.join(os.path.dirname(__file__),'modelo_rendimiento_academico.py')
directorio_destino = f"{joblib.__path__[0]}/"


# Nuevo nombre para el archivo copiado en el destino
nuevo_nombre = 'modelo_rendimiento_academico.pkl'
print(f"...{archivo_a_copiar}")
print(f"...{directorio_destino}")
# Copiar el archivo con un nuevo nombre en el directorio de destino
shutil.copy(archivo_a_copiar, os.path.join(directorio_destino, nuevo_nombre))
# Cargar el modelo entrenado
#modelo_path = os.path.join(os.path.dirname(__file__), 'modelo_rendimiento_academico.pkl')


model = joblib.load("modelo_rendimiento_academico.pkl")
CHECK_THIS_OUT = "check-this-out"
USING_ENTITIES = "using-entities-here"
USING_KEYBOARD = "using-keyboard-here"
SO_COOL = "so-cool"
# Definir la función para manejar el comando /start
async def  start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
     bot = context.bot
     url = helpers.create_deep_linked_url(bot.username, CHECK_THIS_OUT, group=True)
     text = "¡Hola! Soy un bot para predecir el rendimiento académico. Por favor, envía tus calificaciones y promedio anterior.\n" 
     await update.message.reply_text(text)
     #await update.message.reply_text("¡Hola! Soy un bot para predecir el rendimiento académico. Por favor, envía tus calificaciones y promedio anterior.")

# Definir la función para manejar los mensajes de texto
async def predict_score(update, context):

    try:
        # Obtener los datos del mensaje del usuario
        message = update.message.text
        print("..."+message)
        data = [float(x) for x in message.split(" ")]

        # Realizar la predicción con el modelo
        prediction = model.predict([data])
        await update.message.reply_text(f"Tu posible rendimiento académico es: {prediction[0]}")

    except Exception as e:
        await update.message.reply_text("Ha ocurrido un error. Por favor, ingresa tus datos nuevamente.")

# Configurar el token del bot y crear un EventHandler para el bot


#token = "AAG7_g33sZRfoxZ9tqHSes9-gtm3wJM3maM"
token = "6625530086:AAGuYAoQ4P9J5iObJ6VNL46johyeBdEHNV0"

application = Application.builder().token(token).build()

    # More info on what deep linking actually is (read this first if it's unclear to you):
    # https://core.telegram.org/bots/features#deep-linking

    # Register a deep-linking handler
application.add_handler(
        CommandHandler("start",start)

    )
# Manejar los comandos
application.add_handler(CommandHandler("start", start))

# Manejar los mensajes de texto
application.add_handler(MessageHandler(~filters.COMMAND & filters.TEXT, predict_score))

# Iniciar el bot
application.run_polling(allowed_updates=Update.ALL_TYPES)
application.idle()
