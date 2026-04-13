-- Total de dinero por usuario
SELECT 
    user_id,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY user_id;


-- Cantidad de transacciones por usuario
SELECT 
    user_id,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY user_id;


-- Ranking de usuarios por gasto
SELECT 
    user_id,
    SUM(amount) AS total_amount,
    RANK() OVER (ORDER BY SUM(amount) DESC) AS ranking
FROM transactions
GROUP BY user_id;
