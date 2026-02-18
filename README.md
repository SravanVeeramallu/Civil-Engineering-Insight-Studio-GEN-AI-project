Demo Link:https://drive.google.com/file/d/1c85Dm538hVJIh2qba61Sga7iGm--3hNi/view?usp=drive_link
# Civil-Engineering-Insight-Studio-GEN-AI-project

A Streamlit application that uses Google's Gemini AI to analyze civil engineering structures from images.

## Features

- **Upload Image**: Upload an image of a civil engineering structure (bridge, building, dam, etc.).
- **AI Analysis**: Uses Google's Gemini-1.5-Flash (or compatible) model to provide a detailed breakdown including:
    - Type of structure
    - Materials used
    - Estimated dimensions
    - Construction method
    - Notable features
    - Engineering challenges
- **Interactive UI**: Clean and modern user interface built with Steamlit.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SravanVeeramallu/Civil-Engineering-Insight-Studio.git
    cd Civil-Engineering-Insight-Studio
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Google API Key:
        ```env
        GOOGLE_API_KEY=your_api_key_here
        ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Technologies Used

- Python
- Streamlit
- Google Generative AI (Gemini)
- Pillow (PIL)
- Python-dotenv

## License

MIT
