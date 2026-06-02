---
id: 04-4-cryptographic-primitives-proof-integration
sidebar_position: 4
title: "4. Primitivas Criptográficas e Integração de Provas"
slug: cryptographic-primitives-proof-integration
---

## 4.1 Verificação de Identidade (Disponível)

O P2P Protocol utiliza provas ZK para verificação de identidade com preservação de privacidade. Um novo membro pode realizar KYC sem necessidade de confiança ao compartilhar uma prova ZK de sua identidade, mantendo seus dados pessoais privados enquanto constrói reputação on-chain e desbloqueia limites de transação mais altos sem expor dados pessoais brutos na cadeia.

O protocolo atualmente suporta verificação de identidade através de múltiplos métodos baseados em ZK:

- **Verificação de ID governamental** via verificadores de prova ZK on-chain para documentos de identidade suportados.
- **Verificação de conta em redes sociais** via **Reclaim Protocol** [1], que utiliza provas zkTLS para verificar a titularidade e a situação de contas suportadas (LinkedIn, GitHub, X, Instagram, Facebook) sem expor credenciais de acesso ou dados pessoais.
- **Verificação de passaporte** via sistemas de prova ZK que podem verificar idade, nacionalidade e status de sanções sem divulgar conteúdo do documento.

Cada verificação bem-sucedida fortalece a reputação on-chain do usuário e expande sua capacidade de transação dentro do protocolo.

## 4.2 Módulo de Evidência para Verificação de Transações Bancárias (Roadmap)

Um módulo de evidências planejado estenderá as capacidades ZK do protocolo à verificação de transações bancárias para resolução de disputas on-chain. Este módulo utilizará provas baseadas em TLS para que um usuário ou comerciante possa produzir uma testemunha criptográfica de que uma afirmação específica sobre uma transferência bancária ou comprovante de pagamento é verdadeira, sem expor credenciais ou detalhes da transação.

O módulo planejado especificará onde as provas são verificadas:

- **Verificador on-chain** para afirmações compactas e hashes de atestação.
- **Verificador/relayer off-chain** (referência de código aberto) para afirmações complexas ou específicas de cada canal de pagamento, postando uma atestação sucinta de volta on-chain.

> As provas brutas permanecerão com os usuários, e a cadeia armazenará apenas compromissos mínimos e veredictos.

## 4.3 Propriedades de Privacidade

A implementação atual de ZK-KYC fornece:

- **Divulgação não interativa:** compartilha apenas a prova, não os dados subjacentes.
- **Revelação seletiva:** somente os campos exigidos pelo circuito de verificação são expostos ao circuito.
- **Vinculação limitada:** IDs de protocolo e compromissos minimizam a rastreabilidade entre sessões sempre que possível.

O módulo de evidências planejado estenderá essas propriedades de privacidade à verificação de transações bancárias.

---

