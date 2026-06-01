---
id: faq
sidebar_position: 9
title: "Preguntas frecuentes"
slug: faq
---

## ¿En qué cadena están desplegados los contratos?

Los contratos inteligentes del protocolo están activos en Base (EVM). El despliegue en Solana está planificado como parte de la expansión multicadena. El token $P2P es un token SPL en Solana. Consulta las [preguntas frecuentes sobre el token y la cadena](/es/for-token-holders/faq) para más detalles.

## ¿Dónde están las ABI de los contratos?

Las referencias de contratos están listadas en la sección [Referencias de contratos](/es/for-builders/contract-references). La superficie de integración ya es de código abierto: el SDK ([`@p2pdotme/sdk`](https://github.com/p2pdotme/p2pdotme-sdk)), los widgets de React ([`@p2pdotme/widgets`](https://github.com/p2pdotme/widgets)) y los contratos e interfaces del integrador B2B ([`payment-integrators`](https://github.com/p2pdotme/payment-integrators)). Los contratos Diamond del protocolo principal están pendientes de auditoría y serán publicados como código abierto una vez completada.

## ¿Puedo añadir un nuevo país o moneda?

El marco de expansión de divisas utiliza configuraciones YAML de código abierto. Cualquier persona con conocimiento de los medios de pago locales puede proponer una nueva divisa mediante un PR.

## ¿Cómo funcionan las disputas a nivel de contrato?

Los usuarios invocan `raiseDispute` en `OrderProcessorFacet`. Los administradores las resuelven mediante `adminSettleDispute` con un tipo de fallo. La resolución activa los hooks de contabilidad y de RP. Consulta [Disputas](/es/for-builders/disputes) para ver el flujo completo.

## ¿Qué es la arquitectura Diamond?

El protocolo utiliza el estándar EIP-2535 Diamond. La funcionalidad se divide en facetas que comparten almacenamiento, lo que permite actualizaciones modulares sin necesidad de redesplegar el contrato completo.

## ¿Cómo se integra el RP con el flujo de órdenes?

Los hooks de RP están en lista blanca en el `ReputationManager`. Las actualizaciones de volumen de órdenes, las penalizaciones por disputas y las recompensas condicionadas a verificación fluyen a través de estos hooks. Consulta [Reputación](/es/for-builders/reputation).

## ¿Dónde se documenta la gobernanza para los titulares de tokens?

La gobernanza para titulares de tokens (modelo de votación, quórum, descentralización progresiva) está documentada en [`/for-token-holders`](/es/for-token-holders/start-here).

---
