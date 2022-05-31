
#載入LineBot所需要的模組
from flask import Flask,request, abort
from linebot import(LineBotApi,WebhookHandler,WebhookParser)
from linebot.exceptions import (InvalidSignatureError,LineBotApiError)
from linebot.models import *
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.conf import settings
from .scraper import GetStock

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)    
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

    try:
        events = parser.parse(body, signature)  # 傳入的事件
        print(events)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()
 
    for event in events:
 
        if isinstance(event, MessageEvent):  # 如果有訊息事件
 
            stock = GetStock(event.message.text)  #使用者傳入的訊息文字
 
            line_bot_api.reply_message(  # 回應前五間最高人氣且營業中的餐廳訊息文字
                    event.reply_token,
                    TextSendMessage(text=stock.scrape())
            )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
#主程式
import os 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    test.run(host='0.0.0.0', port=port)