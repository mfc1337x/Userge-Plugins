import re

from userge import userge, Message, filters

bios = ['@date4ubot', '@sex24bot', '@sex4ubot']
triggers = ["boring", "@date4ubot", "bored", "wanna chat", "horny",
  "wanna sex", "sex chat", "I want sex chat", "any boy wanna sex"]


async def is_admin(msg: Message, user_id: int) -> bool:
  strings = ["creator", "administrator"]
  admin = (await msg.client.get_chat_member(msg.chat.id, user_id)).status
  return admin in strings


@userge.on_filters(
    filters.group & filters.incoming & ~filters.edited, group=1, check_restrict_perm=True)
async def manage_spammers(msg: Message):
  user = msg.from_user
  bio = (await msg.client.get_chat(user.id)).bio
  for trigger in bios:
    pattern = r"( |^|[^\w])" + re.escape(trigger) + r"( |$|[^\w])"
    if bio and re.search(pattern, bio, re.IGNORECASE):
      if not await is_admin(msg, user.id):
         await msg.chat.kick_member(user.id)
         await msg.reply("banned")
         return
  for trigger in triggers:
    pattern = r"( |^|[^\w])" + re.escape(trigger) + r"( |$|[^\w])"
    if msg.text and re.search(pattern, msg.text.lower(), re.IGNORECASE):
      if not await is_admin(msg, user.id):
        await msg.chat.kick_member(user.id)
        await msg.reply("banned")


@userge.on_filters(filters.group & filters.new_chat_members, group=1, check_restrict_perm=True)
async def manage_welcomes(msg: Message):
  for user in msg.new_chat_members:
    bio = (await msg.client.get_chat(user.id)).bio
    for trigger in bios:
      pattern = r"( |^|[^\w])" + re.escape(trigger) + r"( |$|[^\w])"
      if bio and re.search(pattern, bio, re.IGNORECASE):
        if not await is_admin(msg, user.id):
          await msg.chat.kick_member(user.id)
          await msg.reply("banned.")
  msg.continue_propagation()
