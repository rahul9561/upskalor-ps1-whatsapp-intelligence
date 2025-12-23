# Upskalor AI Hackathon 2025 – PS1
## WhatsApp Intelligence & Intent Routing System

This repository contains the implementation for **Problem Statement 1 (PS1)** of the Upskalor AI Hackathon 2025.

PS1 focuses on building an AI-powered WhatsApp system that understands user intent, validates handwriting images, and routes requests to the appropriate analysis modules.

---

## 🎯 Problem Overview

WhatsApp conversations are unstructured and noisy:
- Users send unclear messages
- Upload incorrect images
- Switch context mid-conversation

This system acts as the **intelligence layer** that:
- Understands user intent
- Validates handwriting images
- Maintains short-term session context
- Routes requests correctly
- Generates a routing PDF report

---

## 🧠 Core Features

### 1. Intent Classification (ML)
Classifies incoming WhatsApp messages into:
- `handwriting_upload`
- `question_asked`
- `unclear_or_other`

**Approach:**
- TF-IDF vectorization
- Logistic Regression classifier
- Trained and evaluated on custom dataset

---

### 2. Handwriting Image Validation
Validates whether the uploaded image is:
- ✅ Human handwritten English text
- ❌ Printed text / screenshot / random image

**Approach:**
- OpenCV-based preprocessing
- Feature-based or CNN-based classification

---

### 3. Conversation Management
- Maintains user context for 10 minutes
- Handles clarification flows
- Prevents broken user journeys

---

### WhatsApp Message → Intent Detection → Image Validation → Routing Decision → PDF Report → WhatsApp


---

## 📄 PDF Output

The system generates a **Conversation Intelligence Report** containing:
- Detected intent
- Confidence score
- Image validation result
- Routing decision
- Next steps for the user

---

## 🛠️ Tech Stack

- Python
- FastAPI (Python)
- Scikit-learn
- OpenCV
- WhatsApp Cloud API / Twilio
- ReportLab / WeasyPrint (PDF generation)

---

## 🚀 Setup Instructions

```bash
git clone https://github.com/rahul9561/upskalor-ps1-whatsapp-intelligence.git
cd upskalor-ps1-whatsapp-intelligence
pip install -r requirements.txt


### 4. WhatsApp → PDF Routing Flow
End-to-end flow:
