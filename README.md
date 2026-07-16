# SIGO

# Sistema Integrado de Gestão Operacional

---

## Objetivo

O SIGO (Sistema Integrado de Gestão Operacional) é uma plataforma desenvolvida para apoiar as atividades do NOC (Network Operation Center), centralizando informações operacionais em um único ambiente.

O sistema permitirá acompanhar:

- Ocorrências
- Circuitos
- Operadoras
- Agenda Técnica
- Passagem de Turno
- Comunicados Operacionais

O Dashboard será público para consulta dentro da organização, enquanto qualquer alteração exigirá autenticação.

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
SIGO/

├── app/
├── instance/
├── MER/
├── config.py
├── run.py
└── README.md
```

---

# Módulos

## Administrativos

- Operadoras
- Cidades
- Circuitos
- Usuários

## Operacionais

- Dashboard
- Ocorrências
- Agenda Técnica
- Passagem de Turno

---

# Estrutura da Documentação

Toda documentação técnica encontra-se na pasta MER.

```
MER/

01-Wireframe.md
02-MER.md
03-ModeloFisico.md
04-RegrasNegocio.md
05-FluxoOcorrencias.md
06-Roadmap.md
07-HistoricoVersoes.md
```

---

# Status Atual

## Sprint 6.1 concluída

Implementado:

- CRUD Operadoras
- CRUD Cidades
- CRUD Circuitos
- CRUD Usuários
- Exclusão protegida
- Validações
- BaseModel
- SQLAlchemy
- Blueprints
- Templates por módulo

---

## Próxima Sprint

Sprint 7

- Login
- Logout
- Controle de acesso
- Dashboard público
- Perfil do usuário

---

Projeto desenvolvido por

**Osmair Pereira**
