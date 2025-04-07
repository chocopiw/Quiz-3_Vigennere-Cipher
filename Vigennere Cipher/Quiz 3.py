# Import regex untuk membersihkan teks
import re

# Plaintext dan key
plaintext = """
Di sebuah desa nelayan, perahu-perahu kayu berbaris rapi di tepian pantai. Seorang nelayan tua
duduk di bawah pohon kelapa, memperbaiki jaring yang rusak setelah semalaman melaut. Anak-
anak berlarian di pasir, tertawa riang sambil mengumpulkan kerang berwarna-warni. Ibu-ibu
sibuk menyiapkan ikan segar untuk dijual di pasar pagi. Angin laut bertiup sepoi-sepoi, membawa
aroma garam yang khas. Burung camar melayang rendah, sesekali menyelam untuk menangkap
ikan kecil. Ombak memecah di tebing karang, menciptakan suara alami yang menenangkan.
Langit biru membentang luas, seakan menyatu dengan lautan tanpa batas.
"""

key = "SOFY NUR KHOLIFAH"

# Fungsi untuk membersihkan teks: huruf besar, hilangkan non-alfabet
def clean_text(text):
    return re.sub(r'[^A-Z]', '', text.upper())

cleaned_plaintext = clean_text(plaintext)
cleaned_key = clean_text(key)

# Fungsi konversi huruf ke angka dan sebaliknya
def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

# Perpanjang kunci agar sepanjang plaintext
extended_key = (cleaned_key * (len(cleaned_plaintext) // len(cleaned_key) + 1))[:len(cleaned_plaintext)]

# Enkripsi dengan Vigenère Cipher: Ci = (Pi + Ki) % 26
ciphertext = ''
for p_char, k_char in zip(cleaned_plaintext, extended_key):
    p_num = char_to_num(p_char)
    k_num = char_to_num(k_char)
    c_num = (p_num + k_num) % 26
    ciphertext += num_to_char(c_num)

# Tampilkan hasil enkripsi (pertama 500 karakter)
print(ciphertext[:500])
