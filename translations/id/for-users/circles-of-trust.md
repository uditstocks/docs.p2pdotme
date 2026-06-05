---
id: circles-of-trust
sidebar_position: 8
title: "Circles of Trust"
slug: circles-of-trust
---

Circle adalah kelompok merchant yang didukung komunitas, dijalankan oleh satu Circle Admin di bawah aturan protokol on-chain yang berlaku bersama. Setiap Circle memiliki mata uang, kumpulan merchant, saldo fiat, dan likuiditas USDC tersendiri. Circle hadir agar orang-orang yang mengenal penjual lokal dapat mengoperasikan dan mendukung mereka, alih-alih satu meja terpusat yang menangani seluruh pasar. Sebagai pembeli, Anda bertransaksi dengan merchant di dalam sebuah Circle.

Anda tidak memilih Circle secara manual saat ini. Protokol menugaskan merchant yang memenuhi syarat ke pesanan Anda berdasarkan faktor real-time seperti likuiditas, status saluran, dan ketersediaan. Pemilihan Circle secara manual dan pengurutan berbasis reputasi direncanakan untuk rilis mendatang. Ketika aplikasi menampilkan informasi Circle di samping sebuah pesanan, informasi tersebut mencerminkan kondisi on-chain seperti jumlah stake merchant dan riwayat pesanan.

Sebuah Circle memberikan dua perlindungan nyata kepada pembeli. Pertama, merchant men-stake USDC dan Circle Admin men-stake $P2P untuk beroperasi, sehingga ada agunan di balik pihak yang bertransaksi dengan Anda. Kedua, setiap Circle didukung oleh cadangan asuransi. Terdapat tiga pool. Circle Admin Insurance Pool (CAIP, cadangan asuransi per-Circle) adalah cadangan per-Circle yang didanai dari bagian biaya pesanan. Circle Admin Loss Reserve (CALR, cadangan kerugian per-admin) adalah buffer per-admin yang didanai dari sebagian hadiah admin. Pool Insurance Pool (PIP, cadangan proteksi seluruh protokol) adalah jaring pengaman cakupan protokol secara menyeluruh. Pool-pool tersebut beserta pendanaannya telah tersedia secara on-chain, dan pekerjaan penyelesaian serta perhitungan hadiah berjalan secara on-chain dan dapat diverifikasi.

Alur pengajuan klaim asuransi secara lengkap sedang diselesaikan dan belum aktif. Ketika fitur ini diluncurkan, klaim akan diajukan oleh merchant kepada pool ketika USDC hilang meskipun merchant telah berperilaku dengan benar, dan setiap klaim akan ditinjau sebelum diselesaikan, bukan dikembalikan secara otomatis. Sebagai pembeli, jalan recourse Anda untuk transaksi yang bermasalah adalah jalur sengketa pesanan, bukan jalur klaim asuransi.

Sisi Anda dalam sengketa dibahas secara lengkap di [Sengketa dan Bukti](/for-users/disputes-and-evidence). Singkatnya, sengketa hanya dapat diajukan satu kali per pesanan, dan admin yang berwenang menyelesaikannya secara on-chain dengan menetapkan kesalahan. Jika merchant dinyatakan bersalah, pesanan diselesaikan dan stablecoin dikirimkan kepada penerima. Tingkatan eskalasi berbasis juri dan berbasis tata kelola direncanakan untuk rilis mendatang.

---
