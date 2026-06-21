---
id: p2pkit-integration
sidebar_position: 11
title: Integración P2PKit
---

# Integración P2PKit

P2PKit permite que los desarrolladores acepten pagos locales y liquiden en USDC, llegando a usuarios en mercados donde los pagos tradicionales con tarjeta no funcionan.

## Descripción General

P2PKit orquesta pagos locales globalmente, permitiendo que su aplicación:

- **Acepte pagos locales** - Los usuarios pagan a través de códigos QR, UPI, PIX, transferencias bancarias y otros métodos locales
- **Liquide en USDC** - Reciba pagos en cadena en USDC en Base, no en cuentas bancarias locales
- **Verifique instantáneamente** - Verificación en cadena de pagos sin riesgo de auto-informe
- **Expanda globalmente** - Llegue a nuevos mercados sin gestionar infraestructura de pagos local

## Cómo Funciona

### 1. El Usuario Inicia el Pago
Los usuarios escanean un código QR o seleccionan su método de pago preferido (UPI, PIX, transferencia bancaria, etc.) en su aplicación. Sin conocimiento de criptografía ni nueva aplicación requerida.

### 2. Recopilación del Socio Local
P2PKit encuentra instantáneamente un socio verificado en el mercado del cliente que recopila el pago localmente.

### 3. Verificación de Pago
Una vez que el socio confirma la recepción de fondos, la transacción liquida en cadena. Toda verificación es criptográfica y verificable.

### 4. Liquidación en USDC
Su aplicación recibe USDC en Base, listo para gastar, transferir o mantener—liquidado en un único token en todos los mercados.

## Características Clave

- **Riesgo Cero de Custodia** - Los contratos inteligentes no custodiales manejan toda la liquidación
- **Liquidación Instantánea** - USDC llega a Base inmediatamente después de la confirmación del pago
- **Soporte Multimoneda** - Acepte pagos en más de 25 monedas fiduciarias
- **Flexibilidad de Método** - Soporte para Wise, Venmo, PIX, UPI, transferencias bancarias, MercadoPago y más
- **Alcance Global** - Opere en mercados emergentes sin relaciones bancarias locales

## Métodos de Pago Soportados

| Método | Monedas |
|--------|---------|
| **Wise** | USD, EUR, GBP, etc. |
| **Venmo** | USD |
| **PIX** | BRL |
| **UPI** | INR |
| **Transferencias Bancarias** | Múltiples |
| **MercadoPago** | BRL, ARS, MXN |
| **Revolut** | USD, EUR, GBP |
| **Zelle** | USD |
| **Monzo** | GBP |

## Ruta de Integración

Para integrar P2PKit con el Protocolo P2P:

1. **Configure P2PKit** - Configure métodos de pago y cuentas de liquidación
2. **Cree Órdenes** - Genere órdenes P2PKit desde su aplicación
3. **Reciba Liquidación** - USDC llega a Base para procesamiento de transacción
4. **Enrute a P2P** - Use el Protocolo P2P para operaciones on/off-ramp si es necesario

## Referencia de API

Para detalles completos de integración y SDK, visite:

- **Documentación Oficial**: [p2pkit.com](https://p2pkit.com/)
- **Paquetes SDK**: `@zkp2p/offramp-sdk` y paquetes relacionados disponibles en npm

## Casos de Uso

- **Remesas Globales** - Acepte pagos locales, liquide en USDC para transferencia en cadena
- **Liquidaciones de Comerciantes** - Acepte pagos de cualquier mercado, liquide en un único stablecoin
- **Comercio Transfronterizo** - Simplifique transacciones multimoneda
- **On-Ramps DeFi** - Conecte métodos de pago locales a liquidez en cadena

## Próximos Pasos

- Revise los puntos de integración del Protocolo P2P en [`/es/for-builders/sdk`](/es/for-builders/sdk)
- Explore parámetros del protocolo en [`/es/for-builders/protocol-parameters`](/es/for-builders/protocol-parameters)
- Verifique referencias de contratos en [`/es/for-builders/contract-references`](/es/for-builders/contract-references)
