function newsCardHTML(){
	return `<a href="{{news_link}}">
				<div class="news-card">
					<div class="news-thumbnail">
						<img src="{{news_thumbnail}}">
					</div>
					<div class="news-title">
						{{news_title}}
					</div>
					<div class="news-date date">
						{{news_date}}
					</div>
				</div>
			</a>`;
}

function naverRealTimeHTML(){
	return `<tr>
				<td class="ranking">{{ranking_index}}</td>
				<td class="ranking-value"><a href="{{ranking_url}}">{{ranking_value}}</a></td>
			</tr>`;
}

function toDoListForm(){
	return ``;
}

function changwonComputerHTML(mode){
	if(mode == "notice"){
		return `<tr>
					<td class="changwon-notice-place"><b class="btn_red">공지</b></td>
					<td class="changwon-title"><a href="{{changwon-computer-link}}">{{changwon-computer-title}}</a></td>
					<td class="changwon-date date">{{changwon-computer-date}}</td>
				</tr>`;
	}
	else if(mode == "post"){
		return `<tr>
					<td class="changwon-notice-place"></td>
					<td class="changwon-title"><a href="{{changwon-computer-link}}">{{changwon-computer-title}}</a></td>
					<td class="changwon-date date">{{changwon-computer-date}}</td>
				</tr>`;
	}
}