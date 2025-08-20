## Alur Kerja Proyek (Project Workflow)

Proyek ini dirancang agar dapat direproduksi sepenuhnya. Berikut adalah langkah-langkah untuk menyiapkan dataset, melatih model, dan melihat hasil deployment-nya.

### 1. Dataset 📊

Dataset yang digunakan dalam proyek ini adalah **SIBI (Sistem Isyarat Bahasa Indonesia)** yang tersedia secara publik di Kaggle.

* **Aksi:** [**Unduh Dataset dari Kaggle di sini**](https://www.kaggle.com/datasets/alvinbintang/sibi-dataset)
* **Instruksi:** Setelah mengunduh, ekstrak file tersebut dan letakkan di dalam direktori utama proyek. Pastikan struktur foldernya sesuai dengan yang dibutuhkan oleh skrip pelatihan.

### 2. Pelatihan Model (Training) ⚙️

Untuk memberikan fleksibilitas dan transparansi, model pra-latih (`.h5`) tidak disertakan secara langsung dalam repository ini. Sebaliknya, Anda dapat melatih model dari awal (from scratch) atau menggunakan transfer learning dengan menjalankan notebook yang telah disediakan.

* **Aksi:** Buka dan jalankan notebook yang ada di dalam folder `notebooks/`. Setiap notebook berisi alur kerja untuk arsitektur model yang berbeda (misalnya `DenseNet201.ipynb`, `MobileNetV2.ipynb`).
* **Hasil:** Setelah proses pelatihan selesai, file model (`.h5`) akan disimpan secara otomatis. Anda kemudian bisa menggunakan model ini untuk tahap deployment.

### 3. Deployment (Streamlit App) 🚀

Aplikasi web interaktif untuk mencoba model ini secara langsung telah dibuat menggunakan **Streamlit**. Kodenya berada di repository GitHub yang terpisah untuk menjaga kerapian dan fokus dari masing-masing proyek.

* **Aksi:** Kunjungi repository di bawah ini untuk melihat kode deployment dan mencoba aplikasinya.
* **Link:** [**➡️ Repository Deployment Aplikasi SIBI dengan Streamlit**](https://github.com/Tharx7/SIBI-Streamlit)

---