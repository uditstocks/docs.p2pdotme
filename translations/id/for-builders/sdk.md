---
id: sdk
sidebar_position: 10
title: "SDK"
slug: sdk
---

Cara termudah untuk mengintegrasikan P2P Protocol ke dalam aplikasi Anda adalah melalui TypeScript SDK (`@p2pdotme/sdk`). SDK ini menyediakan modul siap pakai untuk pesanan, profil pengguna, penetapan harga, konfigurasi mata uang, ZK-KYC, deteksi penipuan, dan penguraian QR, serta provider React dan hooks opsional.

**Agnostik framework.** Inti SDK berupa TypeScript murni, dengan React hooks opsional.
**Agnostik wallet.** Bawa viem client Anda sendiri.
**Tanpa pengecualian.** Semua metode mengembalikan tipe `Result` / `ResultAsync`.
**Modular.** Impor hanya yang Anda butuhkan.

Instalasi:
```bash
npm install @p2pdotme/sdk
```

Kode sumber lengkap: https://github.com/p2pdotme/p2pdotme-sdk

## Pengaturan Lingkungan

### Jaringan

SDK mendukung **Base** (mainnet dan testnet). Pilih salah satu:

| Jaringan | Chain ID | Kasus Penggunaan |
|----------|----------|------------------|
| **Base Mainnet** | 8453 | Produksi (uang nyata) |
| **Base Sepolia** | 84532 | Pengembangan & pengujian |

### Alamat Kontrak

Anda membutuhkan tiga alamat untuk jaringan Anda:

| Variabel | Tujuan |
|----------|--------|
| `DIAMOND_ADDRESS` | Kontrak protokol P2P.me |
| `USDC_ADDRESS` | Kontrak token USDC |
| `SUBGRAPH_URL` | Endpoint GraphQL untuk kueri pesanan |

### Base Sepolia (Testnet)

```env
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest
```

### Base Mainnet (Produksi)

```env
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<deploy-your-own>
```

