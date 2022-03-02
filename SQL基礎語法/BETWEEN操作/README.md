## BETWEEN操作

### 語法:
```
test_expression BETWEEN low_expression AND high_expression
```

```
test_expression >= low_expression AND test_expression <= high_expression
```

- NOT BETWEEN

```
test_expression NOT BETWEEN low_expression AND high_expression
```

```
test_expression < low_expression OR test_expression > high_expression
```

### 範例

- 匯入 invoices.csv

```
SELECT
    InvoiceId,
    BillingAddress,
    Total
FROM
    invoices
WHERE
    Total BETWEEN 14.91 and 18.86    
ORDER BY
    Total; 
```

```
SELECT
    InvoiceId,
    BillingAddress,
    Total
FROM
    invoices
WHERE
    Total NOT BETWEEN 1 and 20
ORDER BY
    Total;    
```

```
SELECT
    InvoiceId,
    BillingAddress,
    InvoiceDate,
    Total
FROM
    invoices
WHERE
    InvoiceDate BETWEEN '2010-01-01' AND '2010-01-31'
ORDER BY
    InvoiceDate;    
```

