
import streamlit as st
from PIL import Image
from ultralytics import YOLO
from huggingface_hub import hf_hub_download
import numpy as np

st.set_page_config(
    page_title="YOLO Tumor Detection",
    page_icon="🧠",
    layout="centered"
)


@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="RawanAlwadeya/YOLOTumorDetection",
        filename="YOLOTumorDetection.pt"
    )
    return YOLO(model_path)

model = load_model()


def detect_tumor(model, pil_image, conf=0.25, imgsz=640):
    """Detect tumor in a given MRI or CT image using the YOLO model."""
    results = model.predict(pil_image, conf=conf, imgsz=imgsz, verbose=False)

    img_bgr = results[0].plot()
    img_rgb = img_bgr[:, :, ::-1]
    pred_img = Image.fromarray(img_rgb)

    pred_classes = results[0].boxes.cls.cpu().numpy().astype(int)
    detected = len(pred_classes) > 0

    return pred_img, detected


st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Detection"])


if page == "Home":
    st.markdown("<h1 style='text-align:center;'>🧠 YOLO Tumor Detection App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Fine-tuned YOLOv8 Model for Brain MRI Analysis</h3>", unsafe_allow_html=True)

    st.write(
        """
        This app uses a **YOLOv8 deep learning model** fine-tuned to detect and highlight 
        **brain tumor regions** in MRI and CT scan images.

        It automatically marks potential tumor areas with bounding boxes, making it easier 
        to visualize and assess abnormal regions in the brain.

        Combining **AI and medical imaging**, this project showcases how modern computer vision 
        can support **early diagnosis and radiology research**.
        """
    )

    st.image(
        "https://www.regionalcancercare.org/wp-content/uploads/2021/08/Human-brain-with-tumor-3D-illustration.jpg",
        caption="Brain Tumor",
        use_container_width=True
    )

    st.info("👉 Go to the **Detection** page from the left sidebar to upload a brain scan and view the model’s prediction.")


elif page == "Detection":
    st.markdown("<h1 style='text-align:center;'>🧠 Brain Tumor Detection</h1>", unsafe_allow_html=True)
    st.write(
        "Upload a **brain MRI or CT image**, and the model will analyze it to detect the presence of a tumor."
    )

    uploaded_file = st.file_uploader("Upload Brain Scan Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file).convert("RGB")

        with st.spinner("Analyzing image for tumor detection..."):
            pred_img, detected = detect_tumor(model, pil_image)

        st.image(pred_img, caption="Model Prediction", use_container_width=True)

        if detected:
            st.error("⚠️ **Tumor Detected** — The model found a region that may indicate a tumor.")
        else:
            st.success("✅ **No Tumor Detected** — The scan appears to be free of visible tumor regions.")