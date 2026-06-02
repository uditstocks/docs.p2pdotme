---
id: token-holder-governance
sidebar_position: 10
title: "Governança para Detentores de Tokens"
slug: token-holder-governance
---

O modelo-alvo concede aos detentores de tokens controle direto sobre o protocolo em duas camadas. Os parâmetros do protocolo e as atualizações são governados pelo Governor on-chain descrito abaixo. A alocação do tesouro e a emissão de tokens são governadas pelo futarquismo MetaDAO na Solana. Os parâmetros abaixo descrevem o Governor on-chain.

| Parâmetro              | Valor. Meta ou valor típico, com limites on-chain entre parênteses |
| ---------------------- | ------------------------------------------------------------------ |
| Poder de Voto          | 1 $P2P em staking = 1 voto (delegável)                             |
| Atraso de Votação      | 1 dia (configurável, de 1s a 30d)                                  |
| Período de Votação     | 7 dias (configurável, de 1h a 30d)                                 |
| Quórum                 | Quórum por snapshot, definido pela governança                      |
| Condição de aprovação  | Votos favoráveis superam os votos contrários e atingem o quórum    |
| Limiar de proposta     | Limitado a 10% do fornecimento total                               |
| Timelock               | 7 dias típico (configurável, de 1h a 30d)                          |

Os parâmetros governados pelo Governor on-chain incluem percentuais de taxas, configuração de spread, regras de staking e slashing, limites de volume de transações, atualizações de contratos inteligentes e listagem de tokens permitidos. A alocação do tesouro e a emissão de tokens são governadas separadamente pelo futarquismo MetaDAO na Solana.

Para detalhes de governança no nível do contrato (funções, permissões, mecânicas de disputas), consulte [`/for-builders`](/pt/for-builders/start-here).

---

