# Import basic module
from flask import Flask, request, abort, send_file, jsonify
from flask_jwt_extended import JWTManager, jwt_required

import sys
import os

# Import custom module
from server.config import Config
from server.messages.flex import flex
from server.helper import chatbot
from server.api.user import user
from server.models import connection


# Import line api
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    MessageAction,
    PostbackEvent,
    FollowEvent, FlexSendMessage, QuickReply, QuickReplyButton)


# start web server
app = Flask(__name__, static_folder='../client/dist/static')

# specify db config
app.config.from_object(Config)

# Init database connection
db = connection.set_connection(app)

# Import models which share the same connection
from server.models.Company import Company
from server.models.Vendor import Vendor
from server.models.Product import Product
from server.helper import xlsx

# specify path
project_folder = os.path.dirname(os.path.abspath(__file__))

# get line channel config
channel_secret = Config.LINE_CHANNEL_SECRET
channel_access_token = Config.LINE_CHANNEL_ACCESS_TOKEN

# Confirm configs
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

# Initialize chat bot
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# Initialize chat bot richMenu
richMenu = chatbot.richMenu(line_bot_api)

# Initialize jwt
jwt = JWTManager()
app.config['JWT_SECRET_KEY'] = 'shang-yao'
jwt.init_app(app)

# Register api
app.register_blueprint(user)

# Flush table
# db.session.query(Company).delete()
db.session.query(Product).delete()
db.session.query(Vendor).delete()
db.session.commit()
xlsx.read_and_seed(db)


# Create rich menu at the first time
# richMenu.flushAllRichMenuThenCreateOne()

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
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text == 'Quick' or text == 'quick':
        text_message = TextSendMessage(
            text='Hi, 我是上耀, 感謝你的加入!\n請點擊選單取得更多資訊\n輸入"Quick"可以再次開啟快速回覆列表',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(
                    label='關於我', text='About me'))
            ]))

        line_bot_api.reply_message(
            event.reply_token,
            text_message
        )
    elif text == 'About me':
        flexObj = flex("about_me")
        message = FlexSendMessage(
            alt_text="projects", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'company':
        company = Company.find(1)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='公司名稱:' + company.name))
    elif text == '商品列表':
        products = Product.findall()
        rtn_text = ""
        for product in products:
            print(f'商品ID:{product.id}')
            vendor = Vendor.find(product.vendor_id)
            vendor_name = vendor.name
            rtn_text += "商品編號:{}, 商品名稱:{}, 廠商名稱:{}\n".format(product.id, product.name, vendor_name)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(rtn_text))
    elif text == 'Side Projects':
        flexObj = flex("side_projects")
        message = FlexSendMessage(
            alt_text="side_projects", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Contests and Awards':
        flexObj = flex("contest_and_award")
        message = FlexSendMessage(
            alt_text="contest_and_award", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Work Experience':
        flexObj = flex("work_experience")
        message = FlexSendMessage(
            alt_text="work_experience", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Skillsets':
        flexObj = flex("skillsets")
        message = FlexSendMessage(
            alt_text="skillsets", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Social Networks':
        flexObj = flex("social_networks")
        message = FlexSendMessage(
            alt_text="social_networks", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    label = event.postback.label


@handler.add(FollowEvent)
def handle_join(event):
    print("follow")
    text_message = TextSendMessage(
        text='Hi, 我是Aaron, 感謝你的加入!\n請點擊選單取得更多資訊\n輸入"Quick"可以再次開啟快速回覆列表',
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(
                label='關於我', text='About me')),
            QuickReplyButton(action=MessageAction(
                label='我的社群帳號', text='Social Networks'))
        ]))

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )


@jwt.expired_token_loader
def my_expired_token_callback():
    return jsonify({
        'status': 401,
        'sub_status': 42,
        'msg': 'The token has expired'
    }), 401


@jwt_required
@app.route('/', defaults={'path': ''})
@app.route("/<string:path>")
@app.route('/<path:path>')
def index_client(path):
    dist_dir = Config.DIST_DIR
    entry = os.path.join(dist_dir, 'index.html')
    print(path)
    return send_file(entry)


if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
