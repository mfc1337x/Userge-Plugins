#Plugin inspired by the Gaali Machine
#Do not touch
#Tere ma gand marale
import asyncio

from userge import userge
import random

LACY_STRINGS = [
  "`Hemu jakar gand mara bsdk`",
  "`backchodi matt kar hemu maa chod denge tumhari`",
  "`Hemu madarchod`",
  "`Hemu ki gand mei ghadhe ka lund`",
  "'Hemu ki biwi chai waale se chudati hai'",
  "'Hemu ki fuddi me thukunga'"
]

NIBBA_STRINGS = [
  "`Abe nibba juznem`",
  "`juznem madarchod`",
  "`juznem mere lund par`",
  "`juznem nibba gandu hai`",
  "`juznem gand marwa kar manega`"
]

DEAD_STRINGS = [
  "`Tumhari insta girl bade paimaane par BBC letee hai`",
  "`Tumhari bndi mujhe se chud rhi hai`",
  "`Dead ka loda chota hai`",
  "`Dead ka insta girl ki fuddi me thukunga`",
  "'Teri insta girl meri malish kar rahi he'",
  "'Dead ki biwi chai waale sai chudati hai'"
]

ABUSE_STRINGS = [
  "`Madharchod`",
  "`Gaandu`",
  "`Chutiya he rah jaye ga`",
  "`Ja be Gaandu`",
  "`Ma ka Bhodsa madharchod`",
  "`mml`",
  "`You MotherFucker`",
  "`Chup ho jaa bosdiwale`"
  "`You Betichod`",
  "`You are lodu no.1`",
  "`Muh Me Lega Bhosdike ?`",
  "`Kya he betichod?`",
  "`Tum ek fuddi ho`",
  "`Abey Ja Na Gandu`",
  "`Randi Ka Bacha`",
  "`Abey Ja Na Madarchod`",
  "`Abey Ja Na Randi`",
  "`Hat bosdike`",
  "`Maaklode gaand maar dunga teri, bosdike`",
  "`Jhaant ka pissu hai tu`",
  "`Jake apni gand marale`",
  "`Aapake pita ek fuddi`",
  "`Group se nikal bhosdike yeha tatti nehi chahiye`",
  "`Apni Maiya Chudale Madarchod`",
  "`Khinaar ki aulaad`",
  "`Bhadwe`",
  "`Tumhaaree maan ek gadhe hai`",
  "`Sale sasti randi ke pille. MADARCHOD`",
  "`Gand me danda de`",
  "`Bhanchod`",
  "`Fuck you bludy bastard bitch`"
]
GEY_STRINGS = [
  "`you gey bsdk`",
  "`you gey`",
  "`you gey in the house`",
  "`you chakka`",
  "`you gey gey gey gey gey gey gey gey`",
  "`you gey go away`",
  "`Tu mach gey`",
]
POTATO_STRINGS = [
  "`Potato gey asf`",
  "`STFU Potato`",
  "`Fuck off Potato`",
  "`Jake apni gand marale`",
  "`Fuddi do apni`",
  "`BC.. Gaand na fulao, maa chod denge tumhari`",
  "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
]
ALONE_STRINGS = [ 
 "`Teri Crush ko chod rha hun`",
 "`Bosdike gaand maar dunga teri",
 "`Chup ho ja lodu`",
 "`Teri Crush ek randi hai`",
 "`Bc tbhi tujhe bhaiyaa bola usne`",
]
@userge.on_cmd("bc$", about = ".bc For Maaki - Plugin Inspired by Krishna")
async def bc_func(message):
	replied = message.reply_to_message
	user_id = replied.from_user.id if replied else message.from_user.id
	user = await userge.get_users(user_id)
	username = user.username
	if username == "juznem":
		gali = random.randint(0, len(NIBBA_STRINGS) - 1)
		reply_gali = NIBBA_STRINGS[gali]
	elif username == "Not_so_dank":
		gali = random.randint(0, len(LACY_STRINGS) - 1)
		reply_gali = LACY_STRINGS[gali]
	elif username == "Alone215":
		gali = random.randint(0, len(ALONE_STRINGS) - 1)
		reply_gali = ALONE_STRINGS[gali]
	elif username == "grave_man":
		gali = random.randint(0, len(DEAD_STRINGS) - 1)
		reply_gali = DEAD_STRINGS[gali]
	else:
		gali = random.randint(0, len(ABUSE_STRINGS) - 1)
		reply_gali = ABUSE_STRINGS[gali]
	await message.edit(reply_gali)

@userge.on_cmd("gey$", about = ".gey for gey - Plugin Inspired by Anime dudes")
async def gey_func(message):
		strGey = random.randint(0, len(GEY_STRINGS) - 1)
		#input_str = event.pattern_match.group(1)
		reply_text = GEY_STRINGS[strGey]
		await message.edit(reply_text)

@userge.on_cmd("aaloo$", about = ".aaloo for Potato sar - Thank you POF, Bhanchod")
async def pot_func(message):
		strPot = random.randint(0, len(POTATO_STRINGS) - 1)
		#input_str = event.pattern_match.group(1)
		reply_text = POTATO_STRINGS[strPot]
		await message.edit(reply_text)
