---
id: faq
sidebar_position: 13
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

## ¿Qué tipo de billetera utilizo?

Se proporciona una billetera dentro de la aplicación durante el inicio de sesión, por lo que no necesita traer la suya. La cuenta es de autocustodia, lo que significa que usted controla las claves y el protocolo no puede recuperar el acceso por usted.

## ¿Por qué mi saldo parece haberse perdido?

Su saldo se mantiene en su cuenta dentro de la aplicación. Verifíquelo primero en la aplicación y consulte la dirección de su cuenta en BaseScan para confirmar el estado on-chain. Si el saldo aún parece incorrecto, contacte al soporte dentro de la aplicación antes de intentar cualquier transferencia on-chain manual.

## ¿La aplicación admite passkeys?

Sí. Puede iniciar sesión con una passkey. Como medida de protección, agregue más de un método de inicio de sesión en la configuración de su billetera, de modo que la pérdida de cualquier método individual no le impida acceder a una cuenta de autocustodia.

## ¿Puedo instalar la aplicación en mi teléfono o computadora?

No existe una publicación en tiendas de aplicaciones nativas. La aplicación se instala como una Progressive Web App (PWA). En dispositivos móviles, abra el sitio y elija Agregar a pantalla de inicio desde el menú del navegador. En una computadora, abra el sitio en Chrome y elija Instalar aplicación desde el menú.
