---
id: p2pkit-integration
sidebar_position: 11
title: Integração P2PKit
---

# Integração P2PKit

P2PKit permite que desenvolvedores aceitem pagamentos locais e liquidem em USDC, alcançando usuários em mercados onde os pagamentos com cartão tradicional não funcionam.

## Visão Geral

P2PKit orquestra pagamentos locais globalmente, permitindo que sua aplicação:

- **Aceite pagamentos locais** - Usuários pagam via códigos QR, UPI, PIX, transferências bancárias e outros métodos locais
- **Liquide em USDC** - Receba pagamentos on-chain em USDC na Base, não em contas bancárias locais
- **Verifique instantaneamente** - Verificação on-chain de pagamentos sem risco de auto-relato
- **Expanda globalmente** - Alcance novos mercados sem gerenciar infraestrutura de pagamento local

## Como Funciona

### 1. Usuário Inicia o Pagamento
Os usuários escaneiam um código QR ou selecionam seu método de pagamento preferido (UPI, PIX, transferência bancária, etc.) em seu aplicativo. Sem conhecimento de criptografia ou novo aplicativo necessário.

### 2. Coleta de Parceiro Local
P2PKit encontra instantaneamente um parceiro verificado no mercado do cliente que coleta o pagamento localmente.

### 3. Verificação de Pagamento
Após o parceiro confirmar o recebimento dos fundos, a transação liquida on-chain. Toda verificação é criptográfica e verificável.

### 4. Liquidação em USDC
Seu aplicativo recebe USDC na Base, pronto para gastar, transferir ou manter. Liquidado em um único token em todos os mercados.

## Características Principais

- **Zero Risco de Custódia** - Contratos inteligentes não-custodiais lidam com toda liquidação
- **Liquidação Instantânea** - USDC chega na Base imediatamente após confirmação do pagamento
- **Suporte Multi-Moeda** - Aceite pagamentos em mais de 25 moedas fiduciárias
- **Flexibilidade de Método** - Suporte para Wise, Venmo, PIX, UPI, transferências bancárias, MercadoPago e mais
- **Alcance Global** - Opere em mercados emergentes sem relacionamentos bancários locais

## Métodos de Pagamento Suportados

| Método | Moedas |
|--------|---------|
| **Wise** | USD, EUR, GBP, etc. |
| **Venmo** | USD |
| **PIX** | BRL |
| **UPI** | INR |
| **Transferências Bancárias** | Múltiplas |
| **MercadoPago** | BRL, ARS, MXN |
| **Revolut** | USD, EUR, GBP |
| **Zelle** | USD |
| **Monzo** | GBP |

## Caminho de Integração

Para integrar P2PKit com o P2P Protocol:

1. **Configure P2PKit** - Configure métodos de pagamento e contas de liquidação
2. **Crie Pedidos** - Gere pedidos P2PKit a partir de sua aplicação
3. **Receba Liquidação** - USDC chega na Base para processamento de transação
4. **Rotear para P2P** - Use P2P Protocol para operações de on/off-ramp se necessário

## Referência de API

Para detalhes completos de integração e SDKs, visite:

- **Documentação Oficial**: [p2pkit.com](https://p2pkit.com/)

## Casos de Uso

- **Remessas Globais** - Aceite pagamentos locais, liquide em USDC para transferência on-chain
- **Liquidações de Comerciante** - Aceite pagamentos de qualquer mercado, liquide em um único stablecoin
- **Comércio Transfronteiriço** - Simplifique transações multifuncionárias
- **On-Ramps DeFi** - Conecte métodos de pagamento locais à liquidez on-chain

## Próximos Passos

- Revise os pontos de integração do P2P Protocol em [`/pt/for-builders/sdk`](/pt/for-builders/sdk)
- Explore parâmetros do protocolo em [`/pt/for-builders/protocol-parameters`](/pt/for-builders/protocol-parameters)
- Verifique referências de contrato em [`/pt/for-builders/contract-references`](/pt/for-builders/contract-references)
