# Wireframe - Dashboard SIGO

---

## Barra Superior

Logo SIGO

Data

Hora

Botão Entrar

---

## Menu Lateral

Dashboard

Ocorrências

Circuitos

Operadoras

Usuários

Configurações

---

## Painel 1

### Fibra

Ocorrências abertas relacionadas aos circuitos.

Informações:

- Cidade
- Circuito
- Operadora
- Status
- Última atualização

---

## Painel 2

### Passagem de Turno

Registro operacional.

Informações:

- procedimentos
- troca de equipamentos
- observações
- atualizações

---

## Painel 3

### Agenda Técnica

Eventos programados.

Os eventos aparecem automaticamente sete dias antes da data.

---

## Painel 4

### Resumo do Dia

Resumo operacional.

Exemplo:

Hoje tivemos uma queda em Porto Alegre.

Operadora Cirion.

Circuito CTA-0001.

Técnico em campo.

---

## Painel Direito

### Última Atualização

Exibe a última movimentação operacional.

Campos:

- Operadora
- Circuito
- Usuário
- Data
- Hora
- Status

---

### Agenda

Mostra o próximo evento.

---

### Alertas Operacionais

Área destinada aos alertas críticos.

Os alertas poderão ser ocultados ou reativados pelo Administrador.

Não serão alimentados automaticamente pelo Zabbix.

O objetivo é evitar alarmes repetitivos.

USUARIO
---------
id
nome
login
senha_hash
perfil
ativo
created_at
updated_at

OPERADORA
----------
id
nome
ativo
created_at
updated_at

CIDADE
-------
id
cidade
estado
ativo
created_at
updated_at

CIRCUITO
---------
id
cidade_id
operadora_id
tipo
designacao
observacao
ativo
created_at
updated_at

OCORRENCIA
-----------
(estrutura será implementada na Sprint 7)

