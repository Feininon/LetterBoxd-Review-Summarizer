 ```mermaid
sequenceDiagram
    participant User as User
    participant Program as Program
    participant Request as Request
    participant Response as Response
    participant BeautifulSoup as BSoup
    participant File as File

    User->>Program: Enter movie name
    Program->>Program: Convert input to lowercase and replace spaces with "-"
    Program->>Program: Construct base URL
    Program->>Program: Set total pages (or input user's choice)
    Program->>Program: Define function scrape_multiple_pages(base_url, total_pages)
    Program->>Program: Inside the function define a for loop to iterate through pages
        for i in range(1,total_pages+1):
            Program->>Program: Construct URL with current page number
            Program->>Program: Call scrape_page(URL)
            Program->>Program: Store returned value (page data or None) in page_data
            Program->>Program: If page_data is not None, write to file
                if page_data:
                    Program->>File: Write page number and page_data to the file
                    Program->>File: Write a line of dashes to separate pages
                else:
                    Program->>Program: Print "No data found on {URL}"

    Function scrape_page as function
    function->>Request: Send GET request to URL
    Request->>Response: Receive response from server
    Response->>function: Check status code (200 or not)
        if response.status_code == 200:
            function->>BSoup: Create BeautifulSoup object using the response text
            function->>BSoup: Find all paragraph tags (<p>)
            function->>function: Iterate through found paragraphs and join their texts into one string
            function->>Program: Return page_data as a string
        else:
            function->>Program: Print "Failed to retrieve page {URL}"
            function->>Program: Return None
```
