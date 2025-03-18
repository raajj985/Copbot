
# CopBot AI Assistant

CopBot AI Assistant is a Streamlit application designed to provide information and assistance related to law enforcement in Tamil Nadu. It leverages natural language processing to answer queries based on embedded legal and procedural documents.

## Features

- **Query Answering**: Ask questions related to law enforcement procedures, legal guidelines, and more.
- **FAQ Section**: Quick access to common queries and their answers.
- **User-Friendly Interface**: Easy-to-navigate interface with Streamlit.

## Project Structure

```
your-project-directory/
│
├── app.py                  # Main Streamlit application file
├── requirements.txt        # Python dependencies
├── embeddings_cache_copbot.pkl  # Embeddings cache file
└── render.yaml             # Render configuration file (optional)
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI API Key

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:8501`.

## Deployment on Render

### Steps

1. **Push to GitHub**:
   - Push your project to a GitHub repository.

2. **Deploy on Render**:
   - Go to [Render](https://render.com/).
   - Click on "New" and select "Web Service".
   - Connect your GitHub repository.
   - Select your repository and branch.
   - Set the build command to `pip install -r requirements.txt`.
   - Set the start command to `streamlit run app.py`.
   - Click on "Create Web Service".

3. **Environment Variables**:
   - Set your `OPENAI_API_KEY` as an environment variable in Render's dashboard settings for security.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [your-email@example.com](mailto:your-email@example.com).
