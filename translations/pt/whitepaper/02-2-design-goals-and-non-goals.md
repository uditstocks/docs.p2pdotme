---
id: 02-2-design-goals-and-non-goals
sidebar_position: 2
title: "2. Objetivos de Design e Não-Objetivos"
slug: design-goals-and-non-goals
---

## 2.1 Objetivos

- On/off-ramp descentralizado entre moeda fiduciária e stablecoins sem custódia de fiat.
- Privacidade por design usando provas ZK para verificação de identidade, mantendo os dados brutos fora da cadeia. A verificação de transações bancárias está planejada (consulte a [Seção 4.2](/pt/whitepaper/cryptographic-primitives-proof-integration))
- Neutralidade crível: as regras no nível do protocolo são abertas, transparentes e atualizáveis via governança.
- Liquidação rápida: conclusão típica em minutos, com meta abaixo de ~90s para trilhos comuns à medida que a rede, a liquidez e a automação evoluem.
- Segurança e integridade: modelo explícito de ameaças, fluxos de disputas e controles de taxa/limite para minimizar fraudes.

## 2.2 Não-Objetivos

- O Protocolo não mantém fiat ou criptoativos de clientes em custódia.
- O Protocolo não garante preço ou liquidez. Ele coordena pares e informações de mercado.
- O Protocolo não armazena dados pessoais em nome dos usuários. Ele registra os compromissos e veredictos necessários on-chain, enquanto as evidências brutas permanecem fora da cadeia.

---
