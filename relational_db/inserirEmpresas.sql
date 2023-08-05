-- alter table empresas MODIFY cnpj VARCHAR(14);
-- desc empresas;
-- insert INTO empresas (nome, cnpj)
-- VALUES ('Empresa 1', 123456789),
--     ('Empresa 2', 987654321),
--     ('Empresa 3', 12345678901234);
insert into empresas_unidades (empresa_id, cidade_id, sede)
values (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)