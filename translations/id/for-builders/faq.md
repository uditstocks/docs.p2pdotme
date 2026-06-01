---
id: faq
sidebar_position: 9
title: "FAQ"
slug: faq
---

## Di chain mana kontrak di-deploy?

Kontrak pintar protokol ini aktif di Base (EVM). Deployment di Solana direncanakan sebagai bagian dari ekspansi multichain. Token $P2P adalah token SPL di Solana. Lihat [FAQ token dan chain](/id/for-token-holders/faq) untuk detailnya.

## Di mana ABI kontrak tersedia?

Referensi kontrak tercantum di bagian [Referensi Kontrak](/id/for-builders/contract-references). Antarmuka integrasi sudah bersumber terbuka: SDK ([`@p2pdotme/sdk`](https://github.com/p2pdotme/p2pdotme-sdk)), widget React ([`@p2pdotme/widgets`](https://github.com/p2pdotme/widgets)), dan kontrak serta antarmuka integrator B2B ([`payment-integrators`](https://github.com/p2pdotme/payment-integrators)). Kontrak Diamond inti protokol sedang menunggu audit dan akan dibuka sebagai sumber terbuka setelahnya.

## Bisakah saya menambahkan negara atau mata uang baru?

Kerangka kerja ekspansi mata uang menggunakan konfigurasi YAML sumber terbuka. Siapa pun yang memiliki pengetahuan tentang jalur pembayaran lokal dapat mengusulkan mata uang baru melalui PR.

## Bagaimana cara kerja sengketa di tingkat kontrak?

Pengguna memanggil `raiseDispute` pada `OrderProcessorFacet`. Admin menyelesaikan sengketa melalui `adminSettleDispute` dengan tipe kesalahan. Penyelesaian memicu akuntansi dan hook RP. Lihat [Sengketa](/id/for-builders/disputes) untuk alur lengkapnya.

## Apa itu arsitektur Diamond?

Protokol ini menggunakan Standar Diamond EIP-2535. Fungsionalitas dibagi ke dalam facet-facet yang berbagi penyimpanan, memungkinkan pembaruan modular tanpa perlu men-deploy ulang seluruh kontrak.

## Bagaimana RP terintegrasi dengan alur order?

Hook RP terdaftar dalam `ReputationManager`. Pembaruan volume order, penalti sengketa, dan hadiah yang diatur oleh verifikasi semuanya mengalir melalui hook ini. Lihat [Reputasi](/id/for-builders/reputation).

## Di mana detail tata kelola untuk pemegang token?

Tata kelola pemegang token (model pemungutan suara, kuorum, desentralisasi progresif) didokumentasikan di [`/for-token-holders`](/id/for-token-holders/start-here).

---
