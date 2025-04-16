**Exercício: Sistema de Clima e Recomendações**  



Neste exercício, você criará duas APIs simples que se comunicam entre si. A primeira API (**API B**) será responsável por fornecer dados de clima de uma cidade, retornando a temperatura em Celsius. A segunda API (**API A**) consumirá esses dados e, com base na temperatura, gerará uma recomendação personalizada para o usuário.  



A **API B** terá um único endpoint, `GET /weather/{city}`, que retornará um JSON contendo o nome da cidade, a temperatura atual e a unidade de medida (Celsius). Por exemplo, uma requisição para `GET /weather/SãoPaulo` poderia retornar `{ "city": "São Paulo", "temp": 25, "unit": "Celsius" }`.  



Já a **API A** terá o endpoint `GET /recommendation/{city}`, que fará uma chamada à **API B** para obter a temperatura da cidade solicitada. Com base nesse valor, ela retornará uma recomendação: se a temperatura estiver acima de 30°C, sugerirá hidratação e protetor solar; se estiver entre 15°C e 30°C, dirá que o clima está agradável; e se for igual ou abaixo de 15°C, recomendará usar um casaco.  



Como tarefa, você deverá implementar ambas as APIs, garantindo que a **API A** consulte corretamente a **API B** e processe a resposta para gerar a recomendação adequada. Para testar, basta chamar o endpoint da **API A** (por exemplo, `GET /recommendation/SãoPaulo`) e verificar se a resposta inclui a temperatura e a sugestão esperada.  



Como desafio opcional, você pode adicionar tratamento de erros (como cidade não encontrada) ou implementar um cache simples na **API A** para evitar consultas repetidas à **API B** quando a mesma cidade for solicitada em um curto período.  
