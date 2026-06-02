---
id: token-holder-governance
sidebar_position: 10
title: "Gobernanza de Titulares de Tokens"
slug: token-holder-governance
---

El modelo objetivo otorga a los titulares de tokens control directo sobre el protocolo en dos capas. Los parámetros del protocolo y las actualizaciones son gobernados por el Governor on-chain descrito a continuación. La asignación del tesoro y la emisión de tokens son gobernados por la futarquía MetaDAO en Solana. Los parámetros a continuación describen el Governor on-chain.

| Parámetro               | Valor. Objetivo o típico, con límites on-chain entre paréntesis |
| ----------------------- | --------------------------------------------------------------- |
| Poder de voto           | 1 $P2P en staking = 1 voto (delegable)                          |
| Retraso de votación     | 1 día (configurable, de 1s a 30d)                               |
| Período de votación     | 7 días (configurable, de 1h a 30d)                              |
| Quórum                  | Quórum por instantánea, establecido por gobernanza              |
| Condición de aprobación | Los votos a favor superan los votos en contra y alcanzan el quórum |
| Umbral de propuesta     | Limitado al 10% del suministro                                  |
| Timelock                | 7 días típico (configurable, de 1h a 30d)                       |

Los parámetros gobernados por el Governor on-chain incluyen porcentajes de comisiones, configuración de spread, reglas de staking y slashing, límites de volumen de transacciones, actualizaciones de contratos inteligentes y whitelisting de tokens. La asignación del tesoro y la emisión de tokens son gobernados de forma independiente por la futarquía MetaDAO en Solana.

Para detalles de gobernanza a nivel de contrato (roles, permisos, mecánicas de disputas), consulte [`/for-builders`](/es/for-builders/start-here).

---
