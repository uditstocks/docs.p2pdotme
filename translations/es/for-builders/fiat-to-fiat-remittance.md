---
id: fiat-to-fiat-remittance
sidebar_position: 6
title: "Remesa Fiat a Fiat"
slug: fiat-to-fiat-remittance
---

El protocolo ya liquida fiat a stablecoin y stablecoin a fiat de forma independiente. La remesa encadena estos dos tramos de manera atómica. El emisor paga en moneda fiduciaria en el País A, el receptor recibe moneda fiduciaria en el País B, y el paso intermedio por stablecoin es invisible para ambas partes.

```mermaid
flowchart LR
    sender[SenderFiatIn] --> onramp[OnrampLeg]
    onramp --> settlement[CrossBorderSettlement]
    settlement --> offramp[OfframpLeg]
    offramp --> receiver[ReceiverFiatOut]
```

Los rieles de onramp, offramp, disputas y emparejamiento ya existen. La clave es que la remesa es un problema de composición puro, construido a partir de primitivas existentes. No se requieren nuevas hipótesis de confianza.

**Novedades para los desarrolladores.**

- Un tipo de orden vinculado que conecta atómicamente los tramos de onramp y offramp
- Un contrato de custodia que retiene la stablecoin entre tramos (si uno falla, el otro recibe el reembolso)
- Un flujo de reclamación para receptores que aún no tienen cuenta
- Visualización de cotización entre divisas y desglose de comisiones transparente

---
