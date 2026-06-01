---
id: faq
sidebar_position: 8
title: "FAQ"
slug: faq
---

## Preciso entender como funcionam os mecanismos on-chain?

Não, você não precisa entender os mecanismos on-chain. O aplicativo cliente cuida de toda a interação com os contratos. Siga os indicadores de status para concluir sua ação.

## Por que meu pedido não foi correspondido instantaneamente?

A atribuição de comerciante depende de fatores de elegibilidade em tempo real, incluindo liquidez, status do canal, limites de volume e disponibilidade operacional. Se nenhum comerciante estiver qualificado, o pedido fica em espera e é cancelado quando o tempo limite expira.

## Posso recorrer de uma disputa?

Não. Na versão atual, uma disputa pode ser aberta apenas uma vez por pedido, e um administrador autorizado a resolve on-chain atribuindo a responsabilidade. Não há etapa de recurso separada. Camadas de escalonamento baseadas em júri e governança estão planejadas para uma versão futura.

## Minha identidade é armazenada on-chain?

Nenhuma PII (Informação Pessoalmente Identificável) bruta é armazenada on-chain. O protocolo usa provas ZK-KYC para verificação de identidade e armazena apenas compromissos e veredictos on-chain.

## Como sei o que fazer a seguir?

O status do seu pedido (`PLACED`, `ACCEPTED`, `PAID`, `COMPLETED`, `CANCELLED`) indica isso. Cada status implica uma próxima ação específica. O aplicativo orienta você durante todo o processo.
