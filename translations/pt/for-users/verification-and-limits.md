---
id: verification-and-limits
sidebar_position: 9
title: "Verificação e Limites"
slug: verification-and-limits
---

O P2P Protocol verifica a identidade com provas de conhecimento zero. A verificação comprova que você atende aos critérios de elegibilidade sem revelar quem você é. Nenhum dado pessoal bruto é armazenado on-chain. O protocolo mantém apenas compromissos e veredictos.

A verificação utiliza vários mecanismos de conhecimento zero, e você precisa completar pelo menos um para realizar pedidos.

O ZK Passport lê seu passaporte via NFC. Você escaneia a página de foto do passaporte e, em seguida, escaneia o chip NFC na contracapa. A prova confirma que você possui um passaporte válido e que atende ao requisito de idade. Seu nome, número do passaporte, foto e demais dados pessoais não são compartilhados.

Na Índia, o Anon Aadhaar verifica que você possui um registro Aadhaar válido. A prova confirma o registro sem divulgar seu número de Aadhaar, e somente o veredicto resultante chega à cadeia.

O Reclaim Protocol verifica uma conta em rede social de forma privada via zkTLS. Ele analisa sinais como a idade e a atividade da conta em relação aos critérios de elegibilidade, sem conceder ao protocolo acesso ao conteúdo da sua conta. Se você receber uma mensagem informando que sua conta não atende aos requisitos de elegibilidade, isso significa que a conta não atingiu os critérios mínimos para aquela plataforma. Nesse caso, você pode usar a verificação por ZK Passport.

A verificação alimenta seus Pontos de Reputação (RP), uma pontuação on-chain que define quanto você pode transacionar. O RP cresce à medida que você verifica sua identidade e que o volume concluído acumulado atinge marcos. Os volumes acumulados concluídos de $1.000, $5.000, $20.000 e $50.000 concedem, cada um, um marco de RP. Pedidos cancelados não contam para seus limites.

Os limites por transação escalam conforme o RP, usando uma proporção por moeda. Os padrões publicados são 1 RP para $1 USDC para INR e ARS, e 1 RP para $2 USDC para BRL e IDR. Os limites por transação possuem um teto, com um limite máximo padrão publicado de $400 por negociação, e um limite mínimo de venda padrão publicado de $100 por negociação. Antes de qualquer verificação ZK, o limite de compra é $0 e a venda está sujeita a esse mínimo. Também se aplicam limites diários e mensais de quantidade de pedidos, com padrões publicados de 5 pedidos de compra por dia e 25 pedidos de compra por mês. Esses são os padrões atuais. O valor vigente aplicado à sua conta é exibido no aplicativo.

---
