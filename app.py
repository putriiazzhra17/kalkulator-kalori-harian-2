import streamlit as st 
import random 
 
# Atur halaman 
st.set_page_config(page_title="Calorie Counting", page_icon="🍱", 
layout="centered") 
 
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
 # Fungsi membuat rekomendasi menu lengkap 
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
# Fungsi menghitung kalori 
def hitung_kalori(berat, tinggi, usia, gender, multiplier): 
    if gender.lower() == "laki-laki": 
        bmr =(10*berat)+(6.25*tinggi)-(5*usia)+5
    else: 
        bmr =(10*berat)+(6.25*tinggi)-(5*usia)-161
    return round(bmr * multiplier) 
 # Gaya CSS 
st.markdown(""" 
<style> 
    .stApp { 
        background-color: #bab86c;  
        color: #333333;  
        font-size: 18px; 
    } 
    table {border: 2px solid #fb8e54;} 
    th {background-color: #fb8e54; color: white;} 
    td {background-color: #f3e9df; color: black;} 
</style> 
""", unsafe_allow_html=True) 
 # Navigasi 
menu = st.sidebar.selectbox("Navigasi", [ 
  "🌎Halaman Utama", "😊Perkenalan Kelompok", "🔢🧮Kalkulator Kalori","💡Tentang"
]) 
 # Halaman Utama 
if menu == "🌎Halaman Utama": 
    st.warning('tekan tombol panah di pojok kiri atas untuk melihat fitur') 
    st.markdown(""" 
    <style> 
    .stApp { 
        background: linear-gradient(rgba(0, 0, 0, 0.80), rgba(0, 0, 0, 0.80)), 
                    url('https://img.freepik.com/free-photo/person-paying-using-nfc
technology_23-2149893740.jpg'); 
        background-size: cover; 
        background-position: center; 
        background-repeat: no-repeat; 
        color: white !important; 
    } 
    </style> 
    """, unsafe_allow_html=True) 
 
    st.title("🍱Calorie Counting - Aplikasi Gizi Sehatmu") 
    st.markdown(""" 
    Selamat datang di **kalkulator kalori harian**, Tujuan aplikasi sederhana untuk 
membantu kamu: 
 
    -🔢Menghitung kebutuhan kalori harian   
    -🍽️Mendapatkan rekomendasi menu 4 Sehat 5 Sempurna    
Silakan gunakan menu di sebelah kiri untuk mulai🙋‍♀️🙋‍♂️      
    """) 
# Halaman Perkenalan 
elif menu == "😊Perkenalan Kelompok": 
    st.header("KELOMPOK 9 (1B-Analisis Kimia)") 
    st.markdown("""  
Kelompok 9 merupakan tim mahasiswa Program Studi Analisis Kimia yang berkolaborasi dalam pengembangan aplikasi ini,
beserta dosen mengarahkan dalam pengembangan project ini. Berikut adalah anggota tim dengan NIM : 

1. Anindya Nadra Irtiza (NIM: 2460325)   
2. Haikal Hirra Habibillah (NIM: 2460382)   
3. Muhamad Rakha Aqila A. P I (NIM: 2460427)   
4. Putri Azzahra Ramadhani (NIM: 2460482)   
5. Yesi Arnesta Laguna Br Ginting (NIM: 2460538) 
""") 
# Halaman Kalkulator Kalori 
elif menu == "🔢Kalkulator Kalori": 
    st.title("🔢Kalkulator Kebutuhan Kalori Harian") 
    st.subheader("Dengan Rekomendasi Menu 4 Sehat 5 Sempurna🥔🥦🥩🍉🥛") 
 
    nama = st.text_input("Nama kamu") 
    bb = st.number_input("Berat badan (kg)", min_value=10.0, max_value=300.0, 
step=0.5) 
    tb = st.number_input("Tinggi badan (cm)", min_value=50.0, max_value=250.0, 
step=0.5) 
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=65, value=18) 
    gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"]) 
 
    aktivitas = st.selectbox( 
        "Tingkat Aktivitas Harian", 
        [ 
            "🙇‍♀Sangat ringan (tidak aktif/fisik minimal)", 
            "🚶‍♂Ringan (jalan kaki ringan, kerja ringan)", 
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
elif menu == "💡Tentang": 
    st.title(💡"Tentang Aplikasi kalkulator kalori harian") 
    st.markdown(""" 
Aplikasi ini dibuat agar pengakses dapat mengetahui kalori hariannya berdasarkan berat badan,tinggi badan,usia dan gender,
serta untuk mengetahui Total Daily Energy Expenditure (TDEE) dengan mengoprasikan BMR dengan nilai aktivitas harian (TDEE=BMR*Nilai aktivitas harian)     
 ### Fitur Utama 
-🔢**Kalkulator Kalori Harian:** Berdasarkan data pribadi dan aktivitas. 
-🍱**Rekomendasi Menu 4 Sehat 5 Sempurna**
-💡**Informasi tentang  Total Daily Energy Expenditure Gizi Seimbang** 
 
Kami harap aplikasi ini bisa membantu kamu dalam mengetahui tentang kalori harian kamu sehari-hari! 🤗💪       
""") 
