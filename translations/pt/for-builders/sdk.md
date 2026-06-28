---
id: sdk
sidebar_position: 10
title: "SDK"
slug: sdk
---

<a class="button button--primary" href="https://discord.com/channels/1443615331783545004/1496425860008509571" target="_blank" style={{ display: 'inline-block', marginBottom: '16px' }}>Obtenha suporte do SDK no Discord</a>

A maneira mais simples de integrar o P2P Protocol ao seu aplicativo é pelo SDK TypeScript (`@p2pdotme/sdk`). Ele oferece módulos prontos para pedidos, perfis de usuário, precificacao, configuracao de moedas, ZK-KYC, deteccao de fraude e leitura de QR, alem de um provider React opcional com hooks.

**Independente de framework.** O nucleo e TypeScript puro, com hooks React opcionais.
**Independente de carteira.** Traga seu proprio cliente viem.
**Sem excecoes.** Todos os metodos retornam tipos `Result` / `ResultAsync`.
**Modular.** Importe apenas o que precisar.

Instalacao:
```bash
npm install @p2pdotme/sdk
```

Codigo-fonte completo: https://github.com/p2pdotme/p2pdotme-sdk

## Configuracao do Ambiente

### Redes

O SDK suporta **Base** (mainnet e testnet). Escolha uma:

| Rede | Chain ID | Uso |
|------|----------|-----|
| **Base Mainnet** | 8453 | Producao (dinheiro real) |
| **Base Sepolia** | 84532 | Desenvolvimento e testes |

### Enderecos dos Contratos

Voce precisa de tres enderecos para a sua rede:

| Variavel | Finalidade |
|----------|-----------|
| `DIAMOND_ADDRESS` | Contrato do protocolo P2P.me |
| `USDC_ADDRESS` | Contrato do token USDC |
| `SUBGRAPH_URL` | Endpoint GraphQL para consulta de pedidos |

### Base Sepolia (Testnet)

```env
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest
```

### Base Mainnet (Producao)

```env
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<deploy-your-own>
```

