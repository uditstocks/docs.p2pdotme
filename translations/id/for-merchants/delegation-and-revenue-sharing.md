---
id: delegation-and-revenue-sharing
sidebar_position: 9
title: "Delegasi dan Bagi Hasil"
slug: delegation-and-revenue-sharing
---

Delegator melakukan stake USDC ke dalam pool delegasi Circle untuk mendukung para merchant di dalamnya dan mendapatkan bagian dari reward merchant yang proporsional dengan jumlah stake yang mereka delegasikan. Circle Admin secara terpisah melakukan stake $P2P untuk membuat dan mengoperasikan Circle. Pendapatan dibagi dalam basis poin yang dikonfigurasi per mata uang. Merchant dan Circle Admin masing-masing menerima bagian dasar dari volume transaksi. Bagian merchant kemudian dibagi berdasarkan rasio self-stake terhadap delegated stake, dan porsi delegated stake selanjutnya dibagi antara merchant, Circle Admin, dan pool delegasi berdasarkan parameter per mata uang yang dapat dikonfigurasi.

Distribusi di dalam Circle ini terpisah dari pembagian pendapatan di tingkat protokol. Pada tingkat protokol, 20 persen pendapatan protokol dialirkan ke treasury dan 80 persen kepada operator jaringan (merchant, Circle Admin, delegator, dan asuransi). Pembagian yang diuraikan di sini mengatur cara porsi operator dari satu pesanan dibagi di dalam Circle, dan ditetapkan dalam basis poin per mata uang. Nilai di bawah ini adalah default spesifikasi saat ini untuk porsi delegated stake, dan nilai live ditampilkan di aplikasi.

| Penerima | Bagian default dari porsi delegated stake |
|----------|-------------------------------------------|
| Merchant | 60 persen |
| Delegator USDC | 20 persen |
| Circle Admin Insurance Pool (CAIP) | 10 persen |
| Circle Admin | 10 persen |

Distribusi reward kepada delegator berbasis snapshot. Pool melacak reward per token dan membayar setiap delegator secara proporsional dengan bagian mereka ketika reward diberitahukan. Delegator mengklaim reward yang telah terhimpun melalui aplikasi dan keluar melalui permintaan dan pendinginan.

*Antarmuka pengguna delegasi lengkap dan mekanisme perutean reward di tingkat Circle direncanakan untuk rilis mendatang.*

---
