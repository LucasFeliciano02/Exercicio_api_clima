from flask import Flask, jsonify
import requests
import redis
import json

app = Flask(__name__)

# Configuração do Redis
cache = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

API_B_URL = "http://localhost:5001/weather"

@app.route('/recommendation/<city>', methods=['GET'])
def get_recommendation(city):
    city_key = city.replace(" ", "")

    # Verifica se está no cache
    cached_data = cache.get(city_key)
    if cached_data:
        print(f"Cache hit: {city_key}")
        data = json.loads(cached_data)
    else:
        print(f"Cache miss: {city_key}. Buscando da API B...")
        try:
            response = requests.get(f"{API_B_URL}/{city_key}")
            if response.status_code != 200:
                return jsonify({"error": "Erro ao obter dados da cidade"}), response.status_code

            data = response.json()
            cache.setex(city_key, 60, json.dumps(data))  # TTL de 60s

        except requests.RequestException:
            return jsonify({"error": "Erro ao conectar a API de clima"}), 500

    temp = data.get("temp")

    if temp is None:
        return jsonify({"error": "Temperatura nao disponivel"}), 500

    # Lógica de recomendação
    if temp > 30:
        recommendation = "Está quente! Beba bastante agua e use protetor solar."
    elif 15 < temp <= 30:
        recommendation = "O clima esta agradavel. Aproveite o dia!"
    else:
        recommendation = "Esta frio! Não esqueça de usar um casaco."

    return jsonify({
        "city": data["city"],
        "temp": temp,
        "unit": data["unit"],
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(port=5000)
