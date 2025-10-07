# **🧠 YOLOTumorDetection: Fine-Tuned YOLOv8 for Brain Tumor Detection**

**YOLOTumorDetection** is a deep learning project designed to detect and localize **brain tumors** in MRI images using **YOLOv8**.  
It demonstrates a complete **medical imaging workflow** — including **data exploration & visualization**, **YOLOv8 fine-tuning**, **evaluation**, and **deployment** using **Streamlit** and **Hugging Face Spaces**.

---

## **🎥 Demo**

- 🔗 [View LinkedIn Demo Post](https://www.linkedin.com/posts/rawan-alwadeya-17948a305_machinelearning-medicalimaging-healthcareai-activity-7381092953752186880-Ul23?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE3YzG0BAZw48kimDDr_guvq8zXgSjDgk_I)  
- 🌐 [Try the App Live on Streamlit](https://yolotumordetection-fny43wuxdseqglmbeudsrx.streamlit.app/)  
- 🤗 [Explore on Hugging Face](https://huggingface.co/RawanAlwadeya/YOLOTumorDetection)  

![App Demo](https://github.com/rawan-alwadiya/YOLOTumorDetection/blob/main/YOLO%20Tumor%20Detection%20App.png)  
![Detection Example](https://github.com/rawan-alwadiya/YOLOTumorDetection/blob/main/Brain%20Tumor%20Detection.png)

---

## **📘 Project Overview**

The project follows an end-to-end **object detection pipeline** focused on medical image analysis:  
- **Exploration & Visualization** – Analyzed MRI dataset and tumor annotations  
- **Transfer Learning (YOLOv8)** – Fine-tuned pretrained YOLOv8 model for medical detection  
- **Evaluation** – Measured precision, recall, and mAP metrics  
- **Deployment** – Built an interactive **Streamlit app** and hosted it on **Hugging Face Spaces**

---

## **🎯 Objective**

Develop and deploy a high-performing **object detection model** to automatically identify and localize **tumorous regions** in brain MRI scans.  
This project supports **diagnostic assistance**, **medical image interpretation**, and **AI research in healthcare**.

---

## **🧠 Modeling Approach**

- **Base Model:** YOLOv8 (Ultralytics implementation, pretrained on COCO dataset)  
- **Fine-Tuning:** Applied transfer learning on the Brain Tumor MRI dataset  
- **Prediction Outputs:** Bounding boxes highlighting detected tumor regions with confidence scores  

---

## **📊 Performance**

**YOLOv8 Brain Tumor Detection Model**  
- **Precision:** `91.16%`  
- **Recall:** `96.87%`  
- **mAP@50:** `96.63%`   

These results show that the fine-tuned YOLOv8 model achieves **strong detection accuracy** and **robust generalization** across diverse MRI images.

---

## **📁 Dataset**

- **Content:** Brain MRI images labeled with tumor regions  
- **Annotations:** Bounding boxes around tumorous areas  
- **Usage:** Training, validation, and testing for YOLOv8 fine-tuning  

---

## **⚙️ Project Workflow**

- **Data Exploration & Visualization** – Inspected MRI dataset and bounding boxes  
- **Transfer Learning** – Fine-tuned YOLOv8 on the tumor detection dataset  
- **Evaluation** – Assessed performance with precision, recall, and mAP metrics  
- **Deployment** – Developed Streamlit web app and published on Hugging Face  

---

## **🚀 Deployment**

Users can upload MRI images to instantly detect and visualize **tumorous regions** using bounding boxes and confidence scores — enabling **fast, reliable medical analysis**.

**Live Links:**  
- Streamlit App: [YOLOTumorDetection](https://yolotumordetection-fny43wuxdseqglmbeudsrx.streamlit.app/)  
- Hugging Face Repo: [YOLOTumorDetection](https://huggingface.co/RawanAlwadeya/YOLOTumorDetection)

---

## **📚 Tech Stack**

**Languages & Libraries:**  
- Python, NumPy, Pandas  
- PyTorch, Ultralytics YOLOv8  
- OpenCV, Matplotlib  
- Streamlit (Deployment)  

**Techniques:**  
- Transfer learning  
- Object detection & bounding box visualization  
- Model evaluation (precision, recall, mAP)  
- Web deployment with Streamlit and Hugging Face  

---

## **💡 Impact**

This project demonstrates how **AI and deep learning** can assist in **medical diagnosis**, helping radiologists and healthcare professionals:  
- Detect tumors faster and more accurately  
- Support early diagnosis and treatment planning  
- Advance research in **medical imaging AI**

---

✨ With **YOLOTumorDetection**, AI-driven **medical imaging systems** can assist clinicians in detecting brain tumors efficiently — improving **diagnostic accuracy**, **speed**, and **patient outcomes**.
