---
id: faq
sidebar_position: 9
title: "FAQ"
slug: faq
---

## Em qual blockchain os contratos estão implantados?

Os contratos inteligentes do protocolo estão ativos na Base (EVM). A implantação na Solana está planejada como parte da expansão multicadeia. O token $P2P é um token SPL na Solana. Consulte o [FAQ de token e blockchain](/pt/for-token-holders/faq) para mais detalhes.

## Onde estão as ABIs dos contratos?

As referências de contratos estão listadas na seção [Referências de Contratos](/pt/for-builders/contract-references). A superfície de integração já é de código aberto: o SDK ([`@p2pdotme/sdk`](https://github.com/p2pdotme/p2pdotme-sdk)), os widgets React ([`@p2pdotme/widgets`](https://github.com/p2pdotme/widgets)) e os contratos e interfaces do integrador B2B ([`payment-integrators`](https://github.com/p2pdotme/payment-integrators)). Os contratos Diamond do protocolo principal estão pendentes de auditoria e serão disponibilizados como código aberto após sua conclusão.

## Posso adicionar um novo país ou moeda?

O framework de expansão de moedas utiliza configurações YAML de código aberto. Qualquer pessoa com conhecimento de rails de pagamento locais pode propor uma nova moeda via PR.

## Como funcionam as disputas no nível do contrato?

Os usuários chamam `raiseDispute` no `OrderProcessorFacet`. Os administradores resolvem via `adminSettleDispute` com um tipo de falha. A resolução aciona hooks de contabilidade e RP. Consulte [Disputas](/pt/for-builders/disputes) para o fluxo completo.

## O que é a arquitetura Diamond?

O protocolo utiliza o Padrão Diamond EIP-2535. A funcionalidade é dividida em facets que compartilham armazenamento, permitindo atualizações modulares sem reimplantar o contrato completo.

## Como o RP se integra ao fluxo de pedidos?

Os hooks de RP estão na lista de permissões do `ReputationManager`. Atualizações de volume de pedidos, penalidades por disputas e recompensas com verificação de acesso fluem por esses hooks. Consulte [Reputação](/pt/for-builders/reputation).

## Onde estão os detalhes de governança para os detentores de tokens?

A governança para detentores de tokens (modelo de votação, quórum, descentralização progressiva) está documentada em [`/for-token-holders`](/pt/for-token-holders/start-here).

---
