from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
အိမ်း
"""
    HELP_TEXT = """
<b><u>ဖိုင် (သို့) ဗီဒီယိုအဖြစ် တင်ရန်</u></b>
➠ တိုက်ရိုက်လင့် ပို့ပေးရုံပဲ

<b><u>Thumbnail ထည့်ရန်</u></b>
➠ ကြိုက်တဲ့ပုံပို့ပေး.. တစ်သက်လုံးသိမ်းထားပေးမယ် 😁

<b><u>Thumbnail ဖျက်ရန်</u></b>
➠ /delthumb လို့ ပို့လိုက်

<b><u>အခု ထည့်ထားတဲ့ Thumbnail ကို ပြန်ရန်</u></b>
➠ /showthumb လို့ ပို့လိုက်

© Channel+ @ChannelPlusUsers
"""
    ABOUT_TEXT = """
- **Bot :** URL Uploader
- **Creator :** [Mrk](https://t.me/LoneWolfCNPlus)
- **Channel :** [MoTech](https://t.me/ChannelPlusUsers)
- **Credits :** `Channel+`
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel+', url='https://t.me/ChannelPlusUsers'),
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel+', url='https://t.me/ChannelPlusUsers'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel+', url='https://t.me/ChannelPlusUsers'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>ဘာ format နဲ့ တင်မလဲ 🤔:</b> <a href='{}'>ဖိုင်ဆိုဒ်ကတော့ အတိအကျ ဖြစ်ချင်မှ ဖြစ်မယ်</a>"""
    CHECKING_LINK = "<code>လင့်ကို တစ်ချက်ကြည့်မယ်</code>⏳"
    BANNED_USER_TEXT = "<code>သွား လာမသုံးနဲ့</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """အကောင့်ဝင်ပြီး ဒေါင်းရတဲ့လင့်တွေဆိုရင် ဒီလိုပို့:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>ဒေါင်းနေပြီ...⏳</code>"    
    UPLOAD_START = "<code>တင်နေပြီ...⚡️</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = " {} စက္ကန့် အတွင်း ဒေါင်းလို့ ပြီးပါတယ် \n\n{} စက္ကန့် အတွင်း တင်လို့ ပြီးပါတယ်"
    RCHD_TG_API_LIMIT = "{} စက္ကန့်အတွင်း ဒေါင်းလို့ ပြီးပါတယ်\nတွေ့ရှိသော ဖိုင်ဆိုဒ်: {}\nTelegram မှာ 2GB ထက် ကျော်ပြီးတော့ တင်လို့မရပါ"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>ဘိ.. ဘော့.. ဘု.. တစ်ခုခုတော့ ချို့ယွင်းနေပီ</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Channel ကို မ join ပဲ လာမသုံးနဲ့ သွား 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
