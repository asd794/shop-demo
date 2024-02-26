import pymysql
from flask import *
from flask_cors import CORS #方法一 處理CORS
from flask_socketio import SocketIO #方法二 處理CORS
from flask_bcrypt import Bcrypt #匯入flask-bcrypt 套件
from werkzeug.utils import secure_filename
import os
import datetime
import random

mysqlserverIP = '192.168.2.169'



app=Flask(
    __name__,
    static_folder="public",
    # static_url_path="/"
)

app.secret_key="secret key for flask test"



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

app_root = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def inde():
    return redirect("/index")

# 上傳 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/upload" ,methods=['GET', 'POST'])
def upload():
    product_name = request.form['product-name']
    product_price = request.form['product-price']
    product_amount = request.form['product-amount']
    product_description = request.form['product-description']
    image = request.files['file']

    conn = pymysql.connect(
    host=mysqlserverIP,
    user='weichih-shop',
    password='weichih-shop',
    database='shop',
    )
    cursor=conn.cursor()
    cursor.execute("insert into Products values(NULL,'"+product_name+"','"+product_description+"',"+product_price+","+product_amount+",'','"+str(datetime.date.today())+"',"+str(session['m_id'])+");")
    conn.commit()
    cursor.execute("select Product_ID from Products where Member_ID="+str(session['m_id'])+";")
    result=cursor.fetchall()
    print(result)
    print(len(result))
    lastPID = result[len(result)-1][0] # 取得會員的最新的產品ID


    UPLOAD_FOLDER = './public/shop_static/picture/'+str(lastPID)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    print(image.headers)
    folder = os.path.exists(UPLOAD_FOLDER)
    if folder == False: # 判斷產品圖片資料夾是否存在 ,如果為false就建立一個
        os.makedirs(UPLOAD_FOLDER)
    print(folder)
    print(image.content_type[6:])
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], '1'+'.'+image.content_type[6:])) # 儲存圖片

    print(type(lastPID))
    cursor.execute("update Products set Image ='"+"./public/shop_static/picture/"+str(lastPID)+"/1."+image.content_type[6:]+"' where Product_ID="+str(lastPID)+";")
    conn.commit()
    conn.close()
    return redirect("/notify?msg=上架完成")


# 資料庫products查詢結果 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/api/products")
def api_prdocuts():
    conn = pymysql.connect(
    host=mysqlserverIP,
    user='weichih-shop',
    password='weichih-shop',
    database='shop',
    )
    cursor=conn.cursor()
    cursor.execute('select * from Products;')
    result_products=cursor.fetchall()
    conn.close()
    label=['Product_ID','Product_Name','Description','Price','Amount,','Image','Date','Member_ID']
    dic={}
    result=[]
    for i in result_products:
        count_dic=0
        for x in i:
            dic[label[count_dic]]=x
            count_dic=count_dic+1
        result.append(dic)
        # print('dic',dic)
        dic={}

    return jsonify(result)

# 資料庫Carts查詢結果 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/api/cart")
def api_cart():
    if "m_id" in session:
        print(session['email'],session['name'],session['m_id'])
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor=conn.cursor()
        cursor.execute("select Carts.Cart_ID,Carts.Price,Carts.Amount,Carts.Member_ID,Carts.Product_ID,Products.Product_Name,Products.Image from Carts inner join Products on Carts.Product_ID=Products.Product_ID where Carts.Member_ID="+str(session['m_id'])+";")
        result_cart=cursor.fetchall()
        conn.close()
        dic={}
        result=[]
        label=['Cart_ID','Price','Amount','Member_ID','Product_ID','Product_Name','Image']
        for i in result_cart:
            count_dic=0
            for x in i:
                dic[label[count_dic]]=x
                count_dic=count_dic+1
            result.append(dic)
            # print('dic',dic)
            dic={}
        return jsonify(result)
    return redirect("/index")

