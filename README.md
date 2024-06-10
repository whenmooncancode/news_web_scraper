This Python script fetches articles from Hacker News over multiple pages and filters them based on their popularity. 
It specifically targets articles with at least 100 votes, and then sorts these articles by the number of votes they've received.

Features
 -Multi-page Scraping: The script can be configured to scrape a specified number of pages from Hacker News.
 -Vote Filtering: Only articles with 100 or more votes are considered, ensuring that only popular articles are fetched.
 -Sorting: Articles are sorted by their vote count, making it easy to identify the most popular content.
 -Customizable: Users can modify the number of pages to scrape by adjusting the num parameter in the get_all_pages function.
