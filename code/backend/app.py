from flask import Flask, render_template
from flask import request
from flask_cors import CORS  # 解决跨域的问题

import solve
from datetime import datetime 

app = Flask(__name__, 
            template_folder='../frontend/dist', 
            static_folder='../frontend/dist/static')


@app.route("/")
def index():
   message = {'sdds'}
      
   return render_template("index.html", message = message)
      
@app.route("/formdata", methods = ['POST', 'GET'])
def formdata():
   # 计时开始
   start = datetime.now()
   
   # 获取表单输入
   data = request.get_json(silent=True)

   # 性别，日期
   gender = 'boy' if data['gender']==u'男孩' else 'girl'
   birthday = datetime.strptime(data['datevalue'][:10], '%Y-%m-%d').date()
   today = datetime.now().date()
   day = (today - birthday).days

   # 处理数据
   inter = solve.Meta(day, gender)
   inter.trans()
   print(inter.result)
   message = data
   # 计时结束
   if app.debug == True:
      end = datetime.now()
      print( u'计算时间为', end - start, 's' )
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)
