# SIGO

> **Sistema Interno de Gerenciamento de Ocorrências**

Aplicação web desenvolvida em **Python + Flask** para gerenciamento operacional da equipe técnica de uma emissora de televisão.

O SIGO foi criado para registrar, acompanhar e documentar ocorrências operacionais, preservando o histórico completo das atividades e facilitando a comunicação entre os turnos.

---

# Status do Projeto

🚧 Em desenvolvimento

Versão atual: **0.1.0**

---

# Objetivo

Centralizar todas as ocorrências da operação técnica em um único sistema, permitindo que qualquer técnico visualize rapidamente o andamento dos trabalhos durante a troca de turno.

O SIGO não pretende substituir um sistema de Help Desk tradicional, mas sim funcionar como um **Diário Operacional Eletrônico**, preservando todas as informações importantes da operação.

---

# Principais Funcionalidades

* Login de usuários
* Controle de acesso por perfil
* Cadastro de ocorrências
* Histórico permanente das atualizações
* Passagem de turno
* Cadastro de circuitos
* Pesquisa avançada
* Relatórios em PDF
* Exportação para Excel
* Backup do banco de dados
* Registro de auditoria das alterações

---

# Perfis de Usuário

## Técnico

* Criar ocorrências
* Atualizar ocorrências
* Consultar registros
* Alterar status
* Pesquisar ocorrências

## Folguista

Mesmo acesso do Técnico.

## Ferista

Mesmo acesso do Técnico.

## Gerente

Acesso completo ao sistema.

Pode:

* Gerenciar usuários
* Editar qualquer ocorrência
* Reabrir ocorrências
* Gerar relatórios
* Visualizar estatísticas

## Administrador

Controle total do sistema.

Pode:

* Configurar o sistema
* Gerenciar usuários
* Criar backups
* Restaurar banco de dados
* Administração geral

---

# Tecnologias

## Backend

* Python 3.13
* Flask
* Flask-Login
* Flask-SQLAlchemy
* SQLAlchemy

## Frontend

* HTML5
* Bootstrap 5
* JavaScript

## Banco de Dados

* SQLite

## Relatórios

* PDF
* Excel (planejado)

---

# Arquitetura

O projeto utiliza o padrão **Application Factory**, recomendado pela documentação oficial do Flask.

Estrutura do projeto:

```text
SIGO/
│
├── app/
│   ├── __init__.py
│   ├── auth/
│   ├── models/
│   ├── reports/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   │
│   └── templates/
│       ├── auth/
│       ├── circuitos/
│       ├── dashboard/
│       ├── layout/
│       ├── ocorrencias/
│       └── usuarios/
│
├── database/
│   └── backups/
│
├── docs/
│
├── exports/
│   ├── excel/
│   └── pdf/
│
├── instance/
│   └── sigo.db
│
├── tests/
│
├── config.py
├── run.py
├── requirements.txt
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

# Banco de Dados

O sistema utiliza **SQLite**.

Motivos da escolha:

* Arquivo único
* Excelente desempenho
* Gratuito
* Não necessita servidor
* Backup simples
* Ideal para aplicações internas

O banco ficará armazenado em:

```text
instance/sigo.db
```

Os backups serão armazenados em:

```text
database/backups/
```

---

# Arquitetura da Aplicação

```text
Navegador
      │
      ▼
Flask (Routes)
      │
 ┌────┼───────────────┐
 │    │               │
 ▼    ▼               ▼
Auth Ocorrências Circuitos
 │    │               │
 └────┼───────────────┘
      ▼
Services
      ▼
SQLAlchemy
      ▼
SQLite
```

---

# Roadmap

## Versão 0.1.0

* [x] Planejamento
* [x] Estrutura inicial
* [x] Configuração do ambiente
* [ ] Aplicação Flask

## Versão 0.2.0

* [ ] Banco SQLite
* [ ] Models

## Versão 0.3.0

* [ ] Sistema de Login

## Versão 0.4.0

* [ ] Dashboard

## Versão 0.5.0

* [ ] Cadastro de Ocorrências

## Versão 0.6.0

* [ ] Histórico

## Versão 0.7.0

* [ ] Cadastro de Circuitos

## Versão 0.8.0

* [ ] Relatórios

## Versão 0.9.0

* [ ] Backup

## Versão 1.0.0

* [ ] Sistema pronto para produção

---

# Boas Práticas do Projeto

Durante o desenvolvimento serão adotados os seguintes padrões:

* PEP 8
* Application Factory
* Blueprints
* SQLAlchemy ORM
* Commits semânticos
* Versionamento Semântico
* Documentação contínua
* Código limpo

---

# Fluxo de Desenvolvimento

Cada etapa do projeto seguirá o seguinte ciclo:

1. Planejamento
2. Desenvolvimento
3. Testes
4. Atualização da documentação
5. Commit
6. Envio para o GitHub

Nenhuma nova funcionalidade será iniciada antes da conclusão da etapa anterior.

---

# Objetivo Final

Desenvolver um sistema simples, rápido e confiável para uso diário da equipe técnica da emissora, garantindo que nenhuma informação operacional seja perdida entre os turnos e mantendo um histórico completo de todas as ocorrências.

O projeto foi concebido para ser de fácil manutenção e preparado para futuras expansões, como integração com Active Directory, API REST, envio de e-mails, notificações e dashboard em tempo real.
