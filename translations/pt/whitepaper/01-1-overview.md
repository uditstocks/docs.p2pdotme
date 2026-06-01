---
id: 01-1-overview
sidebar_position: 1
title: "1. Visão Geral"
slug: overview
---

Hoje, mover dinheiro entre fiat e cripto significa confiar a intermediários seus fundos e sua identidade. P2P Protocol é uma camada não custodial que combina transações em fiat e stablecoin on-chain e verifica a identidade do usuário por meio de provas de conhecimento zero. Os fundos nunca são mantidos por um intermediário, e a identidade é comprovada sem ser divulgada.

## 1.1 De "rampas" a uma economia baseada em privacidade e credibilidade

P2P Protocol começa pelo ponto de estrangulamento mais prático: movimentar entre fiat e stablecoins, sem custódia em escrow. As mesmas trilhas, provas e incentivos que fazem uma rampa honesta funcionar em escala também habilitam a próxima camada: liquidez baseada em credibilidade, fazendo a ponte entre moedas fiat e cripto para todo o DeFi.

Neste modelo, a reputação é conquistada on-chain por meio de negociações concluídas, históricos limpos de disputas e níveis de ZK-KYC, em vez de verificações de conta centralizadas. A privacidade é preservada por padrão por meio de provas de conhecimento zero para verificação de identidade, que revelam apenas que um usuário está verificado e autorizado, sem expor identidades brutas. A utilidade vem primeiro: micropagamentos, saques do dia a dia, salários, remessas e pagamentos a comerciantes são projetados para ser tão simples quanto enviar uma mensagem.

## 1.2 Como "bom" se parece a partir de 2026+

