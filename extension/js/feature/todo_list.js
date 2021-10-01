document.querySelector("div.menu > a").addEventListener("click", () => {
    const $control = $(".todo-list-box");
    
    if($control.css("display") === "none")
        showToDoList($control);
    else
        hideToDoList($control);
})


function showToDoList($control){
    $control.slideDown();
    
}

function hideToDoList($control){
    $control.slideUp();
}

function getToDoList(){
    // TODO 크롬에 저장된 데이터 가져오기
}