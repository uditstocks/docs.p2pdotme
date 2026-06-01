---
id: contract-references
sidebar_position: 5
title: "Referencias de Contratos"
slug: contract-references
---

- `facets/CountryFacet.sol` (gobernanza de configuración de monedas y canales de pago)
- `facets/P2pConfigFacet.sol` (precios, spread, configuración de administración)
- `facets/OrderProcessorFacet.sol` (disputas, límites, umbrales)
- `facets/MerchantRegistryFacet.sol` y `facets/MerchantOnboardFacet.sol` (controles de comerciante, comisiones, depósito/retiro de garantía)
- `facets/OrderFlowFacet.sol` y `facets/OrderFlowHelper.sol` (ciclo de vida de órdenes, emparejamiento, liquidación)
- `ReputationManager.sol` (contrato UUPS independiente, separado del Diamond; hooks de RP, habilitación de recompensas y verificación)
- `storages/MerchantRegistryStorage.sol`, `storages/CountryStorage.sol`, `storages/OrderProcessorStorage.sol`
- `libraries/MerchantRegistryLib.sol`

---
