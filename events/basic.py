from line_bot_api import *

def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 13,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]
    text_message = TextSendMessage(text='''$ 廣島冰茶鋪 $
    讓你不小心斷片~~~~''',emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='5ac21c46040ab15980c9b442',
        sticker_id='003'
    )

    about_us_img = 'https://i.imgur.com/70A4WdI.jpg'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_inage_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message,sticker_message,image_message]
    )

def location_event(event):
    location_message = LocationSendMessage(
        title='廣島冰茶鋪',
        address='80049高雄市新興區中山一路243號',
        latitude=22.635115780380566, 
        longitude=120.3019637852388
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message
    )