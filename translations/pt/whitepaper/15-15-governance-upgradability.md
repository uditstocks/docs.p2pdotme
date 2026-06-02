---
id: 15-15-governance-upgradability
sidebar_position: 15
title: "15. Governança e Atualizabilidade"
slug: governance-upgradability
---

- **Parâmetros:** taxas, limites, pesos de risco de trilhos, conjuntos de oráculos, políticas de prova, cronogramas de caução.
- **Atualizações:** contratos protegidos por timelocks com propostas públicas. A pausa de emergência é limitada a escopos restritos, com extinção automática.
- **Duas camadas:** parâmetros do protocolo e atualizações na Base são governados pelos detentores de $P2P por meio de um Governor on-chain (estilo Compound Bravo, com quórum por snapshot, limite de proposta e timelock integrado). A cunhagem de tokens, alterações no fornecimento e alocação do tesouro são governadas na Solana por meio do mercado de decisão on-chain do MetaDAO, onde o token é emitido e o tesouro é mantido.
- **Situação atual:** os parâmetros do protocolo e as atualizações são operados por um multisig administrativo com membros e restrições publicados, e o Governor on-chain está implantado na Base. Alguns definidores de parâmetros, como os da faceta de configuração do protocolo, já aceitam o Governance Diamond ou um super-administrador como chamador, enquanto os demais definidores são restritos ao super-administrador durante a transição.
- **Transição:** a autoridade sobre parâmetros do protocolo, atualizações e roteiro migra para os detentores de $P2P por meio do Governor on-chain em fases graduais. As fases avançam de um veto administrativo, para o DAO atuando como caminho principal com um backup administrativo, até o controle exclusivo do DAO com um mecanismo de emergência administrativo por tempo limitado. A alocação do tesouro e qualquer alteração no fornecimento de tokens são decididas pela governança de mercado de decisão do MetaDAO na Solana.

---
