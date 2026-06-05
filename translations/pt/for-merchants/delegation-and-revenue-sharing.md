---
id: delegation-and-revenue-sharing
sidebar_position: 9
title: "Delegação e Compartilhamento de Receita"
slug: delegation-and-revenue-sharing
---

Delegadores fazem stake de USDC no pool de delegação de um Círculo para apoiar seus comerciantes e receber uma parcela das recompensas proporcional ao stake delegado. Os Administradores de Círculo fazem stake de $P2P separadamente para criar e operar um Círculo. A receita é dividida em pontos-base configurados por moeda. O comerciante e o Administrador de Círculo recebem cada um uma parcela base do volume de transações. A parcela do comerciante é então distribuída proporcionalmente à razão entre o stake próprio e o stake delegado, e a porção referente ao stake delegado é dividida entre o comerciante, o Administrador de Círculo e o pool de delegação por parâmetros configuráveis por moeda.

Essa distribuição dentro do Círculo é separada da divisão de receita no nível do protocolo. No nível do protocolo, 20 por cento da receita do protocolo é direcionada ao tesouro e 80 por cento aos operadores da rede (comerciantes, Administradores de Círculo, delegadores e seguro). A divisão descrita aqui governa como a parcela dos operadores de um único pedido é compartilhada dentro de um Círculo, e é definida em pontos-base por moeda. Os valores abaixo são os padrões atuais da especificação para a porção do stake delegado e o valor vigente é exibido no aplicativo.

| Destinatário | Parcela padrão da porção de stake delegado |
|--------------|---------------------------------------------|
| Comerciante | 60 por cento |
| Delegadores de USDC | 20 por cento |
| CAIP (Circle Admin Insurance Pool, Pool de Seguro do Administrador de Círculo) | 10 por cento |
| Administrador de Círculo | 10 por cento |

A distribuição de recompensas aos delegadores é baseada em snapshots. O pool rastreia recompensas por token e paga cada delegador proporcionalmente à sua parcela quando as recompensas são notificadas. Os delegadores resgatam as recompensas acumuladas no aplicativo e saem do pool por meio de uma solicitação seguida de um período de carência.

*A interface completa de delegação e os mecanismos de roteamento de recompensas no nível do Círculo estão planejados para uma versão futura.*

---
