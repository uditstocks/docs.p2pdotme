---
id: hierarchy
sidebar_position: 2
title: "Hierarquia"
slug: hierarchy
---

| Nível             | Função                                       | Codinome         |
| ----------------- | -------------------------------------------- | ---------------- |
| Core Team         | Fundadores e líderes do protocolo            | "Core Team"      |
| Country Lead      | Gerencia todas as trilhas em um país         | "Country Lead"   |
| Coordenador       | Coordenadores de trilha                      | "Keymaster"      |
| Colaborador       | Embaixadores da comunidade                   | "Cipher"         |

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

Cada "Keymaster" gerencia até 5 "Ciphers".

## Responsabilidades do Country Lead

Cada "Country Lead" gerencia as quatro trilhas do seu país.

| Codinome             | Escopo                                                          |
| -------------------- | --------------------------------------------------------------- |
| **Relay Guild**      | Canais de Discord/Telegram do país                              |
| **Node Guild**       | Faculdades e eventos locais                                     |
| **Signal Guild**     | Redes sociais regionais (conteúdo em idioma local)              |
| **Forge Guild**      | Traduções, comunidade local de desenvolvedores                  |

---
