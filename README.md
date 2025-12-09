# 🛡️ HateShield AI  
### Multilingual Hate Speech Detection Web Application

HateShield AI is a full-stack web application that detects **abusive / hate speech** in text across **multiple languages (English + Indic languages such as Hindi, Gujarati, etc.)** using a **Transformer-based deep learning model** on the backend and a **modern React + Tailwind CSS** frontend.

---

## 🚀 Features

✅ Real ML model prediction (no rule-based or fake logic)  
✅ Multilingual abusive speech detection  
✅ Severity + confidence scoring  
✅ Clean modern UI (centered card layout)  
✅ REST API built with FastAPI  
✅ Interactive Swagger API docs  
✅ Expandable architecture (DB + Dashboard later)

---

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- HuggingFace Transformers
- PyTorch
- SentencePiece

### Frontend
- React
- Vite
- Tailwind CSS v3
- Axios

---

---

## 📁 Project Folder Structure

```
hate-shield-ai/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI routes
│   │   ├── ml_model.py     # Transformer ML pipeline
│   │   ├── models.py       # Pydantic request/response schemas
│   │   ├── database.py    # (for future use)
│   │   └── config.py
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── tailwind.config.js
    ├── postcss.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css
        └── pages/
            ├── TextAnalyzer.jsx
            └── Dashboard.jsx (future)
```

---

---

## ✅ System Requirements

Make sure these are installed:

✅ Python **3.9+**  
✅ Node.js **18+**  
✅ npm **9+**  
✅ Internet connection (first run downloads the ML model)

Check versions:

```bash
python --version
node --version
npm --version
```

---

---

## 🧪 BACKEND SETUP (FASTAPI + ML)

### Step 1 — Go to backend folder

```bash
cd hate-shield-ai/backend
```

---

### Step 2 — Create virtual environment

```bash
python -m venv venv
```

Activate it:

**PowerShell**
```bash
venv\Scripts\Activate.ps1
```

**CMD**
```bash
venv\Scripts\activate.bat
```

---

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

✅ Ensure `requirements.txt` contains:

```txt
fastapi
uvicorn[standard]
pydantic
python-dotenv
transformers
torch
sentencepiece
```

---

### Step 4 — Start Backend Server

```bash
uvicorn app.main:app --reload
```

---

### Step 5 — Verify API

Open in browser:

```
http://127.0.0.1:8000
```

Expected output:

```json
{"message": "HateShield AI API is running"}
```

---

### Swagger API Docs

Open interactive docs:

```
http://127.0.0.1:8000/docs
```

Test using:

```json
{
  "text": "you are motherfukers..",
  "language": "en"
}
```

---

---

## 🧠 ML MODEL USED

Model:

```
Hate-speech-CNERG/indic-abusive-allInOne-MuRIL
```

It supports:

✅ English  
✅ Hindi  
✅ Gujarati  
✅ Marathi  
✅ Bengali  
✅ Tamil  
✅ Other Indic languages

👉 The model downloads automatically **on first use**.

---

---

## 💻 FRONTEND SETUP (REACT + TAILWIND)

### Step 1 — Go to frontend folder

```bash
cd hate-shield-ai/frontend
```

---

### Step 2 — Install dependencies

```bash
npm install
```

---

### Step 3 — Start Frontend Server

```bash
npm run dev
```

---

### Step 4 — Open UI

Open:

```
http://localhost:5173/
```

✅ You should see:

- Dark gradient background
- Centered white card
- Title **"HateShield AI"**
- Text input box
- Language selector
- Analyze button
- Result display card

---

---

## 🔗 SYSTEM FLOW (END-TO-END)

```
Frontend UI  --->  POST /analyze  --->  FastAPI Backend
                         |
                         v
                Transformer ML Model
                         |
                         v
                  Prediction + Scores
                         |
                         v
                    UI Result Display
```

---

---

## 🔬 API DETAILS

### POST `/analyze`

**Request**

```json
{
  "text": "sample abusive text",
  "language": "en"
}
```

**Response**

```json
{
  "result": {
    "is_hate": true,
    "category": "ABUSIVE",
    "severity": 0.82,
    "language": "en",
    "confidence": 0.97,
    "explanation": "Model predicted 'LABEL_1' (abusive) with confidence 0.97."
  }
}
```

---

---

## ⚠️ COMMON ISSUES

### ❌ `"Method Not Allowed"`

You opened:

```
http://127.0.0.1:8000/analyze
```

in the browser — that sends a GET request.

✅ `/analyze` only accepts POST → use:

- Swagger: `/docs`
- Or frontend UI

---

### ❌ Model Not Found Error

Make sure this line exists inside `backend/app/ml_model.py`:

```python
MODEL_NAME = "Hate-speech-CNERG/indic-abusive-allInOne-MuRIL"
```

Ensure internet works the first time.

---

### ❌ Tailwind CSS Not Working

Check:

- `tailwind.config.js`
- `postcss.config.js`
- `src/index.css` contains:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Restart frontend:

```bash
npm run dev
```

Hard refresh browser:

```
CTRL + SHIFT + R
```

---

---

## 🏭 PRODUCTION BUILD (OPTIONAL)

### Frontend build

```bash
npm run build
```

Output will be created inside:

```
frontend/dist/
```

---

### Backend production run

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Deployable to:

- Render
- Railway
- AWS EC2
- Any VPS

---

---

## 🌱 FUTURE EXTENSIONS

✅ Add MongoDB logging  
✅ User authentication  
✅ Admin moderation dashboard  
✅ Real-time moderation feeds  
✅ Explainable AI with word highlights  
✅ API rate-limiting & role management

---

---

## 👨‍💻 AUTHOR

**Project:** HateShield AI  
**Developer:** *Jayraj Lakkad*  
**Stack:** React • Tailwind • FastAPI • Transformers • PyTorch

---

