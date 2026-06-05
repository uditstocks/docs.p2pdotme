---
id: verifying-transactions-on-chain
sidebar_position: 11
title: "Memverifikasi Transaksi On-Chain"
slug: verifying-transactions-on-chain
---

Protokol menyelesaikan transaksi dalam USDC di Base, sebuah EVM Layer 2. Setiap pesanan dan penyelesaian dicatat secara on-chain, sehingga Anda dapat mengonfirmasi setiap transaksi sendiri menggunakan BaseScan, penjelajah blok publik di [basescan.org](https://basescan.org). BaseScan memungkinkan Anda melihat transaksi untuk suatu alamat, memeriksa saldo token, dan mengetahui apakah sebuah transaksi berhasil beserta detailnya.

Temukan alamat Anda terlebih dahulu. Di aplikasi, buka My Account atau Wallet dan salin alamat tersebut, yang dimulai dengan `0x`.

Untuk mencari alamat, tempelkan ke bilah pencarian BaseScan dan tekan Enter. Halaman alamat menampilkan saldo ETH, token ERC-20 yang dipegang, dan riwayat transaksi lengkap, termasuk transfer token dan panggilan kontrak internal.

Untuk mencari satu transaksi, Anda memerlukan hash transaksinya, yaitu pengenal unik yang terlihat seperti `0x` diikuti oleh 64 karakter heksadesimal. Anda dapat menyalin hash dari riwayat transaksi dalam aplikasi atau dari setiap baris pada halaman alamat BaseScan Anda. Tempelkan hash ke bilah pencarian BaseScan dan tekan Enter.

Halaman transaksi menampilkan kolom yang penting untuk verifikasi.

| Kolom | Arti |
|-------|------|
| Status | Berhasil atau Gagal |
| Block | Nomor blok tempat transaksi dikonfirmasi |
| Timestamp | Tanggal dan waktu transaksi |
| From | Alamat yang mengirimkan transaksi |
| To | Alamat atau kontrak yang menerimanya |
| Transaction Fee | Biaya gas yang dibayarkan |

Ketika sebuah transaksi memindahkan token seperti USDC, gulir ke bagian transfer token untuk melihat token, jumlah, serta alamat pengirim dan penerima. Untuk mengonfirmasi bahwa Anda melihat token yang benar, buka token tersebut dan periksa alamat kontraknya terhadap alamat resmi. Kontrak USDC resmi di Base adalah `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. Base menggunakan chain ID 8453.

Jika sebuah transaksi tidak muncul, tunggu beberapa menit agar dikonfirmasi dan pastikan Anda melakukan pencarian di Base. Jika Anda mengirim dana dan penerima melaporkan tidak ada yang tiba, cari hash tersebut, konfirmasi statusnya adalah Berhasil, dan periksa alamat To serta transfer token. Simpan hash untuk transaksi besar, karena hash tersebut membantu tiket dukungan dan sengketa.

---
