---
id: contract-references
sidebar_position: 5
title: "Referensi Kontrak"
slug: contract-references
---

- `facets/CountryFacet.sol` (tata kelola konfigurasi mata uang dan saluran pembayaran)
- `facets/P2pConfigFacet.sol` (penetapan harga, spread, konfigurasi admin)
- `facets/OrderProcessorFacet.sol` (sengketa, batas, ambang batas)
- `facets/MerchantRegistryFacet.sol` dan `facets/MerchantOnboardFacet.sol` (kontrol merchant, biaya, stake/unstake)
- `facets/OrderFlowFacet.sol` dan `facets/OrderFlowHelper.sol` (siklus hidup order, pencocokan, penyelesaian)
- `ReputationManager.sol` (kontrak UUPS mandiri, terpisah dari Diamond; hook RP, gating reward/verifikasi)
- `storages/MerchantRegistryStorage.sol`, `storages/CountryStorage.sol`, `storages/OrderProcessorStorage.sol`
- `libraries/MerchantRegistryLib.sol`

---
