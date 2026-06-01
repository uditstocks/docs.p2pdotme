---
id: 02-2-design-goals-and-non-goals
sidebar_position: 2
title: "2. Tujuan Desain dan Bukan-Tujuan"
slug: design-goals-and-non-goals
---

## 2.1 Tujuan

- On/off-ramp terdesentralisasi antara mata uang fiat dan stablecoin tanpa escrow fiat.
- Privasi sejak desain menggunakan bukti ZK untuk verifikasi identitas sambil menyimpan data mentah di luar rantai. Verifikasi transaksi bank sedang direncanakan (lihat [Bagian 4.2](/id/whitepaper/cryptographic-primitives-proof-integration)).
- Netralitas yang dapat dipercaya: aturan di tingkat protokol bersifat terbuka, transparan, dan dapat diperbarui melalui tata kelola.
- Penyelesaian cepat: penyelesaian umum dalam hitungan menit, dengan target di bawah sekitar 90 detik untuk jalur umum seiring jaringan, likuiditas, dan otomasi berkembang.
- Keamanan dan integritas: model ancaman yang eksplisit, alur sengketa, dan kontrol tarif/batas untuk meminimalkan penipuan.

## 2.2 Bukan-Tujuan

- Protokol tidak menyimpan fiat atau kripto pelanggan dalam kustodi.
- Protokol tidak menjamin harga atau likuiditas. Protokol mengoordinasikan pihak-pihak yang bertransaksi dan masukan pasar.
- Protokol tidak menyimpan data pribadi atas nama pengguna. Protokol hanya mencatat komitmen dan putusan yang diperlukan di rantai, sementara bukti mentah tetap berada di luar rantai.

---
