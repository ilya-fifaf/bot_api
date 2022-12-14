import telebot
from telebot import types
import paramiko


bot = telebot.TeleBot("TOKEN")


def ssh(command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('ip', username='user', password='password', banner_timeout=200)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command(command)
    return [ssh_stdin, ssh_stdout, ssh_stderr]

@bot.message_handler(commands=['start'])
def start (message):
	bot.reply_to(message, "Your text")

@bot.message_handler(content_types=['text'])
def sus (message):
    if message.text == "Disable server":
        ssh("interface ipip disable ipip-tunnel-gs")
    if message.text == "Enable server":
        ssh("interface ipip enable ipip-tunnel-gs")
bot.infinity_polling()