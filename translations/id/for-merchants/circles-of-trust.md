---
id: circles-of-trust
sidebar_position: 5
title: "Circles of Trust"
slug: circles-of-trust
---

Circles of Trust adalah kumpulan merchant yang didukung komunitas dan dioperasikan oleh seorang Circle Admin. Setiap Circle berfungsi sebagai unit semi-otonom dalam protokol, mengelola jaringan merchantnya sendiri sambil mematuhi aturan protokol on-chain yang berlaku bersama.

Circles mengorganisasi merchant ke dalam kelompok-kelompok yang bertanggung jawab, memungkinkan pengawasan komunitas melalui staking dan delegasi, serta mendistribusikan risiko melalui kumpulan asuransi bertingkat.

```mermaid
flowchart TD
    user[User order]
    orderFlow[Order flow]
    registry[Merchant registry]
    country[Country config]
    assignment[Eligibility and assignment checks]
    settlement[Settlement and accounting]

    user --> orderFlow
    orderFlow --> registry
    orderFlow --> country
    registry --> assignment
    country --> assignment
    assignment --> settlement
```

Registri merchant adalah inti operasional yang dibungkus oleh Circles. Semua operasi merchant bersifat on-chain dan dibatasi oleh peran.

*Entitas Circle kelas pertama dengan siklus hidup tersendiri, peran Circle Admin dengan persyaratan stake yang eksplisit, serta pengelompokan merchant dalam lingkup Circle direncanakan untuk rilis mendatang.*

---
