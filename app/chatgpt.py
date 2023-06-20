# %%
import openai
import os

CHATGPT_API_KEY = os.environ["CHATGPT_API_KEY"]
openai.api_key = CHATGPT_API_KEY

prompt = "ChatGPTの入力"

response = openai.Completion.create(
    engine='text-davinci-003',  # 使用するエンジンを指定します
    prompt=prompt,  # チャットの開始フレーズを指定します
    max_tokens=50,  # 応答の最大トークン数を指定します
    temperature=0.7,  # 応答の多様性を調整します（0.0から1.0の範囲で指定）
    n=1,  # 返される応答の数を指定します
    stop=None,  # 応答を終了するトリガーワードを指定します
    timeout=None  # 応答を取得するまでのタイムアウト時間を指定します（オプション）
)

# 応答を表示します
print(response.choices[0].text.strip())

# %%
