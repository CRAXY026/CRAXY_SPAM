from CRAXYSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from CRAXYSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/29728c17f73d73bdc3da3.jpg"

CRAXY_Help = "🔥 Cʀᴀxʏ Sᴘᴀᴍ Bᴏᴛ 🔥\n\n"
 
CRAXY_Help += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴄʀᴀxʏ ʙᴏᴛ__\n\n"

CRAXY_Help += f" ↧ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧\n\n"

CRAXY_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
CRAXY_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

CRAXY_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
CRAXY_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

CRAXY_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

CRAXY_Help += f" !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

CRAXY_Help += f"© @CRAXYMARRK\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=KAKA_Help,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/marrkmusic"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/CRAXYMARRK")
        ] 
        ]
        )
