---
id: 05-5-trade-protocol-on-and-off-ramp
sidebar_position: 5
title: "5. Trade Protocol (On- dan Off-Ramp)"
slug: trade-protocol-on-and-off-ramp
---

Kami memformalkan siklus hidup order sebagai state machine dengan batas waktu:

**Status:** `OPEN → MATCHED → FUNDED → CONFIRMED → SETTLED | DISPUTED → RESOLVED | EXPIRED`

**Parameter Umum (diatur melalui governance):**

- `T_match` (waktu maksimum untuk menerima kecocokan), `T_fiat` (waktu maksimum untuk melakukan transfer fiat), `T_confirm` (jendela konfirmasi), `T_dispute` (jendela tantangan).
- `B_bond_user`, `B_bond_merchant` (bond kinerja opsional/bobot slashing berdasarkan tier reputasi dan kelas risiko payment rail).
- `min_amount`, `max_amount` per rail/wilayah, jadwal biaya, dan jendela kedaluwarsa kuotasi.

## 5.1 On-Ramp (Fiat → USDC di Base, diperluas ke Solana)

1. **Buka:** Pengguna membuka order BELI dengan jumlah dan rail.
2. **Cocok:** Protokol menugaskan merchant secara on-chain berdasarkan USDC yang di-stake. Bond yang dapat dikembalikan dapat dikunci.
3. **Transfer Fiat:** Pengguna membayar fiat ke rekening yang disediakan dalam `T_fiat`.
4. **Konfirmasi Merchant:** Merchant mengonfirmasi penerimaan pembayaran fiat.
5. **Selesaikan:** Kontrak melepaskan USDC ke pengguna. Biaya dinilai dan bond dibuka kuncinya.
6. **Sengketa:** Jika terjadi konflik, para pihak menyerahkan bukti dan admin yang berwenang mengeluarkan putusan on-chain.

## 5.2 Off-Ramp (USDC di Base → Fiat, diperluas ke Solana)

1. **Buka:** Pengguna membuka order JUAL dan mentransfer USDC ke adapter penyelesaian tanpa eskrow (kontrak menahan atau mengalirkan secara atomik sesuai desain).
2. **Cocok:** Merchant menerima dan mengajukan kuotasi/bond.
3. **Kunci Kripto:** USDC pengguna dikunci untuk penyelesaian.
4. **Merchant Membayar Fiat:** Merchant membayar fiat dan mengonfirmasi penyelesaian, atau pengguna mengajukan tantangan.
5. **Selesaikan:** Kontrak melepaskan USDC ke merchant. Biaya dinilai dan bond dibuka kuncinya.
6. **Sengketa:** Jika terjadi konflik, para pihak menyerahkan bukti dan admin yang berwenang mengeluarkan putusan on-chain.

## 5.3 Kelas Risiko Payment Rail

Rail berbeda-beda (instan/tidak dapat dibalikkan vs reversibel/rentan chargeback). Protokol memetakan rail ke pengganda bond, persyaratan konfirmasi, serta jendela sengketa yang lebih panjang atau lebih pendek.

---