**Untuk subgraph mainnet**: Deploy sendiri menggunakan [repositori P2P.me Subgraph](https://github.com/p2pdotme/subgraph).

### URL RPC

Anda membutuhkan endpoint RPC. Pilihan tersedia:

**Publik (gratis, ada batasan rate):**
```env
# Base Mainnet
REACT_APP_RPC_URL=https://mainnet.base.org

# Base Sepolia Testnet
REACT_APP_RPC_URL=https://sepolia.base.org
```

**Direkomendasikan (komersial, lebih cepat, lebih andal):**
- [Alchemy](https://www.alchemy.com/), tersedia paket gratis
- [Infura](https://www.infura.io/), tersedia paket gratis
- [QuickNode](https://www.quicknode.com/), tersedia paket gratis

### Membuat File `.env.local`

Buat file `.env.local` di direktori root proyek Anda. Salin nilai-nilai dari atas sesuai jaringan yang Anda gunakan:

**Untuk Base Sepolia Testnet:**
```env
# Jaringan
REACT_APP_RPC_URL=https://sepolia.base.org
REACT_APP_CHAIN_ID=84532

# Alamat Kontrak
REACT_APP_DIAMOND_ADDRESS=0xce868398FDaDcA368EAc203222874D6888532aE2
REACT_APP_USDC_ADDRESS=0xDABa329Ed949f28F64019f22c33c3B253B2Ded60
REACT_APP_SUBGRAPH_URL=https://api.studio.thegraph.com/query/110312/indexer-one/version/latest

# Akun Anda (untuk pengujian; khusus pengembangan saja!)
REACT_APP_PRIVATE_KEY=<your-private-key-here>
```

**Untuk Base Mainnet (Produksi):**
```env
# Jaringan
REACT_APP_RPC_URL=https://mainnet.base.org
REACT_APP_CHAIN_ID=8453

# Alamat Kontrak
REACT_APP_DIAMOND_ADDRESS=0x4cad6eC90e65baBec9335cAd728DDC610c316368
REACT_APP_USDC_ADDRESS=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
REACT_APP_SUBGRAPH_URL=<your-deployed-subgraph-url>
```

Muat dalam kode Anda:

```ts
const RPC_URL = import.meta.env.REACT_APP_RPC_URL;
const DIAMOND_ADDRESS = import.meta.env.REACT_APP_DIAMOND_ADDRESS;
const USDC_ADDRESS = import.meta.env.REACT_APP_USDC_ADDRESS;
const SUBGRAPH_URL = import.meta.env.REACT_APP_SUBGRAPH_URL;
```

### Mendapatkan Dana Testnet

Untuk menguji pesanan SELL/PAY di Base Sepolia, Anda membutuhkan ETH dan USDC:

- [Faucet.circle.com](https://faucet.circle.com/), memberikan ETH dan testnet USDC (direkomendasikan)
- [SepoliaFaucet.com](https://sepoliafaucet.com/), ETH saja

## Penyiapan

Instal SDK:
```bash
npm install @p2pdotme/sdk viem
```

Anda membutuhkan:
- **publicClient**: viem `PublicClient` untuk operasi baca
- **walletClient**: viem `WalletClient` untuk operasi tulis
- **diamondAddress**: Kontrak P2P Protocol
- **usdcAddress**: Alamat token USDC
- **subgraphUrl**: Endpoint GraphQL

## Contoh React

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

## Memahami Tipe Result

Semua metode SDK mengembalikan tipe `Result` dari neverthrow (tidak pernah melempar pengecualian):

```ts
const result = await orders.placeOrder.execute(params);

// Selalu gunakan .match() untuk menangani sukses dan error
result.match(
  (success) => {
    // Tangani sukses
    console.log("Success:", success.hash);
  },
  (error) => {
    // Tangani error
    console.error("Error:", error.code, error.message);
  }
);

// Atau periksa dengan .isOk()
if (result.isOk()) {
  console.log("Hash:", result.value.hash);
} else {
  console.log("Error:", result.error.code);
}
```

---

## Pesanan

Modul `orders` menangani semua operasi siklus hidup pesanan.

## Tipe Pesanan

| Tipe | Nilai | Deskripsi |
|------|-------|-----------|
| BUY | `0` | Pengguna menerima USDC, mengirim fiat |
| SELL | `1` | Pengguna mengirim USDC, menerima fiat |
| PAY | `2` | Pengguna mengirim USDC ke wallet |

## Membuat Pesanan BUY

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

## Membuat Pesanan SELL

SELL membutuhkan persetujuan USDC terlebih dahulu:

```ts
// 1. Setujui
await orders.approveUsdc.execute({
  walletClient,
  amount: 10_000_000n,
});

// 2. Buat pesanan
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

// 3. Atur tujuan pembayaran
await orders.setSellOrderUpi.execute({
  walletClient,
  orderId: result.value.meta.orderId,
  paymentAddress: "user@upi",
});
```

## Melacak Pesanan

```ts
// Dapatkan semua pesanan pengguna (mengembalikan tipe Result)
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

// Dapatkan satu pesanan
const singleResult = await orders.getOrder({ orderId: 42n });
singleResult.match(
  (order) => console.log("Order:", order),
  (err) => console.error("Error:", err),
);

// Batalkan pesanan
const cancelResult = await orders.cancelOrder.execute({
  walletClient,
  orderId: "0x123...",
});

cancelResult.match(
  ({ hash }) => console.log("Cancelled! Hash:", hash),
  (err) => console.error("Error:", err.message),
);

// Ajukan sengketa
const disputeResult = await orders.raiseDispute.execute({
  walletClient,
  orderId: "0x123...",
});

disputeResult.match(
  ({ hash }) => console.log("Dispute raised! Hash:", hash),
  (err) => console.error("Error:", err.message),
);
```

## Mendapatkan Biaya

```ts
const result = await orders.getFeeConfig({ currency: "INR" });

result.match(
  (feeConfig) => {
    // Field FeeConfig adalah bigint 6 desimal
    console.log(feeConfig.smallOrderThreshold, feeConfig.smallOrderFixedFee);
  },
  (err) => console.error("Error:", err.code),
);
```

---

## Profil & Batas

Periksa saldo pengguna, allowance USDC, dan batas transaksi.

## Memeriksa Saldo

```ts
// Saldo USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Allowance USDC (sebelum SELL/PAY)
const allowance = await profile.getUsdcAllowance({
  owner: userAddress,
});

// getBalances juga mengembalikan Result:
const balancesResult = await profile.getBalances({ address: userAddress, currency: "INR" });
balancesResult.match(
  (b) => console.log(b.usdc, b.fiat),
  (err) => console.error(err.code),
);
```

## Memeriksa Batas

```ts
const result = await profile.getTxLimits({
  address: userAddress,
  currency: "INR",
});

result.match(
  (limits) => {
    // limits memiliki: buyLimit, sellLimit
    console.log("Buy Limit:", limits.buyLimit);
    console.log("Sell Limit:", limits.sellLimit);
  },
  (err) => console.error("Error:", err.code),
);
```

Batas bergantung pada reputasi, level KYC, dan parameter risiko mata uang.

## Pemeriksaan Pra-transaksi

Sebelum BUY:
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

Sebelum SELL:
```ts
// Dapatkan saldo USDC
const balanceResult = await profile.getUsdcBalance({ address: userAddr });
if (balanceResult.isErr()) throw balanceResult.error;
const usdcBalance = balanceResult.value; // bigint

// Dapatkan batas
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

## Penanganan Error

Dekode error kontrak menjadi pesan yang ramah pengguna.

## Struktur Error

```ts
const error = {
  code: "INSUFFICIENT_BALANCE",
  message: "User has insufficient USDC balance",
  cause: rawError, // underlying error
};
```

## Mendekode Error Kontrak

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

## Kode Error Umum

| Kode | Arti | Tindakan |
|------|------|----------|
| `INVALID_INPUT` | Parameter tidak valid | Periksa input Anda |
| `VALIDATION_ERROR` | Validasi gagal | Perbaiki format data |
| `NETWORK_ERROR` | Error RPC/subgraph | Coba lagi dengan backoff |
| `INSUFFICIENT_ALLOWANCE` | Perlu persetujuan USDC | Panggil `approveUsdc.execute()` |

## Pola Penanganan Error

Degradasi yang baik:
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

Coba ulang dengan backoff:
```ts
async function retryOrder(params, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    const result = await orders.placeOrder.execute(params);

    if (result.isOk()) {
      return result.value;
    }

    const { code } = result.error;

    // Hanya coba ulang pada error jaringan
    if (code === "NETWORK_ERROR") {
      await new Promise(r => setTimeout(r, 1000 * Math.pow(2, i)));
      continue;
    }

    // Jangan coba ulang error validasi
    throw result.error;
  }
}
```

---

## Pola Tingkat Lanjut

Gunakan pemisahan `prepare`/`execute`, relay identity, dan penyimpanan kustom.

## Prepare vs Execute

`prepare()` mengembalikan transaksi mentah tanpa penandatanganan:
```ts
const result = await orders.placeOrder.prepare(params);
// Mengembalikan: { to, data, value, meta }
// Kirim melalui relayer, multisig, atau penanda tangan kustom
```

`execute()` menandatangani dan mengirim dengan viem:
```ts
const result = await orders.placeOrder.execute({
  walletClient,
  ...params
});
```

## Kasus Penggunaan

**Relaying tanpa gas:**
```ts
const tx = await orders.placeOrder.prepare(params);
await relayerApi.send(tx.value);
```

**Multi-sig:**
```ts
const tx = await orders.placeOrder.prepare(params);
await multiSigWallet.queue(tx.value);
```

**Penandatanganan sisi server:**
```ts
const tx = await orders.placeOrder.prepare(params);
const signed = await serverSignAndSend(tx.value);
```

## Relay Identity

SDK menggunakan keypair untuk anonimitas pengirim. Default tersimpan di memori (hilang saat refresh).

Simpan ke localStorage:
```tsx
import { createLocalStorageRelayStore } from "@p2pdotme/sdk/orders";

<SdkProvider
  orders={{
    relayIdentityStore: createLocalStorageRelayStore({ key: "relay" })
  }}
/>
```

Penyimpanan kustom:
```tsx
const store = {
  get: async () => db.getRelayIdentity(),
  set: async (id) => db.saveRelayIdentity(id),
};

<SdkProvider orders={{ relayIdentityStore: store }} />
```

## Mandiri (Tanpa React)

Gunakan factory langsung:
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

// Gunakan keduanya
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

## Contoh

Alur kerja lengkap untuk pola umum.

## Alur BUY

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

## Alur SELL

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

## Memantau Status Pesanan

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
