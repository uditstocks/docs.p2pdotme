---
id: sdk
sidebar_position: 10
title: "SDK"
slug: sdk
---

La forma más sencilla de integrar P2P Protocol en tu aplicación es mediante el SDK de TypeScript (`@p2pdotme/sdk`). Proporciona módulos prediseñados para órdenes, perfiles de usuario, precios, configuración de monedas, ZK-KYC, detección de fraude y análisis de QR, además de un proveedor React opcional con hooks.

**Agnóstico al framework.** El núcleo es TypeScript puro, con hooks de React opcionales.
**Agnóstico a la billetera.** Aporta tu propio cliente viem.
**Sin excepciones.** Todos los métodos devuelven tipos `Result` / `ResultAsync`.
**Modular.** Importa solo lo que necesitas.

Instalación:
```bash
npm install @p2pdotme/sdk
```

Código fuente completo: https://github.com/p2pdotme/p2pdotme-sdk

## Configuración del entorno

### Redes

El SDK admite **Base** (mainnet y testnet). Elige una:

| Red | Chain ID | Caso de uso |
|-----|----------|-------------|
| **Base Mainnet** | 8453 | Producción (dinero real) |
| **Base Sepolia** | 84532 | Desarrollo y pruebas |

### Direcciones de contratos

Necesitas tres direcciones para tu red:

| Variable | Propósito |
|----------|-----------|
| `DIAMOND_ADDRESS` | Contrato del protocolo P2P.me |
| `USDC_ADDRESS` | Contrato del token USDC |
| `SUBGRAPH_URL` | Endpoint GraphQL para consultas de órdenes |

### Base Sepolia (Testnet)

```env
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest
```

### Base Mainnet (Producción)

```env
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<deploy-your-own>
```

