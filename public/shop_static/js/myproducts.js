function myproducts(m_id){
    let request = new XMLHttpRequest();
    request.open('get','http://127.0.0.1/api/products');
    request.send();
    request.addEventListener("readystatechange", () => {
        if(request.readyState === 4 && request.status === 200 ){
            // console.log(a.responseText);
            console.log(request.readyState,request.status);
            let response=request.responseText;
            let json_myproducts=JSON.parse(response);
            console.log('api/myproducts連線正常');
            console.log(json_myproducts);
            console.log(json_myproducts[7].Member_ID);
            // arr_mid=Object.keys(json_myorders);
            // console.log(arr_mid);
            // arr_value=Object.values(json_myorders);
            // for(let i =0; i <json_myproducts.length ;i++){
            //     console.log(i)
            //     if (){}
            // };
            let str='';
            for(let i =0 ; i <json_myproducts.length ;i++){
                if (m_id == json_myproducts[i].Member_ID){
                    str+='<a href="/product-details?Product_ID='+json_myproducts[i].Product_ID+'" style="font-size: 30px;line-height: 50px;">'+json_myproducts[i].Product_Name+'('+json_myproducts[i].Product_ID+')</a><br>';
                };
            };
            // let str='<a href="/index" style="font-size: 30px;line-height: 50px;">一</a><br>';
            let el = document.getElementById('my_products');
            el.innerHTML = str;
    
        }
        else if(request.readyState === 4){
            console.log("抱歉，api/myorders連線狀態出了點問題")
        };
    });
    
};

// let request = new XMLHttpRequest();
// request.open('get','http://127.0.0.1/api/products');
// request.send();
// request.addEventListener("readystatechange", () => {
//     if(request.readyState === 4 && request.status === 200 ){
//         // console.log(a.responseText);
//         console.log(request.readyState,request.status);
//         let response=request.responseText;
//         let json_myproducts=JSON.parse(response);
//         console.log('api/myproducts連線正常');
//         console.log(json_myproducts);
//         console.log(json_myproducts[7].Member_ID);
//         // arr_mid=Object.keys(json_myorders);
//         // console.log(arr_mid);
//         // arr_value=Object.values(json_myorders);
//         // for(let i =0; i <json_myproducts.length ;i++){
//         //     console.log(i)
//         //     if (){}
//         // };
//         let str='<a href="/index" style="font-size: 30px;line-height: 50px;">一</a><br>';
//         let el = document.getElementById('my_products');
//         el.innerHTML = str;

//     }
//     else if(request.readyState === 4){
//         console.log("抱歉，api/myorders連線狀態出了點問題")
//     };
// });