# 資料庫Orders查詢結果 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/api/myorders")
def api_order():
    if "m_id" in session:
        print(session['email'],session['name'],session['m_id'])
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor=conn.cursor()
        cursor.execute("select Orders.Order_ID,Orders.Order_MID,Orders.Price,Orders.Amount,Orders.Name,Orders.Phone,Orders.Address,Orders.Notes,Orders.Datetime,Orders.Product_ID,Orders.Seller_ID,Orders.Buyer_ID,Members.Name,Products.Product_Name from (Orders inner join Members on Orders.Seller_ID=Members.Member_ID) inner join Products on Orders.Product_ID=Products.Product_ID where Buyer_ID="+str(session['m_id'])+";")
        result_orders=cursor.fetchall()
        conn.close()
        dic={}
        result=[]
        label=['Order_ID','Order_MID','Price','Amount','Name','Phone','Address','Notes','Datetime','Product_ID','Seller_ID','Buyer_ID','Seller_Name','Product_Name']
        for i in result_orders:
            count_dic=0
            for x in i:
                dic[label[count_dic]]=x
                count_dic=count_dic+1
            result.append(dic)
            # print('dic',dic)
            dic={}
        # print(result[0])

        m_id=[]
        for i in result:
            if i['Order_MID'] not in m_id:
                m_id.append(i['Order_MID'])
        
        result2={}
        for i in m_id:
            temp_arr=[]
            temp_dic={}
            for x in result:
                if i == x['Order_MID']:
                    for y in x:
                        temp_dic[y]=x[y]
                    temp_arr.append(temp_dic)
                    temp_dic={}
            result2[i]=temp_arr
            temp_arr=[]

        # print(result2)

        return jsonify(result2)

# index頁面 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/index")
def index():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        print(session['email'],session['name'],session['m_id'])
        return render_template("/shop/index.html",email=session['email'],name=session['name'],m_id=session['m_id'])
    # cursor.execute('select * from')
    return render_template("/shop/index.html")

# shop頁面 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/shop")
def shop():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        print(session['email'],session['name'],session['m_id'])
        return render_template("/shop/shop.html",email=session['email'],name=session['name'],m_id=session['m_id'])
    # cursor.execute('select * from')
    return render_template("/shop/shop.html")


# 上架產品頁面 shelves.html demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/shelves")
def shelves():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        print(session['email'],session['name'],session['m_id'])
        return render_template("/shop/shelves.html",email=session['email'],name=session['name'],m_id=session['m_id'])
    else:
        return redirect("/index")

# product-details頁面 /product-details?Product_ID=1    demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/product-details")
def index_details():
    Product_ID=request.args.get("Product_ID") # 前端?Product_ID傳入值
    conn = pymysql.connect(
        host=mysqlserverIP,
        user='weichih-shop',
        password='weichih-shop',
        database='shop',
    )
    cursor=conn.cursor()
    cursor.execute('select Products.Product_ID,Products.Product_Name,Products.Description,Products.Price,Products.Amount,Products.Image,Products.Date,Products.Member_ID,Members.Name from Products inner join Members on Products.Member_ID=Members.Member_ID where Product_ID='+Product_ID+';')
    result_product=cursor.fetchall()
    conn.close()
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        print(session['email'],session['name'],session['m_id'])
        return render_template("/shop/product-details.html",email=session['email'],name=session['name'],m_id=session['m_id'],Product_ID=result_product[0][0],Product_Name=result_product[0][1],Description=result_product[0][2],Price=result_product[0][3],Amount=result_product[0][4],Image=result_product[0][5],Member_ID=result_product[0][7],Name=result_product[0][8])
    return render_template("/shop/product-details.html",Product_ID=result_product[0][0],Product_Name=result_product[0][1],Description=result_product[0][2],Price=result_product[0][3],Amount=result_product[0][4],Image=result_product[0][5],Member_ID=result_product[0][7],Name=result_product[0][8])


