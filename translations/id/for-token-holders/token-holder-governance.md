---
id: token-holder-governance
sidebar_position: 10
title: "Tata Kelola Pemegang Token"
slug: token-holder-governance
---

Model target memberikan pemegang token kendali langsung atas protokol melalui dua lapisan. Parameter protokol dan peningkatan diatur oleh Governor on-chain yang dijelaskan di bawah ini. Alokasi treasury dan pencetakan token diatur oleh MetaDAO futarchy di Solana. Parameter di bawah ini menjelaskan Governor on-chain.

| Parameter           | Nilai. Target atau tipikal, dengan batas on-chain dalam tanda kurung |
| ------------------- | -------------------------------------------------------------------- |
| Kekuatan Suara      | 1 $P2P yang di-stake = 1 suara (dapat didelegasikan)                 |
| Penundaan Pemungutan Suara | 1 hari (dapat dikonfigurasi, 1 detik hingga 30 hari)          |
| Periode Pemungutan Suara  | 7 hari (dapat dikonfigurasi, 1 jam hingga 30 hari)            |
| Kuorum              | Kuorum snapshot, ditetapkan oleh tata kelola                         |
| Kondisi Kelulusan   | Suara mendukung melampaui suara menentang dan memenuhi kuorum         |
| Ambang Batas Proposal | Dibatasi maksimal 10% dari total pasokan                           |
| Timelock            | 7 hari (tipikal, dapat dikonfigurasi, 1 jam hingga 30 hari)          |

Parameter yang diatur oleh Governor on-chain mencakup persentase biaya, konfigurasi spread, aturan staking dan slashing, batas volume transaksi, peningkatan smart contract, dan penambahan token ke whitelist. Alokasi treasury dan pencetakan token diatur secara terpisah oleh MetaDAO futarchy di Solana.

Untuk detail tata kelola di tingkat kontrak (peran, izin, mekanisme sengketa), lihat [`/for-builders`](/id/for-builders/start-here).

---
