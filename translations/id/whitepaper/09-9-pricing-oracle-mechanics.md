---
id: 09-9-pricing-oracle-mechanics
sidebar_position: 9
title: "9. Mekanisme Penetapan Harga & Oracle"
slug: pricing-oracle-mechanics
---

Protokol menentukan harga indikatif menggunakan adaptor oracle bawaan yang mengumpulkan kurs dari bursa terpilih dan platform P2P ke dalam median/TWAP dengan mekanisme fallback. Oracle ini menganalisis data harga dari berbagai bursa terpusat maupun P2P untuk menentukan harga perdagangan pasangan stablecoin-fiat yang bersangkutan.

**Parameter:** kumpulan sumber, batas kedaluwarsa data, ambang batas deviasi, dan pemutus sirkuit. Kuotasi memiliki waktu kedaluwarsa untuk membatasi eksposur. Jika oracle gagal atau melampaui batas deviasi, pesanan dijeda atau dikutip ulang.

---
