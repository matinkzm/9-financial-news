#9-financial-news

This project is 9th project from this link : https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea

in this project i created a small ETL data pipeline to get financial news and remove redundancy and save it into a csv file.

first I get the full data using request library and convert it to html using beautiful soup.
by inspecting in this link : https://www.businesstoday.in/latest/economy you can see that the news are in 'a' tag.

also it has two classes of data in 'a' tag : none and <class 'bs4.element.NavigableString'>
we need the second one.

after selecting the correct class we remove news shorter that 35 char because they are false data.

at last load the clean data into a csv file.