# add-cart 加入購物車 /add-cart demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/add-cart" ,methods=["post"])
def add_cart():
    if "m_id" in session:
        amount = request.form["add-cart"]
        price = request.form["price"]
        product_ID = request.form["product_ID"]
        if amount == "0":
            print("數量為0,重新導到/product-details?Product_ID="+product_ID)
            return redirect("/product-details?Product_ID="+product_ID)
        print("amount=",type(amount),amount)
        print("price=",type(price),price)
        print("product_ID=",type(product_ID),product_ID)
        print("m_id=",type(session["m_id"]),session["m_id"])
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor = conn.cursor()
        cursor.execute("select * from Carts where Member_ID="+str(session["m_id"])+" and Product_ID="+product_ID+";")
        result_cart = cursor.fetchone()
        if result_cart == None:
            cursor.execute("insert into Carts values(NULL,"+price+","+amount+","+str(session["m_id"])+","+product_ID+");")
            conn.commit()
            conn.close()
            return redirect("/product-details?Product_ID="+product_ID)
        else:
            cursor.execute("select Amount from Products where Product_ID="+product_ID+";")
            result_product = cursor.fetchone()
            print("result_product[0]",type(result_product[0]))
            # print("數量",result_cart[0][2],type(result_cart[0][2]))
            if result_cart[2]+int(amount) <= result_product[0]:
                cursor.execute("update Carts set Amount="+str(result_cart[2]+int(amount))+" where Member_ID="+str(session["m_id"])+" and Product_ID="+product_ID+";")
                conn.commit()
                conn.close()
                print("update Carts set Amount="+str(result_cart[2]+int(amount))+" where Member_ID="+str(session["m_id"])+" and Product_ID="+product_ID+";")
                return redirect("/product-details?Product_ID="+product_ID)
            else:
                return redirect("/notify?msg=訂購數量加購物車數量 超過產品總量")

    else:
        return redirect("/login")

# 購物車刪除/cart-delete?Cart_id=?? demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/cart-delete")
def cart_delete():
    Cart_ID = request.args.get("Cart_ID")
    print(Cart_ID)
    if "email" in session: # 判斷session有無資料，
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor=conn.cursor()
        cursor.execute('delete from Carts where Cart_ID='+Cart_ID)
        conn.commit()
        conn.close()

    return redirect("/index")

# check out 購物車結帳 /chechout demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/checkout")
def checkout():
    if "email" in session: # 判斷session有無資料，沒有就導向到/
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor=conn.cursor()
        cursor.execute("select * from Carts where Member_ID="+str(session['m_id'])+";")
        result=cursor.fetchall()
        print(result)
        conn.close()

        print(session['email'],session['name'],session['m_id'])
        return render_template("/shop/checkout.html",email=session['email'],name=session['name'],m_id=session['m_id'])
    # cursor.execute('select * from')
    return redirect("/login")

