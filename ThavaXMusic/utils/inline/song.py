from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𓆩♡𓆪 ɴᴇᴛᴡᴏʀᴋ 𓆩♡𓆪", url=f"https://t.me/The_Art_Of_Self_Healing",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
