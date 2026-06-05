---
id: circles-of-trust
sidebar_position: 8
title: "Circles of Trust"
slug: circles-of-trust
---

Un Circle es un grupo de comerciantes respaldado por la comunidad, operado por un Circle Admin bajo las reglas compartidas del protocolo on-chain. Cada Circle tiene su propia moneda, conjunto de comerciantes, saldo fiat y liquidez en USDC. Los Circles existen para que las personas que conocen a los vendedores locales puedan operarlos y apoyarlos, en lugar de que una mesa central gestione cada mercado. Como comprador, usted opera con comerciantes dentro de un Circle.

Hoy en día, usted no selecciona un Circle de forma manual. El protocolo asigna un comerciante elegible a su orden basándose en factores en tiempo real como la liquidez, el estado del canal y la disponibilidad. La selección manual de Circle y la clasificación basada en reputación están planificadas para una versión futura. Cuando la aplicación muestra información del Circle junto a una orden, refleja el estado on-chain, como el stake del comerciante y el historial de órdenes.

Un Circle ofrece dos protecciones concretas al comprador. En primer lugar, los comerciantes depositan USDC en stake y los Circle Admins depositan $P2P en stake para operar, por lo que existe colateral detrás de las personas con quienes opera. En segundo lugar, cada Circle está respaldado por reservas de seguro. Existen tres fondos. El Circle Admin Insurance Pool (CAIP, fondo de seguro del administrador del Circle) es una reserva por Circle financiada con una parte de las comisiones de las órdenes. El Circle Admin Loss Reserve (CALR, reserva de pérdidas del administrador del Circle) es un buffer por administrador financiado con una porción de las recompensas del administrador. El Pool Insurance Pool (PIP, fondo de seguro general del protocolo) es un respaldo a nivel de protocolo. Los fondos y su financiamiento están activos on-chain, y el trabajo de liquidación y la contabilidad de recompensas se ejecutan on-chain y son verificables.

El flujo completo de reclamaciones de seguro está siendo finalizado y aún no está activo. Cuando se publique, los comerciantes podrán presentar reclamaciones contra los fondos cuando se pierda USDC pese a un comportamiento correcto del comerciante, y cada reclamación será revisada antes de su liquidación, no reembolsada de forma automática. Como comprador, la vía de recurso ante una operación fallida es el proceso de disputa de la orden, no el proceso de reclamación de seguro.

Su parte en una disputa está cubierta en su totalidad en [Disputas y evidencias](/for-users/disputes-and-evidence). En resumen, se puede abrir una disputa una vez por orden, y un administrador autorizado la resuelve on-chain asignando la responsabilidad. Si el comerciante tiene la culpa, la orden se completa y el stablecoin se liquida al destinatario. Los niveles de escalamiento basados en jurado y en gobernanza están planificados para una versión futura.

---
