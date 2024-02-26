var a = new XMLHttpRequest();
a.open('get','http://127.0.0.1/api/products');
a.send();
a.addEventListener("readystatechange", () => {
    if(a.readyState === 4 && a.status === 200 ){
        // console.log(a.responseText);
        console.log(a.readyState,a.status);
        let response=a.responseText;
        let json=JSON.parse(response);
        // let users=json[8].Product_Name
        let array = [];
        let ran = 0;
        for(let i=0;i<8;i++){
            ran = Math.floor(Math.random()*json.length);
            while(array.includes(ran)==true){
                ran = Math.floor(Math.random()*json.length);
            };
            array.push(ran);
            switch(true){
                case (i==0):
                    var str='<div class="isotope-item chair home-decor col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title" id="first"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></div></div></div></div>';
                    break;
                case (i==1):
                    var str2='<div class="isotope-item ptable col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></div></div></div></div>';
                    break;
                case (i==2):
                    var str3='<div class="isotope-item lighting col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></div></div></div></div>';
                    break;
                case (i==3):
                    var str4='<div class="isotope-item ptable home-decor col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></span></div></div></div></div>';
                    break;
                case (i==4):
                    var str5='<div class="isotope-item chair lighting col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></span></div></div></div></div>';
                    break;
                case (i==5):
                    var str6='<div class="isotope-item chair col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></span></div></div></div></div>';
                    break;
                case (i==6):
                    var str7='<div class="isotope-item ptable col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Productgvhjnmf bsgvh mbj Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></span></div></div></div></div>';
                    break;
                case (i==7):
                    var str8='<div class="isotope-item home-decor lighting col-xl-3 col-lg-4 col-md-6 col-12 mb-50"><div class="product-item text-center"><!-- Product Image --><div class="product-img"><!-- Image --><a class="image" href="product-details?Product_ID='+json[ran].Product_ID+'"><img src="'+json[ran].Image+'" alt="" width="388px" height="422px"></a><!-- Action Button --><div class="action-btn fix"><!-- <a href="#" title="Add to Cart"><i class="pe-7s-cart"></i>add to cart</a> --></div></div><!-- Portfolio Info --><div class="product-info text-left"><!-- Title --><h5 class="title"><a href="product-details?Product_ID='+json[ran].Product_ID+'">'+json[ran].Product_Name+'</a></h5><!-- Price Ratting --><div class="price-ratting fix"><span class="price float-start"><span class="new">$'+json[ran].Price+'</span></span></span></div></div></div></div>';
                    break;
            };
        };
        console.log(array);
        let el = document.getElementById("index-products");
        el.innerHTML=str+str2+str3+str4+str5+str6+str7+str8;
        // el.textContent = json.length;
    }
    else if(a.readyState === 4){
        console.log("抱歉，連線狀態出了點問題")
    };
});
