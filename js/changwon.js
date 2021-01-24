fetch(url["changwon_computer"])
.then(res => res.json())
.then(res => {
    showChangwonComputer(res);
})

function showChangwonComputer(data){
    $(".changwon_data > tbody > tr").remove();

    const notice_count_max = 3;
    const post_count_max = 4;
    let notice_count = 0;
    let post_count = 0;

    for(let i = 0; i < data.length; i++){
        let html = '';
        if(data[i]["notice"] === "true" && notice_count != notice_count_max){
            html = changwonComputerHTML("notice");
            notice_count++;
        }
        else if(data[i]["notice"] === "false" && post_count != post_count_max){
            html = changwonComputerHTML("post");
            post_count++;
        }

        if(html.length == 0) continue;

        html = html.replace("{{changwon-computer-link}}", data[i]["link"]);
        html = html.replace("{{changwon-computer-title}}", data[i]["title"]);
        html = html.replace("{{changwon-computer-date}}", data[i]["date"]);

        $(".changwon_data > tbody").append(html);
    }
}