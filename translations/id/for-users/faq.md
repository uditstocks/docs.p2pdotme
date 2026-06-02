---
id: faq
sidebar_position: 8
title: "FAQ"
slug: faq
---

## Apakah saya perlu memahami mekanisme on-chain?

Tidak, Anda tidak diwajibkan untuk memahami mekanisme on-chain. Aplikasi klien menangani semua interaksi kontrak. Ikuti petunjuk status untuk menyelesaikan tindakan Anda.

## Mengapa pesanan saya tidak dicocokkan secara instan?

Penugasan merchant bergantung pada faktor kelayakan secara real-time, termasuk likuiditas, status saluran, batas volume, dan ketersediaan operasional. Jika tidak ada merchant yang memenuhi syarat, pesanan akan menunggu dan dibatalkan saat habis waktu.

## Bisakah saya mengajukan banding atas sengketa?

Tidak. Dalam rilis saat ini, sengketa hanya dapat diajukan satu kali per pesanan, dan admin yang berwenang menyelesaikannya secara on-chain dengan menetapkan kesalahan. Tidak ada langkah banding terpisah. Tingkatan eskalasi berbasis juri dan berbasis tata kelola direncanakan untuk rilis mendatang.

## Apakah identitas saya disimpan di on-chain?

Tidak ada PII (Informasi Identitas Pribadi) mentah yang disimpan di on-chain. Protokol menggunakan bukti ZK-KYC untuk verifikasi identitas dan hanya menyimpan komitmen serta keputusan di on-chain.

## Bagaimana saya tahu apa yang harus dilakukan selanjutnya?

Status pesanan Anda (`PLACED`, `ACCEPTED`, `PAID`, `COMPLETED`, `CANCELLED`) memberitahu Anda. Setiap status mengimplikasikan tindakan berikutnya yang spesifik. Aplikasi akan memandu Anda melaluinya.