- Um usuário em qualquer país suportado pode comprar, vender ou pagar via stablecoins em minutos, com meta de conclusão abaixo de 90 segundos nas trilhas mais rápidas, sem entregar custódia a ninguém. O custo mediano permanece abaixo de $0,20 por $100.
- Comerciantes são combinados on-chain com base em USDC depositado em stake, com spread definido no nível do protocolo em vez de por competição entre comerciantes. O sistema Proof-of-Credibility cuida da prevenção de fraudes e da categorização de limites de transação.
- ZK-KYC desbloqueia limites mais altos e caminhos mais rápidos, mantendo dados pessoais fora da cadeia.
- Mais de 99% das disputas são resolvidas por provas dentro da janela de contestação, em vez de por moderação manual.
- A credibilidade é portável. Reputação e limites acompanham o usuário entre clientes e países, sem expor identidade pessoal.
- O acesso é neutro. Múltiplas carteiras e aplicativos, incluindo [Coins.me](https://coins.me) como front-end de referência para o consumidor, todos utilizam os mesmos SDKs permissionless sobre o Protocolo, sem gateway privilegiado.
- À medida que a credibilidade se acumula, novos produtos (pagamentos parcelados, comércio sem escrow, salários transfronteiriços, seguro de disputas) podem ser construídos sem necessidade de refazer o KYC de todo mundo. Salários, remessas, pagamentos de marketplaces e checkouts são liquidados sem custódia e sem formulários de KYC em papel.

## 1.3 Primeiros princípios

1. **Não custodial por construção.** Sem escrow em fiat. Cripto mantido de forma atômica apenas para liquidação quando necessário.
2. **Preservação da privacidade.** Prove o que é necessário e não revele nada mais. A privacidade é tratada tanto como uma preocupação de interface do usuário quanto criptográfica, e a melhor verificação de identidade é aquela que prova o que é necessário e nada mais.
3. **Neutralidade crível.** Regras abertas, atualizáveis por governança, sem rotas especiais para nenhum cliente.
4. **Útil e simples.** A interface é direcionada a usuários não especializados: um fluxo de "Comprar USDC" ou "Sacar" com um toque, com o protocolo gerenciando a complexidade subjacente.
5. **Reputação conquistada e portável.** A reputação é conquistada por atividade on-chain, acompanha o usuário entre clientes e países, e pode ser revogada por penalidades explícitas. Nunca é comprada ou vendida.
6. **Agnóstico de protocolo.** O design não depende de nenhuma L2, oráculo ou fornecedor de provas específico. As implementações podem mudar sem reescrever o whitepaper.

## 1.4 O que P2P Protocol é (e o que não é)

**É:** uma camada de coordenação aberta e descentralizada que combina de forma trustless um comprador com um comerciante on-chain com base em USDC em stake, liquida negociações com coordenação on-chain e encaminha taxas e parâmetros por meio de governança.

**Não é:** um custodiante, um banco ou um corretor de dados. P2P Protocol não custódia fiat, não armazena informações pessoais dos usuários e não promete rendimentos fixos.

## 1.5 Por que isso importa agora

Na última década, as criptomoedas resolveram as finanças programáticas, mas deixaram o mundo real de fora. Hoje, três curvas finalmente se cruzam:

- Trilhas locais instantâneas (UPI/PIX/QRIS/ALIAS/SPEI/Pago Movil) são mainstream.
- ZK prático pode atestar fatos do mundo real sem expor os dados, já utilizado para verificação de identidade, com provas de transações bancárias no roadmap.
- L2s e stablecoins tornaram os pequenos pagamentos baratos e rápidos o suficiente para importar.

P2P Protocol está exatamente nessa interseção. Ele coordena transferências em fiat e stablecoin e verifica a identidade do usuário com provas, sem tomar custódia de fundos nem armazenar dados de identidade pessoal.

## 1.6 DeFi baseado em credibilidade (além da sobrecolateralização)

A sobrecolateralização tornou o DeFi inicial seguro, mas torna o uso cotidiano custoso e difícil de acessar. P2P Protocol propõe um segundo pilar: **credibilidade**. Limites conquistados e melhores preços vêm de histórico limpo, negociações concluídas e níveis de ZK-KYC, em vez de bloquear 200% de colateral. A privacidade se mantém por padrão, já que os usuários revelam provas de ação em vez de identidades. O mesmo gráfico de credibilidade é componível: suporta pagamentos parcelados, comércio sem escrow e primitivos de crédito leves no futuro.

## 1.7 Um protocolo para pessoas, não apenas para usuários avançados

O protocolo é projetado para um usuário com um telefone e um salário, e não para uma mesa de operações profissional. Deve permanecer confiável em $15 tanto quanto em $1.500. A verificação segue um modelo de divulgação mínima: as verificações ZK-KYC provam apenas o predicado exigido e não revelam identificadores pessoais.

## 1.8 Agnóstico de protocolo por design

Fornecedores e cadeias vão mudar, mas os princípios não podem. O whitepaper se compromete com:

- Nenhuma L2, oráculo ou provedor de provas específico embutido na lógica.
- Interfaces claras (registro de verificadores, adaptador de oráculo, registro de trilhas) para que partes possam ser substituídas sem reescrever o documento ou o contrato social.
- Código aberto e descentralização de cada parte do Protocolo como bens públicos.

## 1.9 Credibilidade com privacidade

Pense no Proof-of-Credibility do P2P Protocol como um bem público em si mesmo:

- É conquistado, ajustado apenas por penalidades explícitas, e difícil de manipular.
- É portável entre clientes e países via compromissos on-chain, não PDFs na caixa de entrada de alguém.
- É privacidade em primeiro lugar. Apenas compromissos e vereditos são públicos, e as evidências brutas ficam com você ou com seu verificador escolhido.

## 1.10 Conformidade programável (política sem dossiês)

A maioria das pessoas quer duas coisas ao mesmo tempo: privacidade e legalidade. P2P Protocol torna isso prático:

- **Política como parâmetros:** trilhas, tempos limite e requisitos de prova são governados on-chain por região e classe de risco.
- **Níveis de ZK-KYC** satisfazem verificações de "usuário permitido" mantendo PII fora da cadeia.
- **Necessidades no estilo Travel Rule** podem ser atendidas por circuitos de divulgação seletiva (planejados) quando uma contraparte é uma empresa registrada, sem transformar o protocolo em um corretor de dados.

## 1.11 O que se desbloqueia se acertarmos isso

As mesmas trilhas e provas suportam renda sem fronteiras, para que criadores, contratados e trabalhadores remotos recebam onde vivem sem custódia de câmbio. Marketplaces liquidam pagamentos a comerciantes e vendedores nas trilhas locais de forma instantânea, com spreads justos, sem reconciliação manual em CSV. Uma camada compartilhada de credibilidade e liquidez entre os domínios de moeda fiat e cripto suporta finanças comunitárias como poupanças rotativas, microcréditos e marketplaces sem escrow. Os usuários mantêm a capacidade de transferir valor de forma privada e legal durante períodos de perturbação bancária local ou estresse de controle de capital.

## 1.12 Filosofia de administração e governança

- Neutralidade crível acima da conveniência. Mudanças passam por governança transparente com salvaguardas (timelocks, pausas restritas, auditorias).
- Minimizar a governança onde possível: parametrizar, não microgerenciar.
- Válvulas de segurança públicas: disjuntores de oráculo, descontinuação de verificadores e pausas de emergência com expiração automática.
- Mentalidade de recompensa aberta: pague para encontrar falhas cedo e publique correções abertamente.

## 1.13 O que não vamos comprometer

O protocolo não custódia fiat em nenhuma circunstância. Não armazena informações de identificação pessoal (PII) on-chain. Nenhum cliente recebe roteamento privilegiado, e todo integrador usa as mesmas interfaces. Componentes que não podem ser comprovados ou auditados de forma independente não são admitidos no núcleo do protocolo.

## 1.14 Marcos que importam

- **Ubiquidade:** presença crível de comerciantes em cada par de região/trilha principal.
- **Alcance geográfico:** expansão para 20+ mercados na Ásia, África, América Latina e MENA.
- **Presença multi-chain:** o deployment do protocolo se expande além da Base para Solana como chain hub, com chains de alto desempenho adicionais suportadas como spokes.
- **Componibilidade:** aplicativos de terceiros lançando recursos úteis no SDK sem pedir permissão.
- **Legitimidade sem intermediários:** reguladores e equipes de risco podem ler a especificação, verificar parâmetros on-chain e entender como a segurança é alcançada, sem backdoors.
- **Recursos do roadmap:** para propostas atuais de trilha de funcionalidades (incluindo remessas e expansão de moedas), veja [`/for-builders`](/pt/for-builders/start-here).

---
