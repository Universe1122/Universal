fetch(url["hackerone"])
.then(res => res.json())
.then(res => {
    $(".hackerone-loading").remove();
    
    const show_list_cnt = 8;

    for(let i=0; i<show_list_cnt; i++){
        let html = hackeroneHTML();

        if(res[i]["severity"] == "Critical"){
            let severity_html = `<b class="btn_red">Critical</b>`;
            html = html.replace("{{severity}}", severity_html);
        }
        else if(res[i]["severity"] == "High"){
            let severity_html = `<b class="btn_orange">High</b>`;
            html = html.replace("{{severity}}", severity_html);
        }
        else if(res[i]["severity"] == "Medium"){
            let severity_html = `<b class="btn_yellow">Medium</b>`;
            html = html.replace("{{severity}}", severity_html);
        }
        else if(res[i]["severity"] == "None"){
            let severity_html = `<b class="btn_green">None</b>`;
            html = html.replace("{{severity}}", severity_html);
        }
        
        html = html.replace("{{link}}", res[i]["link"]);
        html = html.replace("{{title}}", res[i]["title"]);
        html = html.replace("{{target}}", res[i]["target"]);
        html = html.replace("{{timestamp}}", res[i]["timestamp"]);

        $(".hackerone-data").append(html);
    }
})