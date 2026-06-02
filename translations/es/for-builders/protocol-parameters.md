---
id: protocol-parameters
sidebar_position: 2
title: "Parámetros del Protocolo"
slug: protocol-parameters
---

El comportamiento del protocolo está fuertemente parametrizado en lugar de estar codificado de forma fija, porque los mercados son distintos. Un spread adecuado para INR/USDC en los rieles de UPI sería incorrecto para BRL/USDC en PIX. La parametrización permite que el protocolo se adapte por moneda sin necesidad de volver a desplegar contratos.

- **Precios y spread.** Spread base e incremento de precio por moneda, ajustados según las condiciones de liquidez local.

- **Límites de riesgo.** Stake mínimo, límites de volumen, límites de RP por USDC y límites máximos por transacción. Estos controlan el nivel de riesgo que el protocolo asume por comerciante y por usuario.

- **Controles de comisiones.** Porcentaje de comisión para comerciantes y comisiones fijas para órdenes pequeñas, calibrados para que las microtransacciones sean viables sin subsidiarlas.

- **Controles operativos.** Ciclos de vida de activación de monedas y canales de pago.

---
