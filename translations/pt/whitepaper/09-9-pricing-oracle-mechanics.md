---
id: 09-9-pricing-oracle-mechanics
sidebar_position: 9
title: "9. Mecânica de Preços e Oráculos"
slug: pricing-oracle-mechanics
---

O Protocolo determina preços indicativos usando adaptadores de oráculo incorporados que agregam taxas de exchanges selecionadas e locais P2P em uma mediana/TWAP com fallbacks. Esses oráculos analisam dados de preço de uma variedade de exchanges, tanto centralizadas quanto P2P, para determinar o preço de negociação do par stablecoin-fiat em questão.

**Parâmetros:** conjunto de fontes, limites de obsolescência, limiares de desvio e disjuntores de circuito. As cotações carregam uma data de expiração para limitar a exposição. Se o oráculo falhar ou exceder os limites de desvio, os pedidos são pausados ou re-cotados.

---
