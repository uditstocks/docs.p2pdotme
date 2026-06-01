---
id: 15-15-governance-upgradability
sidebar_position: 15
title: "15. Gobernanza y Actualizabilidad"
slug: governance-upgradability
---

- **Parámetros:** comisiones, límites, pesos de riesgo por carril, conjuntos de oráculos, políticas de prueba, calendarios de bonos.
- **Actualizaciones:** contratos protegidos por timelocks con propuestas públicas. La pausa de emergencia se limita a ámbitos estrechos, con extinción automática.
- **Dos capas:** los parámetros del protocolo y las actualizaciones en Base son gobernados por los titulares de $P2P a través de un Governor on-chain (estilo Compound Bravo, con quórum por snapshot, umbral de propuesta y timelock integrado). La emisión de tokens, los cambios de suministro y la asignación del tesoro se gobiernan en Solana a través del mercado de decisiones on-chain de MetaDAO, donde el token se emite y el tesoro se custodia.
- **Hoy:** los parámetros del protocolo y las actualizaciones son operados por un multisig administrador con miembros y restricciones publicados, y el Governor on-chain está desplegado en Base. Algunos ajustadores de parámetros, como los del facet de configuración del protocolo, ya aceptan como llamador tanto el Governance Diamond como un super-administrador, mientras que los ajustadores restantes están bajo control exclusivo del super-administrador durante la transición.
- **Transición:** la autoridad sobre los parámetros del protocolo, las actualizaciones y la hoja de ruta pasa a los titulares de $P2P a través del Governor on-chain en fases escalonadas. Las fases avanzan desde un veto del administrador, hasta que el DAO actúe como vía principal con respaldo del administrador, hasta el control exclusivo del DAO con un backstop de emergencia del administrador por tiempo limitado. La asignación del tesoro y cualquier cambio en el suministro de tokens se deciden a través de la gobernanza por mercado de decisiones de MetaDAO en Solana.

---
