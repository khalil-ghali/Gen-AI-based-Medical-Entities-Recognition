from dotenv import load_dotenv
import os
from data_loader import DataLoader
from text_splitter import TextSplitter
from entity_extraction import EntityExtraction

def main():
    # Load environment variables
    load_dotenv()
    data_file_path = os.getenv("DATA_FILE_PATH")
    huggingface_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

    # Load conversation data
    data_loader = DataLoader(data_file_path)
    conversation = data_loader.load_conversation()

    # Split text into chunks
    text_splitter = TextSplitter()
    texts = text_splitter.split_text(conversation)

    # Extract entities
    entity_extraction = EntityExtraction(huggingface_api_token)
    extracted_data = entity_extraction.extract_entities(texts)

    # Output results
    print("Extracted Data:")
    for data in extracted_data:
        print(data)

if __name__ == "__main__":
    main()