# Visualizing Twitter

This project aims to graphically represent the following information about Twitter given a keyword (or hashtag).

  - Number of tweets posted each day in the past week containing the keyword
  - Popular terms appearing in those tweets
  - Geographical positions of authors of those tweets
  - The most retweeted tweets containing the keyword

In this project, Python is used for scraping tweets and outputting processed data in JSON format. The tweets are stored in MongoDB. Data visualization is done by D3.js and Leaflet.js.

> The Twitter Search API is not aimed for completeness, so some tweets may be missing from the result. However, the general trend should not be affected.

To properly view index.html, a web server is required. One simple solution is to use Python's utility module:
```sh
python -m http.server 8080
```
where 8080 is the chosen port for HTTP service.
