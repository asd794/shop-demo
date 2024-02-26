function login_function(email,name){
    // email="5566@gmail.com";
    // name="";
    console.log("有進入FUNCTION");
    if(email == "" || email == "" || name == "" || name == ""){
        console.log("email或name是空值");
        let el = document.getElementById("accountmenu");
        let str = "<li><a href=\"/login\">Log in</a></li><li><a href=\"/register\">Register</a></li>";
        el.innerHTML=str;
        return;
    };
    console.log(email,name);
    let el = document.getElementById("login-name");
    let str = "<div>Welcome, "+name+"</div>";
    el.innerHTML = str;
    let el2 = document.getElementById("accountmenu");
    let str2 = "<li><a href=\"/member\">My Account</a></li><li><a href=\"/shelves\">上架產品</a></li><li><a href=\"/myproducts\">我的產品</a></li><li><a href=\"/myorders\">訂單記錄</a></li><li><a href=\"/logout\">Log out</a></li>";
    el2.innerHTML=  str2;
    
    let request = new XMLHttpRequest();
    request.open('get','http://127.0.0.1/api/cart');
    request.send();
    request.addEventListener("readystatechange", () => {
        if(request.readyState === 4 && request.status === 200 ){
            // console.log(a.responseText);
            console.log(request.readyState,request.status);
            console.log('有近來login.js檔案喔');
            let response=request.responseText;
            let json=JSON.parse(response);
            let j = JSON.stringify(response);
            console.log(json);
            // console.log(j);
            // console.log(response["Amount"]);
            console.log(json.length);
            // console.log(json[0].Product_Name);
            // label=['Cart_ID','Price','Amount','Member_ID','Product_ID','Product_Name'];
            // console.log(json[0]);

            let cart_str = "";
            let cart_total = 0;
            for(let i=0 ;i<json.length ;i++){
                cart_str = cart_str + '<div class="single-cart clearfix"><div class="cart-image"><a href="product-details?Product_ID='+json[i].Product_ID+'"><img src="'+json[i].Image+'" alt="" width="75px" height="85px"></a></div><div class="cart-info"><h5><a href="product-details.html">'+json[i].Product_Name+'</a></h5><p>$'+json[i].Price+' x '+json[i].Amount+'</p><a href="cart-delete?Cart_ID='+json[i].Cart_ID+'" class="cart-delete" title="Remove this item"><i class="pe-7s-trash"></i></a></div></div>';
                cart_total = cart_total + json[i].Price*json[i].Amount;

            };
            let cart_el = document.getElementById("cart-products");
            cart_el.innerHTML = cart_str;
            let cart_el2 = document.getElementById("cart-total");
            cart_el2.innerHTML = '<h5>Total <span>$'+cart_total+'</span></h5>';
            let cart_el3 = document.getElementById("carts_amount");
            cart_el3.innerHTML = json.length;
        }
        else if(request.readyState === 4){
            console.log("抱歉，api/cart連線狀態出了點問題")
        };
    });


};

// let e="eee";
// let n="nnn";
// if(e !=undefined && e !=null && n !=undefined && n !=null){
//     console.log("e n 不等於空值");
// };
// console.log(e,n)

console.log("--------loginNNNNNNNNNNNNNNNNN----------");
// login_function();