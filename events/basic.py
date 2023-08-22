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

    text_message = TextSendMessage(text='''$ 始午健康餐盒 $
原型食物-提供您每日健康的一餐

營養標示-計算健康的每一步

拒絕精緻-紫米、糙米、紅藜

保溫用膳-提供保溫裝備直到您用餐。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )

    about_us_img = 'https://i.imgur.com/70A4WdI.jpg'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])
    
def location_event(event):
    location_message = LocationSendMessage(
        title='Master SPA',
        address='110台北市信義區信義路五段7號',
        latitude=25.0333695,
        longitude=121.5638839
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)