---
id: hierarchy
sidebar_position: 2
title: "Hierarki"
slug: hierarchy
---

| Level        | Peran                                     | Nama Kode      |
| ------------ | ----------------------------------------- | -------------- |
| Core Team    | Pendiri dan pimpinan protokol             | "Core Team"    |
| Country Lead | Mengelola semua jalur di suatu negara     | "Country Lead" |
| Coordinator  | Koordinator jalur                         | "Keymaster"    |
| Contributor  | Ambassador komunitas                      | "Cipher"       |

```mermaid
flowchart TD
    CT["1. Core Team"]

    subgraph india [India]
        CL_IN["2. Country Lead"]
        KM_IN_Relay["3. Keymaster - Relay Guild"]
        KM_IN_Node["3. Keymaster - Node Guild"]
        KM_IN_Signal["3. Keymaster - Signal Guild"]
        KM_IN_Forge["3. Keymaster - Forge Guild"]
        CL_IN --> KM_IN_Relay
        CL_IN --> KM_IN_Node
        CL_IN --> KM_IN_Signal
        CL_IN --> KM_IN_Forge
    end

    subgraph brazil [Brazil]
        CL_BR["2. Country Lead"]
        KM_BR["3. Keymasters..."]
        CL_BR --> KM_BR
    end

    subgraph other [Other Countries...]
        CL_X["2. Country Lead"]
        KM_X["3. Keymasters..."]
        CL_X --> KM_X
    end

    CT --> CL_IN
    CT --> CL_BR
    CT --> CL_X
```

Setiap "Keymaster" mengelola hingga 5 "Cipher".

## Tanggung Jawab Country Lead

Setiap "Country Lead" mengelola keempat jalur di negaranya.

| Nama Kode        | Cakupan                                                        |
| ---------------- | -------------------------------------------------------------- |
| **Relay Guild**  | Saluran Discord/Telegram negara                                |
| **Node Guild**   | Kampus dan acara lokal                                         |
| **Signal Guild** | Media sosial regional (konten dalam bahasa lokal)              |
| **Forge Guild**  | Terjemahan, komunitas pengembang lokal                         |

---
