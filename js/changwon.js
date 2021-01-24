changwonRequest(url["changwon_computer"]);

const menu_event = document.getElementsByClassName("changwon-menu");
for(let i = 0; i < menu_event.length; i++){
    menu_event[i].addEventListener("click", (ele) => {
        if(ele.path[0].innerText.indexOf("창원대 컴공") != -1)
            changwonRequest(url["changwon_computer"]);
        else
            changwonRequest(url["changwon_waggle"]);
    })
}


function changwonRequest(url){
    $(".changwon_data > tbody > tr").remove();
    const html = `<tr>
                        <td><img src="/image/loading2.gif" width="100px"></td>
                    </tr>`
    $(".changwon_data > tbody").append(html);

    fetch(url)
    .then(res => res.json())
    .then(res => {
        showChangwonData(res);
    })
}

function showChangwonData(data){
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