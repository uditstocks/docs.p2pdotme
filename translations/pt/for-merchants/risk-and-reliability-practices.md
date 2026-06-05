---
id: risk-and-reliability-practices
sidebar_position: 11
title: "Práticas de Risco e Confiabilidade"
slug: risk-and-reliability-practices
---

- Responda rapidamente aos pedidos atribuídos.
- Mantenha os metadados dos canais e os dados de pagamento precisos.
- Evite operar canais quando não estiver disponível.
- Preserve os registros de evidências para pagamentos contestados.
- Trate cancelamentos e disputas como sinais de qualidade para aprimorar as operações.

## Padrão de Pagamento Recorrente no PIX

Um padrão a ser observado no rail PIX é o de um pagamento configurado para se repetir automaticamente em datas futuras, às vezes identificado como PIX recorrente, PIX automático, ou plano anual ou mensal. Concluir esse tipo de pedido pode autorizar cobranças além da transação única que está diante de você. Não conclua o pedido. Cancele-o e reporte-o com o ID do pedido.

Se você acredita ter autorizado um pagamento recorrente por engano, cancele a recorrência no seu aplicativo bancário e reporte-o com o ID do pedido. A detecção de fraudes no protocolo é executada off-chain por meio da API de Fraudes da SEON nos eventos de cadastro, verificação e transação. O Diamond on-chain aplica as janelas de disputa, as penalidades de Reputation Points e os bloqueios de lista de bloqueio. Ele não pontua transações, portanto o seu julgamento no momento do pagamento é a primeira linha de defesa.

---
