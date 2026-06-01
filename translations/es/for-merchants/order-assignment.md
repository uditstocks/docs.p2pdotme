---
id: order-assignment
sidebar_position: 7
title: "Asignación de Órdenes"
slug: order-assignment
---

La asignación de órdenes está condicionada por verificaciones del comerciante y del canal de pago.

- Estado en línea/fuera de línea
- Estado de lista negra, disputas y solicitudes de retiro de participación
- Verificaciones de capacidad de órdenes en curso
- Estado activo/aprobado del canal de pago
- Verificaciones de volumen diario y mensual
- Umbrales de liquidez respaldados por moneda fiat y participación

La asignación es determinista y ocurre en cadena. Las verificaciones se aplican en capas, de modo que una sola condición fallida excluye a un comerciante del grupo de candidatos sin afectar a los demás.

---
