---
id: contract-references
sidebar_position: 5
title: "Referências de Contratos"
slug: contract-references
---

- `facets/CountryFacet.sol` (governança de configuração de moedas e canais de pagamento)
- `facets/P2pConfigFacet.sol` (precificação, spread, configuração administrativa)
- `facets/OrderProcessorFacet.sol` (disputas, limites, limiares)
- `facets/MerchantRegistryFacet.sol` e `facets/MerchantOnboardFacet.sol` (controles de comerciante, taxas, stake/unstake)
- `facets/OrderFlowFacet.sol` e `facets/OrderFlowHelper.sol` (ciclo de vida do pedido, correspondência, liquidação)
- `ReputationManager.sol` (contrato UUPS independente, separado do Diamond, com hooks de RP e controle de acesso a recompensas/verificação)
- `storages/MerchantRegistryStorage.sol`, `storages/CountryStorage.sol`, `storages/OrderProcessorStorage.sol`
- `libraries/MerchantRegistryLib.sol`

---
