---
id: faq
sidebar_position: 13
title: "FAQ"
slug: faq
---

## Preciso entender como funcionam os mecanismos on-chain?

Não, você não precisa entender os mecanismos on-chain. O aplicativo cliente cuida de toda a interação com os contratos. Siga os indicadores de status para concluir sua ação.

## Por que meu pedido não foi correspondido instantaneamente?

A atribuição de comerciante depende de fatores de elegibilidade em tempo real, incluindo liquidez, status do canal, limites de volume e disponibilidade operacional. Se nenhum comerciante estiver qualificado, o pedido fica em espera e é cancelado quando o tempo limite expira.

## Posso recorrer de uma disputa?

Não. Na versão atual, uma disputa pode ser aberta apenas uma vez por pedido, e um administrador autorizado a resolve on-chain atribuindo a responsabilidade. Não há etapa de recurso separada. Camadas de escalonamento baseadas em júri e em governança estão planejadas para uma versão futura.

## Minha identidade é armazenada on-chain?

Nenhuma PII (Informação Pessoalmente Identificável) bruta é armazenada on-chain. O protocolo usa provas ZK-KYC para verificação de identidade e armazena apenas compromissos e veredictos on-chain.

## Como sei o que fazer a seguir?

O status do seu pedido (`PLACED`, `ACCEPTED`, `PAID`, `COMPLETED`, `CANCELLED`) indica isso. Cada status implica uma próxima ação específica. O aplicativo orienta você durante todo o processo.

## Que tipo de carteira eu uso?

Uma carteira é fornecida no aplicativo durante o login, portanto você não precisa trazer a sua própria. A conta é autocustodial, o que significa que você controla as chaves e o protocolo não pode recuperar o acesso por você.

## Por que meu saldo parece estar faltando?

Seu saldo é mantido na sua conta no aplicativo. Verifique-o no aplicativo primeiro e pesquise o endereço da sua conta no BaseScan para confirmar o estado on-chain. Se o saldo ainda parecer incorreto, entre em contato com o suporte no aplicativo antes de tentar qualquer transferência on-chain manual.

## O aplicativo suporta passkeys?

Sim. Você pode fazer login com uma passkey. Como medida de segurança, adicione mais de um método de login nas configurações da sua carteira para que a perda de um único método não resulte em bloqueio de uma conta autocustodial.

## Posso instalar o aplicativo no meu telefone ou computador?

Não há listagem em loja de aplicativos nativa. O aplicativo é instalado como um Progressive Web App (PWA). No celular, abra o site e escolha Adicionar à Tela Inicial no menu do navegador. No computador, abra o site no Chrome e escolha Instalar aplicativo no menu.
