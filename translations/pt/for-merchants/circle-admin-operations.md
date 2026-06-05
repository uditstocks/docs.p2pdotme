---
id: circle-admin-operations
sidebar_position: 13
title: "Operações do Administrador de Círculo"
slug: circle-admin-operations
---

Um Administrador de Círculo opera um grupo de comerciantes com respaldo comunitário sob uma única moeda e uma única configuração. A função consiste em gerir uma unidade operacional local. Você recruta comerciantes e aprova seus canais de pagamento, resolve disputas dentro do seu Círculo, oferece suporte operacional e monitora o desempenho dos comerciantes. Cada carteira pode operar um Círculo, registrado on-chain pelo endereço do administrador.

## O que a função não inclui

Diversas responsabilidades estão explicitamente fora do escopo do Administrador de Círculo, pois o protocolo as executa automaticamente.

- O processamento de pagamentos e a liquidação ocorrem automaticamente on-chain.
- Nenhum recurso de terceiros é custodiado pelo administrador. Os saldos são depositados em custódia e liquidados pelo Diamond.
- O KYC dos usuários é realizado pela camada de verificação do protocolo, não pelo administrador.

## Criando um Círculo

A criação de um Círculo é permissionless. Qualquer carteira que atenda ao stake mínimo de $P2P por moeda pode criar um, desde que ainda não opere um Círculo e que o nome escolhido seja globalmente único. A moeda já deve estar registrada no protocolo.

1. Conecte sua carteira à interface do Administrador de Círculo.
2. Configure o nome do Círculo, a moeda operacional, uma URL de comunidade e a configuração de aprovação automática para canais de pagamento. A aprovação manual é a opção mais conservadora.
3. Faça stake de $P2P no protocolo. O stake é registrado no seu endereço de administrador e permanece bloqueado enquanto o Círculo opera.
4. Confirme a transação. O Círculo passa para o estado ativo assim que o stake estiver aplicado.

O stake mínimo do administrador é definido por país. O padrão atual da especificação equivale a $250 USDC em $P2P. O mínimo on-chain pode não estar definido até que um país seja configurado, portanto o valor mínimo exibido no aplicativo é o valor de referência. Um Círculo passa para o estado inativo se o stake do administrador cair abaixo do mínimo configurado. Você pode adicionar stake a qualquer momento e pode solicitar o desbloqueio até o mínimo por meio de um fluxo de solicitação com período de carência.

## Custos e mecânica de receita

O custo para operar é o stake de $P2P bloqueado acrescido do gas das transações. O stake é uma garantia operacional, não uma taxa. Ele é devolvido pelo fluxo de desbloqueio sujeito ao período de carência e pode ser confiscado por um super administrador em casos de conduta inadequada devidamente definidos.

Do ponto de vista da receita, um Círculo recebe uma comissão expressa como parcela do volume do Círculo. O padrão atual é 0,25 por cento do volume do Círculo, distribuído entre o Administrador de Círculo e os detentores de $P2P da comunidade em proporção configurável. O valor vigente é exibido no aplicativo. Uma parcela dos ganhos do administrador é retida como reserva rotativa bloqueada (CALR, Circle Admin Loss Reserve) antes de se tornar disponível para resgate. A proporção entre o Administrador de Círculo e os detentores de $P2P da comunidade, bem como a parcela bloqueada, são configuráveis por moeda.

## Controle de acesso e delegação de funções

Um Administrador de Círculo detém as permissões padrão do Círculo e pode conceder permissões específicas a colaboradores por meio de controle de acesso baseado em capacidades, com escopo por Círculo. As concessões comuns incluem aprovação ou rejeição de canais de pagamento de comerciantes, resolução de disputas e inclusão de comerciantes em lista de bloqueio. As concessões podem ser revogadas a qualquer momento e são revogadas automaticamente quando a função de administrador é transferida. A concessão de uma permissão não transfere a responsabilidade. O Administrador de Círculo permanece responsável pelas decisões tomadas sob as permissões concedidas.

## Status do Círculo e rejeição

Um Círculo está ativo enquanto o stake do administrador for igual ou superior ao mínimo e o Círculo não tiver sido rejeitado. Liquidações de disputas com responsabilidade atribuída ao comerciante incrementam um contador de disputas por Círculo. Quando esse contador ultrapassa o limite configurado para a moeda, o Círculo passa automaticamente para o estado rejeitado e o cadastro de novos comerciantes é bloqueado até que um super administrador redefina o contador. Não há decremento automático do contador com base no tempo.

---
