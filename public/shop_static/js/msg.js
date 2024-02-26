function funMsg(msg){
    console.log("有進入msg.js funMsg");
    // console.log(msg);
    if(msg == '帳密註冊完成'){
        // document.location.href="https://booooo.online/";
        let el =document.getElementById('button');
        el.innerHTML='<div>'+msg+'<a href="http://127.0.0.1/login"><br><button>立即登入</button></a>';
    }else if(msg = '上架完成'){
        let el =document.getElementById('button');
        el.innerHTML='<div>'+msg+'<a href="http://127.0.0.1"><br><button>返回首頁</button></a>';
    };
};
// document.location.href="https://booooo.online/";