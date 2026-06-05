---
id: delegation-and-revenue-sharing
sidebar_position: 9
title: "Delegación y Distribución de Ingresos"
slug: delegation-and-revenue-sharing
---

Los delegadores depositan USDC en el pool de delegación de un Círculo para respaldar a sus comerciantes y obtener una parte de las recompensas del comerciante proporcional a su stake delegado. Los Administradores de Círculo depositan $P2P por separado para crear y operar un Círculo. Los ingresos se dividen en puntos base configurados por moneda. El comerciante y el Administrador de Círculo reciben cada uno una participación base del volumen de transacciones. La participación del comerciante se distribuye luego según la proporción entre el stake propio y el stake delegado, y la porción del stake delegado se divide a su vez entre el comerciante, el Administrador de Círculo y el pool de delegación mediante parámetros configurables por moneda.

Esta distribución dentro del Círculo es independiente de la distribución de ingresos a nivel de protocolo. A nivel de protocolo, el 20 por ciento de los ingresos del protocolo se dirige al tesoro y el 80 por ciento a los operadores de la red (comerciantes, Administradores de Círculo, delegadores y seguros). La distribución descrita aquí regula cómo se comparte la porción de los operadores de un pedido individual dentro de un Círculo, y se define en puntos base por moneda. Los valores a continuación son los valores por defecto actuales del spec para la porción del stake delegado; el valor vigente se muestra en la aplicación.

| Destinatario | Participación por defecto de la porción del stake delegado |
|--------------|-----------------------------------------------------------|
| Comerciante | 60 por ciento |
| Delegadores de USDC | 20 por ciento |
| CAIP (Circle Admin Insurance Pool, Pool de Seguro del Administrador de Círculo) | 10 por ciento |
| Administrador de Círculo | 10 por ciento |

La distribución de recompensas a los delegadores se basa en instantáneas. El pool registra las recompensas por token y paga a cada delegador en proporción a su participación cuando se notifican las recompensas. Los delegadores reclaman las recompensas acumuladas en la aplicación y retiran su participación mediante una solicitud con periodo de espera (cooldown).

*La interfaz completa de delegación y la mecánica de distribución de recompensas a nivel de Círculo están planificadas para una versión futura.*

---
