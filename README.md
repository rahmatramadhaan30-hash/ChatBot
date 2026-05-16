# Asisten Rahmat

Simple Streamlit-based chatbot menggunakan Groq (Llama).

## Deskripsi
Asisten AI bernama asisten rahmat yang membantu menjelaskan istilah IT & Data Science dengan gaya santai.

## File Penting
- `app.py`
- `requirements.txt`

## Cara Pakai
1. Pasang dependensi:

Gunakan Python 3.12

install dlu streamlit dan langchainnya nya dengan cara 
bash
"python -m pip install streamlit" dan "python -m pip install langchain_groq"

kemudian 

```bash
pip install -r requirements.txt
```

2. (Opsional) Atur API key Groq di `app.py` dengan mengganti nilai `groq_api_key`.

3. Jalankan aplikasi:

```bash
streamlit run app.py
```

4. Buka browser ke alamat yang ditampilkan Streamlit.

## Catatan
- Jangan commit API key publik ke GitHub. Kalau mau aman, gunakan environment variable atau secret GitHub.

## Lisensi
Free to use.
