from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3
from .models import Foods
import requests
import openai
import settings_local_ 




# Create your views here.

#IoTからデータを取得
@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        # POSTリクエストからデータを取得
        data = request.POST.get('data', None)
        if data:
            # データのパース
            result = json.loads(data)
            
            # データベースにデータを保存
            Foods.save_data(result['id'], result['food_name'])
            
            # 応答の作成
            response = "データを受信し、保存しました。"
            return HttpResponse(response)
        else:
            # データがない場合の処理
            return HttpResponse("データがありません。")
    else:
        # POSTリクエスト以外の場合の処理
        return HttpResponse("POSTリクエストを送信してください。")

def meal_suggestion(request):
    # Foods.take_data(id) を呼び出してJSONレスポンスを取得する
    response_data = Foods.take_data(id)

    # JSONデータを文字列に変換する
    json_data = json.dumps(response_data)

    # JSONデータを辞書に変換
    data_dict = json.loads(json_data)

    # "id"キーが存在するかを判定する
    if "id" in data_dict:
        #food_nameを辞書として扱いたい
        food_name = data_dict['food_name']
        sentence = f'以下は冷蔵庫にある食材のリストである。これらの食材から作れるおすすめ料理を3つ返してください。冷蔵庫にある食材リスト: {food_name}ただし、回答は以下のフォーマットに従うものとする。#フォーマット: {{"メニュー1": "おすすめメニュー1", "メニュー2": "おすすめメニュー2", "メニュー3": "おすすめメニュー3"}}'
        # ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "日本語で応答してください"
                },
                {
                    "role": "user",
                    "content": sentence
                },
            ],
        )

        chat_results = json.dumps(response["choices"][0]["message"]["content"])
        return HttpResponse(json.dumps({'message': chat_results}), content_type='application/json')
        
    else:
        # HttpResponseを使ってエラーのJSONレスポンスを返す
        return HttpResponse(json.dumps({'message': '食材がありません'}), content_type='application/json')

    



##以下、メモ書き

    if request.method == 'POST':
        food_list = []
        for key in request.form.keys():
            if key.startswith("food_"):
                food_list.append(request.form.get(key))
            if key.startswith("number_"):
                number_list.append(request.form.get(key))
        
        for i in range(len(food_list)):
            ingredients = Ingredients(name=food_list[i], number=int(number_list[i]))

            db.session.add(ingredients)
            db.session.commit()

        return redirect("/cook")

    else:
        ingredients = Ingredients.query.all()

        food_box = []

        for ingredient in ingredients:
           food_box.append({ingredient.name :ingredient.number})

        message = f'いま冷蔵庫の中に以下のような食材が入っています。(食材と個数の辞書形式になっています。) + {food_box} + これらを使って作れるレシピを提案してください'

        #message = "いま冷蔵庫の中に以下のような食材が入っています。人参1本、玉ねぎ1個、ジャガイモ1個、カレーのルー。これらを使って作れるレシピを3つ提案してください"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message},]
            )
        print(response.choices[0]["message"]["content"].strip())

        return render_template("cook.html", ingredients=ingredients, message=response.choices[0]["message"]["content"].strip())
    
    return render(request, 'blog/post_list.html', {})