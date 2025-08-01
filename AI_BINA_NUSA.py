import os
import threading
import customtkinter as ctk
import tkinter.messagebox as msg
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Memuat variabel lingkungan dari file .env
load_dotenv()

class AssistenChatbotGUI:
    def __init__(self, master):
        """
        Inisialisasi GUI utama untuk aplikasi Asisten Guru.
        
        Parameters:
            master: Window utama dari aplikasi
        """
        self.master = master
        # Konfigurasi dasar window
        self.master.title("Asisten Guru - SMK BINA NUSA")
        self.master.geometry("650x768")
        self.master.resizable(True, True)
        
        # Set tema dark mode dan file tema custom
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("theme.json")

        # Ambil token Hugging Face dari environment variable
        self.HF_TOKEN = os.getenv("HF_TOKEN")
        if not self.HF_TOKEN:
            msg.showerror("Error", "Token Hugging Face tidak ditemukan di file .env")
            self.master.destroy()
            return

        # Inisialisasi client Hugging Face Inference
        self.client = InferenceClient(api_key=self.HF_TOKEN)

        # Setup antarmuka pengguna
        self.setup_ui()
        
        # Tampilkan pesan sambutan awal
        self.update_chat(
            "Asisten",
            "Hallo, saya Asisten Guru saat ini, saya menggunakan Mesin Meta-AI-Llama-3.2–3B",
            "bot",
        )

    def setup_ui(self):
        """
        Mengatur semua komponen antarmuka pengguna.
        Membuat frame utama, area chat, input, dan tombol-tombol.
        """
        # Frame utama sebagai container
        self.main_frame = ctk.CTkFrame(self.master, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Label judul aplikasi
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="SMK BINA NUSA\nAsisten Guru",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color="#9d07aa",
            justify="center",
        )
        self.title_label.pack(pady=(20, 5))

        # Label subtitle
        self.subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Pembelajaran apa yang tidak kamu mengerti? - Saya akan membantumu!",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#d73ce6",
        )
        self.subtitle.pack(pady=(0, 10))

        # Frame untuk area chat (scrollable)
        self.chat_frame = ctk.CTkScrollableFrame(
            self.main_frame, width=600, height=400
        )
        self.chat_frame.pack(pady=(0, 15))

        # Label untuk input user
        self.input_label = ctk.CTkLabel(
            self.main_frame,
            text="Apa yang ingin kamu tanyakan?",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.input_label.pack()

        # Textbox untuk input user
        self.input_box = ctk.CTkTextbox(
            self.main_frame, height=60, width=400, corner_radius=10
        )
        self.input_box.pack(pady=(5, 10))

        # Frame untuk tombol-tombol
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=10)

        # Tombol kirim pesan
        self.send_button = ctk.CTkButton(
            self.button_frame, text="Kirim Prompt (Enter)", command=self.send_message
        )
        self.send_button.pack(side="left", padx=10)

        # Tombol bersihkan chat
        self.clear_button = ctk.CTkButton(
            self.button_frame, text="Bersihkan Prompt", command=self.clear_chat
        )
        self.clear_button.pack(side="left", padx=10)

        # Status bar untuk menampilkan informasi
        self.status_bar = ctk.CTkLabel(
            self.main_frame,
            text="Siap digunakan! Koneksi API ke Meta-AI-Llama-3.2–3B berhasil.",
            height=20,
            font=ctk.CTkFont(size=12),
            text_color="#d73ce6",
        )
        self.status_bar.pack(fill="x", padx=20, pady=(10, 5))

        # Binding tombol Enter untuk mengirim pesan
        self.master.bind("<Return>", lambda e: self.send_message())

    def create_bubble_frame(self, sender, message, is_user=False):
        """
        Membuat frame bubble chat dengan gaya khusus.
        
        Parameters:
            sender: Nama pengirim pesan
            message: Isi pesan
            is_user: Boolean apakah pesan dari user atau bot
            
        Returns:
            CTkFrame: Frame bubble chat yang sudah di-styling
        """
        # Buat frame dengan corner radius dan warna berbeda untuk user/bot
        bubble_frame = ctk.CTkFrame(
            self.chat_frame,
            corner_radius=15,
            fg_color="#e6d5f7" if not is_user else "#d5f7e6",
            border_color="#8a6dae",
            border_width=1,
        )

        # Label nama pengirim (tebal)
        sender_label = ctk.CTkLabel(
            bubble_frame,
            text=sender + ":",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#4B0082",
            anchor="w",
            justify="left",
        )
        sender_label.pack(anchor="w", padx=10, pady=(5, 0))

        # Label isi pesan
        message_label = ctk.CTkLabel(
            bubble_frame,
            text=message,
            font=ctk.CTkFont(size=12),
            text_color="#333333",
            anchor="w",
            justify="left",
            wraplength=500,  # Auto wrap text jika terlalu panjang
        )
        message_label.pack(anchor="w", padx=10, pady=(0, 5), fill="x")

        return bubble_frame

    def update_chat(self, sender, message, msg_type="user"):
        """
        Menambahkan pesan baru ke area chat dalam bentuk bubble.
        
        Parameters:
            sender: Nama pengirim
            message: Isi pesan
            msg_type: Tipe pesan ('user' atau 'bot')
        """
        is_user = msg_type == "user"
        display_name = "Anda" if is_user else "Asisten"

        # Buat bubble chat baru
        bubble = self.create_bubble_frame(display_name, message, is_user)
        
        # Tampilkan bubble di sisi kanan untuk user, kiri untuk bot
        bubble.pack(fill="x", padx=5, pady=5, anchor="e" if is_user else "w")

        # Auto-scroll ke bagian bawah chat
        self.chat_frame._parent_canvas.yview_moveto(1.0)

    def clear_chat(self):
        """
        Membersihkan seluruh isi chat dan menampilkan pesan default.
        """
        # Hapus semua widget di frame chat
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        # Tampilkan pesan default setelah clear
        self.update_chat(
            "Asisten",
            "Percakapan sudah dibersihkan, ada yang ingin kamu tanyakan lagi?",
            "bot",
        )

    def send_message(self):
        """
        Mengirim pesan dari user dan memprosesnya.
        """
        # Ambil input dari textbox
        prompt = self.input_box.get("1.0", "end").strip()
        if prompt:
            # Tampilkan pesan user di chat
            self.update_chat("Anda", prompt, "user")
            # Bersihkan input box
            self.input_box.delete("1.0", "end")
            # Proses pesan di thread terpisah agar GUI tidak freeze
            threading.Thread(
                target=self.get_response, args=(prompt,), daemon=True
            ).start()

    def get_response(self, prompt):
        """
        Mendapatkan respons dari model AI berdasarkan prompt user.
        
        Parameters:
            prompt: Pertanyaan/input dari user
        """
        # Update status
        self.status_bar.configure(text="Asisten sedang berpikir...")
        
        try:
            # Kirim request ke Hugging Face Inference API
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3.2-3B-Instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "Kamu adalah Asisten Guru, bantu siswa dengan ramah dan bahasa Indonesia yang mudah dimengerti.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=256,  # Batas maksimal token respons
                temperature=0.7,  # Mengontrol kreativitas respons
                top_p=0.9,       # Mengontrol variasi respons
            )
            
            # Ambil isi respons
            reply = response.choices[0].message.content
            
            # Tampilkan respons di chat
            self.update_chat("Asisten", reply, "bot")
            
            # Update status
            self.status_bar.configure(text="Siap digunakan! Koneksi API Ke Meta-AI-Llama-3.2-3B berhasil.")
            
        except Exception as e:
            # Tangani error dan tampilkan pesan
            self.status_bar.configure(text=f"Terjadi kesalahan: {str(e)}")
            msg.showerror("Error", str(e))


if __name__ == "__main__":
    # Buat window utama dan jalankan aplikasi
    root = ctk.CTk()
    app = AssistenChatbotGUI(root)
    root.mainloop()