**Para o subgraph em mainnet**: Implante o seu proprio usando o [repositorio P2P.me Subgraph](https://github.com/p2pdotme/subgraph).

### URLs de RPC

Voce precisa de um endpoint RPC. Opcoes:

**Publico (gratuito, com limite de taxa):**
```env
# Base Mainnet
REACT_APP_RPC_URL=https://mainnet.base.org

# Base Sepolia Testnet
REACT_APP_RPC_URL=https://sepolia.base.org
```

**Recomendado (comercial, mais rapido e confiavel):**
- [Alchemy](https://www.alchemy.com/), nivel gratuito disponivel
- [Infura](https://www.infura.io/), nivel gratuito disponivel
- [QuickNode](https://www.quicknode.com/), nivel gratuito disponivel

### Configurar o Arquivo `.env.local`

Crie um `.env.local` na raiz do seu projeto. Copie os valores acima de acordo com a sua rede:

**Para Base Sepolia Testnet:**
```env
# Rede
REACT_APP_RPC_URL=https://sepolia.base.org
REACT_APP_CHAIN_ID=84532

# Enderecos dos Contratos
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest

# Sua Conta (para testes; apenas em desenvolvimento!)
REACT_APP_PRIVATE_KEY=<your-private-key-here>
```

**Para Base Mainnet (Producao):**
```env
# Rede
REACT_APP_RPC_URL=https://mainnet.base.org
REACT_APP_CHAIN_ID=8453

# Enderecos dos Contratos
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<your-deployed-subgraph-url>
```

Carregue no seu codigo:

```ts
const RPC_URL = import.meta.env.REACT_APP_RPC_URL;
const DIAMOND_ADDRESS = import.meta.env.REACT_APP_DIAMOND_ADDRESS;
const USDC_ADDRESS = import.meta.env.REACT_APP_USDC_ADDRESS;
const SUBGRAPH_URL = import.meta.env.REACT_APP_SUBGRAPH_URL;
```

### Obtendo Fundos na Testnet

Para testar pedidos SELL/PAY na Base Sepolia, voce precisa de ETH e USDC:

- [Faucet.circle.com](https://faucet.circle.com/), fornece tanto ETH quanto USDC testnet (recomendado)
- [SepoliaFaucet.com](https://sepoliafaucet.com/), somente ETH

## Configuracao

Instale o SDK:
```bash
npm install @p2pdotme/sdk viem
```

Voce precisara de:
- **publicClient**: `PublicClient` do viem para leituras
- **walletClient**: `WalletClient` do viem para escrita
- **diamondAddress**: contrato do P2P Protocol
- **usdcAddress**: endereco do token USDC
- **subgraphUrl**: endpoint GraphQL

## Exemplo com React

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
      amount: 10_000_000n, // 10 USDC (6 decimais)
      fiatAmount: 850_000_000n, // 850 INR (6 decimais)
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

## Entendendo os Tipos Result

Todos os metodos do SDK retornam tipos `Result` do neverthrow (sem lancamento de excecoes):

```ts
const result = await orders.placeOrder.execute(params);

// Sempre use .match() para tratar sucesso e erro
result.match(
  (success) => {
    // Tratar sucesso
    console.log("Success:", success.hash);
  },
  (error) => {
    // Tratar erro
    console.error("Error:", error.code, error.message);
  }
);

// Ou verifique com .isOk()
if (result.isOk()) {
  console.log("Hash:", result.value.hash);
} else {
  console.log("Error:", result.error.code);
}
```

---

## Pedidos

O modulo `orders` gerencia todas as operacoes do ciclo de vida de um pedido.

## Tipos de Pedido

| Tipo | Valor | Descricao |
|------|-------|-----------|
| BUY | `0` | Usuario recebe USDC, envia fiat |
| SELL | `1` | Usuario envia USDC, recebe fiat |
| PAY | `2` | Usuario envia USDC para uma carteira |

## Registrar Pedido BUY

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

## Registrar Pedido SELL

SELL exige aprovacao de USDC primeiro:

```ts
// 1. Aprovar
await orders.approveUsdc.execute({
  walletClient,
  amount: 10_000_000n,
});

// 2. Registrar pedido
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

// 3. Definir destino de pagamento
await orders.setSellOrderUpi.execute({
  walletClient,
  orderId: result.value.meta.orderId,
  paymentAddress: "user@upi",
});
```

## Acompanhar Pedidos

```ts
// Obter todos os pedidos do usuario (retorna tipo Result)
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

// Obter pedido individual
const singleResult = await orders.getOrder({ orderId: 42n });
singleResult.match(
  (order) => console.log("Order:", order),
  (err) => console.error("Error:", err),
);

// Cancelar pedido
const cancelResult = await orders.cancelOrder.execute({
  walletClient,
  orderId: "0x123...",
});

cancelResult.match(
  ({ hash }) => console.log("Cancelled! Hash:", hash),
  (err) => console.error("Error:", err.message),
);

// Abrir disputa
const disputeResult = await orders.raiseDispute.execute({
  walletClient,
  orderId: "0x123...",
});

disputeResult.match(
  ({ hash }) => console.log("Dispute raised! Hash:", hash),
  (err) => console.error("Error:", err.message),
);
```

## Obter Taxas

```ts
const result = await orders.getFeeConfig({ currency: "INR" });

result.match(
  (feeConfig) => {
    // Os campos de FeeConfig sao bigints com 6 decimais
    console.log(feeConfig.smallOrderThreshold, feeConfig.smallOrderFixedFee);
  },
  (err) => console.error("Error:", err.code),
);
```

---

## Perfil e Limites

Verifique saldos do usuario, permissao de USDC e limites de negociacao.

## Verificar Saldos

```ts
// Saldo de USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Permissao de USDC (antes de SELL/PAY)
const allowance = await profile.getUsdcAllowance({
  owner: userAddress,
});

// getBalances tambem retorna um Result:
const balancesResult = await profile.getBalances({ address: userAddress, currency: "INR" });
balancesResult.match(
  (b) => console.log(b.usdc, b.fiat),
  (err) => console.error(err.code),
);
```

## Verificar Limites

```ts
const result = await profile.getTxLimits({
  address: userAddress,
  currency: "INR",
});

result.match(
  (limits) => {
    // limits contem: buyLimit, sellLimit
    console.log("Buy Limit:", limits.buyLimit);
    console.log("Sell Limit:", limits.sellLimit);
  },
  (err) => console.error("Error:", err.code),
);
```

Os limites dependem de reputacao, nivel de KYC e parametros de risco da moeda.

## Verificacoes Previas

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
// Obter saldo de USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Obter limites
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

## Tratamento de Erros

Decodifique erros de contrato em mensagens compreensivas para o usuario.

## Estrutura de Erros

```ts
const error = {
  code: "INSUFFICIENT_BALANCE",
  message: "User has insufficient USDC balance",
  cause: rawError, // erro subjacente
};
```

## Decodificar Erros de Contrato

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

## Codigos de Erro Comuns

| Codigo | Significado | Acao |
|--------|-------------|------|
| `INVALID_INPUT` | Parametros invalidos | Verifique as entradas |
| `VALIDATION_ERROR` | Validacao falhou | Corrija o formato dos dados |
| `NETWORK_ERROR` | Erro de RPC/subgraph | Tente novamente com backoff |
| `INSUFFICIENT_ALLOWANCE` | Aprovacao de USDC necessaria | Chame `approveUsdc.execute()` |

## Padroes de Tratamento de Erros

Degradacao graceful:
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

Retry com backoff:
```ts
async function retryOrder(params, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    const result = await orders.placeOrder.execute(params);

    if (result.isOk()) {
      return result.value;
    }

    const { code } = result.error;

    // Tentar novamente apenas em erros de rede
    if (code === "NETWORK_ERROR") {
      await new Promise(r => setTimeout(r, 1000 * Math.pow(2, i)));
      continue;
    }

    // Nao tentar novamente em erros de validacao
    throw result.error;
  }
}
```

---

## Padroes Avancados

Use a separacao `prepare`/`execute`, identidade de relay e armazenamento customizado.

## Prepare vs Execute

`prepare()` retorna a transacao bruta sem assinar:
```ts
const result = await orders.placeOrder.prepare(params);
// Retorna: { to, data, value, meta }
// Envie via relayer, multisig ou assinador customizado
```

`execute()` assina e envia com viem:
```ts
const result = await orders.placeOrder.execute({
  walletClient,
  ...params
});
```

## Casos de Uso

**Relay sem gas:**
```ts
const tx = await orders.placeOrder.prepare(params);
await relayerApi.send(tx.value);
```

**Multi-sig:**
```ts
const tx = await orders.placeOrder.prepare(params);
await multiSigWallet.queue(tx.value);
```

**Assinatura no lado do servidor:**
```ts
const tx = await orders.placeOrder.prepare(params);
const signed = await serverSignAndSend(tx.value);
```

## Identidade de Relay

O SDK usa um par de chaves para anonimato do remetente. O padrao e em memoria (perdido ao atualizar a pagina).

Persistir no localStorage:
```tsx
import { createLocalStorageRelayStore } from "@p2pdotme/sdk/orders";

<SdkProvider
  orders={{
    relayIdentityStore: createLocalStorageRelayStore({ key: "relay" })
  }}
/>
```

Armazenamento customizado:
```tsx
const store = {
  get: async () => db.getRelayIdentity(),
  set: async (id) => db.saveRelayIdentity(id),
};

<SdkProvider orders={{ relayIdentityStore: store }} />
```

## Standalone (Sem React)

Use as factories diretamente:
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

// Usar os modulos
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

## Exemplos

Fluxos completos para os padroes mais comuns.

## Fluxo de Compra

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

## Fluxo de Venda

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

## Monitorar Status do Pedido

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
