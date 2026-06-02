---
id: order-assignment
sidebar_position: 7
title: "Penugasan Pesanan"
slug: order-assignment
---

Penugasan pesanan dibatasi oleh pemeriksaan merchant dan saluran pembayaran.

- Status online/offline
- Status daftar hitam, sengketa, dan permintaan penarikan stake
- Pemeriksaan kapasitas pesanan yang sedang berjalan
- Status aktif/disetujui saluran pembayaran
- Pemeriksaan volume harian dan bulanan
- Ambang batas likuiditas fiat dan berbasis stake

Penugasan bersifat deterministik dan terjadi di rantai. Pemeriksaan dilakukan secara berlapis sehingga satu kondisi yang gagal akan menghapus merchant dari kumpulan kandidat tanpa memengaruhi yang lain.

---
