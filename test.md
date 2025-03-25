 ```mermaid
graph LR
start->User Input
User Input->Format Check
    Format Check->URL Construction
        URL Construction->Scrape Multiple Pages
            Scrape Multiple Pages->For Loop
                For Loop->Construct Page URL
                For Loop->Call scrape_page(url) with the constructed url
                For Loop->Check if data is found
                    If Data Found->Write Data to File
                    Else->Print "No data found on {URL}"
            Scrape Multiple Pages->Return Data (or None)
        URL Construction->Data Storage Name Creation
            Data Storage Name Creation->Create formatted name
        URL Construction->Pass formatted_name and total pages to scrape_multiple_pages function
```
