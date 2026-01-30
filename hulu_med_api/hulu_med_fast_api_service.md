# 🧠 Hulu-Med FastAPI Service

A full-stack medical AI demo that exposes the **Hulu-Med vision–language model** as a REST API using **FastAPI**, with a simple web-based front-end for image-based medical question answering.

---

## 📌 Project Overview

**Hulu-Med** is a multimodal medical foundation model capable of understanding:
- 🖼 Medical images (X-ray, CT, MRI, pathology)
- 📝 Natural language medical questions

and generating **human-readable medical answers**.

This project turns the research model into a **real, usable service**:
- A FastAPI backend for inference
- A lightweight browser-based frontend
- One command to run everything

---

## 🏗 Architecture

```
Browser (Frontend)
        ↓
     FastAPI API
        ↓
   Hulu-Med Model
        ↓
 Medical Text Answer
```

---

## ✨ Features

- Upload medical images via browser
- Ask free-form medical questions
- Get AI-generated medical explanations
- REST API for integration with other systems
- Simple UI for demos and presentations

---

## 📂 Project Structure

```
hulu_med_api/
│
├── backend/
│   ├── main.py              # FastAPI app
│   ├── model/               # Hulu-Med model & loaders
│   ├── requirements.txt
│   ├── run.sh
│   └── venv/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── run.sh                   # Run backend + frontend
```

---

## ⚙️ Installation

### 1️⃣ Create virtual environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ PyTorch is large. Installation may take several minutes.

---

## 🚀 Running the Project

From the project root:

```bash
chmod +x run.sh
./run.sh
```

This will start:
- 🧠 Backend API → http://localhost:8000
- 🌐 Frontend UI → http://localhost:3000

---

## 🔌 API Usage

### `POST /infer`

**Request** (multipart form):
- `image`: medical image file
- `prompt`: medical question

**Response**:
```json
{
  "answer": "AI-generated medical explanation"
}
```

---

## 🖥 Frontend Usage

1. Open `http://localhost:3000`
2. Upload a medical image
3. Enter a medical question
4. Click **Analyze**
5. View the AI-generated answer

---

## 📖 About Hulu-Med

Hulu-Med is a **general-purpose medical vision–language model** designed to:
- Perform medical image understanding
- Answer clinical questions
- Generalize across imaging modalities

This project **does not claim clinical validity** and is intended for:
- Research
- Education
- Demonstration purposes only

---

## ⚠️ Disclaimer

🚨 **This system is NOT a medical device.**

- Do not use for real clinical decisions
- Outputs are AI-generated and may be incorrect
- Always consult medical professionals

---

## 🎓 Use Cases

- Academic demos
- AI research prototypes
- Portfolio projects
- Medical AI experimentation

---

## 📜 License

This project follows the license terms of the original **Hulu-Med** repository.
Please refer to the original paper and codebase for usage restrictions.

---

## 🙌 Acknowledgements

- Hulu-Med authors and contributors
- PyTorch & Hugging Face ecosystem
- FastAPI community

---

## ⭐ Future Improvements

- React-based frontend
- Docker & Docker Compose
- GPU optimization
- Model quantization
- Medical report generation

---

**Built for learning, research, and exploration of medical AI systems.**

