import re

def clean_reviews(text):
    # Define regex pattern to extract reviews with star ratings
    review_pattern = re.compile(r'([★]+[\u00BD]?)\s+Watched by .*?\d{1,2} \w{3} \d{4}\s+(.+?)(?=\n\n|$)', re.DOTALL)
    
    # Find all matches of reviews
    reviews = review_pattern.findall(text)
    
    # Format extracted reviews
    formatted_reviews = [f"{rating.strip()}\n{review.strip()}" for rating, review in reviews]
    
    return '\n\n'.join(formatted_reviews)
def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        input_text = file.read()
    return input_text
  
# Usage
file_path = "the substance 12pages.txt"  # Replace with your actual file path
formatted_text = process_file(file_path)
raw_reviews=formatted_text
cleaned_reviews = clean_reviews(raw_reviews)
print(cleaned_reviews)  # Cleaned review text
