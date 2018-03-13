from luis_setter import LuisBotSetter
bot = LuisBotSetter()
result = bot.getTokens('mail')
print (type(result))
print (result)