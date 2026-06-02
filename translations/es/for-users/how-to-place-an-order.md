---
id: how-to-place-an-order
sidebar_position: 3
title: "Cómo Realizar un Pedido"
slug: how-to-place-an-order
---

1. Abre la aplicación y selecciona `BUY`, `SELL` o `PAY`.
2. Ingresa el monto y los datos del destinatario o del pago requeridos.
3. Envía el pedido y espera la asignación de un comerciante.
4. Sigue las instrucciones de la aplicación para completar la transferencia y la confirmación.

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
