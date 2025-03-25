import ollama
from star_clean import clean_reviews

# Load the text data from the file
def load_reviews(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        text_data = file.read()
    return text_data

# Function to send text to Llama 3.2 for summarization
def summarize_reviews_with_llama(text_data):
    # Append instruction to the text data
    text_data += "\n\nPlease respond in English."
    
    # Call the Llama 3.2 model
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", 
             "content": f'''FORMAT:
             there will be starts which indicate the rating out of 5 and  "Watched by [USERNAME] [DATE]"
             [REVIEW]
             consider the ratings and reviews and summarize it within 250 words 
             respond in english
             do not try to find the movie name just summarize the reviews
             EVEN IF THE REVIEW IS IN SOME OTHER LANGUAGE PLEASE RESPOND IN ENGLISH
             here is the reviews: \n{text_data}
             '''}
        ]
    )
    
    # Print the entire response to debug
    # print("Response from Llama 3.2:", response)  
    
    # Extract the summary from the correct structure
    if 'message' in response and 'content' in response['message']:
        return response['message']['content']
    else:
        return "No summary available."

# Main code
file_path = "the-brutalist_reviews.txt"  # Path to your file with reviews
text_data = load_reviews(file_path)
cleaned_data = clean_reviews(text_data)
# Call the summarizer
summary = summarize_reviews_with_llama(cleaned_data)

# Display the summary
print("Summary of Reviews:\n", summary)
