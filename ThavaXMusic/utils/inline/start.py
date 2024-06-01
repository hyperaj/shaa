from pyrogram.types import InlineKeyboardButton

import config
from ThavaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𓆩♡𓆪 ᴀᴅᴅ ᴍᴇ 𓆩♡𓆪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𓆩♡𓆪 ʜᴇʟᴘ 𓆩♡𓆪", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𓆩♡𓆪 ɴᴇᴛᴡᴏʀᴋ 𓆩♡𓆪", url=f"https://t.me/Team_Hypers_Networks"),
            InlineKeyboardButton(text="𓆩♡𓆪 ᴜᴘᴅᴀᴛᴇ 𓆩♡𓆪", url=f"https://t.me/Hyper_networks_updates"),
        ],
        [
            InlineKeyboardButton(text="𓆩♡𓆪 ᴏᴡɴᴇʀ 𓆩♡𓆪", url=f"https://t.me/healer_selvaa"),
            InlineKeyboardButton(text="𓆩♡𓆪 Dᴇᴠᴇʟᴏᴘᴇʀ 𓆩♡𓆪", url=f"https://t.me/King_0f_izzy"),
        ],
    ]
    return buttons
