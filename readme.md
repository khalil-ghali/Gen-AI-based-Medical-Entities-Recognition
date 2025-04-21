# Gen AI-Based Medical Entities Recognition

This repository provides a solution for extracting medical entities from text using state-of-the-art generative AI models. It leverages the power of the `langchain` framework and Hugging Face's `transformers` to create an efficient pipeline for identifying and extracting structured information from unstructured medical text.

## Features

- **Entity Extraction**: Extracts structured medical entities such as doctor and patient information from text.
- **Customizable Schema**: Uses a predefined schema (`DoctorPatientSchema`) for entity extraction, which can be extended or modified as needed.
- **Hugging Face Integration**: Utilizes the `tiiuae/falcon-7b-instruct` model from Hugging Face for high-quality language understanding and generation.
- **Scalable Pipeline**: Designed to process multiple text inputs efficiently.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gen-ai-medical-entities-recognition.git
   cd gen-ai-medical-entities-recognition
   ```

## How to Run

Follow these steps to run the repository:

### Prerequisites

1. **Python**: Ensure you have Python 3.8 or higher installed.
2. **Dependencies**: Install the required Python packages listed in `requirements.txt`.

### Steps to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following variables:
   ```plaintext
   DATA_FILE_PATH=/path/to/your/data/file.txt
   HUGGINGFACE_API_TOKEN=your_huggingface_api_token
   ```

3. **Run the Application**:
   Navigate to the `src` directory and execute the main script:
   ```bash
   python main.py
   ```

4. **View Results**:
   The extracted medical entities will be printed in the console.

### Example Input and Output

- **Input**: A text file containing unstructured medical conversations.
- **Output**: Structured medical entities such as doctor and patient information.

### Notes

- Ensure the `DATA_FILE_PATH` points to a valid text file containing the medical conversations.
- Obtain a Hugging Face API token from [Hugging Face](https://huggingface.co/) and set it in the `.env` file.

### Troubleshooting

- If you encounter issues with missing dependencies, ensure all packages in `requirements.txt` are installed.
- Verify that the `.env` file is correctly configured and accessible.
- Contact us