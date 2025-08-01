<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Asisten Guru - SMK BINA NUSA</title>
  <style>
    body { font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: #f7f3ff; color: #402E5C; margin: 0; padding: 0; }
    .container { max-width: 700px; margin: 40px auto; background: #fff; border-radius: 16px; box-shadow: 0 4px 24px #d3cffc; padding: 32px; }
    h1 { color: #7C63A6; font-size: 2.5em; margin-bottom: 0.2em; }
    h2 { color: #6C5090; margin-top: 1.5em; }
    ul { padding-left: 1.2em; }
    code, pre { background: #eae8fc; border-radius: 6px; padding: 2px 6px; }
    .badge { display: inline-block; background: #7C63A6; color: #fff; border-radius: 8px; padding: 2px 10px; font-size: 0.9em; margin-right: 6px; }
    .howto { background: #f3efff; border-left: 4px solid #7C63A6; padding: 16px; margin: 18px 0; border-radius: 8px; }
    .footer { text-align: center; color: #837CB9; margin-top: 32px; font-size: 0.95em; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 Asisten Guru <span class="badge">SMK BINA NUSA</span></h1>
    <p>
      <b>Asisten Guru</b> adalah aplikasi chatbot berbasis <b>Meta-AI-Llama-3.2–3B</b> yang membantu siswa memahami materi pelajaran dengan bahasa Indonesia yang mudah dimengerti.
    </p>
    <h2>✨ Fitur Utama</h2>
    <ul>
      <li>Antarmuka modern dengan <b>CustomTkinter</b> dan tema cantik</li>
      <li>Integrasi <b>Hugging Face Inference API</b> untuk AI Chatbot</li>
      <li>Bubble chat interaktif & auto-scroll</li>
      <li>Mode gelap & responsif</li>
      <li>Pesan sambutan dan status koneksi API</li>
    </ul>
    <h2>🔧 Dependensi</h2>
    <pre>
pip install -r requirments.txt
    </pre>
    <ul>
      <li><code>customtkinter</code></li>
      <li><code>dotenv</code></li>
      <li><code>huggingface_hub</code></li>
    </ul>
    <h2>🚀 Cara Menggunakan</h2>
    <div class="howto">
      <ol>
        <li>Clone atau download project ini.</li>
        <li>Buat file <code>.env</code> dan isi dengan token Hugging Face:<br>
          <code>HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"</code>
        </li>
        <li>Install semua dependensi:<br>
          <code>pip install -r requirments.txt</code>
        </li>
        <li>Jalankan aplikasi:<br>
          <code>python AI_BINA_NUSA.py</code>
        </li>
        <li>Tanyakan apapun seputar pelajaran, dan Asisten Guru akan membantu!</li>
      </ol>
    </div>
    <h2>📦 Struktur Project</h2>
    <ul>
      <li><code>AI_BINA_NUSA.py</code> &mdash; Source code utama aplikasi</li>
      <li><code>theme.json</code> &mdash; File tema CustomTkinter</li>
      <li><code>.env</code> &mdash; Token API Hugging Face</li>
      <li><code>requirments.txt</code> &mdash; Daftar dependensi pip</li>
    </ul>
    <div class="footer">
      Dibuat dengan ❤️ untuk SMK BINA NUSA &mdash; 2025
    </div>
  </div>
</body>
</html>

Catatan:

Pastikan file .env berisi token API Hugging Face yang valid.
Jalankan perintah pip install -r requirments.txt sebelum menjalankan aplikasi.