# order 購物車結帳下單 /order demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/order" ,methods=["post"])
def order():
    Name = request.form['name']
    Address = request.form['address']
    Email = request.form['email']
    Phone = request.form['phone']
    Notes = request.form['notes']
    random_string = ""
    for ran in range(10):
        random_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        random_string += random_letter    

    conn = pymysql.connect(
    host=mysqlserverIP,
    user='weichih-shop',
    password='weichih-shop',
    database='shop',
    )
    cursor=conn.cursor()
    cursor.execute("select * from Carts where Member_ID="+str(session['m_id'])+";")
    memberCart = cursor.fetchall()
    cursor.execute("delete from Carts where Member_ID="+str(session['m_id'])+";")
    cursor.execute("select Product_ID,Price,Amount,Member_ID from Products where Product_ID="+'6'+";")
    product = cursor.fetchone()

    loc_dt = datetime.datetime.today()
    loc_dt_format = loc_dt.strftime("%Y-%m-%d %H:%M:%S") #當前時間2024-02-23 09:03:36

    # print(loc_dt_format)
    for i in memberCart:
        cursor.execute("select Amount,Member_ID from Products where Product_ID="+str(i[4])+";")
        productAmountMid = cursor.fetchone()
        update_amount = productAmountMid[0]-i[2]
        print('產品訂單數量',i[2],'產品總數',productAmountMid[0],'扣除後',update_amount)
        if update_amount > 0:
            print('Product_ID',i[4],'扣除後>1')
            print("update Products set Amount="+str(update_amount)+" where Product_ID="+str(i[4])+";")
            cursor.execute("update Products set Amount="+str(update_amount)+" where Product_ID="+str(i[4])+";")
            print("insert into Orders values(NULL,'"+random_string+"',"+str(i[1])+","+str(i[2])+",'"+Name+"',"+Phone+",'"+Address+"','"+Notes+"','"+loc_dt_format+"',"+str(i[4])+","+str(productAmountMid[1])+","+str(session['m_id'])+");")
            cursor.execute("insert into Orders values(NULL,'"+random_string+"',"+str(i[1])+","+str(i[2])+",'"+Name+"',"+Phone+",'"+Address+"','"+Notes+"','"+loc_dt_format+"',"+str(i[4])+","+str(productAmountMid[1])+","+str(session['m_id'])+");")
        else:
            print('Product_ID',i[4],'扣除後=0')
            # print("delete from Products where Product_ID="+str(i[4])+";")
            # cursor.execute("delete from Products where Product_ID="+str(i[4])+";")
            print("update Products set Amount="+str(update_amount)+" where Product_ID="+str(i[4])+";")
            cursor.execute("update Products set Amount="+str(update_amount)+" where Product_ID="+str(i[4])+";")
            print("insert into Orders values(NULL,'"+random_string+"',"+str(i[1])+","+str(i[2])+",'"+Name+"',"+Phone+",'"+Address+"','"+Notes+"','"+loc_dt_format+"',"+str(i[4])+","+str(productAmountMid[1])+","+str(session['m_id'])+");")
            cursor.execute("insert into Orders values(NULL,'"+random_string+"',"+str(i[1])+","+str(i[2])+",'"+Name+"',"+Phone+",'"+Address+"','"+Notes+"','"+loc_dt_format+"',"+str(i[4])+","+str(productAmountMid[1])+","+str(session['m_id'])+");")
    print(len(memberCart))
    print(memberCart[0][2])
    print(product)
    print(Name,Address,Email,Phone,Notes)
    conn.commit()
    conn.close()
    return redirect("/checkout")


# 登入頁面 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/login")
def login():
    if "m_id" in session:
        return redirect("/index")
    return render_template("/shop/login.html")

# 註冊頁面 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/register")
def register():
    if "m_id" in session:
        return redirect("/index")
    return render_template("/shop/register.html")

# 會員頁面 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/member")
def member():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        return render_template("/shop/member.html",m_id=session['m_id'],email=session['email'],name=session['name'])
    else:
        return redirect("/login")

# 訂單記錄 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/myorders")
def myorders():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        return render_template("/shop/myorders.html",m_id=session['m_id'],email=session['email'],name=session['name'])
    else:
        return redirect("/login")
    
# 我的產品 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/myproducts")
def myproducts():
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        return render_template("/shop/myproducts.html",m_id=session['m_id'],email=session['email'],name=session['name'])
    else:
        return redirect("/login")    

# 通知頁面 /notify?msg=錯誤訊息 demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/notify")
def error():
    message=request.args.get("msg","發生問題,請聯絡客服")
    if "m_id" in session: # 判斷session有無資料，沒有就導向到/
        return render_template("/shop/notify.html",message=message,m_id=session['m_id'],email=session['email'],name=session['name'])
    else:
        return render_template("/shop/notify.html")

# 處理會員註冊mysql demo-shop -----------------------------------------------------------------------------------------------------------
@app.route("/signup" ,methods=["post"])
def signup():
    conn = pymysql.connect(
    host=mysqlserverIP,
    user='weichih-shop',
    password='weichih-shop',
    database='shop',
    )
    cursor=conn.cursor()
    # 從前端接收form資料
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    compare_email=(email,)
    cursor.execute('select Email from Members;')
    result=cursor.fetchall()
    if compare_email in result:
        print(email,'在裡面,不新增至資料庫')
        conn.close()
        return redirect("/notify?msg=Email已被註冊,請重新註冊")
    else:
        print(email,'未在資料庫裡面,所以新增到會員資料庫')
        cursor.execute("insert into Members values(null,'%s','%s','%s');" % (name,email,password))
        conn.commit()
        conn.close()
        # return render_template('/shop/register.html')
        return redirect("/notify?msg=帳密註冊完成")

