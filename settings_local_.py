"""
このファイルに環境変数を書く。このファイルは各自でローカルに保存
どうやって、環境変数を管理するか決める必要あり、このファイルか、コンテナ作るか、シェルスクリプトを書くか
xxxの中身を変える。
"""

#SECRET_KEY = 'xxx'
#API_KEY = 'xxx'

import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
