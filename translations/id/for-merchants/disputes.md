---
id: disputes
sidebar_position: 8
title: "Disputes"
slug: disputes
---

Jika sengketa diajukan, ikuti langkah-langkah berikut.

1. Tinjau konteks pesanan dan stempel waktu.
2. Kirimkan bukti pendukung melalui aplikasi.
3. Ikuti pembaruan penyelesaian dan transisi status pesanan yang dihasilkan.

Sengketa diselesaikan secara on-chain oleh Circle Admin dari pesanan (atau pemegang kapabilitas yang diotorisasi untuk Circle tersebut), yang menentukan kesalahan pengguna atau merchant. Jendela sengketa mengatur kapan sengketa dapat diajukan.

```mermaid
flowchart TD
    Order["Order in Progress"] --> Issue["Issue/Conflict Detected"]
    Issue --> Dispute["Dispute Raised (escrowed USDC held)"]
    
    subgraph Evidence["Evidence Phase"]
        User["User submits payment evidence (redacted reference)"]
    end
    
    Dispute --> Evidence
    Evidence --> Review["Admin Review (On-Chain Settlement)"]
    
    Review -- "Fault determination" --> Outcome
    
    subgraph Outcome["Settlement & Penalties"]
        Release["Release/Refund USDC"]
        Slash["Slash Performance Bond"]
        RP["Reputation (RP) Adjustment"]
    end
```

*Tingkatan eskalasi berbasis juri dan finalitas melalui pemungutan suara tata kelola untuk sengketa direncanakan untuk rilis mendatang.*

---
