let request = new XMLHttpRequest();
request.open('get','http://127.0.0.1/api/cart');
request.send();
request.addEventListener("readystatechange", () => {
    if(request.readyState === 4 && request.status === 200 ){
        // console.log(a.responseText);
        console.log(request.readyState,request.status);
        let response=request.responseText;
        let json=JSON.parse(response);
        console.log('有近來checkout js檔案喔');
        console.log(json.length);
        console.log(json[0].Product_Name);
        // label=['Cart_ID','Price','Amount','Member_ID','Product_ID','Product_Name'];
        console.log(json[0]);
        let str = "";
        let total = 0;
        let cart_str = "";
        for(let i=0 ;i<json.length ;i++){
            str = str +'<tr><td class="product-name">'+json[i].Product_Name+'   $'+json[i].Price +'<strong class="product-qty"> x '+json[i].Amount+'</strong></td><td class="product-total"><span class="amount">$'+json[i].Price*json[i].Amount+'</span></td></tr>';
            total = total + json[i].Price*json[i].Amount;
            cart_str = cart_str + '<div class="single-cart clearfix"><div class="cart-image"><a href="product-details.html"><img src="./public/shop_static/picture/cart-1.jpg" alt=""></a></div><div class="cart-info"><h5><a href="product-details.html">'+json[i].Product_Name+'</a></h5><p>$'+json[i].Price+' x '+json[i].Amount+'</p><a href="cart-delete?Cart_ID='+json[i].Cart_ID+'" class="cart-delete" title="Remove this item"><i class="pe-7s-trash"></i></a></div></div>';
        };
        let el = document.getElementById("order-checkout");
        el.innerHTML = str;
        let el2 = document.getElementById("order-total");
        el2.innerHTML = '<th>Order Total</th><td><strong>$ '+total+'</strong></td>';
        let cart_el = document.getElementById("cart-products");

        cart_el.innerHTML = cart_str;
        let cart_el2 = document.getElementById("cart-total");
        cart_el2.innerHTML = '<h5>Total <span>$'+total+'</span></h5>';
        let cart_el3 = document.getElementById("carts_amount");
        cart_el3.innerHTML = json.length;
    }
    else if(request.readyState === 4){
        console.log("抱歉，api/cart連線狀態出了點問題")
    };
});
