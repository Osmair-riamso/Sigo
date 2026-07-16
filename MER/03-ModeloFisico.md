# Modelo Físico

## BaseModel

```
id
ativo
created_at
updated_at
```

Todas as tabelas herdam BaseModel.

---

## OPERADORA

```
id
nome
```

---

## CIDADE

```
id
cidade
estado
```

---

## CIRCUITO

```
id
cidade_id
operadora_id
tipo
designacao
observacao
```

---

## USUARIO

```
id
nome
login
senha_hash
perfil
```

---

## OCORRENCIA

Estrutura será implementada na Sprint 8.
