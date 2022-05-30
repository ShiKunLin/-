
#載入LineBot所需要的模組
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

test = Flask(__name__)



# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('j7hu22/J4MsEH+LFbuJInkn8NvCxa1V0TUfSeiFLoXeQwyxMu2FCWoeUfvz/hY+w0AIUCgM1Jv2M5wDxPoYl0zT7fq1x/8uyStI4kUfDg7vye48BTqDgZpuukZWYenVH3noY2UsQx4E21VJkwjZUNQdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('1103901155d758664f42b49765099061')

line_bot_api.push_message('U02fc785bca1c72493e65e003e46b8db0', TextSendMessage(text='你可以開始了'))

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
import re

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if re.match("你是誰",message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage("才不告訴你勒~~"))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))
    
import os 
#主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    test.run(host='0.0.0.0', port=port)
