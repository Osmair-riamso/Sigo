# SIGO

**Sistema Integrado de Gestão Operacional**

---

## Objetivo

O SIGO é um sistema desenvolvido para apoiar a operação diária do NOC (Network Operation Center), centralizando informações operacionais, ocorrências, circuitos, operadoras e comunicados em um único painel.

O principal objetivo é permitir que qualquer colaborador visualize rapidamente:

- O que aconteceu.
- O que está acontecendo.
- O que acontecerá nos próximos dias.

Alterações de informações exigem autenticação, porém a consulta ao Dashboard é pública dentro da organização.

---

# Tecnologias

- Python 3.12+
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- Bootstrap 5

---

# Estrutura do Projeto

```
Sigo/

│
├── app/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   └── __init__.py
│
├── instance/
│
├── MER/
│
├── config.py
├── run.py
└── README.md
```

---

# Módulos

- Dashboard
- Ocorrências
- Circuitos
- Operadoras
- Usuários
- Configurações

---

# Dashboard

A tela inicial será composta por quatro painéis principais.

## Painel Fibra

Apresenta todas as ocorrências relacionadas aos circuitos de comunicação.

Exibe:

- cidade
- circuito
- operadora
- status
- última atualização

---

## Painel Passagem de Turno

Informações importantes entre as equipes.

Exemplos:

- atualizações
- procedimentos
- equipamentos
- observações operacionais

---

## Painel Agenda Técnica

Apresenta eventos programados.

Os eventos passam a aparecer automaticamente sete dias antes da data agendada.

---

## Painel Resumo do Dia

Resumo operacional diário.

Exemplos:

- ocorrências do dia
- impactos
- observações importantes

---

## Painel Lateral

Exibe:

- Última atualização operacional.
- Próxima atividade agendada.
- Alertas operacionais.

---

# Banco de Dados

Inicialmente será utilizado SQLite.

Posteriormente o sistema poderá migrar para PostgreSQL sem alterações na aplicação.

---

# Documentação

Toda documentação do projeto encontra-se na pasta:

```
MER/
```

---

# Roadmap

- ✅ Estrutura Flask
- ✅ Banco SQLite
- ✅ Cadastro de Operadoras
- ✅ Cadastro de Usuários
- 🚧 Dashboard
- ⏳ Login
- ⏳ Circuitos
- ⏳ Ocorrências
- ⏳ Relatórios

## Status do Projeto

Atualmente o SIGO encontra-se na fase de desenvolvimento da estrutura administrativa.

### Funcionalidades implementadas

- Dashboard inicial
- Cadastro de Operadoras
- Cadastro de Cidades
- Cadastro de Circuitos
- Cadastro de Usuários
- Banco de dados SQLite utilizando SQLAlchemy
- Arquitetura modular utilizando Blueprints
- Templates organizados por módulo
- Estrutura preparada para autenticação com Flask-Login

### Funcionalidades em desenvolvimento

- CRUD completo (Editar/Excluir)
- Login de usuários
- Cadastro de Ocorrências
- Histórico de ocorrências
- Dashboard dinâmico
- Agenda operacional
- Passagem de turno
- Integração futura com Zabbix

---
## Estrutura do Projeto

app/
│
├── routes/
│   ├── main.py
│   ├── operadoras.py
│   ├── cidades.py
│   ├── circuitos.py
│   ├── usuarios.py
│   └── ocorrencias.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── operadoras/
│   ├── cidades/
│   ├── circuitos/
│   ├── usuarios/
│   └── ocorrencias/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── models.py
└── __init__.py

## Módulos do Sistema

### Administrativos

- Operadoras
- Cidades
- Circuitos
- Usuários

### Operacionais

- Ocorrências
- Agenda
- Passagem de Turno
- Dashboard

## Roadmap

### Sprint 6

- CRUD completo
- Editar
- Excluir
- Confirmação de exclusão

### Sprint 7

- Login
- Controle de acesso

### Sprint 8

- Ocorrências
- Histórico
- Timeline

### Sprint 9

- Dashboard dinâmico
- Agenda
- Passagem de turno

### Sprint 10

- Integração com Zabbix

Projeto desenvolvido por Osmair Pereira.