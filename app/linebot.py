import json
import os
from linebot import (LineBotApi, WebhookHandler)

def __init__():
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
    line_bot_api = LineBotApi(ACCESS_TOKEN)
    handler = WebhookHandler(CHANNEL_SECRET)
    ChatGPT_API = "GPT-3のAPIキー"


# ヘルパー関数　-----------------------------------
def getJSON_Value(JSON, key):
    # JSONデータをPythonの辞書型に変換する
    data_dict = json.loads(JSON)
    # データを操作する（ここでは単に表示しています）
    return data_dict[key]

# -----------------------------------




# ユーザー認証／登録
def userAuth():
    # googleアカウント認証と関連づける
    return

# 登録時メッセージ
# LINE公式デベロッパーで設定します

# ユーザーガイド
def userGuide():
    return

# LINE応答① 朝の定型文
def goodMorning():
    return

# LINE応答② 天気予報
def weatherForecast():
    return

# LINE応答③ 今日の予定
def todaySchedule():
    return

# LINE応答④ 予定の編集（Googleカレンダー呼び出し）
def editGoogleCarendor():
    return

# LINE応答⑤ 自動リマインド
def autoRemind():
    return