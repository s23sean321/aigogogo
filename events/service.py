from line_bot_api import *
from urllib.parse import parse_qsl
import datetime

from extensions import db
from models.user import User
from models.reservation import Reservation

services = {
    1:{
        'category':'A餐-雞肉套餐',
        'img_url':'https://i.imgur.com/6Jrc4NX.jpg',
        'title':'打拋雞肉',
        'duration':'80min',
        'description':'爆香蒜及辣椒，加入碎雞肉拌炒，以小蕃茄及九層塔快拌輔味',
        'price':100,
        'post_url':'https://icook.tw/recipes/66369'
    },
    2:{
        'category':'B餐-豬肉套餐',
        'img_url':'https://i.imgur.com/OO3EM1P.jpg',
        'title':'黑胡椒豬肉',
        'duration':'80min',
        'description':'醬油醃製豬肉拌炒洋蔥，以黑胡椒粒提香增辣，豐富你味蕾的一刻',
        'price':100,
        'post_url':'https://icook.tw/recipes/66369'
    },
    3:{
        'category':'F餐-蔬菜套餐',
        'img_url':'https://i.imgur.com/zo59nEc.jpg',
        'title':'鍋邊素食',
        'duration':'80min',
        'description':'燙青菜、低油低鹽調味，清淡的一餐不造成任何負擔',
        'price':80,
        'post_url':'https://icook.tw/recipes/66369'
    },
    4:{
        'category':'G餐-特別套餐',
        'img_url':'https://i.imgur.com/LYZRbcR.jpg',
        'title':'松阪豬肉',
        'duration':'80min',
        'description':'使用氣炸鍋將肉質自身油脂逼出，原味、天然、就是這樣有嚼勁',
        'price':130,
        'post_url':'https://icook.tw/recipes/66369'
    },

}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇用餐品項',
        template = ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/6Jrc4NX.jpg',
                    action=PostbackAction(
                        lable='A餐-雞肉套餐',
                        dispaly_text='想訂購雞肉套餐',
                        data='action=service&category=A餐-雞肉套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/OO3EM1P.jpg',
                    action=PostbackAction(
                        lable='B餐-豬肉套餐',
                        dispaly_text='想訂購豬肉套餐',
                        data='action=service&category=B餐-豬肉套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/zo59nEc.jpg',
                    action=PostbackAction(
                        lable='F餐-蔬菜套餐',
                        dispaly_text='想訂購蔬菜套餐',
                        data='action=service&category=F餐-蔬菜套餐'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/LYZRbcR.jpg',
                    action=PostbackAction(
                        lable='G餐-特別套餐',
                        dispaly_text='想訂購特別套餐',
                        data='action=service&category=G餐-特別套餐'
                    )
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])




def service_event(event):
    data = dict(parse_qsl(event.postback.data))

    bubbles=[]

    for service_id in services:
        if services[service_id]['category'] ==data['category']:
            service = services[service_id]
            bubble = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/iGOrobf.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Brown Cafe",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "4.0",
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Place",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Time",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "10:00 - 23:00",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "CALL",
                        "uri": "https://linecorp.com"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "WEBSITE",
                        "uri": "https://linecorp.com"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
            }

            bubbles.append(bubble)


    flex_message = FlexSendMessage(
        alt_text='請選擇預約項目',
        contents={
            "type":"carousel",
            "contents":bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])