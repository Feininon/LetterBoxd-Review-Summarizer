import ollama

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
            {"role": "user", "content": f"in the following there will be some reviews and stuff identify each review and summarize every review with 250 words EVEN IF THE REVIEW IS IN SOME OTHER LANGUAGE PLEASE RESPOND IN ENGLISH: \n{text_data}"}
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
file_path = "the substance 12pages.txt"  # Path to your file with reviews
text_data = load_reviews(file_path)

# Call the summarizer
summary = summarize_reviews_with_llama(text_data)

# Display the summary
print("Summary of Reviews:\n", summary)
