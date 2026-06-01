---
id: disputes-and-evidence
sidebar_position: 6
title: "Disputas y evidencias"
slug: disputes-and-evidence
---

Si la contraparte no cumple con su obligación, puede abrir una disputa on-chain. La elegibilidad depende del tipo y el estado de la orden.

- Órdenes BUY: se puede abrir una disputa entre 15 minutos y 24 horas después de que se realizó la orden, y solo si marcó la orden como pagada antes de que fuera cancelada.
- Órdenes SELL y PAY: se puede abrir una disputa entre 30 minutos y 7 días después de que se realizó la orden, y solo después de que la orden alcance el estado COMPLETED.

Para abrir una disputa:

1. Abra la orden y seleccione la opción de disputa una vez que la ventana esté activa.
2. Envíe las evidencias solicitadas dentro de la app. El protocolo registra una referencia redactada de su pago como evidencia on-chain.
3. Monitoree el estado de la disputa hasta que se resuelva.

Solo se puede abrir una disputa por orden.

Las disputas se resuelven on-chain por un administrador autorizado que determina la responsabilidad. Si el merchant tiene la culpa, la orden se completa y el stablecoin se liquida al destinatario. Si se determina que usted tiene la culpa, la orden permanece cancelada y se aplica una penalización de reputación, que un administrador puede revertir si posteriormente demuestra que el reclamo fue honesto. Los niveles de escalamiento basados en jurado están planeados para una versión futura.

---
