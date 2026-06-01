---
id: 04-4-cryptographic-primitives-proof-integration
sidebar_position: 4
title: "4. Primitif Kriptografi & Integrasi Bukti"
slug: cryptographic-primitives-proof-integration
---

## 4.1 Verifikasi Identitas (Aktif)

P2P Protocol menggunakan bukti ZK untuk verifikasi identitas yang menjaga privasi. Anggota baru dapat melakukan KYC tanpa kepercayaan pihak ketiga dengan berbagi bukti ZK atas identitas mereka, menjaga data pribadi tetap privat sekaligus membangun reputasi on-chain dan membuka batas transaksi yang lebih tinggi tanpa mengungkapkan PII mentah di on-chain.

Protokol saat ini mendukung verifikasi identitas melalui beberapa metode berbasis ZK:

- **Verifikasi ID Pemerintah** melalui verifier bukti ZK on-chain untuk dokumen identitas yang didukung.
- **Verifikasi akun sosial** melalui **Reclaim Protocol** [1], yang menggunakan bukti zkTLS untuk memverifikasi kepemilikan dan status akun yang didukung (LinkedIn, GitHub, X, Instagram, Facebook) tanpa mengekspos kredensial akun atau data pribadi.
- **Verifikasi paspor** melalui sistem bukti ZK yang dapat memverifikasi usia, kewarganegaraan, dan status sanksi tanpa mengungkapkan isi dokumen.

Setiap verifikasi yang berhasil memperkuat reputasi on-chain pengguna dan memperluas kapasitas transaksi mereka dalam protokol.

## 4.2 Modul Bukti untuk Verifikasi Transaksi Bank (Roadmap)

Modul bukti yang direncanakan akan memperluas kemampuan ZK protokol ke verifikasi transaksi bank untuk penyelesaian sengketa on-chain. Modul ini akan menggunakan bukti berbasis TLS sehingga pengguna atau merchant dapat menghasilkan saksi kriptografis bahwa pernyataan tertentu tentang transfer bank atau tanda terima pembayaran adalah benar, tanpa mengekspos kredensial atau detail transaksi.

Modul yang direncanakan akan menentukan tempat bukti diverifikasi:

- **Verifier on-chain** untuk klaim ringkas dan hash attestasi.
- **Verifier/relayer off-chain** (referensi open-source) untuk pernyataan yang kompleks atau spesifik terhadap jalur pembayaran tertentu, yang memposting attestasi ringkas kembali ke on-chain.

> Bukti mentah akan tetap berada pada pengguna, dan chain hanya menyimpan komitmen dan putusan yang minimal.

## 4.3 Properti Privasi

Implementasi ZK-KYC saat ini menyediakan:

- **Pengungkapan non-interaktif:** berbagi hanya buktinya, bukan data yang mendasarinya.
- **Pengungkapan selektif:** hanya field yang diperlukan oleh sirkuit verifikasi yang diekspos ke sirkuit tersebut.
- **Keterkaitan terbatas:** ID protokol dan komitmen meminimalkan keterkaitan lintas-sesi sejauh memungkinkan.

Modul bukti yang direncanakan akan memperluas properti privasi ini ke verifikasi transaksi bank.

---
