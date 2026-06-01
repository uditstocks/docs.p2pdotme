---
id: how-to-place-an-order
sidebar_position: 3
title: "Cara Memasang Pesanan"
slug: how-to-place-an-order
---

1. Buka aplikasi dan pilih `BUY`, `SELL`, atau `PAY`.
2. Masukkan jumlah serta detail penerima/pembayaran yang diperlukan.
3. Kirim pesanan dan tunggu penugasan merchant.
4. Ikuti petunjuk aplikasi untuk transfer dan konfirmasi.

```mermaid
flowchart TD
    start[Start the app] --> choose[Choose order type]
    choose --> buy[BUY]
    choose --> sell[SELL]
    choose --> pay[PAY]
    buy --> submit[Submit order]
    sell --> submit[Submit order]
    pay --> submit[Submit order]
    submit --> assign[Merchant assigned]
    assign --> transfer[Complete transfer step]
    transfer --> finish[Order final state]
```

---
