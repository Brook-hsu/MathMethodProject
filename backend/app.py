from flask import Flask, render_template
from flask import request
from flask.helpers import make_response
from flask.wrappers import Response
from flask_cors import CORS  # 解决跨域的问题

import solve
from datetime import datetime 

app = Flask(__name__, 
            template_folder='../frontend/dist', 
            static_folder='../frontend/dist/static')


@app.route("/")
def index():
   return render_template("index.html")
      
@app.route("/formdata", methods = ['POST', 'GET'])
def formdata():
   # 计时开始
   start = datetime.now()
   
   # 获取表单输入
   data = request.get_json(silent=True)
   # 性别，日期
   gender = data['gender']
   birthday = datetime.strptime(data['datevalue'][:10], '%Y-%m-%d').date()
   today = datetime.now().date()
   day = (today - birthday).days

   # 处理数据
   inter = solve.Meta(day, gender)
   message = inter.trans()
   mon = int ( day / 30 )
   message['moonage'] = (u'{}月'.format(mon) if mon else '') \
                     + (u'{}天'.format(day%30) if day%30 else '') \
                     + (u'刚出生' if day==0 else '')
   message['querytime'] = datetime.now()

   # 计时结束
   if app.debug == True:
      end = datetime.now()
      print( u'计算时间为', end - start, 's' )
   
   Response(message)
   # print(message)
   return message

if __name__ == '__main__':
   app.run()
