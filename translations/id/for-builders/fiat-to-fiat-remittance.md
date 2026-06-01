---
id: fiat-to-fiat-remittance
sidebar_position: 6
title: "Remitansi Fiat-ke-Fiat"
slug: fiat-to-fiat-remittance
---

Protokol ini sudah menyelesaikan transaksi fiat-ke-stablecoin dan stablecoin-ke-fiat secara independen. Remitansi menggabungkan kedua leg tersebut secara atomik. Pengirim membayar dengan fiat di Negara A, penerima mendapat fiat di Negara B, dan lompatan stablecoin di tengahnya tidak terlihat oleh keduanya.

```mermaid
flowchart LR
    sender[SenderFiatIn] --> onramp[OnrampLeg]
    onramp --> settlement[CrossBorderSettlement]
    settlement --> offramp[OfframpLeg]
    offramp --> receiver[ReceiverFiatOut]
```

Jalur onramp, offramp, sengketa, dan pencocokan semuanya sudah tersedia. Wawasan kuncinya adalah bahwa remitansi murni merupakan masalah komposisi yang dibangun dari primitif-primitif yang sudah ada. Tidak diperlukan asumsi kepercayaan baru.

**Yang baru bagi para builder.**

- Tipe order yang terhubung yang secara atomik menghubungkan leg onramp dan offramp
- Kontrak escrow yang menahan stablecoin di antara leg (kegagalan pada satu sisi akan mengembalikan dana ke sisi lainnya)
- Alur klaim penerima bagi mereka yang belum memiliki akun
- Tampilan kuotasi lintas mata uang dan rincian biaya yang transparan

---
