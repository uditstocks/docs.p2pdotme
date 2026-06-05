---
id: verification-and-limits
sidebar_position: 9
title: "Verifikasi dan Batas Transaksi"
slug: verification-and-limits
---

P2P Protocol memverifikasi identitas menggunakan bukti zero-knowledge. Verifikasi membuktikan bahwa Anda memenuhi kriteria kelayakan tanpa mengungkapkan siapa Anda. Tidak ada data pribadi mentah yang disimpan secara on-chain. Protokol hanya menyimpan komitmen dan keputusan.

Verifikasi menggunakan beberapa jalur zero-knowledge, dan Anda perlu melewati setidaknya satu untuk dapat menempatkan pesanan.

ZK Passport membaca paspor Anda melalui NFC. Anda memindai halaman foto paspor, lalu memindai chip NFC di sampul belakang. Bukti ini mengonfirmasi bahwa Anda memegang paspor yang sah dan memenuhi persyaratan usia. Nama, nomor paspor, foto, dan data pribadi lainnya tidak dibagikan.

Di India, Anon Aadhaar memverifikasi bahwa Anda memegang catatan Aadhaar yang sah. Bukti mengonfirmasi catatan tersebut tanpa mengungkapkan nomor Aadhaar Anda, dan hanya keputusan yang dihasilkan yang sampai ke blockchain.

Reclaim Protocol memverifikasi akun media sosial Anda secara privat melalui zkTLS. Sistem ini memeriksa sinyal seperti usia dan aktivitas akun terhadap kriteria kelayakan, tanpa memberikan protokol akses ke konten akun Anda. Jika Anda melihat pesan bahwa akun Anda tidak memenuhi persyaratan kelayakan, berarti akun Anda tidak melewati kriteria minimum untuk platform tersebut. Anda dapat menggunakan verifikasi ZK Passport sebagai gantinya.

Verifikasi berkontribusi pada Reputation Points (RP) Anda, yaitu skor on-chain yang menentukan berapa banyak yang dapat Anda transaksikan. RP bertumbuh seiring Anda memverifikasi identitas dan ketika volume transaksi yang diselesaikan mencapai tonggak tertentu. Volume kumulatif yang diselesaikan sebesar $1.000, $5.000, $20.000, dan $50.000 masing-masing memberikan tonggak RP. Pesanan yang dibatalkan tidak dihitung terhadap batas Anda.

Batas per-transaksi meningkat seiring RP, menggunakan rasio per-mata uang. Default yang dipublikasikan adalah 1 RP menjadi $1 USDC untuk INR dan ARS, dan 1 RP menjadi $2 USDC untuk BRL dan IDR. Batas per-transaksi dibatasi dengan cap default yang dipublikasikan sebesar $400 per perdagangan, dan terdapat batas minimum jual default yang dipublikasikan sebesar $100 per perdagangan. Sebelum verifikasi ZK apa pun, batas beli adalah $0 dan penjualan dibatasi oleh minimum tersebut. Jumlah pesanan harian dan bulanan juga berlaku, dengan default yang dipublikasikan sebesar 5 pesanan beli per hari dan 25 pesanan beli per bulan. Ini adalah default saat ini. Nilai aktual yang berlaku untuk akun Anda ditampilkan di dalam aplikasi.

---
