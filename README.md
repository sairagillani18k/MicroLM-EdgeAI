# MicroLM-EdgeAI: Small Language Model API for NLP on Edge Devices

![MicroLM-EdgeAI](https://user-images.githubusercontent.com/your-image.jpg)

## Overview
**MicroLM-EdgeAI** is a lightweight NLP API that runs small language models (**SLMs**) like TinyBERT and DistilBERT for **text summarization** and **sentiment analysis**. This project is designed for **edge AI applications**, making it ideal for **resource-constrained devices** such as **Raspberry Pi, Jetson Nano, and low-power servers**.

---

##  Features
✅ **Fast & Efficient** – Runs on small devices with minimal hardware requirements.  
✅ **Text Summarization** – Condense long text into key points.  
✅ **Sentiment Analysis** – Classify text as positive, negative, or neutral.  
✅ **Lightweight & Optimized** – Uses pre-trained small models for low latency.  
✅ **REST API** – Simple endpoints for easy integration.  

---

## Setup & Installation

### 🔹 1. Clone the Repository  
```
git clone https://github.com/yourusername/MicroLM-EdgeAI.git
cd MicroLM-EdgeAI
```

### 🔹 2. Install Dependencies  
```
pip install torch transformers flask
```

### 🔹 3. Run the API Server  
```
python app.py
```
The server will start at **http://127.0.0.1:5000**.

---

## 🚀 How to Use the API

### 📝 **Text Summarization**  
**Endpoint:** `/summarize`  
**Method:** `POST`  
**Request Body (JSON):**  
```
{
    "text": "Artificial Intelligence (AI) is revolutionizing many industries, bringing automation and insights that were previously impossible..."
}
```
**Response (JSON):**  
```
{
    "summary": "AI is transforming industries with automation and insights."
}
```

---

### 📊 **Sentiment Analysis**  
**Endpoint:** `/sentiment`  
**Method:** `POST`  
**Request Body (JSON):**  
```
{
    "text": "I love this project! It's absolutely amazing."
}
```
**Response (JSON):**  
```
{
    "sentiment": {
        "label": "POSITIVE",
        "score": 0.99
    }
}
```

---

## 🌍 Deployment (Optional)  

### 🔹 Run on Raspberry Pi or Jetson Nano  
Install dependencies and run the server as usual.  

### 🔹 Deploy with Docker  
```
docker build -t microlm-edgeai .
docker run -p 5000:5000 microlm-edgeai
```

---