# 處理會員登入mysql demo-shop ----------------------------------------------------------------------------------------------------------
@app.route("/signin" ,methods=["post"])
def signin():
    # 從前端傳入email和password
    email=request.form["email"]
    password=request.form["password"]
    conn = pymysql.connect(
    host=mysqlserverIP,
    user='weichih-shop',
    password='weichih-shop',
    database='shop',
    )
    if email == "" or password == "": # 判斷email或密碼是空的
        print("email 或 密碼 是空的")
        return redirect("/notify?msg=帳密不能為空,請重新登入")
    cursor=conn.cursor()
    compare_email=(email,) # 多加逗號為了跟查詢資料庫(email查詢有逗號)比對
    compare_password=password
    print("前端輸入信箱登入",compare_email)
    print("前端輸入密碼登入",compare_password)
    cursor.execute('select Email from Members;')
    result_email=cursor.fetchall()
    if compare_email in result_email:
        print(email,'EMAIL正確,繼續比對PASSWORD')
        cursor.execute("select Password,Name,Member_ID from Members where Email = '%s';" % (email))
        result_password_name=cursor.fetchall()
        if compare_password == result_password_name[0][0]:
            print(password,'密碼也正確,歡迎登入')
            session['email']=email
            # session['password']=password
            session['name']=result_password_name[0][1]
            session['m_id']=result_password_name[0][2]
            # cursor.execute("select Name from Members where Email")
            conn.close()
            print(type(session['email']))
            print("登入成功",session['email'],password,session['name'],session['m_id'])
            print(session)
            return redirect("/index")
        else:
            conn.close()
            print('輸入的password錯誤')
            return redirect("/notify?msg=帳號密碼輸入錯誤")
    else:
        conn.close()
        print('輸入的email錯誤')
    return redirect("/notify?msg=帳號密碼輸入錯誤")
# 會員登出 清除session demo-shop ----------------------------------------------------------------------------------------------------------
@app.route("/logout")
def signout():
    del session["email"]
    del session["name"]
    del session["m_id"]
    session.clear()
    print(session) # 確認session是否清除
    return redirect("/index")

# 處理變更名稱Name demo-shop ----------------------------------------------------------------------------------------------------------
@app.route("/changeName" ,methods=['post'])
def changeName():
    newName = request.form["newName"]
    if newName == "":
        return redirect("/notify?msg=新名稱欄位不能為空")
    else:
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor = conn.cursor()
        cursor.execute("update Members set Name='"+newName+"' where Member_id="+str(session['m_id'])+";")
        conn.commit()
        conn.close()
        print(session['m_id'],newName,session['name'])
        session['name'] = newName # 更改session['name']為新的名稱
        print(session['m_id'],newName,session['name'])
        return redirect("/member")

# 處理變更密碼password demo-shop ----------------------------------------------------------------------------------------------------------
@app.route("/changePassword" ,methods=['post'])
def changePassword():
    oldPassword = request.form["oldPassword"]
    newPassword = request.form["newPassword"]
    if oldPassword == "" or newPassword == "":
        return redirect("/notify?msg=舊、新密碼欄位不能為空")
    else:
        conn = pymysql.connect(
            host=mysqlserverIP,
            user='weichih-shop',
            password='weichih-shop',
            database='shop',
        )
        cursor = conn.cursor()
        cursor.execute("select Password from Members where Member_ID='"+str(session['m_id'])+"';")
        result = cursor.fetchone()
        print('查詢舊的密碼',result[0])
        if oldPassword == result[0]:
            cursor.execute("update Members set Password='"+newPassword+"' where Member_id="+str(session['m_id'])+";")
            conn.commit()
            conn.close()
            return redirect("/logout")
        else:
            return redirect("/notify?msg=舊密碼輸入錯誤")




if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
