## IS NULL

### 語法:

- 匯入tracks.csv

```
Column = NULL
```

### 範例:
```
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer = NULL;
```

### 語法:

```
{ column | expression } IS NULL;
```

### 範例:

```
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NULL
ORDER BY 
    Name;   
```

### 語法:

```
expression | column IS NOT NULL
```

### 範例:

```
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY 
    Name;      
```

