for(let i = 0; i < Object.keys(url).length; i++){
	getNews(Object.keys(url)[i], url[Object.keys(url)[i]]);
}

function getNews(news, url){
	fetch(url)
	.then((res) => res.json())
	.then((res) => {
		news_data[news] = res;
		
		$("." + news + "-total-page-num").text(calculatePage(news_data[news].length));
		showNews(res, "." + news);
	})
}

function showNews(data, selector){
	$(selector).children().remove();
	
	for(let i = 0; i < data.length; i++){
		let html = newsCardHTML();

		html = html.replace("{{news_link}}", data[i].link);
		html = html.replace("{{news_title}}", data[i].title);
		html = html.replace("{{news_date}}", data[i].date);
		
		if(data[i].img == "None")
			html = html.replace("{{news_thumbnail}}", "https://www.tellerreport.com/images/no-image.png");
		else
			html = html.replace("{{news_thumbnail}}", data[i].img);

		$(selector).append(html);

		if(i+1 == 6)
			break;
	}
}

function calculatePage(news_length){
	return Math.ceil(news_length / post_max);
}