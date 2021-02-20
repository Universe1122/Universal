fetch(url["kisa_notice"])
.then(res => res.json())
.then(res => {
    showKisaNoticeData(res);
})

function showKisaNoticeData(data){
    $(".kisa_data > tbody > tr").remove();

    for(let i = 0; i < data.length; i++){
        let html = kisaNoticeHTML();
        
        html = html.replace("{{kisa-link}}", data[i]["link"])
        html = html.replace("{{kisa-date}}", data[i]["date"])
        html = html.replace("{{kisa-title}}", data[i]["title"])

        $(".kisa_data > tbody").append(html);
    }
}