**Para el subgraph en mainnet**: Despliega el tuyo propio utilizando el [repositorio P2P.me Subgraph](https://github.com/p2pdotme/subgraph).

### URLs de RPC

Necesitas un endpoint RPC. Opciones:

**Público (gratuito, con límite de tasa):**
```env
# Base Mainnet
REACT_APP_RPC_URL=https://mainnet.base.org

# Base Sepolia Testnet
REACT_APP_RPC_URL=https://sepolia.base.org
```

**Recomendado (comercial, más rápido y fiable):**
- [Alchemy](https://www.alchemy.com/), nivel gratuito disponible
- [Infura](https://www.infura.io/), nivel gratuito disponible
- [QuickNode](https://www.quicknode.com/), nivel gratuito disponible

### Configurar el archivo `.env.local`

Crea un archivo `.env.local` en la raíz de tu proyecto. Copia los valores anteriores según tu red:

**Para Base Sepolia Testnet:**
```env
# Red
REACT_APP_RPC_URL=https://sepolia.base.org
REACT_APP_CHAIN_ID=84532

# Direcciones de contratos
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest

# Tu cuenta (solo para pruebas, únicamente en desarrollo)
REACT_APP_PRIVATE_KEY=<your-private-key-here>
```

**Para Base Mainnet (Producción):**
```env
# Red
REACT_APP_RPC_URL=https://mainnet.base.org
REACT_APP_CHAIN_ID=8453

# Direcciones de contratos
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<your-deployed-subgraph-url>
```

Carga en tu código:

```ts
const RPC_URL = import.meta.env.REACT_APP_RPC_URL;
const DIAMOND_ADDRESS = import.meta.env.REACT_APP_DIAMOND_ADDRESS;
const USDC_ADDRESS = import.meta.env.REACT_APP_USDC_ADDRESS;
const SUBGRAPH_URL = import.meta.env.REACT_APP_SUBGRAPH_URL;
```

### Obtener fondos en testnet

Para probar órdenes SELL/PAY en Base Sepolia, necesitas ETH + USDC:

- [Faucet.circle.com](https://faucet.circle.com/), proporciona ETH + USDC de testnet (recomendado)
- [SepoliaFaucet.com](https://sepoliafaucet.com/), solo ETH

## Configuración

Instala el SDK:
```bash
npm install @p2pdotme/sdk viem
```

Necesitas:
- **publicClient**: `PublicClient` de viem para lecturas
- **walletClient**: `WalletClient` de viem para escrituras
- **diamondAddress**: contrato de P2P Protocol
- **usdcAddress**: dirección del token USDC
- **subgraphUrl**: endpoint GraphQL

## Ejemplo con React

```tsx
import { SdkProvider, useOrders, useProfile } from "@p2pdotme/sdk/react";
import { createPublicClient, createWalletClient, http } from "viem";
import { baseSepolia } from "viem/chains";

const publicClient = createPublicClient({
  chain: baseSepolia,
  transport: http(RPC_URL),
});

const walletClient = createWalletClient({
  chain: baseSepolia,
  transport: http(RPC_URL),
  account: YOUR_ACCOUNT,
});

function App() {
  return (
    <SdkProvider
      publicClient={publicClient}
      diamondAddress={DIAMOND_ADDRESS}
      usdcAddress={USDC_ADDRESS}
      subgraphUrl={SUBGRAPH_URL}
    >
      <OrderFlow />
    </SdkProvider>
  );
}

function OrderFlow() {
  const orders = useOrders();
  const profile = useProfile();

  async function buyUsdc() {
    const result = await orders.placeOrder.execute({
      walletClient,
      orderType: 0, // BUY
      currency: "INR",
      user: userAddress,
      recipientAddr: userAddress,
      amount: 10_000_000n, // 10 USDC (6 decimals)
      fiatAmount: 850_000_000n, // 850 INR (6 decimals)
      fiatAmountLimit: 0n,
    });

    result.match(
      ({ hash, meta }) => console.log("Order placed:", hash),
      (err) => console.error(`Error: ${err.code} - ${err.message}`),
    );
  }

  return <button onClick={buyUsdc}>Buy USDC</button>;
}
```

## Tipos Result

Todos los métodos del SDK devuelven tipos `Result` de neverthrow (nunca lanzan excepciones):

```ts
const result = await orders.placeOrder.execute(params);

// Usa siempre .match() para manejar éxito y error
result.match(
  (success) => {
    // Manejar éxito
    console.log("Success:", success.hash);
  },
  (error) => {
    // Manejar error
    console.error("Error:", error.code, error.message);
  }
);

// O comprueba con .isOk()
if (result.isOk()) {
  console.log("Hash:", result.value.hash);
} else {
  console.log("Error:", result.error.code);
}
```

---

## Órdenes

El módulo `orders` gestiona todas las operaciones del ciclo de vida de una orden.

## Tipos de orden

| Tipo | Valor | Descripción |
|------|-------|-------------|
| BUY | `0` | El usuario recibe USDC y envía fiat |
| SELL | `1` | El usuario envía USDC y recibe fiat |
| PAY | `2` | El usuario envía USDC a una billetera |

## Crear una orden BUY

```ts
const result = await orders.placeOrder.execute({
  walletClient,
  orderType: 0,
  currency: "INR",
  user: userAddress,
  recipientAddr: userAddress,
  amount: 10_000_000n,
  fiatAmount: 850_000_000n,
  fiatAmountLimit: 0n,
});
```

## Crear una orden SELL

Las órdenes SELL requieren aprobación de USDC primero:

```ts
// 1. Aprobar
await orders.approveUsdc.execute({
  walletClient,
  amount: 10_000_000n,
});

// 2. Crear la orden
const result = await orders.placeOrder.execute({
  walletClient,
  orderType: 1, // SELL
  currency: "INR",
  user: userAddress,
  recipientAddr: userAddress,
  amount: 10_000_000n,
  fiatAmount: 850_000_000n,
  fiatAmountLimit: 0n,
});

// 3. Establecer destino de pago
await orders.setSellOrderUpi.execute({
  walletClient,
  orderId: result.value.meta.orderId,
  paymentAddress: "user@upi",
});
```

## Seguimiento de órdenes

```ts
// Obtener todas las órdenes del usuario (devuelve tipo Result)
const result = await orders.getOrders({
  userAddress: userAddress,
  limit: 20,
  skip: 0,
});

result.match(
  (ordersList) => {
    console.log(`Found ${ordersList.length} orders`);
    ordersList.forEach((order) => {
      console.log(`Order ${order.orderId}: ${order.status}`);
    });
  },
  (err) => console.error(`Error: ${err.code}`),
);

// Obtener una sola orden
const singleResult = await orders.getOrder({ orderId: 42n });
singleResult.match(
  (order) => console.log("Order:", order),
  (err) => console.error("Error:", err),
);

// Cancelar una orden
const cancelResult = await orders.cancelOrder.execute({
  walletClient,
  orderId: "0x123...",
});

cancelResult.match(
  ({ hash }) => console.log("Cancelled! Hash:", hash),
  (err) => console.error("Error:", err.message),
);

// Abrir una disputa
const disputeResult = await orders.raiseDispute.execute({
  walletClient,
  orderId: "0x123...",
});

disputeResult.match(
  ({ hash }) => console.log("Dispute raised! Hash:", hash),
  (err) => console.error("Error:", err.message),
);
```

## Obtener comisiones

```ts
const result = await orders.getFeeConfig({ currency: "INR" });

result.match(
  (feeConfig) => {
    // Los campos de FeeConfig son bigints con 6 decimales
    console.log(feeConfig.smallOrderThreshold, feeConfig.smallOrderFixedFee);
  },
  (err) => console.error("Error:", err.code),
);
```

---

## Perfil y límites

Consulta saldos del usuario, allowance de USDC y límites de operación.

## Consultar saldos

```ts
// Saldo de USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Allowance de USDC (antes de SELL/PAY)
const allowance = await profile.getUsdcAllowance({
  owner: userAddress,
});

// getBalances también devuelve un Result:
const balancesResult = await profile.getBalances({ address: userAddress, currency: "INR" });
balancesResult.match(
  (b) => console.log(b.usdc, b.fiat),
  (err) => console.error(err.code),
);
```

## Consultar límites

```ts
const result = await profile.getTxLimits({
  address: userAddress,
  currency: "INR",
});

result.match(
  (limits) => {
    // limits tiene: buyLimit, sellLimit
    console.log("Buy Limit:", limits.buyLimit);
    console.log("Sell Limit:", limits.sellLimit);
  },
  (err) => console.error("Error:", err.code),
);
```

Los límites dependen de la reputación, el nivel de KYC y los parámetros de riesgo de la moneda.

## Verificaciones previas

Antes de BUY:
```ts
const result = await profile.getTxLimits({
  address: userAddr,
  currency: "INR",
});

result.match(
  (limits) => {
    if (amount > limits.buyLimit) {
      console.log("Exceeds buy limit");
    } else {
      console.log("Amount OK");
    }
  },
  (err) => console.error("Error:", err.code),
);
```

Antes de SELL:
```ts
// Obtener saldo de USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Obtener límites
const limitsResult = await profile.getTxLimits({
  address: userAddr,
  currency: "INR",
});

limitsResult.match(
  (limits) => {
    if (usdcBalance < amount) {
      console.log("Insufficient USDC");
    } else if (amount > limits.sellLimit) {
      console.log("Exceeds sell limit");
    } else {
      console.log("Can sell");
    }
  },
  (err) => console.error("Error:", err.code),
);
```

---

## Manejo de errores

Decodifica errores del contrato en mensajes comprensibles para el usuario.

## Estructura del error

```ts
const error = {
  code: "INSUFFICIENT_BALANCE",
  message: "User has insufficient USDC balance",
  cause: rawError, // error subyacente
};
```

## Decodificar errores del contrato

```ts
import {
  parseContractError,
  getContractErrorMessage,
} from "@p2pdotme/sdk/orders";

orders.placeOrder.execute(params).match(
  ({ hash }) => console.log("Placed:", hash),
  (err) => {
    const code = parseContractError(err.cause);
    const message = getContractErrorMessage(code);
    showToast(message); // "Order amount exceeds limit"
  },
);
```

## Códigos de error comunes

| Código | Significado | Acción |
|--------|-------------|--------|
| `INVALID_INPUT` | Parámetros inválidos | Revisa los datos de entrada |
| `VALIDATION_ERROR` | Validación fallida | Corrige el formato de los datos |
| `NETWORK_ERROR` | Error de RPC/subgraph | Reintenta con retroceso exponencial |
| `INSUFFICIENT_ALLOWANCE` | Se necesita aprobación de USDC | Llama a `approveUsdc.execute()` |

## Patrones de manejo de errores

Degradación gradual:
```ts
const result = await orders.placeOrder.execute(params);

result.match(
  (success) => {
    return { ok: true, hash: success.hash };
  },
  (error) => {
    console.error(`Error [${error.code}]: ${error.message}`);
    return { ok: false, message: error.message };
  },
);
```

Reintento con retroceso exponencial:
```ts
async function retryOrder(params, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    const result = await orders.placeOrder.execute(params);

    if (result.isOk()) {
      return result.value;
    }

    const { code } = result.error;

    // Solo reintentar en errores de red
    if (code === "NETWORK_ERROR") {
      await new Promise(r => setTimeout(r, 1000 * Math.pow(2, i)));
      continue;
    }

    // No reintentar errores de validación
    throw result.error;
  }
}
```

---

## Patrones avanzados

Usa la separación `prepare`/`execute`, identidad del relay y almacenamiento personalizado.

## Prepare vs Execute

`prepare()` devuelve la transacción sin firmar:
```ts
const result = await orders.placeOrder.prepare(params);
// Devuelve: { to, data, value, meta }
// Envía mediante relayer, multisig o firmante personalizado
```

`execute()` firma y envía con viem:
```ts
const result = await orders.placeOrder.execute({
  walletClient,
  ...params
});
```

## Casos de uso

**Relay sin gas:**
```ts
const tx = await orders.placeOrder.prepare(params);
await relayerApi.send(tx.value);
```

**Multi-sig:**
```ts
const tx = await orders.placeOrder.prepare(params);
await multiSigWallet.queue(tx.value);
```

**Firma en el servidor:**
```ts
const tx = await orders.placeOrder.prepare(params);
const signed = await serverSignAndSend(tx.value);
```

## Identidad del relay

El SDK utiliza un par de claves para anonimizar al remitente. Por defecto está en memoria (se pierde al actualizar la página).

Persistir en localStorage:
```tsx
import { createLocalStorageRelayStore } from "@p2pdotme/sdk/orders";

<SdkProvider
  orders={{
    relayIdentityStore: createLocalStorageRelayStore({ key: "relay" })
  }}
/>
```

Almacenamiento personalizado:
```tsx
const store = {
  get: async () => db.getRelayIdentity(),
  set: async (id) => db.saveRelayIdentity(id),
};

<SdkProvider orders={{ relayIdentityStore: store }} />
```

## Sin React (standalone)

Usa las factories directamente:
```ts
import { createOrders } from "@p2pdotme/sdk/orders";
import { createProfile } from "@p2pdotme/sdk/profile";
import { createPublicClient, http } from "viem";
import { baseSepolia } from "viem/chains";

const publicClient = createPublicClient({
  chain: baseSepolia,
  transport: http("https://sepolia.base.org"),
});

const orders = createOrders({
  publicClient,
  diamondAddress: "0xce868398FDaDcA368EAc203222874D6888532aE2",
  usdcAddress: "0xDABa329Ed949f28F64019f22c33c3B253B2Ded60",
  subgraphUrl: "https://api.studio.thegraph.com/query/110312/indexer-one/version/latest",
});

const profile = createProfile({
  publicClient,
  diamondAddress: "0xce868398FDaDcA368EAc203222874D6888532aE2",
  usdcAddress: "0xDABa329Ed949f28F64019f22c33c3B253B2Ded60",
});

// Úsalos
const orderResult = await orders.getOrder({ orderId: "0x123..." });
orderResult.match(
  (order) => console.log("Order:", order),
  (err) => console.error("Error:", err),
);

const balanceResult = await profile.getUsdcBalance({ address: "0x..." });
if (balanceResult.isErr()) throw balanceResult.error;
console.log("USDC:", balanceResult.value); // bigint
```

---

## Ejemplos

Flujos completos para patrones habituales.

## Flujo de compra

```ts
async function buyUsdc(userAddr, currency, fiatAmount) {
  const limitsResult = await profile.getTxLimits({ address: userAddr, currency });
  if (limitsResult.isErr()) throw limitsResult.error;
  if (fiatAmount > limitsResult.value.buyLimit) throw new Error("Exceeds limit");

  const priceClient = createPrices({ publicClient, diamondAddress });
  const priceResult = await priceClient.getPriceConfig({ currency });
  if (priceResult.isErr()) throw priceResult.error;
  const usdcAmount = (fiatAmount * 1_000_000n) / priceResult.value.buyPrice;

  return await orders.placeOrder.execute({
    walletClient,
    orderType: 0,
    currency,
    user: userAddr,
    recipientAddr: userAddr,
    amount: usdcAmount,
    fiatAmount,
    fiatAmountLimit: 0n,
  });
}
```

## Flujo de venta

```ts
async function sellUsdc(userAddr, currency, usdcAmount) {
  const balanceResult = await profile.getUsdcBalance({ address: userAddr });
  if (balanceResult.isErr()) throw balanceResult.error;
  if (balanceResult.value < usdcAmount) throw new Error("Insufficient USDC");

  const allowance = await profile.getUsdcAllowance({ owner: userAddr });
  if (allowance < usdcAmount) {
    await orders.approveUsdc.execute({ walletClient, amount: usdcAmount });
  }

  const priceClient = createPrices({ publicClient, diamondAddress });
  const priceResult = await priceClient.getPriceConfig({ currency });
  if (priceResult.isErr()) throw priceResult.error;
  const fiatAmount = (usdcAmount * priceResult.value.sellPrice) / 1_000_000n;

  const placed = await orders.placeOrder.execute({
    walletClient,
    orderType: 1,
    currency,
    user: userAddr,
    recipientAddr: userAddr,
    amount: usdcAmount,
    fiatAmount,
    fiatAmountLimit: 0n,
  });

  if (!placed.isOk()) return placed;

  return await orders.setSellOrderUpi.execute({
    walletClient,
    orderId: placed.value.meta.orderId,
    paymentAddress: "user@upi",
  });
}
```

## Seguimiento del estado de una orden

```ts
function useOrderStatus(orderId) {
  const [order, setOrder] = useState(null);
  const orders = useOrders();

  useEffect(() => {
    let poll;
    const fn = async () => {
      const result = await orders.getOrder({ orderId });
      if (result.isOk()) setOrder(result.value);
    };

    fn();
    poll = setInterval(fn, 3000);
    return () => clearInterval(poll);
  }, [orderId, orders]);

  return order;
}
```
