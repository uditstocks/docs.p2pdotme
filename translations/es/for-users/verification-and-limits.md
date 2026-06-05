---
id: verification-and-limits
sidebar_position: 9
title: "Verificación y límites"
slug: verification-and-limits
---

P2P Protocol verifica la identidad mediante pruebas de conocimiento cero (ZK). La verificación demuestra que usted cumple con los criterios de elegibilidad sin revelar quién es. No se almacena ningún dato personal en bruto on-chain. El protocolo guarda únicamente compromisos criptográficos y veredictos.

La verificación utiliza varios métodos de ZK, y es necesario superar al menos uno para colocar órdenes.

ZK Passport lee su pasaporte a través de NFC. Usted escanea la página de la foto de su pasaporte y luego escanea el chip NFC en la contraportada. La prueba confirma que usted posee un pasaporte válido y que cumple el requisito de edad. Su nombre, número de pasaporte, foto y demás datos personales no son compartidos.

En India, Anon Aadhaar verifica que usted posee un registro Aadhaar válido. La prueba confirma el registro sin divulgar su número de Aadhaar, y solo el veredicto resultante llega a la cadena.

Reclaim Protocol verifica una cuenta de red social de forma privada a través de zkTLS. Comprueba señales como la antigüedad de la cuenta y la actividad frente a los criterios de elegibilidad, sin dar al protocolo acceso al contenido de su cuenta. Si recibe un mensaje indicando que su cuenta no cumple los requisitos de elegibilidad, su cuenta no superó los criterios mínimos para esa plataforma. En ese caso puede utilizar la verificación mediante ZK Passport.

La verificación alimenta sus Puntos de Reputación (RP), una puntuación on-chain que determina cuánto puede transaccionar. Los RP crecen a medida que verifica su identidad y a medida que su volumen completado alcanza hitos. El volumen acumulado completado en $1,000, $5,000, $20,000 y $50,000 otorga un hito de RP. Las órdenes canceladas no cuentan para sus límites.

Los límites por transacción escalan con los RP, usando una proporción por moneda. Los valores por defecto publicados son 1 RP a $1 USDC para INR y ARS, y 1 RP a $2 USDC para BRL y IDR. Los límites por transacción tienen un tope máximo, con un tope por defecto publicado de $400 por operación, y existe un límite mínimo de venta por defecto publicado de $100 por operación. Antes de cualquier verificación ZK, el límite de compra es $0 y la venta está acotada por ese mínimo. También se aplican límites diarios y mensuales de órdenes, con valores por defecto publicados de 5 órdenes de compra por día y 25 órdenes de compra por mes. Estos son los valores por defecto actuales. El valor vigente que aplica a su cuenta se muestra en la aplicación.

---
