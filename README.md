Image Analyzer (AI Vision App)

A simple AI-powered web app that analyzes and describes images using deep learning. Built with Streamlit and Hugging Face Transformers.

Features
Upload any image (JPG, PNG)
AI-generated image description 
Detects objects, people, and scene context
Fast and simple web interface
Runs locally on your system

Model Used
This project uses:
BLIP
(Salesforce/blip-image-captioning-base)

BLIP is a lightweight vision-language model that generates captions for images.

Tech Stack
Python 
Streamlit 
PyTorch 
Hugging Face Transformers 
Pillow 

Project Structure
image_analyzer/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies

How It Works
1. Upload an image
2. The model processes the image
3. AI generates a caption describing the image
4. Output is displayed on screen

Future Improvements
1. Chat with image feature
2. Faster model optimization
3. Object detection support
4. PDF report generation
