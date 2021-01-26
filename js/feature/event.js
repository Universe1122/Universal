let left_list = document.getElementsByClassName("fa-chevron-left");
let right_list = document.getElementsByClassName("fa-chevron-right");

for(let i = 0; i < left_list.length; i++){
    left_list[i].addEventListener("click", (e) => {
        let news_value = e.path[2].querySelector("input").value;
        let current_page_num = parseInt($("." + news_value + "-current-page-num").text());
        let total_page_num = parseInt($("." + news_value + "-total-page-num").text());
        
        if(current_page_num == 1)
            return;
        
        let data = news_data[news_value].slice((current_page_num - 2) * post_max);
        showNews(data, "." + news_value);
        
        $("." + news_value + "-current-page-num").text(current_page_num - 1);
    })
    
    right_list[i].addEventListener("click", (e) => {
        let news_value = e.path[2].querySelector("input").value;
        let current_page_num = parseInt($("." + news_value + "-current-page-num").text());
        let total_page_num = parseInt($("." + news_value + "-total-page-num").text());
        
        if(current_page_num == total_page_num)
            return;
        
        let data = news_data[news_value].slice(current_page_num * post_max);
        showNews(data, "." + news_value);
        
        $("." + news_value + "-current-page-num").text(current_page_num + 1);
    })
}