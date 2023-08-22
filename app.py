from flask import Flask, request, abort
from events.service import *
from events.basic import *
from line_bot_api import *

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message_text = str(event.message.text).lower()

    if message_text == '@關於我們':
        about_us_event(event)

    elif message_text == '@營業據點':
        location_event(event)

    elif message_text == '@預約服務':
        service_category_event(event)


@handler.add(PostbackAction)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    if data.get('action')=='service':
        service_event(event)




@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg="""讓始午成為你健康的一餐
    
-選單>關於我們:可看到每日菜單"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg)
    )


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

        
if __name__ == "__main__":
    app.run()