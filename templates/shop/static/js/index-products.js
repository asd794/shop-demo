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
        let str="";
        var el = document.getElementById("result");
        for(let i=0;i<json.length;i++){
            let content="<li>"+json[i].Product_Name+"</li>";
            str+=content;
        }
        el.innerHTML = str;
        // el.textContent = json.length;
    }
    else if(a.readyState === 4){
        console.log("抱歉，連線狀態出了點問題")
    } 
});