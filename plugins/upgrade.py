"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited 
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd ```9207590890@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Nived_1_0_1")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://p.paytm.me/xCTH/02bzrs6p"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/02bzrs6p")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 1231  🇮🇳/🌎 15$  per Year 
	
	**VIP 2 **
	Daily Upload limit Unlimited
	Price Rs  2051  🇮🇳/🌎 25$  per Year
	
	
	Pay Using Upi I'd ```9207590890@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Nived_1_0_1")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://p.paytm.me/xCTH/02bzrs6p"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/02bzrs6p")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
