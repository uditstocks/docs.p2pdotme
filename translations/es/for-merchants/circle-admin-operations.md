---
id: circle-admin-operations
sidebar_position: 13
title: "Operaciones del Administrador de Círculo"
slug: circle-admin-operations
---

Un Administrador de Círculo opera un grupo de comerciantes respaldado por la comunidad bajo una moneda y una configuración. La función consiste en gestionar una unidad operativa local: reclutar comerciantes y aprobar sus canales de pago, resolver disputas dentro del Círculo, brindar soporte operativo y supervisar el rendimiento de los comerciantes. Cada billetera puede operar un Círculo, registrado en cadena por la dirección del administrador.

## Lo que la función no incluye

Varias responsabilidades quedan explícitamente fuera del alcance del Administrador de Círculo, porque el protocolo las gestiona de forma autónoma.

- El procesamiento y la liquidación de pagos se ejecutan automáticamente en cadena.
- El administrador no custodia fondos de terceros. Los saldos quedan en custodia (escrow) y son liquidados por el Diamond.
- El KYC de los usuarios es gestionado por la capa de verificación del protocolo, no por el administrador.

## Creación de un Círculo

La creación de un Círculo es sin permiso. Cualquier billetera que cumpla con el stake mínimo de $P2P por moneda puede crear uno, siempre que no esté operando ya un Círculo y que el nombre elegido sea único a nivel global. La moneda debe estar ya registrada en el protocolo.

1. Conecta tu billetera a la interfaz de Administrador de Círculo.
2. Configura el nombre del Círculo, la moneda de operación, una URL de comunidad y el ajuste de aprobación automática para los canales de pago. La aprobación manual es la opción más conservadora.
3. Realiza el stake de $P2P en el protocolo. El stake queda registrado contra tu dirección de administrador y permanece bloqueado mientras el Círculo opera.
4. Confirma la transacción. El Círculo pasa a un estado activo una vez que tu stake esté en vigor.

El stake mínimo del administrador se define por país. El valor por defecto del spec actual es el equivalente a $250 USDC en $P2P. El mínimo en cadena puede estar sin configurar hasta que se configure un país, por lo que el mínimo vigente que se muestra en la aplicación es el valor de referencia. Un Círculo se vuelve inactivo si el stake del administrador cae por debajo del mínimo configurado. Puedes agregar stake en cualquier momento y puedes solicitar el retiro hasta el mínimo mediante un flujo de solicitud con periodo de espera (cooldown).

## Costos y mecánica de ingresos

El costo de operación es el stake de $P2P bloqueado más el gas de las transacciones. El stake es colateral operativo, no una comisión. Se devuelve a través del flujo de retiro sujeto al cooldown, y puede ser recortado (slashed) por un super administrador en casos de conducta indebida definidos.

En cuanto a los ingresos, un Círculo genera una comisión expresada como participación del volumen del Círculo. El valor por defecto actual es el 0,25 por ciento del volumen del Círculo, distribuido entre el Administrador de Círculo y los stakers de $P2P de la comunidad en una proporción configurable. El valor vigente se muestra en la aplicación. Una porción de las ganancias del administrador queda retenida como buffer rotativo bloqueado (Circle Admin Loss Reserve, CALR) antes de ser reclamable. La distribución entre el Administrador de Círculo, los stakers de $P2P de la comunidad y la porción bloqueada son configurables por moneda.

## Control de acceso y delegación de funciones

Un Administrador de Círculo posee los permisos por defecto del Círculo y puede otorgar permisos específicos a colaboradores mediante control de acceso basado en capacidades, con alcance por Círculo. Los permisos más comunes son la aprobación o el rechazo de canales de pago de comerciantes, la resolución de disputas y la inclusión de comerciantes en listas negras. Los permisos son revocables en cualquier momento y se revocan automáticamente cuando el rol de administrador se transfiere. El otorgamiento de un permiso no transfiere la responsabilidad. El Administrador de Círculo sigue siendo responsable de las decisiones tomadas bajo los permisos otorgados.

## Estado del Círculo y rechazo

Un Círculo está activo mientras el stake del administrador se encuentre en o por encima del mínimo y el Círculo no haya sido rechazado. Las liquidaciones de disputas con falta del comerciante incrementan un contador de disputas por Círculo. Cuando el contador supera el umbral configurado para la moneda, el Círculo pasa automáticamente a un estado rechazado y la incorporación de nuevos comerciantes queda bloqueada hasta que un super administrador reinicie el contador. No existe un decaimiento automático del contador basado en el tiempo.

---
