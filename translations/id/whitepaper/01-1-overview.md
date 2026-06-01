---
id: 01-1-overview
sidebar_position: 1
title: "1. Ikhtisar"
slug: overview
---

Saat ini, memindahkan uang antara fiat dan kripto berarti mempercayakan dana dan identitas Anda kepada perantara. P2P Protocol adalah lapisan non-kustodial yang mencocokkan transaksi fiat dan stablecoin secara on-chain serta memverifikasi identitas pengguna melalui zero-knowledge proof. Dana tidak pernah disimpan oleh perantara, dan identitas dibuktikan tanpa diungkapkan.

## 1.1 Dari "on/off-ramp" menuju ekonomi berbasis privasi dan kredibilitas

P2P Protocol dimulai dari titik paling praktis, yaitu perpindahan antara fiat dan stablecoin, tanpa escrow kustodial. Rails, proof, dan insentif yang sama yang membuat ramp yang jujur bekerja dalam skala besar juga memungkinkan lapisan berikutnya: likuiditas berbasis kredibilitas, menjembatani kesenjangan antara mata uang fiat dan kripto, untuk seluruh DeFi.

Dalam model ini, reputasi diperoleh on-chain melalui transaksi yang selesai, riwayat sengketa yang bersih, dan tingkatan ZK-KYC, bukan melalui verifikasi akun terpusat. Privasi dijaga secara default melalui zero-knowledge proof untuk verifikasi identitas, yang hanya mengungkapkan bahwa pengguna telah diverifikasi dan diizinkan, tanpa mengekspos identitas mentah. Kegunaan diutamakan: mikro-pembayaran, off-ramp sehari-hari, gaji, remitansi, dan pembayaran merchant dirancang agar terasa semudah mengirim pesan.

## 1.2 Seperti apa "keberhasilan" di tahun 2026 ke atas

