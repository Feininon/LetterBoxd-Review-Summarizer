```mermaid
graph LR;
    User Input[Enter Movie Title] --> Movie Title;
    Movie Title -->|Scrape Review Page| Review Page;
    Review Page -->|Start Scraping Loop| Scraping Loop;
    Scraping Loop -->|Success/Failed| Write to File;
    Write to File --> Review Text[Review Data];
    alt Yes/No/Timeout
        |
        |
        |-- Yes --> Review Text;
        |-- No --> No Data;
        |-- Timeout --> Error;
```
