---
id: 01-1-overview
sidebar_position: 1
title: "1. Descripción general"
slug: overview
---

Hoy en día, mover dinero entre fiat y cripto implica confiar en intermediarios con tus fondos y tu identidad. P2P Protocol es una capa no custodial que empareja transacciones fiat y de stablecoin en la cadena y verifica la identidad del usuario mediante pruebas de conocimiento cero. Los fondos nunca son retenidos por un intermediario, y la identidad se demuestra sin ser revelada.

## 1.1 De las "rampas" a una economía basada en privacidad y credibilidad

P2P Protocol parte del cuello de botella más práctico: moverse entre fiat y stablecoins sin custodia en depósito en garantía. Los mismos rieles, pruebas e incentivos que hacen funcionar una rampa honesta a escala también habilitan la capa siguiente: liquidez basada en credibilidad, que cierra la brecha entre monedas fiat y criptográficas para todo DeFi.

En este modelo, la reputación se gana en la cadena a través de operaciones completadas, historiales de disputas limpios y niveles ZK-KYC, en lugar de mediante una verificación de cuentas centralizada. La privacidad se preserva por defecto mediante pruebas de conocimiento cero para la verificación de identidad, que solo revelan que un usuario está verificado y autorizado, sin exponer identidades sin procesar. La utilidad es lo primero: micropagos, retiros cotidianos, salarios, remesas y pagos a comerciantes están diseñados para ser tan sencillos como enviar un mensaje.

## 1.2 Cómo se ve el éxito en 2026+

