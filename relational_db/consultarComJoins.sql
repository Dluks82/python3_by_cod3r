-- select *
-- from cidades c
--     INNER JOIN prefeitos p ON c.id = p.cidade_id;
-- select *
-- from cidades c
--     LEFT JOIN prefeitos p ON c.id = p.cidade_id;
-- select *
-- from cidades c
--     RIGHT JOIN prefeitos p ON c.id = p.cidade_id;
select *
from cidades c
    LEFT JOIN prefeitos p ON c.id = p.cidade_id
UNION
select *
from cidades c
    RIGHT JOIN prefeitos p ON c.id = p.cidade_id;