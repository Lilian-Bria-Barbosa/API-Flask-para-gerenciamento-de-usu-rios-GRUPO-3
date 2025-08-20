# 📌 API Flask - Gerenciamento de Usuários

## 📖 Descrição
Esta é uma API simples desenvolvida em **Flask** para realizar operações de CRUD (Create, Read, Update e Delete) de usuários.  
Os dados são armazenados em memória (listas Python) e podem ser manipulados via requisições HTTP.  

---

## 🚀 Tecnologias utilizadas
- [Python 3](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  

---

## ⚙️ Instalação e execução

1. Clone este repositório:  
   ```bash
   git clone https://github.com/Lilian-Bria-Barbosa/API-Flask-para-gerenciamento-de-usu-rios-GRUPO-3.git

   ```

2. Crie um ambiente virtual (opcional, mas recomendado):  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:  
   ```bash
   pip install flask
   ```

4. Execute a aplicação:  
   ```bash
   python app.py
   ```

5. Acesse no navegador ou no Postman:  
   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Endpoints

### ➕ Criar usuário
`POST /users`  
**Body (JSON):**  
```json
{
  "nome": "Maria",
  "email": "maria@gmail.com"
}
```

---

### 📋 Listar todos os usuários
`GET /users`  
**Resposta (JSON):**  
```json
[
  {
    "id": 1,
    "nome": "Maria",
    "email": "maria@gmail.com"
  }
]
```

---

### 🔍 Buscar usuário por ID
`GET /users/<id>`  
**Resposta (JSON):**  
```json
{
  "id": 1,
  "nome": "Maria",
  "email": "maria@gmail.com"
}
```

---

### ✏️ Atualizar usuário
`PUT /users/<id>`  
**Body (JSON):**  
```json
{
  "nome": "Maria Silva"
}
```

---

### ❌ Deletar usuário
`DELETE /users/<id>`  
**Resposta (JSON):**  
```json
{
  "message": "Usuário excluído com sucesso"
}
```

---

## 🧪 Testes no Postman
Você pode importar a **coleção de testes** no Postman ou testar diretamente via cURL.  

Exemplo cURL (POST usuário):  
```bash
curl -X POST http://127.0.0.1:5000/users \\
   -H "Content-Type: application/json" \\
   -d '{"nome": "Maria", "email": "maria@gmail.com"}'
```

---

## ✨ Autor
👩‍💻 Desenvolvido por **Cindy, Lavínia, Leticia, Lilian**
