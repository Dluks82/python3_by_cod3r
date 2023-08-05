-- select regiao as 'Região',
--     sum(populacao) as Total
-- from estados
-- GROUP BY regiao
-- ORDER BY Total DESC;
-- select sum(populacao) as Total
-- from estados;
select avg(populacao) as Total
from estados;