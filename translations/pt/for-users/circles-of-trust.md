---
id: circles-of-trust
sidebar_position: 8
title: "Círculos de Confiança"
slug: circles-of-trust
---

Um Círculo é um grupo de comerciantes com respaldo comunitário, operado por um Administrador de Círculo sob regras de protocolo compartilhadas on-chain. Cada Círculo possui sua própria moeda, conjunto de comerciantes, saldo em moeda fiduciária e liquidez em USDC. Os Círculos existem para que as pessoas que conhecem os vendedores locais possam operá-los e apoiá-los, em vez de uma central única administrar todos os mercados. Como comprador, você negocia com comerciantes dentro de um Círculo.

Hoje, você não seleciona um Círculo manualmente. O protocolo atribui um comerciante elegível ao seu pedido com base em fatores em tempo real, como liquidez, status do canal e disponibilidade. A seleção manual de Círculo e a ordenação por reputação estão planejadas para uma versão futura. Quando o aplicativo exibe informações de Círculo junto a um pedido, isso reflete o estado on-chain, como stake do comerciante e histórico de pedidos.

Um Círculo oferece ao comprador duas proteções concretas. Primeiro, os comerciantes fazem stake de USDC e os Administradores de Círculo fazem stake de $P2P para operar, de modo que há colateral por trás das pessoas com quem você negocia. Segundo, cada Círculo é respaldado por reservas de seguro. Existem três pools. O CAIP (Pool de Seguro do Administrador de Círculo, reserva de seguro por Círculo) é uma reserva por Círculo financiada com uma parcela das taxas de pedido. O CALR (Reserva de Perdas do Administrador de Círculo) é um buffer por administrador financiado com uma parcela das recompensas do administrador. O PIP (Pool Insurance Pool, fundo de seguro global do protocolo) é um mecanismo de último recurso em nível de protocolo. Os pools e seu financiamento estão ativos on-chain, e o trabalho de liquidação e a contabilidade de recompensas são executados on-chain e são verificáveis.

O fluxo completo de solicitação de seguro ainda está sendo finalizado e ainda não está disponível. Quando for lançado, as solicitações serão feitas por comerciantes contra os pools nos casos em que USDC for perdido apesar do comportamento adequado do comerciante, e cada solicitação será analisada antes da liquidação, não reembolsada automaticamente. Como comprador, o seu recurso em caso de negociação problemática é o caminho de disputa do pedido, não o caminho de solicitação de seguro.

O seu lado de uma disputa está coberto integralmente em [Disputas e Evidências](/pt/for-users/disputes-and-evidence). Em resumo, uma disputa pode ser aberta uma vez por pedido, e um administrador autorizado a resolve on-chain atribuindo a responsabilidade. Se o comerciante for o responsável, o pedido é concluído e a stablecoin é liquidada para o destinatário. Camadas de escalonamento baseadas em júri e em governança estão planejadas para uma versão futura.

---
