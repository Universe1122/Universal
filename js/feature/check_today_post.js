function checkTodayPost(){
    const now = new Date();
    const year = now.getFullYear(),
            month = padLeft(now.getMonth() + 1, 2),
            day = padLeft(now.getDate(), 2);
    const today = year + "." + month + "." + day;

    for(let i = 0; i < $(".date").length; i++){
        if($(".date")[i].innerText.indexOf(today) != -1){
            $($(".date")[i]).css("color", "red");
        }
    }
}