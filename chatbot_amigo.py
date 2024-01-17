from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import logging

class ChatBotAmigable:
    def __init__(self):
        # Crear una nueva instancia de ChatBot
        self.chatbot = ChatBot(
            "AmigoBot",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3'
        )

        # Configurar la respuesta por defecto en caso de no saber qué responder
        self.chatbot.default_response = 'Lo siento, no entiendo la pregunta. ¿Puedes formularla de otro modo?'
        self.chatbot.maximum_similarity_threshold = 0.90

        # Crear un nuevo entrenador para el bot
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train("chatterbot.corpus.english")

        # Entrenador personalizado con mis propias conversaciones
        personal_trainer = ListTrainer(self.chatbot)
        personal_trainer.train([
            "Hola",
            "¡Hola! ¿Cómo puedo ayudarte?",
            "¿Cuál es tu nombre?",
            "Me llamo AmigoBot, soy un bot de chat creado para ayudarte."
        ])

    def obtener_respuesta(self, mensaje):
        # Obtener una respuesta a la entrada del usuario
        respuesta = self.chatbot.get_response(mensaje)
        return respuesta

# Configurar el registro de ChatterBot 
logging.basicConfig(level=logging.INFO)

# Crear una nueva instancia del bot
bot = ChatBotAmigable()

# Interfaz de consola para interactuar con el bot
print("ChatBotAmigable (escribe 'salir' para terminar)")
while True:
    try:
        usuario_input = input("Tú: ")
        if usuario_input.lower() == 'salir':
            break
        respuesta = bot.obtener_respuesta(usuario_input)
        print(f"AmigoBot: {respuesta}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
