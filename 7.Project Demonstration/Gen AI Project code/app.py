from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI with API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found. Please add GOOGLE_API_KEY to your .env file.")
    st.stop()

genai.configure(api_key=api_key)


def get_gemini_response(input_text, image, prompt):
    """
    Function to get response from Gemini model.

    Args:
        input_text: User input text
        image: List containing image data in the format required by Gemini
        prompt: The prompt to send to the model

    Returns:
        str: The text response from the model
    """
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):
    """
    Function to read the uploaded image and format it for Gemini Pro model.

    Args:
        uploaded_file: The uploaded file object from Streamlit

    Returns:
        list: A list containing image data formatted for Gemini API

    Raises:
        FileNotFoundError: If no file is uploaded
    """
    if uploaded_file is not None:
        # Read the file's binary data
        bytes_data = uploaded_file.getvalue()

        # Create image parts in the required format
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


def main():
    """Main function to run the Streamlit application."""
    st.set_page_config(page_title="Civil Engineering Structure Analysis", layout="centered")

    st.header("🏗️ Civil Engineering Structure Analysis")
    st.subheader("Powered by Google Gemini AI")

    # Description
    st.markdown("""
    This application uses Google's Gemini AI model to analyze civil engineering structures
    from images. Upload an image of a structure and provide a prompt to get detailed analysis.
    """)

    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📝 Input Prompt")
        input_prompt = st.text_area(
            "Enter your prompt for analysis:",
            value="Analyze this civil engineering structure image. Provide a detailed breakdown including: type of structure, materials used, estimated dimensions, construction method, notable features, and any engineering challenges visible.",
            height=150
        )

    with col2:
        st.subheader("🖼️ Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image of a civil engineering structure:",
            type=["jpg", "jpeg", "png", "gif", "bmp"]
        )

    if uploaded_file is not None:
        st.success("Image uploaded successfully!")

        # Display the uploaded image
        st.subheader("Uploaded Image Preview:")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        # Create a submit button
        submit_button = st.button("🔍 Analyze Structure", type="primary")

        if submit_button:
            if input_prompt.strip() == "":
                st.error("Please enter a prompt for analysis.")
            else:
                with st.spinner("Analyzing the structure..."):
                    try:
                        # Prepare the image for Gemini
                        image_data = input_image_setup(uploaded_file)

                        # Get response from Gemini
                        response = get_gemini_response(
                            input_text="Analyze the following image:",
                            image=image_data,
                            prompt=input_prompt
                        )

                        # Display the response
                        st.subheader("📊 Analysis Results:")
                        st.markdown(response)

                        # Add a copy button for convenience
                        st.download_button(
                            label="📥 Download Analysis",
                            data=response,
                            file_name="structure_analysis.txt",
                            mime="text/plain"
                        )

                    except FileNotFoundError as e:
                        st.error(f"Error: {e}")
                    except Exception as e:
                        st.error(f"An error occurred during analysis: {str(e)}")
    else:
        st.info("👆 Please upload an image to get started with the analysis.")


if __name__ == "__main__":
    main()
