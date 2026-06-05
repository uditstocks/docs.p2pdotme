---
id: risk-and-reliability-practices
sidebar_position: 11
title: "Praktik Manajemen Risiko dan Keandalan"
slug: risk-and-reliability-practices
---

- Tanggapi pesanan yang ditetapkan dengan cepat.
- Jaga agar metadata saluran dan detail pembayaran selalu akurat.
- Hindari mengoperasikan saluran saat tidak tersedia.
- Simpan jejak bukti untuk pembayaran yang dipersengketakan.
- Jadikan pembatalan dan sengketa sebagai sinyal kualitas untuk meningkatkan operasi.

## Pola Pembayaran Berulang PIX

Satu pola yang perlu diwaspadai pada jalur PIX adalah pembayaran yang dikonfigurasi untuk berulang secara otomatis pada tanggal mendatang, kadang diberi label PIX berulang, PIX otomatis, atau paket tahunan maupun bulanan. Menyelesaikan pesanan semacam itu dapat mengotorisasi tagihan di luar satu transaksi yang sedang Anda hadapi. Jangan selesaikan pesanan tersebut. Batalkan dan laporkan dengan ID pesanan.

Jika Anda yakin telah mengotorisasi pembayaran berulang secara tidak sengaja, batalkan pengulangan tersebut di aplikasi perbankan Anda dan laporkan dengan ID pesanan. Deteksi penipuan pada protokol berjalan off-chain melalui SEON Fraud API pada peristiwa pendaftaran, verifikasi, dan transaksi. Diamond on-chain menerapkan batas waktu sengketa, penalti Reputation Point, dan gerbang daftar hitam. Diamond tidak menilai transaksi, sehingga penilaian Anda pada saat pembayaran adalah lini pertahanan pertama.

---
