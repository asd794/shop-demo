function productAmount (amount){
    console.log("有進來productAmount方法")
    let el = document.getElementById("amount-option");
    let str = '<option value="0">數量</option>';
    for (let i = 1 ;i <= amount ;i++){
        str+= '<option value="'+i+'">'+i+'</option>'; 
    };
    console.log(str);
    el.innerHTML = str;
};
// productAmount();
function asd(){
    console.log("有叫到asd方法");
};

function otherClear (){
    let el = document.getElementById("other-products");
    el.innerHTML = "";
};


