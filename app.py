import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

st.title("Image Analyzer")

@st.cache_resource
def load_model():
    model_name = "Salesforce/blip-image-captioning-base"

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name)

    return processor, model


processor, model = load_model()

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize((384, 384))

    st.image(image, use_container_width=True)

    if st.button("Analyze"):

        inputs = processor(image, return_tensors="pt")

        output = model.generate(**inputs, max_new_tokens=100)

        result = processor.decode(output[0], skip_special_tokens=True)

        st.subheader("Result")
        st.write(result)