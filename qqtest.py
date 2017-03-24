from qqbot import QQBotSlot as qqbotslot,RunBot
from random import randint
import juheapi

@qqbotslot
def onQQMessage(bot, contact, member, content):
	if '@ME' in content:
		# //拿取回答答案
		wenti = content.split('[@ME]')[-1]
		daan = juheapi.main(wenti)
		bot.SendTo(contact,'@'+member.name+"  "+daan)
	elif '@' in content and '光' in content:
		wenti = content.split('光')[-1]
		daan = juheapi.main(wenti)
		bot.SendTo(contact,'@'+member.name+"  "+daan)

RunBot()