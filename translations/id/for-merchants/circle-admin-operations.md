---
id: circle-admin-operations
sidebar_position: 13
title: "Operasi Circle Admin"
slug: circle-admin-operations
---

Seorang Circle Admin mengoperasikan kelompok merchant yang didukung komunitas di bawah satu mata uang dan satu konfigurasi. Peran ini adalah menjalankan unit operasional lokal. Anda merekrut merchant dan menyetujui saluran pembayaran mereka, menyelesaikan sengketa di dalam Circle Anda, memberikan dukungan operasional, dan memantau kinerja merchant. Setiap wallet dapat mengoperasikan satu Circle, yang dicatat secara on-chain berdasarkan alamat admin.

## Yang bukan menjadi tanggung jawab peran ini

Beberapa hal berada secara eksplisit di luar tanggung jawab Circle Admin, karena protokol yang menanganinya.

- Pemrosesan dan penyelesaian pembayaran berjalan secara otomatis on-chain.
- Tidak ada dana pihak ketiga yang dipegang oleh admin. Saldo dieskrow dan diselesaikan oleh Diamond.
- KYC pengguna ditangani oleh lapisan verifikasi protokol, bukan oleh admin.

## Membuat Circle

Pembuatan Circle bersifat permissionless. Wallet mana pun yang memenuhi persyaratan minimum stake $P2P per mata uang dapat membuatnya, dengan syarat wallet tersebut belum mengoperasikan Circle lain dan nama yang dipilih unik secara global. Mata uang tersebut harus sudah terdaftar di protokol.

1. Hubungkan wallet Anda ke antarmuka Circle Admin.
2. Konfigurasi nama Circle, mata uang operasional, URL komunitas, dan pengaturan persetujuan otomatis untuk saluran pembayaran. Persetujuan manual adalah pilihan yang lebih konservatif.
3. Lakukan stake $P2P ke protokol. Stake dicatat terhadap alamat admin Anda dan tetap terkunci selama Circle beroperasi.
4. Konfirmasi transaksi. Circle beralih ke status aktif setelah stake Anda tersedia.

Minimum stake admin ditetapkan per negara. Default spesifikasi saat ini adalah setara $250 USDC dalam $P2P. Minimum on-chain mungkin belum diatur hingga suatu negara dikonfigurasi, sehingga nilai minimum live yang ditampilkan di aplikasi bersifat otoritatif. Circle menjadi tidak aktif jika stake admin turun di bawah minimum yang dikonfigurasi. Anda dapat menambahkan stake kapan saja, dan Anda dapat mengajukan permintaan untuk melakukan unstake hingga batas minimum melalui alur permintaan dan pendinginan.

## Mekanisme biaya dan pendapatan

Biaya operasional adalah stake $P2P yang terkunci ditambah gas transaksi. Stake adalah jaminan operasional, bukan biaya. Stake dikembalikan melalui alur unstake sesuai ketentuan pendinginan, dan dapat dipotong oleh super admin dalam kasus pelanggaran yang telah ditetapkan.

Dari sisi pendapatan, sebuah Circle memperoleh komisi Circle yang dinyatakan sebagai bagian dari volume Circle. Default saat ini adalah 0,25 persen dari volume Circle, dibagi antara Circle Admin dan para staker komunitas $P2P berdasarkan rasio yang dapat dikonfigurasi. Nilai live ditampilkan di aplikasi. Sebagian penghasilan admin ditahan sebagai buffer bergulir yang terkunci (Circle Admin Loss Reserve) sebelum dapat diklaim. Pembagian antara Circle Admin dan para staker komunitas $P2P serta porsi yang terkunci dapat dikonfigurasi per mata uang.

## Kontrol akses dan pendelegasian tugas

Circle Admin memegang izin default untuk Circle dan dapat memberikan izin tertentu kepada pembantu melalui kontrol akses berbasis kapabilitas, dengan cakupan per Circle. Pemberian izin yang umum mencakup persetujuan atau penolakan saluran pembayaran merchant, penyelesaian sengketa, dan pemblokiran merchant. Pemberian izin dapat dicabut kapan saja, dan dicabut secara otomatis ketika peran admin dialihkan. Pemberian izin tidak mengalihkan akuntabilitas. Circle Admin tetap bertanggung jawab atas keputusan yang dibuat berdasarkan izin yang diberikan.

## Status Circle dan penolakan

Sebuah Circle aktif selama stake admin berada pada atau di atas minimum dan Circle belum ditolak. Penyelesaian sengketa yang membebankan kesalahan pada merchant menambah penghitung sengketa per Circle. Ketika penghitung melampaui ambang batas yang dikonfigurasi untuk mata uang tersebut, Circle secara otomatis beralih ke status ditolak dan penerimaan merchant baru diblokir hingga super admin mereset penghitung. Tidak ada peluruhan otomatis berbasis waktu terhadap penghitung tersebut.

---
