import streamlit as st
import random

# Atur halaman
st.set_page_config(
    page_title="Calorie Counting",
    page_icon="🍱",
    layout="centered"
)

# CSS dengan gambar background di halaman utama
st.markdown("""
<style>
    /* Background umum aplikasi */
    .stApp {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2d3436;
        font-size: 18px;
        padding: 10px;
        background: #f5f7fa;  /* fallback background */
    }

    /* Background khusus halaman utama dengan gambar */
    .page-main .stApp {
        background-image: url('https://i.imgur.com/XGm7SnN.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #fff;
        text-shadow: 0 0 8px rgba(0,0,0,0.7);
        padding: 40px 20px;
    }

    /* Container putih transparan untuk teks supaya lebih jelas */
    .page-main .css-1d391kg, .page-main .css-1v3fvcr {
        background-color: rgba(255, 255, 255, 0.85) !important;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        color: #2d3436 !important;
    }

    /* Heading */
    h1, h2, h3, h4 {
        color: #0e6251;
        text-shadow: none;
    }

    /* Tombol */
    .stButton>button {
        background-color: #00b894;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }

    .stButton>button:hover {
        background-color: #019875;
    }

    /* Background kartu input dan output kalkulator */
    .css-1d391kg, .css-1v3fvcr {
        background-color: #ffffffcc !important;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    }

    /* Sidebar styling */
    .css-1v3fvcr {
        background-color: #ffffffcc !important;
    }
</style>
""", unsafe_allow_html=True)


# DATA MENU
karbo = [("Nasi Putih", 175, "150 gram"), ("Nasi Merah", 150, "150 gram"),
         ("Kentang Rebus", 140, "200 gram"), ("Ubi Rebus", 120, "200 gram"),
         ("Roti Gandum", 110, "2 lembar")]

lauk = [("Ayam Panggang", 250, "100 gram"), ("Tahu Goreng", 120, "2 potong"),
        ("Tempe Oreg", 160, "2 potong"), ("Ikan Bakar", 200, "100 gram"),
        ("Telur Rebus", 90, "1 butir")]

sayur = [("Sayur Bayam", 40, "1 mangkok"), ("Capcay", 80, "1 mangkok"),
         ("Sawi Rebus", 60, "1 piring"), ("Sayur Asem", 50, "1 mangkok"),
         ("Sup Wortel", 55, "1 mangkok")]

buah = [("Apel", 95, "1 buah"), ("Pisang", 105, "1 buah"),
        ("Pepaya", 60, "100 gram"), ("Semangka", 50, "150 gram"),
        ("Jeruk", 80, "1 buah")]

susu = [("Susu Sapi", 150, "1 gelas"), ("Susu Kedelai", 100, "1 gelas"),
        ("Yoghurt", 120, "1 cup"), ("Susu Almond", 90, "1 gelas"),
        ("Susu Cokelat", 180, "1 gelas")]

# Fungsi buat menu
def buat_menu_4_sehat_5_sempurna(jumlah=10):
    menu_list = []
    for _ in range(jumlah):
        k = random.choice(karbo)
        l = random.choice(lauk)
        s = random.choice(sayur)
        b = random.choice(buah)
        u = random.choice(susu)
        total_kalori = k[1] + l[1] + s[1] + b[1] + u[1]
        menu_str = (
            f"{k[0]} ({k[2]}) + {l[0]} ({l[2]}) + {s[0]} ({s[2]}) + "
            f"{b[0]} ({b[2]}) + {u[0]} ({u[2]})\n**Total Kalori: {total_kalori} kkal**"
        )
        menu_list.append(menu_str)
    return menu_list

# Fungsi hitung kalori
def hitung_kalori(berat, tinggi, usia, gender, multiplier):
    if gender.lower() == "laki-laki":
        bmr = (10 * berat) + (6.25 * tinggi) - (5 * usia) + 5
    else:
        bmr = (10 * berat) + (6.25 * tinggi) - (5 * usia) - 161
    return round(bmr * multiplier)

