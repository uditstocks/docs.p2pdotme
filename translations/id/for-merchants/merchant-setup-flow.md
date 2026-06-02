---
id: merchant-setup-flow
sidebar_position: 2
title: "Alur Pengaturan Merchant"
slug: merchant-setup-flow
---

## Langkah 1 Daftar dan Stake

1. Daftar sebagai merchant untuk mata uang yang aktif.
2. Stake likuiditas penyelesaian yang diperlukan.
3. Konfirmasi profil merchant dan status operasional Anda.

## Langkah 2 Tambahkan Saluran Pembayaran

1. Tambahkan saluran pembayaran untuk jalur yang Anda dukung.
2. Tunggu status persetujuan yang diperlukan.
3. Jaga saluran yang telah disetujui tetap aktif dan mutakhir.

```mermaid
flowchart LR
    register[Register merchant] --> stake[Stake liquidity]
    stake --> addPc[Add payment channels]
    addPc --> approvePc[Channel approval]
    approvePc --> live[Assignable merchant state]
```

---
