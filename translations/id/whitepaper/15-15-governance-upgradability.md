---
id: 15-15-governance-upgradability
sidebar_position: 15
title: "15. Tata Kelola & Kemampuan Peningkatan"
slug: governance-upgradability
---

- **Parameter:** biaya, batas, bobot risiko jalur, set oracle, kebijakan bukti, jadwal obligasi.
- **Peningkatan:** kontrak di balik timelock dengan proposal publik. Jeda darurat dibatasi pada lingkup yang sempit, dengan sunset otomatis.
- **Dua lapisan:** parameter protokol dan peningkatan di Base diatur oleh pemegang $P2P melalui Governor on-chain (gaya Compound Bravo, dengan kuorum snapshot, ambang proposal, dan timelock terintegrasi). Pencetakan token, perubahan pasokan, dan alokasi treasury diatur di Solana melalui pasar keputusan on-chain MetaDAO, tempat token diterbitkan dan treasury disimpan.
- **Saat ini:** parameter protokol dan peningkatan dioperasikan oleh multisig admin dengan anggota dan batasan yang dipublikasikan, dan Governor on-chain telah diterapkan di Base. Beberapa penyetel parameter, seperti yang ada pada facet konfigurasi protokol, sudah menerima baik Governance Diamond maupun super-admin sebagai pemanggil, sementara penyetel lainnya masih dibatasi oleh super-admin selama masa transisi.
- **Transisi:** otoritas atas parameter protokol, peningkatan, dan peta jalan berpindah ke pemegang $P2P melalui Governor on-chain dalam fase bertahap. Fase-fase tersebut berkembang dari veto admin, ke DAO sebagai jalur utama dengan cadangan admin, hingga kontrol hanya oleh DAO dengan backstop darurat admin yang dibatasi waktu. Alokasi treasury dan segala perubahan pada pasokan token diputuskan melalui tata kelola pasar keputusan MetaDAO di Solana.

---
