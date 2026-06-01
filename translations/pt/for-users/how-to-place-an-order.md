---
id: how-to-place-an-order
sidebar_position: 3
title: "Como Fazer um Pedido"
slug: how-to-place-an-order
---

1. Abra o aplicativo e selecione `BUY`, `SELL` ou `PAY`.
2. Informe o valor e os dados do destinatário/pagamento exigidos.
3. Envie o pedido e aguarde a atribuição do comerciante.
4. Siga as instruções do aplicativo para realizar a transferência e confirmar a operação.

```mermaid
flowchart TD
    start[Start the app] --> choose[Choose order type]
    choose --> buy[BUY]
    choose --> sell[SELL]
    choose --> pay[PAY]
    buy --> submit[Submit order]
    sell --> submit[Submit order]
    pay --> submit[Submit order]
    submit --> assign[Merchant assigned]
    assign --> transfer[Complete transfer step]
    transfer --> finish[Order final state]
```

---
