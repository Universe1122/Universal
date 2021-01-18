function newsCardHTML(){
	return `<a href="{{news_link}}">
				<div class="news-card">
					<div class="news-thumbnail">
						<img src="{{news_thumbnail}}">
					</div>
					<div class="news-title">
						{{news_title}}
					</div>
					<div class="news-date">
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