- Un usuario en cualquier país admitido puede comprar, vender o pagar mediante stablecoins en minutos, con un objetivo de finalización en menos de 90 segundos en rieles rápidos, sin ceder la custodia a nadie. El costo mediano se mantiene por debajo de $0.20 por cada $100.
- Los comerciantes se emparejan en la cadena en función del USDC apostado, con el diferencial establecido a nivel de protocolo en lugar de por competencia entre comerciantes. El sistema Proof-of-Credibility se encarga de la prevención de fraude y la asignación por niveles de límites de transacción.
- ZK-KYC desbloquea límites más altos y caminos más rápidos manteniendo los datos personales fuera de la cadena.
- Más del 99% de las disputas se resuelven mediante pruebas dentro del período de impugnación, en lugar de por moderación manual.
- La credibilidad es portable. La reputación y los límites viajan con el usuario entre clientes y países sin exponer la identidad personal.
- El acceso es neutral. Múltiples billeteras y aplicaciones, incluida [Coins.me](https://coins.me) como interfaz de consumidor de referencia, utilizan los mismos SDK sin permisos sobre el Protocolo, sin pasarela privilegiada.
- A medida que la credibilidad se acumula, nuevos productos (pagos en cuotas, comercio sin custodia, salarios transfronterizos, seguro de disputas) pueden construirse sin volver a verificar la identidad del mundo. Salarios, remesas, pagos de mercados y compras se liquidan sin custodia y sin formularios de KYC en papel.

## 1.3 Principios fundamentales

1. **No custodial por construcción.** Sin depósito en garantía en fiat. La criptomoneda solo se retiene atómicamente para la liquidación cuando sea necesario.
2. **Preservación de la privacidad.** Demostrar lo necesario y no revelar nada más. La privacidad se trata como una preocupación de interfaz de usuario tanto como criptográfica, y la mejor verificación de identidad es la que prueba lo requerido y nada más.
3. **Neutralidad creíble.** Reglas abiertas, actualizables por gobernanza, sin rutas especiales para ningún cliente.
4. **Útil y simple.** La interfaz está dirigida a usuarios no expertos: un flujo de "Comprar USDC" o "Retirar" con un solo toque, con el protocolo gestionando la complejidad subyacente.
5. **Reputación ganada y portable.** La reputación se gana mediante actividad en la cadena, viaja con el usuario entre clientes y países, y puede revocarse mediante penalizaciones explícitas. Nunca se compra ni se vende.
6. **Agnóstico al protocolo.** El diseño no depende de ningún único L2, oráculo o proveedor de pruebas. Las implementaciones pueden cambiar sin reescribir el documento técnico.

## 1.4 Qué es P2P Protocol (y qué no es)

**Es:** una capa de coordinación abierta y descentralizada que empareja de forma fiable a un comprador con un comerciante en la cadena basándose en USDC apostado, liquida operaciones con coordinación en la cadena y enruta comisiones y parámetros a través de la gobernanza.

**No es:** un custodio, un banco ni un intermediario de datos. P2P Protocol no custodia fiat, no almacena la información personal de los usuarios y no promete rendimientos fijos.

## 1.5 Por qué esto importa ahora

Durante la última década, las criptomonedas resolvieron las finanzas programáticas, pero dejaron el mundo real fuera. Hoy tres curvas se cruzan finalmente:

- Los rieles locales instantáneos (UPI/PIX/QRIS/ALIAS/SPEI/Pago Movil) son ya corrientes.
- El ZK práctico puede atestiguar hechos del mundo real sin exponer los datos, ya se usa para verificación de identidad, con pruebas de transacciones bancarias en la hoja de ruta.
- Los L2 y las stablecoins han hecho que los pagos pequeños sean lo suficientemente baratos y rápidos como para ser relevantes.

P2P Protocol se sitúa exactamente en esa intersección. Coordina transferencias fiat y de stablecoin y verifica la identidad del usuario con pruebas, sin tomar la custodia de los fondos ni almacenar datos de identidad personal.

## 1.6 DeFi basado en credibilidad (más allá de la sobrecolateralización)

La sobrecolateralización hizo que el DeFi temprano fuera seguro, pero hace que el uso cotidiano sea costoso y difícil de acceder. P2P Protocol propone un segundo pilar: la **credibilidad**. Los límites ganados y los mejores precios provienen de un historial limpio, operaciones completadas y niveles ZK-KYC, en lugar de bloquear el 200% de colateral. La privacidad se mantiene por defecto, ya que los usuarios revelan pruebas de acción en lugar de identidades. El mismo grafo de credibilidad es componible: soportará pagos en cuotas, comercio sin custodia y primitivas de crédito ligeras en el futuro.

## 1.7 Un protocolo para personas, no solo para usuarios avanzados

El protocolo está diseñado para un usuario con un teléfono y un sueldo, no para una mesa de operaciones profesional. Debe seguir siendo fiable en $15 tanto como en $1,500. La verificación sigue un modelo de divulgación mínima: las verificaciones ZK-KYC prueban solo el predicado requerido y no revelan ningún identificador personal.

## 1.8 Agnóstico al protocolo por diseño

Los proveedores y las cadenas cambiarán, pero los principios no pueden hacerlo. El documento técnico se compromete a:

- Ningún único L2, oráculo o proveedor de pruebas incorporado a la lógica.
- Interfaces claras (registro de verificadores, adaptador de oráculos, registro de rieles) para que las partes puedan intercambiarse sin reescribir el documento ni el contrato social.
- Apertura del código fuente y descentralización de cada parte del Protocolo como bienes públicos.

## 1.9 Credibilidad con privacidad

Piensa en el Proof-of-Credibility de P2P Protocol como un bien público en sí mismo:

- Se gana, se ajusta solo mediante penalizaciones explícitas y es difícil de manipular.
- Es portable entre clientes y países mediante compromisos en la cadena, no PDFs en la bandeja de entrada de alguien.
- Es de privacidad primero. Solo los compromisos y los veredictos son públicos, y las evidencias sin procesar permanecen contigo o con el verificador que elijas.

## 1.10 Cumplimiento programable (política sin expedientes)

La mayoría de las personas quieren dos cosas a la vez: privacidad y legalidad. P2P Protocol hace esto práctico:

- **Política como parámetros:** los rieles, los tiempos de espera y los requisitos de prueba se gobiernan en la cadena por región y clase de riesgo.
- **Niveles ZK-KYC** satisfacen las verificaciones de "usuario autorizado" manteniendo los datos PII fuera de la cadena.
- **Las necesidades de tipo Travel Rule** pueden satisfacerse mediante circuitos de divulgación selectiva (planificado) cuando la contraparte es una empresa registrada, sin convertir el protocolo en un intermediario de datos.

## 1.11 Qué se desbloquea si lo hacemos bien

Los mismos rieles y pruebas soportan ingresos sin fronteras, para que creadores, contratistas y trabajadores remotos cobren donde viven sin custodia de cambio. Los mercados liquidan pagos a vendedores en rieles locales de forma instantánea, con diferenciales justos, sin conciliación manual en CSV. Una capa de credibilidad y liquidez compartida entre los dominios de moneda fiat y criptográfica soporta finanzas comunitarias como ahorros rotativos, microcréditos y mercados sin custodia. Los usuarios mantienen la capacidad de transferir valor de forma privada y legal durante períodos de interrupción bancaria local o tensión por controles de capital.

## 1.12 Filosofía de administración y gobernanza

- Neutralidad creíble sobre conveniencia. Los cambios pasan por una gobernanza transparente con salvaguardas (timelocks, pausas acotadas, auditorías).
- Minimizar la gobernanza donde sea posible: parametrizar, no microgestionar.
- Válvulas de seguridad públicas: disyuntores de oráculos, retiros de verificadores y pausas de emergencia con caducidad automática.
- Mentalidad de recompensa abierta: pagar por encontrar fallos pronto y publicar las correcciones abiertamente.

## 1.13 En lo que no transigiremos

El protocolo no custodia fiat bajo ninguna circunstancia. No almacena ninguna información de identificación personal (PII) en la cadena. Ningún cliente recibe enrutamiento privilegiado, y todo integrador utiliza las mismas interfaces. Los componentes que no puedan probarse o auditarse de forma independiente no se admiten en el núcleo del protocolo.

## 1.14 Hitos que importan

- **Ubicuidad:** una presencia de comerciantes creíble en cada par de región/riel principal.
- **Alcance geográfico:** expansión a más de 20 mercados en Asia, África, América Latina y MENA.
- **Presencia multi-cadena:** el despliegue del protocolo se expande más allá de Base a Solana como cadena central, con cadenas adicionales de alto rendimiento soportadas como ramificaciones.
- **Componibilidad:** aplicaciones de terceros que ofrecen funciones útiles sobre el SDK sin pedir permiso.
- **Legitimidad de autoservicio:** reguladores y equipos de riesgo pueden leer la especificación, verificar los parámetros en la cadena y entender cómo se logra la seguridad, sin puertas traseras.
- **Funcionalidades de hoja de ruta:** para las propuestas actuales del seguimiento de funciones (incluidas remesas y expansión de divisas), consulta [`/for-builders`](/es/for-builders/start-here).

---
