---
id: protocol-parameters
sidebar_position: 2
title: "Parameter Protokol"
slug: protocol-parameters
---

Perilaku protokol sangat bergantung pada parameter yang dapat dikonfigurasi, bukan dikodekan secara tetap, karena kondisi pasar berbeda-beda. Spread yang tepat untuk INR/USDC di jalur UPI akan salah jika diterapkan pada BRL/USDC di PIX. Parameterisasi memungkinkan protokol beradaptasi per mata uang tanpa perlu melakukan deploy ulang kontrak.

- **Penetapan harga dan spread.** Spread dasar dan kenaikan harga per mata uang, disesuaikan dengan kondisi likuiditas lokal.

- **Batas risiko.** Batas stake minimum, batas volume, batas RP per USDC, dan batas transaksi maksimum. Parameter ini mengatur seberapa besar risiko yang ditanggung protokol per merchant dan per pengguna.

- **Kontrol biaya.** Persentase biaya merchant dan biaya tetap untuk pesanan kecil, yang disetel agar transaksi mikro tetap layak tanpa disubsidi.

- **Kontrol operasional.** Siklus hidup aktivasi mata uang dan saluran pembayaran.

---
