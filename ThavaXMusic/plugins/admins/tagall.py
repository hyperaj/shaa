from ThavaXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [" உண்மை END என்றால் முடிவு என்பது முடிவல்ல முயற்சிகள் ஒருபோதும் இறக்காது. ",
           " உலகத்தை மாற்ற நீங்கள் பயன்படுத்தக்கூடிய மிக சக்திவாய்ந்த ஆயுதம் கல்வி. ",
           " ஒருபோதும் தவறு செய்யாத ஒருவர் புதிதாக எதையும் முயற்சித்ததில்லை. ",
           " உங்கள் பாதையில் கடினமான தடைகள் ஏராளமாக உள்ளன. அவற்றில் ஒன்றாக உங்களை அனுமதிக்காதீர்கள். ",
           " என்னால் மட்டுமே என் வாழ்க்கையை மாற்ற முடியும். எனக்காக யாராலும் முடியாது ",
           " என்னால் முடியும் என்று நினைக்கிறேன். என்னால் முடியும் என்று எனக்குத் தெரியும். ",
           " கற்றல் பிழையின்றி ஒருபோதும் தோல்வியடையாது ",
           " உலகில் நீங்கள் காண விரும்பும் மாற்றமாக நீங்கள் இருக்க வேண்டும். ",
           " கடின உழைப்புக்கு ஈடு இணையில்லை." ,
           " வாய்ப்புக்காக காத்திருக்காதீர்கள், உருவாக்குங்கள் ",
           "  ெற்றி என்பது அனைத்து முயற்சிகளின் கூட்டுத்தொகை, மீண்டும் மீண்டும் ஒரு நாள் மற்றும் நாள் முழுவதும். ",
           " வெற்றி பெறுவதற்கான எனது உறுதிப்பாடு போதுமானதாக இருந்தால் தோல்வி என்னை ஒருபோதும் முந்தாது. ",
           " தன்னம்பிக்கை மற்றும் கடின உழைப்பு எப்போதும் உங்களுக்கு வெற்றியைத் தரும். ",
           " நான் உண்மையில் ஒரு ராஜா, ஏனென்றால் என்னை எப்படி ஆள வேண்டும் என்று எனக்குத் தெரியும்.",
           " உங்கள் நேரம் குறைவாக உள்ளது, எனவே வேறொருவரின் வாழ்க்கையை வாழ்ந்து வீணாக்காதீர்கள். மற்றவர்களின் சிந்தனையின் முடிவுகளுடன் வாழும் கோட்பாட்டால் சிக்கிக்கொள்ளாதீர்கள். ",
           " உங்கள் கயிற்றின் முனையை அடைந்ததும், அதில் ஒரு முடிச்சைக் கட்டி தொங்க விடுங்கள். ",
           " நீங்கள் முற்றிலும் தனித்துவமானவர் என்பதை எப்போதும் நினைவில் கொள்ளுங்கள். மற்றவர்களைப் போலவே. ",
           " என்னிடம் சொல்லுங்கள், நான் மறந்துவிட்டேன், எனக்குக் கற்றுக் கொடுங்கள், நான் நினைவில் கொள்கிறேன், என்னை ஈடுபடுத்துங்கள், நான் கற்றுக்கொள்கிறேன். ",
           " உலகின் சிறந்த மற்றும் அழகான விஷயங்களை பார்க்கவோ அல்லது தொடவோ முடியாது - அவை இதயத்தால் உணரப்பட வேண்டும். ",
           " இறுதியில், உங்கள் வாழ்க்கையில் வருடங்கள் கணக்கிடப்படுவதில்லை. இது உங்கள் ஆண்டுகளில் உள்ள வாழ்க்கை. ",
           " ஒவ்வொரு நாளும் இரண்டாம் வாய்ப்பு ஆகும். ",
           " நான் வெற்றியைப் பற்றி கனவு கண்டதில்லை. அதற்காக உழைத்தேன். ",
           " உறுதியுடன் எழுந்திருங்கள் மற்றும் திருப்தியுடன் படுக்கைக்குச் செல்லுங்கள். ",
           " நீங்கள் சோர்வாக இருந்தால், வெளியேறாமல் ஓய்வெடுக்க கற்றுக்கொள்ளுங்கள்.",
           " நீங்கள் எவ்வளவு அதிகமாக கொடுக்கிறீர்களோ, அவ்வளவு மகிழ்ச்சியாக இருப்பீர்கள்.",
           " ஒவ்வொரு நாளும் உங்கள் தலைசிறந்த படைப்பாக ஆக்குங்கள். ",
           " நேற்றிலிருந்து கற்றுக்கொள்ளுங்கள், இன்றைக்கு வாழ்க, நாளைய நம்பிக்கை. கேள்வி கேட்பதை நிறுத்தக் கூடாது என்பதே முக்கியம். ",
           " வாய்ப்பு நடக்காது, நீங்கள் அவற்றை உருவாக்க வேண்டும். ",
           " நாளைக்கு இறப்பது போல் வாழுங்கள். என்றென்றும் வாழ்வது போல் கற்றுக்கொள்ளுங்கள். ",
           " நான் தோல்வியடையவில்லை. வேலை செய்யாத 10,000 வழிகளைக் கண்டுபிடித்தேன்.",
           " உண்மை END என்றால் முடிவு என்பது முடிவல்ல முயற்சிகள் ஒருபோதும் இறக்காது ", 
           " உலகத்தை மாற்ற நீங்கள் பயன்படுத்தக்கூடிய மிக சக்திவாய்ந்த ஆயுதம் கல்வி ", 
           " ஒருபோதும் தவறு செய்யாத ஒருவர் புதிதாக எதையும் முயற்சித்ததில்லை ", 
           " உங்கள் பாதையில் கடினமான தடைகள் ஏராளமாக உள்ளன. அவற்றில் ஒன்றாக உங்களை அனுமதிக்காதீர்கள் ", 
           " என்னால் மட்டுமே என் வாழ்க்கையை மாற்ற முடியும். எனக்காக யாராலும் முடியாது " 
           " என்னால் முடியும் என்று நினைக்கிறேன். என்னால் முடியும் என்று எனக்குத் தெரியும் ", 
           " கற்றல் பிழையின்றி ஒருபோதும் தோல்வியடையாது ", 
           " உலகில் நீங்கள் காண விரும்பும் மாற்றமாக நீங்கள் இருக்க வேண்டும் ", 
           " கடின உழைப்புக்கு ஈடு இணையில்லை." , 
           " வாய்ப்புக்காக காத்திருக்காதீர்கள், உருவாக்குங்கள் ", 
           " வெற்றி என்பது அனைத்து முயற்சிகளின் கூட்டுத்தொகை, மீண்டும் மீண்டும் ஒரு நாள் மற்றும் நாள் முழுவதும் ", 
           " வெற்றி பெறுவதற்கான எனது உறுதிப்பாடு போதுமானதாக இருந்தால் தோல்வி என்னை ஒருபோதும் முந்தாது ", 
           " தன்னம்பிக்கை மற்றும் கடின உழைப்பு எப்போதும் உங்களுக்கு வெற்றியைத் தரும் ", 
           " நான் உண்மையில் ஒரு ராஜா, ஏனென்றால் என்னை எப்படி ஆள வேண்டும் என்று எனக்குத் தெரியும்", 
           " உங்கள் நேரம் குறைவாக உள்ளது, எனவே வேறொருவரின் வாழ்க்கையை வாழ்ந்து வீணாக்காதீர்கள். மற்றவர்களின் சிந்தனையின் முடிவுகளுடன் வாழும் கோட்பாட்டால் சிக்கிக்கொள்ளாதீர்கள் ", 
           " உங்கள் கயிற்றின் முனையை அடைந்ததும், அதில் ஒரு முடிச்சைக் கட்டி தொங்க விடுங்கள் ", 
           " நீங்கள் முற்றிலும் தனித்துவமானவர் என்பதை எப்போதும் நினைவில் கொள்ளுங்கள். மற்றவர்களைப் போலவே ", 
           " என்னிடம் சொல்லுங்கள், நான் மறந்துவிட்டேன், எனக்குக் கற்றுக் கொடுங்கள், நான் நினைவில் கொள்கிறேன், என்னை ஈடுபடுத்துங்கள், நான் கற்றுக்கொள்கிறேன் ", 
           " உலகின் சிறந்த மற்றும் அழகான விஷயங்களை பார்க்கவோ அல்லது தொடவோ முடியாது - அவை இதயத்தால் உணரப்பட வேண்டும் ", 
           " இறுதியில், உங்கள் வாழ்க்கையில் வருடங்கள் கணக்கிடப்படுவதில்லை. இது உங்கள் ஆண்டுகளில் உள்ள வாழ்க்கை ", 
           " ஒவ்வொரு நாளும் இரண்டாம் வாய்ப்பு ஆகும் ", 
           " நான் வெற்றியைப் பற்றி கனவு கண்டதில்லை. அதற்காக உழைத்தேன் ", 
           " உறுதியுடன் எழுந்திருங்கள் மற்றும் திருப்தியுடன் படுக்கைக்குச் செல்லுங்கள் ", 
           " நீங்கள் சோர்வாக இருந்தால், வெளியேறாமல் ஓய்வெடுக்க கற்றுக்கொள்ளுங்கள் ", 
           " நீங்கள் எவ்வளவு அதிகமாக கொடுக்கிறீர்களோ, அவ்வளவு மகிழ்ச்சியாக இருப்பீர்கள் ", 
           " ஒவ்வொரு நாளும் உங்கள் தலைசிறந்த படைப்பாக ஆக்குங்கள் ", 
           " நேற்றிலிருந்து கற்றுக்கொள்ளுங்கள், இன்றைக்கு வாழ்க, நாளைய நம்பிக்கை. கேள்வி கேட்பதை நிறுத்தக் கூடாது என்பதே முக்கியம்", 
           " வாய்ப்பு நடக்காது, நீங்கள் அவற்றை உருவாக்க வேண்டும் வாய்ப்பு ", 
           " நாளைக்கு இறப்பது போல் வாழுங்கள். என்றென்றும் வாழ்வது போல் கற்றுக்கொள்ளுங்கள் ", 
           " நான் தோல்வியடையவில்லை. வேலை செய்யாத 10,000 வழிகளைக் கண்டுபிடித்தேன் ", 
           " தோல்வி  என்பது மகத்துவத்திற்கான மற்றொரு  படியாகும் ", 
           " ஒவ்வொரு மனிதனுக்கும்  ஒரு குறிப்பிட்ட எண்ணிக்கையிலான இதயத்துடிப்புகள் இருப்பதாக  நான் நம்புகிறேன்  என்னுடைய எதையும்  வீணாக்க  நான் விரும்பவில்லை ", 
           " மிகப்பெரிய ஆபத்து எந்த  ஆபத்தையும் எடுக்காதது  மிக விரைவாக மாறிக்கொண்டிருக்கும் உலகில்  தோல்விக்கு உத்தரவாதம்  அளிக்கும் ஒரே  உத்தி ஆபத்துக்களை எடுக்காமல் இருப்பதுதான் ", 
           " சிறந்த  பழிவாங்கல் மிகப்பெரிய வெற்றியாகும்", 
           " உற்சாகம் இல்லாமல் பெரிதாக எதுவும் சாதிக்கவில்லை ", 
           " உங்கள்  எதிர்காலத்தை உங்களால்  மாற்ற முடியாது  ஆனால் உங்கள்  பழக்கங்களை மாற்றலாம்  நிச்சயமாக உங்கள் பழக்கவழக்கங்கள் உங்கள்  எதிர்காலத்தை மாற்றும் ", 
           " தோல்வியை விட சந்தேகம் அதிக கனவுகளைக் கொல்கிறது ", 
           " விஷயங்கள்  சிறப்பாக இருக்கும்  என்று  நீங்கள் எதிர்பார்க்கும் எதிர்காலத்தை  நீங்கள் விரும்புகிறீர்கள், விஷயங்கள்  மோசமாக இருக்கும்  என்று  நீங்கள் எதிர்பார்க்கும்  இடத்தில் இல்லை ", 
           " ஒரு அவுன்ஸ் பொறுமை டன்கள் பிரசங்கிப்பதை விட மதிப்புமிக்கது ", 
           " வானத்தைப் பார் நாம் தனியாக இல்லை முழுப் பிரபஞ்சமும் நமக்கு நட்பாக இருக்கிறது  கனவு கண்டு வேலை செய்பவர்களுக்கு மட்டுமே சதி செய்கிறது ",
           " The only way to do great work is to love what you do ”, 
           “ In the middle of every difficulty lies opportunity ”, 
           “ Be yourself everyone else is already taken ”, 
           “ Growth begins when we start to accept our own weakness ”, 
           “ Believe you can, and you’re halfway there ”, 
           “ You are never too old to set another goal or to dream a new dream ”, 
           “ Life is not about waiting for the storm to pass but about learning to dance in the rain ”, 
           “ Folks are usually about as happy as they make their minds up to be ”, 
           “ Learning is a weightless treasure you can always carry easily ”, 
           “ The great thing in this world is not so much where we are but in what direction we are going ”, 
           “ Do what you can, with what you have, where you are ”, 
           “ Your time is limited, so don’t waste it living someone else’s life ”, 
           “ Success usually comes to those who are too busy to be looking for it ”, 
           “ The only limit to our realization of tomorrow will be our doubts of today, ”
           “ Success is walking from failure to failure with no loss of enthusiasm ”, 
           “ The best time to plant a tree was 20 years ago. The second best time is now ”, 
           “ Great minds discuss ideas average minds discuss events small minds discuss people ”, 
           “ Don’t watch the clock do what it does  Keep going ”, 
           “ The future belongs to those who believe in the beauty of their dreams ”, 
           “ It always seems impossible until it’s done ”, 
           “ The secret of getting ahead is getting started ”, 
           “ Every moment is a fresh beginning ”, 
           “ Life is a journey, and if you fall in love with the journey, you will be in love forever ”, 
           “ Life is a series of natural and spontaneous changes. Don’t resist them  that only creates sorrow Let reality be reality  Let things flow naturally forward in whatever way they like ”, 
           “ Happiness consists not in having much, but in being content with little ”, 
           “ Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart ”, 
           “ Life isn’t about finding yourself. Life is about creating yourself ”, 
           “ There is no substitute for hard work ”, 
           “ Life is a great big canvas, and you should throw all the paint on it you can ”, 
           “ Things work out best for those who make the best of how things work out ”, 
           " Life is about making an impact, not making an income ”, 
           “ Less perfection, more authenticity ”, 
           “ Simplicity is the ultimate sophistication ”, 
           “ Every moment matters ”, 
           “ Find joy in the ordinary ”, 
           “ Life is short; make it sweet ”, 
           “ Cherish the little things ", 
           “ Life is beautiful when you stop and look around ”, 
           “ Be a voice not an echo ”, 
           “ Happiness is homemade ”,
           ]

@app.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")
