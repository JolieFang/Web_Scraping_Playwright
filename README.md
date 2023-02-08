# Web_Scraping_Playwright
The project utilized Playwright for performing web scraping of monthly visitor data from websites in a headless mode on a Linux server. The implementation was containerized within a Docker container to provide increased efficiency and scalability. To make the scraped data easily accessible, a Flask web server was integrated to serve the data through HTTP requests.Lastly, Python script was ran on the local machine that calls Flask 5 times concurrently as a stress test. 

# Tools and Libraies used:
- Playwright
- Docker
- Flask

# How to use:

- Run: "docker build -t web_scrap . && docker run -p 3000:3000 web_scrap"
- Endpoint to call: http://localhost:3000/

# Result:
![alt text](https://github.com/JolieFang/Web_Scraping_Playwright/blob/main/Result.jpeg)
