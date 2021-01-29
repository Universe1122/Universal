const api = 'e46e811ad359e15423c1777468c635b0';
const city = "seoul"
const weather_url = `https://pro.openweathermap.org/data/2.5/forecast/hourly?q=${city}&appid=${api}&mode=json`
fetch(weather_url)
.then(res => res.json())
.then(console.log(res));