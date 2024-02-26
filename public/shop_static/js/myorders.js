let request = new XMLHttpRequest();
request.open('get','http://127.0.0.1/api/myorders');
request.send();
request.addEventListener("readystatechange", () => {
    if(request.readyState === 4 && request.status === 200 ){
        // console.log(a.responseText);
        console.log(request.readyState,request.status);
        let response=request.responseText;
        let json_myorders=JSON.parse(response);
        console.log('api/myorders連線正常');
        console.log(json_myorders);
        arr_mid=Object.keys(json_myorders);
        console.log(arr_mid);
        arr_value=Object.values(json_myorders);
        console.log(arr_value);
        console.log(arr_value[0][0].Product_Name);
        let str='';
        for (let i =0 ;i <arr_mid.length ;i++){
            let total=0
            for (let x =0 ;x <arr_value[i].length ;x++){
                total+=arr_value[i][x].Price*arr_value[i][x].Amount;
            };
            console.log(arr_mid[i]);
            str+="<tr class=\"parent\"><td>"+arr_mid[i]+"</td><td>"+arr_value[i][0].Datetime+"</td><td>"+arr_value[i][0].Name+"</td><td>"+arr_value[i][0].Phone+"</td><td>"+arr_value[i][0].Address+"</td><td>$"+total+"</td><td>"+arr_value[i][0].Notes+"</td></tr>";
            for (let x =0 ;x <arr_value[i].length ;x++){
                str+="<tr class=\"child\"><td></td><td>"+arr_value[i][x].Product_Name+"("+arr_value[i][x].Product_ID+")</td><td>"+arr_value[i][x].Seller_Name+"("+arr_value[i][x].Seller_ID+")</td><td>單價$"+arr_value[i][x].Price+"</td><td>數量"+arr_value[i][x].Amount+"</td><td>價格$"+arr_value[i][x].Price*arr_value[i][x].Amount+"</td><td></td></tr>";
            };
        };


        let el = document.getElementById("my-orders");
        el.innerHTML = str;
                
        // console.log(json.length);
        // console.log(json[0].Product_Name);
        // label=['Cart_ID','Price','Amount','Member_ID','Product_ID','Product_Name'];

        // console.log(json[0]);
        // let str = "";
        // let total = 0;
        // let cart_str = "";
        // for(let i=0 ;i<json.length ;i++){
        //     str = str +'<tr><td class="product-name">'+json[i].Product_Name+'   $'+json[i].Price +'<strong class="product-qty"> x '+json[i].Amount+'</strong></td><td class="product-total"><span class="amount">$'+json[i].Price*json[i].Amount+'</span></td></tr>';
        //     total = total + json[i].Price*json[i].Amount;
        //     cart_str = cart_str + '<div class="single-cart clearfix"><div class="cart-image"><a href="product-details.html"><img src="./public/shop_static/picture/cart-1.jpg" alt=""></a></div><div class="cart-info"><h5><a href="product-details.html">'+json[i].Product_Name+'</a></h5><p>$'+json[i].Price+' x '+json[i].Amount+'</p><a href="cart-delete?Cart_ID='+json[i].Cart_ID+'" class="cart-delete" title="Remove this item"><i class="pe-7s-trash"></i></a></div></div>';
        // };
        // let el = document.getElementById("order-checkout");
        // el.innerHTML = str;
        // let el2 = document.getElementById("order-total");
        // el2.innerHTML = '<th>Order Total</th><td><strong>$ '+total+'</strong></td>';
        // let cart_el = document.getElementById("cart-products");

        // cart_el.innerHTML = cart_str;
        // let cart_el2 = document.getElementById("cart-total");
        // cart_el2.innerHTML = '<h5>Total <span>$'+total+'</span></h5>';
        // let cart_el3 = document.getElementById("carts_amount");
        // cart_el3.innerHTML = json.length;
    }
    else if(request.readyState === 4){
        console.log("抱歉，api/myorders連線狀態出了點問題")
    };
});
