---
id: verifying-transactions-on-chain
sidebar_position: 11
title: "Verificación de transacciones on-chain"
slug: verifying-transactions-on-chain
---

El protocolo liquida en USDC sobre Base, un Layer 2 de EVM. Cada orden y liquidación queda registrada on-chain, por lo que usted puede confirmar cualquier transacción por su cuenta usando BaseScan, el explorador de bloques público en [basescan.org](https://basescan.org). BaseScan le permite ver las transacciones de una dirección, consultar saldos de tokens y verificar si una transacción fue exitosa junto con sus detalles.

Primero encuentre su dirección. En la aplicación, abra Mi cuenta o Billetera y copie la dirección, que comienza con `0x`.

Para consultar una dirección, péguela en la barra de búsqueda de BaseScan y presione Enter. La página de la dirección lista el saldo de ETH, los tokens ERC-20 que posee y el historial completo de transacciones, incluidas las transferencias de tokens y las llamadas internas a contratos.

Para consultar una transacción individual, necesita su hash de transacción, un identificador único que comienza con `0x` seguido de 64 caracteres hexadecimales. Puede copiar el hash desde el historial de transacciones dentro de la aplicación o desde cualquier fila en la página de su dirección en BaseScan. Pegue el hash en la barra de búsqueda de BaseScan y presione Enter.

La página de la transacción muestra los campos relevantes para la verificación.

| Campo | Significado |
|-------|-------------|
| Status | Exitosa o Fallida |
| Block | El número de bloque donde se confirmó la transacción |
| Timestamp | La fecha y hora de la transacción |
| From | La dirección que envió la transacción |
| To | La dirección o contrato que la recibió |
| Transaction Fee | El costo de gas pagado |

Cuando una transacción mueve un token como USDC, desplácese hasta la sección de transferencias de tokens para ver el token, el monto y las direcciones de envío y recepción. Para confirmar que está consultando el token correcto, abra el token y verifique su dirección de contrato contra la oficial. El contrato canónico de USDC en Base es `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. Base usa el chain ID 8453.

Si una transacción no aparece, espere unos minutos a que se confirme y asegúrese de estar buscando en Base. Si envió fondos y el destinatario informa que no recibió nada, busque el hash, confirme que el estado es Success y verifique la dirección To y la transferencia de tokens. Conserve los hashes de las transacciones de mayor valor, ya que son de utilidad para los tickets de soporte y disputa.

---
