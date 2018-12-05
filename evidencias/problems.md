Data Quality
===

Tabelas Vazias
---

[output](./table-rows-count.pdf)
```sql
select t.name, p.rows from sys.partitions p
join sys.tables t on p.object_id=t.object_id
where t.type='u' and p.rows = 0;
```

Transações com saldo negativo
---

[output](./negative-balance-transactions.md)
```sql
select * from dbo.CashlessTransactions where Balance < 0;
```

Transações antes de 2014
---

[output](./before2014-transactions.md)
```sql
select CAST(Date as DATETIME) from dbo.CashlessTransactions where CAST(Date as  DATETIME) < '2014-01-01';
```

Transações com Ordem negativa
---

[output](./negative-sequencial-transactions.md)
```sql
select * from dbo.CashlessTransactions where SequentialTransaction < 0;
```

Transações de Produto com quantidade 0
---

[output](./zero-products-count.md)
```sql
select * from dbo.CashlessTransactionProducts where Count = 0;
```

Ativações de cartão em datas inconsistentes
---

[output](./inconsistent-activation-data.md)
```sql
select * from dbo.CustomerSmartcards where ActivatedAt < '2014-12-31' or ActivatedAt > '2018-10-25';
```

# idade