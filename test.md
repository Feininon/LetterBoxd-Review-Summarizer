 ```mermaid
graph LR
start-->A[User Input]
A-->B{Format Check}
B-->|URL Construction|C[Construct base URL]
C-->D[Scrape_Multiple_Pages]
D-->E[For Loop]
    E1: for i in range(1, total_pages + 1):
        E2: url = f"{base_url}/page/{i}"
        E3: page_data = scrape_page(url)
        E4: if page_data:
            E5: file.write(f"Page {i}:\n")
            E6: file.write(page_data)
            E7: file.write("\n" + "-"*40 + "\n")
            E8: continue
        E9: print(f"No data found on {url}")
    E10: continue
E-->D
A-->F[Data Storage Name Creation]
F-->G{formatted_name}
G-->C
```
