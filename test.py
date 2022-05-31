#載入LineBot所需要的模組
from flask import Flask,request, abort
from linebot import(LineBotApi,WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

test = Flask(__name__)




# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('j7hu22/J4MsEH+LFbuJInkn8NvCxa1V0TUfSeiFLoXeQwyxMu2FCWoeUfvz/hY+w0AIUCgM1Jv2M5wDxPoYl0zT7fq1x/8uyStI4kUfDg7vye48BTqDgZpuukZWYenVH3noY2UsQx4E21VJkwjZUNQdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('1103901155d758664f42b49765099061')

line_bot_api.push_message('U02fc785bca1c72493e65e003e46b8db0', TextSendMessage(text='你可以開始了'))


# 監聽所有來自 /callback 的 Post Request
@test.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    test.logger.info("Request body: " + body)

# handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####

@handler.add(MessageEvent, message=TextMessage)
def  handle_message(event):
    message = text=event.message.text
    if "股票" in message:
        buttons_template_message = TemplateSendMessage(
        alt_text= "股票資訊",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                        thumbnail_image_url="https://histock.tw/uploadimages/51819/10c4372f6ef040e5e6f916d33e8a5ce5.png",
                        title = message[3:] + "股票資訊",
                        text="請點選想查詢的股票資訊",
                        actions=[
                            MessageAction(
                                label= message[3:] +"個股資訊",
                                text= "個股資訊" + message[3:]),
                            MessageAction(
                                label=message[3:] + "個股新聞",
                                text="個股新聞" +message[3:]),
                            ]
                        ),

                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))


#主程式
import os 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    test.run(host='0.0.0.0', port=port)