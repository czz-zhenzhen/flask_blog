from flask import Flask, render_template, request,redirect

app = Flask(__name__)

"""
@app.route('/request')
def request_view():
    print(dir(request))
    return render_template('child.html',params=request)
print(dir(request))
"""


@app.route('/get', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        print(request.args.get('uname','jgj'))
        print(request.args.get('upwd','122'))
        print(request.args.getlist('hobby'))
        print('get')
        # 重定向
        res = redirect('/')
        # print(res)
        # return res
        f = request.files['uimg']
        # 蒋文件保存在制定的文件夹
        filename = f.filename
        # 获取文件名
        f.save('img/' + filename)
        return "get"
    else:
        print(request.form.get('name','admin'))
        print(request.form.get('upwd','45454'))
        print(request.form.getlist('hobby'))
        print('post')
        print(request.files)
        f = request.files['uimg']
        # 蒋文件保存在制定的文件夹
        filename = f.filename
        # 获取文件名
        f.save('img/' + filename)
        return "post"

    # return render_template('01-get.html')


@app.route('/register',methods = ['GET','POST'])
def registers(name='admin',upwd='45454@.com',upwd1='faff45454',upwd2='45454',upwd3='45454'):
    if request.method == 'get':
        print(request.args.get(name))
        print(request.args.get(upwd))
        print(request.args.get(upwd1))
        print(request.args.get(upwd2))
        print(request.args.get(upwd3))

        # return redirect('login.html')
        return render_template('register.html')
    else:
        print(request.form.get(name))
        print(request.form.get(upwd))
        print(request.form.get(upwd1))
        print(request.form.get(upwd2))
        print(request.form.get(upwd3))
        # return redirect('login.html')
        return render_template('register.html')
@app.route('/login',methods = ['GET','POST'])
def logins():
    render_template('login.html')
@app.route('/index',methods = ['GET','POST'])
def index():
    #获取请求消息头
    print(request.headers)
    if 'Accept-Encoding' in request.headers:
        print('list_referer:',request.headers['Accept-Encoding'])
    else:
        print('not')

    return render_template('list.html')



@app.route('/form')

def form_view():
    print(request.files)
    f = request.files['uimg']
    # 蒋文件保存在制定的文件夹
    filename = f.filename
    # 获取文件名
    f.save('img/'+filename)
    return render_template('01-get.html')






if __name__ == "__main__":
    app.run(debug=True)
