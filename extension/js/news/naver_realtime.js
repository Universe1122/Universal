fetch(url["naver_realtime"])
.then((res) => res.json())
.then((res) => {
    showNaverRealtime(res)
})

function showNaverRealtime(data){
    let table_idx = 0;
    const result_table = "";

    $(".naver-realtime-loading").remove();

    for(let i = 0; i < 10; i++){
        if(i == 5) table_idx = 1;

        let html = naverRealTimeHTML();

        html = html.replace("{{ranking_index}}", data[i].rank);
        html = html.replace("{{ranking_value}}", data[i].rank_name);
        html = html.replace("{{ranking_url}}", data[i].url);

        $(".naver-realtime")[table_idx].innerHTML += html;
    }

}