```mermaid
graph LR;
    User Input --> Movie Title;
    Movie Title --> Review Page;
    Review Page --> Scraping Loop;
    Review Page --> Write to File;
    Scraping Loop --> Write to File;
    Write to File --> Review Text;
    alt Yes/No/Timeout
        |
        |
        |-- Yes --> Write to File;
        |-- No --> Write to File;
        |-- Timeout --> Fail;
```
