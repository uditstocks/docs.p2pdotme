---
id: p2pkit-integration
sidebar_position: 11
title: Integrasi P2PKit
---

# Integrasi P2PKit

P2PKit memungkinkan pengembang untuk menerima pembayaran lokal dan menyelesaikan dalam USDC, menjangkau pengguna di pasar di mana pembayaran kartu tradisional tidak bekerja.

## Ringkasan

P2PKit mengorkestrasi pembayaran lokal secara global, memungkinkan aplikasi Anda untuk:

- **Terima pembayaran lokal** - Pengguna membayar melalui kode QR, UPI, PIX, transfer bank, dan metode lokal lainnya
- **Selesaikan dalam USDC** - Terima pembayaran on-chain dalam USDC di Base, bukan dalam rekening bank lokal
- **Verifikasi instan** - Verifikasi on-chain pembayaran tanpa risiko pelaporan sendiri
- **Perluas secara global** - Jangkau pasar baru tanpa mengelola infrastruktur pembayaran lokal

## Cara Kerjanya

### 1. Pengguna Memulai Pembayaran
Pengguna memindai kode QR atau memilih metode pembayaran pilihan mereka (UPI, PIX, transfer bank, dll.) di aplikasi Anda. Tidak diperlukan pengetahuan kripto atau aplikasi baru.

### 2. Pengumpulan Mitra Lokal
P2PKit secara instan menemukan mitra terverifikasi di pasar pelanggan yang mengumpulkan pembayaran secara lokal.

### 3. Verifikasi Pembayaran
Setelah mitra mengonfirmasi penerimaan dana, transaksi diselesaikan on-chain. Semua verifikasi bersifat kriptografis dan dapat diverifikasi.

### 4. Penyelesaian USDC
Aplikasi Anda menerima USDC di Base, siap dibelanjakan, ditransfer, atau disimpan—diselesaikan dalam satu token di semua pasar.

## Fitur Utama

- **Risiko Penyimpanan Nol** - Kontrak pintar non-custodial menangani semua penyelesaian
- **Penyelesaian Instan** - USDC tiba di Base segera setelah konfirmasi pembayaran
- **Dukungan Multi-Mata Uang** - Terima pembayaran dalam lebih dari 25 mata uang fiat
- **Fleksibilitas Metode** - Dukung Wise, Venmo, PIX, UPI, transfer bank, MercadoPago, dan banyak lagi
- **Jangkauan Global** - Beroperasi di pasar berkembang tanpa hubungan perbankan lokal

## Metode Pembayaran yang Didukung

| Metode | Mata Uang |
|--------|----------|
| **Wise** | USD, EUR, GBP, dll. |
| **Venmo** | USD |
| **PIX** | BRL |
| **UPI** | INR |
| **Transfer Bank** | Berbeda |
| **MercadoPago** | BRL, ARS, MXN |
| **Revolut** | USD, EUR, GBP |
| **Zelle** | USD |
| **Monzo** | GBP |

## Jalur Integrasi

Untuk mengintegrasikan P2PKit dengan Protokol P2P:

1. **Konfigurasi P2PKit** - Setel metode pembayaran dan akun penyelesaian
2. **Buat Pesanan** - Hasilkan pesanan P2PKit dari aplikasi Anda
3. **Terima Penyelesaian** - USDC tiba di Base untuk pemrosesan transaksi
4. **Rute ke P2P** - Gunakan Protokol P2P untuk operasi on/off-ramp jika diperlukan

## Referensi API

Untuk detail integrasi lengkap dan SDK, kunjungi:

- **Dokumentasi Resmi**: [p2pkit.com](https://p2pkit.com/)
- **Paket SDK**: `@zkp2p/offramp-sdk` dan paket terkait tersedia di npm

## Kasus Penggunaan

- **Pengiriman Uang Global** - Terima pembayaran lokal, selesaikan dalam USDC untuk transfer on-chain
- **Penyelesaian Pedagang** - Terima pembayaran dari pasar mana pun, selesaikan dalam satu stablecoin
- **Perdagangan Lintas Batas** - Sederhanakan transaksi multimata uang
- **On-Ramps DeFi** - Hubungkan metode pembayaran lokal ke likuiditas on-chain

## Langkah Berikutnya

- Tinjau titik integrasi Protokol P2P di [`/id/for-builders/sdk`](/id/for-builders/sdk)
- Jelajahi parameter protokol di [`/id/for-builders/protocol-parameters`](/id/for-builders/protocol-parameters)
- Periksa referensi kontrak di [`/id/for-builders/contract-references`](/id/for-builders/contract-references)
