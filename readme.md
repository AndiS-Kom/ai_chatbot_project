# 🤖 Asisten Guru <span style="background:#7C63A6;color:#fff;border-radius:8px;padding:2px 10px;">SMK BINA NUSA</span>

**Asisten Guru** adalah aplikasi chatbot berbasis **Meta-AI-Llama-3.2–3B** yang membantu siswa memahami materi pelajaran dengan bahasa Indonesia yang mudah dimengerti.

## ✨ Fitur Utama
- Antarmuka modern dengan **CustomTkinter** dan tema cantik
- Integrasi **Hugging Face Inference API** untuk AI Chatbot
- Bubble chat interaktif & auto-scroll
- Mode gelap & responsif
- Pesan sambutan dan status koneksi API

## 🔧 Dependensi

Install semua dependensi dengan:
```bash
pip install -r requirments.txt
```

Daftar dependensi:
- `customtkinter`
- `python-dotenv`
- `huggingface_hub`

## 🚀 Cara Menggunakan

1. Clone atau download project ini.
2. Buat file `.env` dan isi dengan token Hugging Face:
   ```
   HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   ```
3. Install semua dependensi:
   ```
   pip install -r requirments.txt
   ```
4. Jalankan aplikasi:
   ```
   python AI_BINA_NUSA.py
   ```
5. Tanyakan apapun seputar pelajaran, dan Asisten Guru akan membantu!

## 📦 Struktur Project
- `AI_BINA_NUSA.py` — Source code utama aplikasi
- `theme.json` — File tema CustomTkinter
- `.env` — Token API Hugging Face
- `requirments.txt` — Daftar dependensi pip

---

**Catatan:**  
Pastikan file `.env` berisi token API Hugging Face yang valid.  
Jalankan perintah `pip install -r requirments.txt` sebelum menjalankan aplikasi.

Dibuat dengan ❤️ untuk SMK BINA NUSA — 2025