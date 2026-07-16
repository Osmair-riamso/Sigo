# Regras de Negócio

## Padrão dos CRUDs

Todos os cadastros seguem o padrão:

- Cadastro
- Edição
- Ativação
- Inativação
- Exclusão protegida

---

## Exclusão

Somente poderá ser excluído um registro que:

- esteja inativo;
- não possua vínculos.

---

## Operadoras

Não podem ser excluídas se existirem circuitos vinculados.

---

## Cidades

Não podem ser excluídas se existirem circuitos vinculados.

---

## Usuários

Não podem ser excluídos se existirem ocorrências vinculadas.

---

## Circuitos

Não podem ser excluídos se existirem ocorrências vinculadas.

---

## Circuitos Duplicados

Uma operadora pode possuir diversos circuitos.

É proibido repetir a mesma designação para a mesma cidade e operadora.
