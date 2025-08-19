from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
current_id = 1

# ROTA (POST)
@app.route("/users", methods=["POST"])
def create_user():
    global current_id
    data = request.json
    if not data or "nome" not in data or "email" not in data:
        return jsonify({"error": "Dados inválidos"}), 400
    
    new_user = {
        "id": current_id, 
        "nome": data["nome"],
        "email": data["email"]
    }
    users.append(new_user)
    current_id += 1
    return jsonify(new_user),201

#ROTA (GET) 
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users),200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404


#ROTA (PUT)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        user["nome"] = data.get("nome", user["nome"])
        user["email"] = data.get("email", user["email"])
        return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado" }), 404


#ROTA DELETE 
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global user
    user =  next((u for u in users if u["id"] == user_id), None)

    if user:
        users.remove(user)
        return jsonify({"message": "Usuário excluído com sucesso"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__=="__main__":
    app.run(debug=True)


