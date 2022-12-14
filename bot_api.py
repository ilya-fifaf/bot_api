import telebot
from telebot import types
import paramiko


bot = telebot.TeleBot("TOKEN") #"TOKEN" заменить на свой токен

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="ip", username="user", password="password",look_for_keys=False, allow_agent=False)
ssh = client.invoke_shell()
transport=client.get_transport()
channel = transport.open_session()
@bot.message_handler(commands=['start'])
def start (message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	v1 = types.KeyboardButton("Выключить сервер")
	markup.add(v1)
	bot.reply_to(message, "КУ", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def sus (message):
    if message.text == "Выключить сервер":
        stdin, stdout, stderr = ssh.exec_command("ipip-tunnel-gs link down")
    if message.text == "Включить сервер":
        stdin, stdout, stderr = ssh.exec_command("interface ipip enable ipip-tunnel-gs")
ssh.close()
bot.infinity_polling()