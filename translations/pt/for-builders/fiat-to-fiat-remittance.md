---
id: fiat-to-fiat-remittance
sidebar_position: 6
title: "Remessas Fiat para Fiat"
slug: fiat-to-fiat-remittance
---

O protocolo já liquida fiat para stablecoin e stablecoin para fiat de forma independente. As remessas encadeiam essas duas etapas de forma atômica. O remetente paga em moeda fiduciária no País A, o destinatário recebe em moeda fiduciária no País B, e a passagem pela stablecoin no meio é invisível para ambos.

```mermaid
flowchart LR
    sender[SenderFiatIn] --> onramp[OnrampLeg]
    onramp --> settlement[CrossBorderSettlement]
    settlement --> offramp[OfframpLeg]
    offramp --> receiver[ReceiverFiatOut]
```

As trilhas de onramp, offramp, disputa e correspondência já existem. O ponto central é que a remessa é puramente um problema de composição construído a partir de primitivas existentes. Nenhuma nova premissa de confiança é necessária.

**O que há de novo para desenvolvedores.**

- Um tipo de ordem vinculada que conecta atomicamente as etapas de onramp e offramp
- Um contrato de escrow que retém a stablecoin entre as etapas (falha em um lado reembolsa o outro)
- Um fluxo de reivindicação para destinatários que ainda não possuem contas
- Exibição de cotação entre moedas e detalhamento transparente de tarifas

---