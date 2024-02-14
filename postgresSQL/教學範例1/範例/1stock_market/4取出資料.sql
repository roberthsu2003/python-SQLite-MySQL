SELECT date,adj_close,volume,股市.name,country
FROM 股市 JOIN 市場 ON 股市.name = 市場.name;