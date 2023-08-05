from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage
)

line_bot_api = LineBotApi('17cd07656f61c6930db75c4087509e1e')
handler=WebhookHandler ('gX8T/+93KFTGbRQiZeveSsf/czvQTibLG1Jk0tCGwC0LpzxqGKzeOdEgMzO1b0vkgnT9/i9PE9kgw18gRaPX0WbMzwsiP/ZKGyrkhs5alXgeJZUbHnkdBzekZSl+c535OR/x2LEBuJNuXVAZe5x2BwdB04t89/1O/w1cDnyilFU=')
