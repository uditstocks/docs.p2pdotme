---
id: 05-5-trade-protocol-on-and-off-ramp
sidebar_position: 5
title: "5. Protocolo de Negociação (On-Ramp e Off-Ramp)"
slug: trade-protocol-on-and-off-ramp
---

Formalizamos o ciclo de vida de uma ordem como uma máquina de estados com tempos limite:

**Estados:** `OPEN → MATCHED → FUNDED → CONFIRMED → SETTLED | DISPUTED → RESOLVED | EXPIRED`

**Parâmetros Comuns (governados):**

- `T_match` (tempo máximo para aceitar uma correspondência), `T_fiat` (tempo máximo para realizar a transferência em moeda fiduciária), `T_confirm` (janela de confirmação), `T_dispute` (janela de contestação).
- `B_bond_user`, `B_bond_merchant` (caução de desempenho opcional/pesos de slashing por nível de reputação e classe de risco do meio de pagamento).
- `min_amount`, `max_amount` por meio/região, tabelas de taxas e janelas de expiração de cotação.

## 5.1 On-Ramp (Moeda Fiduciária → USDC na Base, com expansão para Solana)

1. **Abrir:** O usuário abre uma ordem de COMPRA com valor e meio de pagamento.
2. **Correspondência:** O protocolo atribui um comerciante on-chain com base no USDC em staking. Cauções reembolsáveis podem ser bloqueadas.
3. **Pagamento Fiduciário:** O usuário paga em moeda fiduciária para a conta fornecida dentro de `T_fiat`.
4. **Confirmação do Comerciante:** O comerciante confirma o recebimento do pagamento em moeda fiduciária.
5. **Liquidação:** O contrato libera o USDC para o usuário. As taxas são cobradas e as cauções desbloqueadas.
6. **Contestação:** Em caso de conflito, as partes submetem evidências e os administradores autorizados emitem um veredicto on-chain.

## 5.2 Off-Ramp (USDC na Base → Moeda Fiduciária, com expansão para Solana)

1. **Abrir:** O usuário abre uma ordem de VENDA e transfere USDC para o adaptador de liquidação sem custódia (o contrato retém ou transmite atomicamente conforme o design).
2. **Correspondência:** O comerciante aceita e publica cotação/caução.
3. **Bloqueio de Cripto:** O USDC do usuário é bloqueado para liquidação.
4. **Pagamento Fiduciário pelo Comerciante:** O comerciante paga em moeda fiduciária e confirma a conclusão, ou o usuário contesta.
5. **Liquidação:** O contrato libera o USDC para o comerciante. As taxas são cobradas e as cauções desbloqueadas.
6. **Contestação:** Em caso de conflito, as partes submetem evidências e os administradores autorizados emitem um veredicto on-chain.

## 5.3 Classes de Risco dos Meios de Pagamento

Os meios de pagamento diferem entre si (instantâneo/irreversível versus reversível/sujeito a estorno). O protocolo mapeia cada meio a multiplicadores de caução, requisitos de confirmação e janelas de contestação mais longas ou mais curtas.

---