# Navigasi
menu = st.sidebar.selectbox("Navigasi", [
    "🌎Halaman Utama", "🔢Kalkulator Kalori", "📖Tentang"
])

# Beri kelas khusus agar CSS background gambar hanya untuk halaman utama
if menu == "🌎Halaman Utama":
    st.markdown('<div class="page-main">', unsafe_allow_html=True)

# Halaman Utama
if menu == "🌎Halaman Utama":
    st.warning('Tekan tombol panah di pojok kiri atas untuk melihat fitur')
    st.title("🍱Calorie Counting - Aplikasi Giziku")
    st.markdown("""
    Selamat datang di **kalkulator kalori harian**, tujuan aplikasi ini sederhana:

    - 🔢 Menghitung kebutuhan kalori harian  
    - 🍽️ Mendapatkan rekomendasi menu 4 Sehat 5 Sempurna  
    - 💡 Informasi tentang Total Daily Energy Expenditure (TDEE) dan gizi seimbang  
    Silakan gunakan menu di sebelah kiri untuk mulai 🙋‍♀️🙋‍♂️
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman Kalkulator Kalori
elif menu == "🔢Kalkulator Kalori":
    st.title("🔢 Kalkulator Kebutuhan Kalori Harian")
    st.subheader("Dengan Rekomendasi Menu 4 Sehat 5 Sempurna 🥔🥦🥩🍉🥛")

    nama = st.text_input("Nama kamu")
    bb = st.number_input("Berat badan (kg)", min_value=10.0, max_value=300.0, step=0.5)
    tb = st.number_input("Tinggi badan (cm)", min_value=50.0, max_value=250.0, step=0.5)
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=65, value=18)
    gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])

    aktivitas = st.selectbox(
        "Tingkat Aktivitas Harian",
        [
            "🙇‍♂️Sangat ringan (tidak aktif/fisik minimal)",
            "🚶‍♂️Ringan (jalan kaki ringan, kerja ringan)",
            "🏊Sedang (olahraga 3-5 hari/minggu)",
            "🏋️‍♀️Berat (aktivitas fisik berat atau olahraga intensif)",
            "💪Sangat berat (latihan keras tiap hari atau pekerjaan fisik berat)"
        ]
    )

    aktivitas_dict = {
        "🙇‍♂️Sangat ringan (tidak aktif/fisik minimal)": 1.2,
        "🚶‍♂️Ringan (jalan kaki ringan, kerja ringan)": 1.375,
        "🏊Sedang (olahraga 3-5 hari/minggu)": 1.55,
        "🏋️‍♀️Berat (aktivitas fisik berat atau olahraga intensif)": 1.725,
        "💪Sangat berat (latihan keras tiap hari atau pekerjaan fisik berat)": 1.9
    }

    if st.button("Hitung Kalori"):
        multiplier = aktivitas_dict[aktivitas]
        kalori = hitung_kalori(bb, tb, usia, gender, multiplier)
        st.success(f"{nama}, kebutuhan kalori harianmu sekitar {kalori} kkal.")
        st.markdown("### Rekomendasi Menu 4 Sehat 5 Sempurna:")
        rekomendasi = buat_menu_4_sehat_5_sempurna(10)
        for i, menu_item in enumerate(rekomendasi, 1):
            st.markdown(f"{i}. {menu_item}")
        st.balloons()

# Halaman Tentang
elif menu == "📖Tentang":
    st.title("📖 Tentang Aplikasi Kalkulator Kalori Harian")
    st.markdown("""
Aplikasi ini dibuat agar pengguna dapat mengetahui kalori hariannya berdasarkan berat badan, tinggi badan, usia, dan gender, serta menghitung Total Daily Energy Expenditure (TDEE) dengan mengalikan BMR dan nilai aktivitas harian.

### Fitur Utama:
- 🔢 **Kalkulator Kalori Harian**  
- 🍱 **Rekomendasi Menu 4 Sehat 5 Sempurna**  
- 💡 **Informasi TDEE & Gizi Seimbang**  

Kami harap aplikasi ini bisa membantu kamu dalam menjaga asupan dan pola makan sehat. Eat smart yaa!! 🤗💪
""")
