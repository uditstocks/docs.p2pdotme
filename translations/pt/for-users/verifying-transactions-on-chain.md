---
id: verifying-transactions-on-chain
sidebar_position: 11
title: "Verificando Transações On-Chain"
slug: verifying-transactions-on-chain
---

O protocolo liquida em USDC na Base, uma Layer 2 EVM. Cada pedido e liquidação é registrado on-chain, de modo que você pode confirmar qualquer transação por conta própria usando o BaseScan, o explorador de blocos público em [basescan.org](https://basescan.org). O BaseScan permite visualizar as transações de um endereço, verificar saldos de tokens e confirmar se uma transação foi concluída com sucesso, junto com seus detalhes.

Encontre seu endereço primeiro. No aplicativo, abra Minha Conta ou Carteira e copie o endereço, que começa com `0x`.

Para pesquisar um endereço, cole-o na barra de pesquisa do BaseScan e pressione Enter. A página do endereço lista o saldo de ETH, os tokens ERC-20 mantidos e o histórico completo de transações, incluindo transferências de tokens e chamadas internas de contratos.

Para pesquisar uma transação específica, você precisa do hash da transação, um identificador único com o formato `0x` seguido de 64 caracteres hexadecimais. Você pode copiar o hash do histórico de transações no aplicativo ou de qualquer linha na página de endereço do BaseScan. Cole o hash na barra de pesquisa do BaseScan e pressione Enter.

A página da transação exibe os campos relevantes para verificação.

| Campo | Significado |
|-------|-------------|
| Status | Sucesso ou Falha |
| Block | O número do bloco onde a transação foi confirmada |
| Timestamp | A data e o horário da transação |
| From | O endereço que enviou a transação |
| To | O endereço ou contrato que a recebeu |
| Transaction Fee | O custo de gas pago |

Quando uma transação movimenta um token como USDC, role até a seção de transferência de tokens para ver o token, o valor e os endereços de envio e recebimento. Para confirmar que você está vendo o token correto, abra o token e verifique o endereço do contrato em relação ao oficial. O contrato canônico do USDC na Base é `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. A Base utiliza o chain ID 8453.

Se uma transação não aparecer, aguarde alguns minutos para que seja confirmada e verifique se está pesquisando na Base. Se você enviou fundos e o destinatário relatar que nada chegou, pesquise o hash, confirme que o status é Sucesso e verifique o endereço To e a transferência de token. Guarde os hashes de transações de grande valor, pois eles auxiliam nos tickets de suporte e de disputa.

---
