---
id: faq
sidebar_position: 8
title: "FAQ"
slug: faq
---

## ¿Necesito entender los mecanismos on-chain?

No, no es necesario entender los mecanismos on-chain. La aplicación cliente gestiona toda la interacción con los contratos. Siga las indicaciones de estado para completar su acción.

## ¿Por qué mi orden no se emparejó de inmediato?

La asignación de un comerciante depende de factores de elegibilidad en tiempo real, entre ellos la liquidez, el estado del canal, los límites de volumen y la disponibilidad operativa. Si ningún comerciante cumple los requisitos, la orden queda en espera y se cancela cuando expira el tiempo límite.

## ¿Puedo apelar una disputa?

No. En la versión actual, una disputa solo puede abrirse una vez por orden y un administrador autorizado la resuelve on-chain asignando la responsabilidad. No existe una instancia de apelación separada. Los niveles de escalamiento basados en jurado y en gobernanza están planificados para una versión futura.

## ¿Mi identidad se almacena on-chain?

No se almacena ningún dato personal en bruto (Información de Identificación Personal) on-chain. El protocolo utiliza pruebas ZK-KYC para la verificación de identidad y almacena on-chain únicamente compromisos criptográficos y veredictos.

## ¿Cómo sé cuál es el siguiente paso?

El estado de su orden (`PLACED`, `ACCEPTED`, `PAID`, `COMPLETED`, `CANCELLED`) se lo indica. Cada estado implica una acción específica a continuación. La aplicación le guía durante todo el proceso.
