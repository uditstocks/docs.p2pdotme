---
id: 02-2-design-goals-and-non-goals
sidebar_position: 2
title: "2. Objetivos de diseño y no-objetivos"
slug: design-goals-and-non-goals
---

## 2.1 Objetivos

- On/off-ramp descentralizado entre fiat y stablecoins sin custodia de fiat.
- Privacidad por diseño mediante pruebas ZK para la verificación de identidad, manteniendo los datos sin procesar fuera de la cadena. La verificación de transacciones bancarias está planificada (ver [Sección 4.2](/es/whitepaper/cryptographic-primitives-proof-integration))
- Neutralidad creíble: las reglas a nivel de protocolo son abiertas, transparentes y actualizables mediante gobernanza.
- Liquidación rápida: finalización típica en minutos, con objetivo de menos de ~90 segundos para las vías más comunes a medida que mejoren la red, la liquidez y la automatización.
- Seguridad e integridad: modelo de amenazas explícito, flujos de disputas y controles de tasas y límites para minimizar el fraude.

## 2.2 No-Objetivos

- El Protocolo no mantiene en custodia fiat ni criptomonedas de los clientes.
- El Protocolo no garantiza precio ni liquidez. Coordina pares e información de mercado.
- El Protocolo no almacena datos personales en nombre de los usuarios. Registra en cadena los compromisos y veredictos necesarios, mientras las evidencias sin procesar permanecen fuera de la cadena.

---
