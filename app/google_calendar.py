# %%
"""debug用のファイル、グーグルカレンダーからイベントとその日時を取得"""
import datetime
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# ユーザーのgoogle_mailアカウント
USER_EMAIL = os.environ["USER_EMAIL"]

# 認証情報ファイルのパス
credentials_file = '../credentials.json'

# GoogleカレンダーAPIのスコープ
scopes = ['https://www.googleapis.com/auth/calendar.readonly']

# 認証情報を読み込む
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)

# GoogleカレンダーAPIのクライアントを作成する
service = build('calendar', 'v3', credentials=credentials)

# 今日の日付を取得する
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
start_of_day = datetime.datetime(now.year, now.month, now.day, tzinfo=pytz.timezone('Asia/Tokyo'))
end_of_day = start_of_day + datetime.timedelta(days=3)

# イベントの取得パラメータを設定する
events_result = service.events().list(
    calendarId=USER_EMAIL,
    timeMin=start_of_day.isoformat(),
    timeMax=end_of_day.isoformat(),
    singleEvents=True,
    orderBy='startTime'
).execute()

# イベントのリストを取得する
events = events_result.get('items', [])

# イベント情報を格納するリスト
event_list = []

if not events:
    print('今日の予定はありません。')
else:
    print('今日の予定:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        summary = event['summary']
        
        # 日付、時刻、イベントを分割してリストに格納
        start_datetime = datetime.datetime.fromisoformat(start)
        end_datetime = datetime.datetime.fromisoformat(end)
        date = start_datetime.date()
        start_hour = start_datetime.hour
        start_minute = start_datetime.minute
        end_hour = end_datetime.hour
        end_minute = end_datetime.minute
        
        event_info = {
            'date': date,
            'start_hour': start_hour,
            'start_minute': start_minute,
            'end_hour': end_hour,
            'end_minute': end_minute,
            'summary': summary
        }
        event_list.append(event_info)
        
        print(f'{start} - {end}: {summary}')

# 例
for event in event_list:
    date = event['date']
    start_hour = event['start_hour']
    start_minute = event['start_minute']
    end_hour = event['end_hour']
    end_minute = event['end_minute']
    summary = event['summary']
    print(f"日付: {date}, 開始時刻: {start_hour}:{start_minute:02d}, 終了時刻: {end_hour}:{end_minute:02d}, イベント: {summary}")
# %%
