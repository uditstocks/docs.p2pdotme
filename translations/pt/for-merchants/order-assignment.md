---
id: order-assignment
sidebar_position: 7
title: "Atribuição de Pedidos"
slug: order-assignment
---

A atribuição de pedidos é restrita por verificações do comerciante e do canal de pagamento.

- Estado online/offline
- Status de lista negra, disputa e solicitação de desfazimento de stake
- Verificações de capacidade de pedidos em andamento
- Status ativo/aprovado do canal de pagamento
- Verificações de volume diário e mensal
- Limites de liquidez garantidos por fiat e por stake

A atribuição é determinística e on-chain. As verificações são aplicadas em camadas, de modo que uma única condição reprovada remove o comerciante do conjunto de candidatos sem afetar os demais.

---
