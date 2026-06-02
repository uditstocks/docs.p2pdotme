---
id: 11-11-security-model
sidebar_position: 11
title: "11. Model Keamanan"
slug: security-model
---

## 11.1 Asumsi & Pihak yang Berpotensi Jahat

- Ketersediaan jaringan di Base (ekspansi multi-rantai ke Solana direncanakan), serta ketersediaan oracle. Asumsi mayoritas jujur tidak diperlukan untuk jalur fiat.
- Pihak yang berpotensi jahat mencakup pelaku penipuan chargeback, pemalsu bukti, manipulator oracle, griefer, dan sybil.

## 11.2 Mitigasi

- Jaminan dan pemotongan (slashing), jendela waktu berbasis kelas jalur, persyaratan verifikasi bukti, penjaga deviasi oracle, serta pembatasan laju dan batas transaksi.
- **Audit & Hadiah Bug:** Kontrak inti, verifier, dan sirkuit akan menjalani audit independen. Program hadiah bug publik akan beroperasi sebelum dan sesudah TGE.

---
