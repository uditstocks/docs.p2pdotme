---
id: risk-and-reliability-practices
sidebar_position: 11
title: "Prácticas de Riesgo y Confiabilidad"
slug: risk-and-reliability-practices
---

- Responde con prontitud a los pedidos asignados.
- Mantén los metadatos de los canales y los datos de pago exactos.
- Evita operar canales cuando no estés disponible.
- Conserva registros de evidencia para pagos en disputa.
- Trata las cancelaciones y las disputas como señales de calidad para mejorar las operaciones.

## Patrón de Pago Recurrente en PIX

Un patrón que debes vigilar en el riel PIX es un pago configurado para repetirse automáticamente en fechas futuras, a veces etiquetado como PIX recurrente, PIX automático o plan anual o mensual. Completar un pedido de ese tipo puede autorizar cobros más allá de la transacción única que tienes frente a ti. No completes el pedido. Cancélalo y repórtalo con el ID del pedido.

Si crees que autorizaste un pago repetitivo por error, cancela la recurrencia en tu aplicación bancaria y repórtalo con el ID del pedido. La detección de fraude en el protocolo se ejecuta fuera de cadena a través de la API de fraude SEON en los eventos de registro, verificación y transacción. El Diamond en cadena aplica los plazos de disputa, las penalizaciones de Reputation Points y las compuertas de lista negra. No puntúa transacciones, por lo que tu criterio en el momento del pago es la primera línea de defensa.

---
