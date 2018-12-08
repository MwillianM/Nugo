Data Quality
===

Tabelas Vazias
---

```sql
select t.name, p.rows from sys.partitions p
join sys.tables t on p.object_id=t.object_id
where t.type='u' and p.rows = 0;
```

Transações com saldo negativo
---

```sql
select * from dbo.CashlessTransactions where Balance < 0;
```

Transações antes de 2014
---

```sql
select CAST(Date as DATETIME) from dbo.CashlessTransactions where CAST(Date as  DATETIME) < '2014-01-01';
```

Transações com Ordem Inconsistent
---

```sql
select * from dbo.CashlessTransactions where SequentialTransaction < 0;
```

Transações de Produto com quantidade 0
---

```sql
select * from dbo.CashlessTransactionProducts where Count = 0;
```

Ativações de cartão em datas inconsistentes
---

```sql
select * from dbo.CustomerSmartcards where ActivatedAt not BETWEEN '2014-12-31' and '2018-10-25';
```

Pessoas com idade inconsistentes
---

```sql
SELECT * FROM dbo.Persons WHERE BirthDate not BETWEEN '1918-10-25' and '2018-10-25';
```

Funcionários com menos de 18 anos
---

```sql
SELECT b.BirthDate, a.* FROM dbo.Users a LEFT JOIN dbo.Persons b ON b.IdPerson = a.IdPerson WHERE b.BirthDate > '2001-10-25' ;
```