---
id: faq
sidebar_position: 13
title: "FAQ"
slug: faq
---

## Apakah saya perlu memahami mekanisme on-chain?

Tidak, Anda tidak diwajibkan untuk memahami mekanisme on-chain. Aplikasi klien menangani semua interaksi kontrak. Ikuti petunjuk status untuk menyelesaikan tindakan Anda.

## Mengapa pesanan saya tidak dicocokkan secara instan?

Penugasan merchant bergantung pada faktor kelayakan secara real-time, termasuk likuiditas, status saluran, batas volume, dan ketersediaan operasional. Jika tidak ada merchant yang memenuhi syarat, pesanan akan menunggu dan dibatalkan saat habis waktu.

## Bisakah saya mengajukan banding atas sengketa?

Tidak. Dalam rilis saat ini, sengketa hanya dapat diajukan satu kali per pesanan, dan admin yang berwenang menyelesaikannya secara on-chain dengan menetapkan kesalahan. Tidak ada langkah banding terpisah. Tingkatan eskalasi berbasis juri dan berbasis tata kelola direncanakan untuk rilis mendatang.

## Apakah identitas saya disimpan secara on-chain?

Tidak ada PII (Personally Identifiable Information, Informasi Identitas Pribadi) mentah yang disimpan secara on-chain. Protokol menggunakan bukti ZK-KYC untuk verifikasi identitas dan hanya menyimpan komitmen serta keputusan secara on-chain.

## Bagaimana saya tahu apa yang harus dilakukan selanjutnya?

Status pesanan Anda (`PLACED`, `ACCEPTED`, `PAID`, `COMPLETED`, `CANCELLED`) memberitahu Anda. Setiap status mengimplikasikan tindakan berikutnya yang spesifik. Aplikasi akan memandu Anda melaluinya.

## Jenis dompet apa yang saya gunakan?

Dompet disediakan di dalam aplikasi saat masuk, sehingga Anda tidak perlu membawa dompet sendiri. Akun bersifat self-custodial, yang berarti Anda yang mengendalikan kunci dan protokol tidak dapat memulihkan akses untuk Anda.

## Mengapa saldo saya tampak hilang?

Saldo Anda disimpan di akun dalam aplikasi. Periksa terlebih dahulu di dalam aplikasi, lalu cari alamat akun Anda di BaseScan untuk mengonfirmasi kondisi on-chain. Jika saldo masih terlihat tidak benar, hubungi dukungan dalam aplikasi sebelum mencoba transfer on-chain secara manual.

## Apakah aplikasi mendukung passkey?

Ya. Anda dapat masuk menggunakan passkey. Sebagai langkah pengamanan, tambahkan lebih dari satu metode masuk di pengaturan dompet Anda agar kehilangan satu metode tidak mengunci Anda dari akun self-custodial.

## Bisakah saya menginstal aplikasi di ponsel atau komputer saya?

Tidak ada listing di toko aplikasi native. Aplikasi diinstal sebagai Progressive Web App (PWA). Di ponsel, buka situs dan pilih Add to Home Screen dari menu browser. Di komputer, buka situs di Chrome dan pilih Install app dari menu.