- Pengguna di negara mana pun yang didukung dapat membeli, menjual, atau membayar melalui stablecoin dalam hitungan menit, dengan target penyelesaian di bawah 90 detik pada rails yang cepat, tanpa memberikan kustodi kepada siapa pun. Biaya median tetap di bawah $0,20 per $100.
- Merchant dicocokkan on-chain berdasarkan USDC yang di-stake, dengan spread ditetapkan di tingkat protokol alih-alih melalui persaingan merchant. Sistem Proof-of-Credibility menangani pencegahan penipuan dan penentuan batas transaksi.
- ZK-KYC membuka batas yang lebih tinggi dan jalur yang lebih cepat sambil menjaga data pribadi tetap off-chain.
- Lebih dari 99% sengketa diselesaikan oleh proof dalam jangka waktu tantangan, bukan melalui moderasi manual.
- Kredibilitas bersifat portabel. Reputasi dan batas berpindah bersama pengguna di berbagai klien dan negara tanpa mengekspos identitas pribadi.
- Akses bersifat netral. Berbagai dompet dan aplikasi, termasuk [Coins.me](https://coins.me) sebagai referensi antarmuka konsumen, semuanya menggunakan SDK permissionless yang sama di atas Protokol, tanpa gateway yang diistimewakan.
- Seiring kredibilitas terakumulasi, produk baru (pembayaran angsuran, perdagangan tanpa escrow, gaji lintas batas, asuransi sengketa) dapat dibangun tanpa perlu KYC ulang seluruh dunia. Gaji, remitansi, pembayaran marketplace, dan checkout diselesaikan tanpa kustodi dan tanpa formulir KYC kertas.

## 1.3 Prinsip-prinsip dasar

1. **Non-kustodial secara konstruksi.** Tidak ada escrow fiat. Kripto hanya ditahan secara atomik untuk penyelesaian bila diperlukan.
2. **Menjaga privasi.** Buktikan apa yang diperlukan dan jangan ungkapkan hal lain. Privasi diperlakukan sebagai perhatian antarmuka pengguna sekaligus kriptografi, dan verifikasi identitas terbaik adalah yang membuktikan apa yang diperlukan dan tidak lebih dari itu.
3. **Netralitas yang kredibel.** Aturan terbuka, dapat diperbarui melalui governance, tanpa jalur khusus untuk klien mana pun.
4. **Berguna dan sederhana.** Antarmuka menargetkan pengguna non-ahli: alur "Beli USDC" atau "Cairkan" satu ketuk, dengan protokol menangani kompleksitas yang mendasarinya.
5. **Reputasi yang diperoleh dan portabel.** Reputasi diperoleh melalui aktivitas on-chain, berpindah bersama pengguna di berbagai klien dan negara, dan dapat dicabut melalui penalti yang eksplisit. Reputasi tidak pernah dibeli atau dijual.
6. **Protokol-agnostik.** Desain tidak bergantung pada satu L2, oracle, atau vendor proof tertentu. Implementasi dapat berubah tanpa perlu menulis ulang whitepaper.

## 1.4 Apa yang P2P Protocol adalah (dan bukan)

**Adalah:** lapisan koordinasi terbuka dan terdesentralisasi yang secara trustless mencocokkan pembeli dengan merchant on-chain berdasarkan USDC yang di-stake, menyelesaikan perdagangan dengan koordinasi on-chain, dan merutekan biaya serta parameter melalui governance.

**Bukan:** kustodian, bank, atau data broker. P2P Protocol tidak mengkustodikan fiat, tidak menyimpan informasi pribadi pengguna, dan tidak menjanjikan imbal hasil tetap.

## 1.5 Mengapa ini penting sekarang

Selama satu dekade terakhir, kripto memecahkan masalah keuangan terprogram tetapi meninggalkan dunia nyata di luar pintu. Hari ini tiga kurva akhirnya bertemu:

- Rails lokal instan (UPI/PIX/QRIS/ALIAS/SPEI/Pago Movil) sudah menjadi arus utama.
- ZK praktis dapat membuktikan fakta dunia nyata tanpa mengekspos data, sudah digunakan untuk verifikasi identitas, dengan bukti transaksi bank dalam peta jalan.
- L2 dan stablecoin telah membuat pembayaran kecil cukup murah dan cepat untuk diperhatikan.

P2P Protocol berada tepat di persimpangan itu. Protokol ini mengkoordinasikan transfer fiat dan stablecoin serta memverifikasi identitas pengguna dengan proof, tanpa mengambil kustodi dana atau menyimpan data identitas pribadi.

## 1.6 DeFi berbasis kredibilitas (melampaui over-kolateralisasi)

Over-kolateralisasi membuat DeFi awal aman, tetapi hal itu membuat penggunaan sehari-hari menjadi mahal dan sulit diakses. P2P Protocol mengusulkan pilar kedua: **kredibilitas**. Batas yang diperoleh dan harga yang lebih baik berasal dari riwayat yang bersih, transaksi yang selesai, dan tingkatan ZK-KYC, bukan dari mengunci 200% agunan. Privasi terjaga secara default, karena pengguna mengungkapkan proof tindakan bukan identitas. Graf kredibilitas yang sama bersifat komposabel: mendukung pembayaran angsuran, perdagangan tanpa escrow, dan primitif kredit ringan di masa depan.

## 1.7 Protokol untuk semua orang, bukan hanya pengguna berpengalaman

Protokol dirancang untuk pengguna dengan ponsel dan gaji, bukan meja trading profesional. Protokol harus tetap andal pada $15 sebagaimana pada $1.500. Verifikasi mengikuti model pengungkapan minimal: verifikasi ZK-KYC hanya membuktikan predikat yang diperlukan dan tidak mengungkapkan pengenal pribadi apa pun.

## 1.8 Protokol-agnostik berdasarkan desain

Vendor dan chain akan berubah, tetapi prinsip-prinsipnya tidak bisa. Whitepaper berkomitmen pada:

- Tidak ada satu L2, oracle, atau penyedia proof yang tertanam dalam logika.
- Antarmuka yang jelas (registri verifier, adaptor oracle, registri rail) sehingga komponen dapat diganti tanpa menulis ulang whitepaper atau kontrak sosial.
- Open-sourcing dan desentralisasi setiap bagian Protokol sebagai barang publik.

## 1.9 Kredibilitas dengan Privasi

Anggap Proof-of-Credibility dari P2P Protocol sebagai barang publik itu sendiri:

- Ini diperoleh, hanya disesuaikan oleh penalti eksplisit, dan sulit dimanipulasi.
- Ini portabel di berbagai klien dan negara melalui komitmen on-chain, bukan PDF di kotak masuk seseorang.
- Ini mengutamakan privasi. Hanya komitmen dan keputusan yang bersifat publik, dan bukti mentah tetap bersama Anda atau verifier pilihan Anda.

## 1.10 Kepatuhan terprogram (kebijakan tanpa dossier)

Kebanyakan orang menginginkan dua hal sekaligus: privasi dan legalitas. P2P Protocol membuat ini praktis:

- **Kebijakan-sebagai-parameter:** rails, batas waktu, dan persyaratan proof diatur on-chain berdasarkan wilayah dan kelas risiko.
- **Tingkatan ZK-KYC** memenuhi pemeriksaan "pengguna yang diizinkan" sambil menjaga PII tetap off-chain.
- **Kebutuhan serupa Travel Rule** dapat dipenuhi melalui sirkuit pengungkapan selektif (direncanakan) ketika pihak lawan adalah bisnis terdaftar, tanpa mengubah protokol menjadi data broker.

## 1.11 Apa yang terbuka jika kita berhasil

Rails dan proof yang sama mendukung pendapatan tanpa batas, sehingga kreator, kontraktor, dan pekerja jarak jauh dibayar di tempat mereka tinggal tanpa kustodi pertukaran. Marketplace menyelesaikan pembayaran merchant kepada penjual di rails lokal secara instan, dengan spread yang adil, tanpa rekonsiliasi CSV manual. Lapisan kredibilitas dan likuiditas bersama antara domain mata uang fiat dan kripto mendukung keuangan komunitas seperti tabungan bergilir, pinjaman mikro, dan marketplace tanpa escrow. Pengguna mempertahankan kemampuan untuk mentransfer nilai secara privat dan sah selama periode gangguan perbankan lokal atau tekanan kontrol modal.

## 1.12 Pengelolaan dan filosofi governance

- Netralitas yang kredibel di atas kenyamanan. Perubahan melalui governance yang transparan dengan batasan pengaman (timelock, jeda terbatas, audit).
- Minimalkan governance bila memungkinkan: parametrize, jangan micromanage.
- Katup pengaman publik: circuit breaker oracle, sunset verifier, dan jeda darurat dengan kedaluwarsa otomatis.
- Mindset bounty terbuka: bayar untuk menemukan celah lebih awal dan publikasikan perbaikan secara terbuka.

## 1.13 Yang tidak akan kami kompromikan

Protokol tidak mengkustodikan fiat dalam keadaan apa pun. Tidak menyimpan informasi yang dapat mengidentifikasi pribadi (PII) on-chain. Tidak ada klien yang menerima perutean istimewa, dan setiap integrator menggunakan antarmuka yang sama. Komponen yang tidak dapat dibuktikan atau diaudit secara independen tidak diterima ke dalam inti protokol.

## 1.14 Tonggak yang penting

- **Ubiquitas:** kehadiran merchant yang kredibel di setiap pasangan wilayah/rail utama.
- **Jangkauan geografis:** ekspansi ke 20+ pasar di Asia, Afrika, Amerika Latin, dan MENA.
- **Kehadiran multi-chain:** penerapan protokol meluas melampaui Base ke Solana sebagai chain hub, dengan chain berperforma tinggi tambahan yang didukung sebagai spoke.
- **Komposabilitas:** aplikasi pihak ketiga yang menghadirkan fitur berguna pada SDK tanpa meminta izin.
- **Legitimasi mandiri:** regulator dan tim risiko dapat membaca spesifikasi, memverifikasi parameter on-chain, dan memahami bagaimana keamanan dicapai, tanpa backdoor.
- **Fitur peta jalan:** untuk proposal jalur fitur saat ini (termasuk remitansi dan ekspansi mata uang), lihat [`/for-builders`](/id/for-builders/start-here).

---
