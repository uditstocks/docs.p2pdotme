---
id: 08-8-dispute-resolution
sidebar_position: 8
title: "8. Penyelesaian Sengketa"
slug: dispute-resolution
---

Protokol ini dirancang untuk meminimalkan pengungkapan data yang tidak diperlukan selama proses sengketa. Apabila pengguna mengajukan sengketa, pihak lawan dapat menyerahkan bukti transaksi tanpa mengekspos data pribadi tambahan. Dalam implementasi kontrak saat ini, sengketa diselesaikan secara on-chain oleh admin yang berwenang berdasarkan bukti yang diserahkan dan aturan kesalahan protokol. Verifikasi transaksi bank yang menjaga privasi serta penyelesaian otomatis yang lebih mendalam merupakan bagian dari peta jalan (lihat [Bagian 4.2](/id/whitepaper/cryptographic-primitives-proof-integration)).

## 8.1 Jangka Waktu dan Beban Pembuktian

Kewajiban bawaan: pihak yang mengklaim penyelesaian wajib menyediakan bukti penyelesaian. Pihak penantang dapat mengajukan bukti tandingan (misalnya, laporan bank yang menunjukkan dana tidak diterima). Jalur gagal-buktikan akan memicu slashing atau pengembalian dana sesuai dengan aturan Protokol.

## 8.2 Sanksi atas Klaim Palsu

Apabila seorang pembeli mencoba melanjutkan transaksi tanpa benar-benar melakukan transfer fiat terlebih dahulu, mereka berisiko kehilangan Poin Reputasi, sehingga menciptakan disinsentif ekonomi yang kuat terhadap perilaku penipuan.

---
