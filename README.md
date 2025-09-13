Aplicativo de Análise de Sinais
Este aplicativo oferece funcionalidades de análise de sinal com uma interface web. Ele calcula medidas estatísticas e análise de tendência para sequências numéricas.

Recursos
Validação de entrada para números separados por vírgula.

Análise estatística, incluindo:

Cálculo da média

Detecção do valor mínimo

Detecção do valor máximo

Análise de tendência (crescente, decrescente ou estável).

Backend com API RESTful.

Interface de frontend simples e responsiva.

Configuração
Configuração do Backend
Navegue até o diretório do backend:

cd backend

Instale as dependências do Python:

pip install -r requirements.txt

Inicie o servidor FastAPI:

uvicorn main:app --reload

A API estará disponível em http://localhost:8000.

Configuração do Frontend
Abra o arquivo index.html em um navegador da web.

Certifique-se de que o servidor backend está em execução.

Documentação da API
Endpoint de Análise de Sinal
POST /analyze

Corpo da requisição:

JSON

{
  "signal": [1, 2, 3, 4, 5]
}
Resposta:

JSON

{
  "media": 3.0,
  "min": 1,
  "max": 5,
  "tendencia": "crescente"
}
A tendência pode ser uma das seguintes:

"crescente"
"decrescente"
"estável"

Uso
Insira uma sequência de números separados por vírgulas no campo de entrada.

Exemplo: 1,2,3,4,5

Clique no botão "Analisar Sinal".

Veja os resultados da análise abaixo do formulário.

Requisitos Técnicos
Python 3.7+

FastAPI

NumPy

Navegador da web moderno com JavaScript habilitado

Conexão com a internet para as dependências

Desenvolvimento
A documentação da API está disponível em http://localhost:8000/docs quando o servidor backend está em execução.

Tratamento de Erros
Formatos de entrada inválidos acionarão a validação no frontend.

O backend valida os dados de entrada usando modelos Pydantic.

Erros de rede são capturados e exibidos ao usuário.

Licença
Este projeto está licenciado sob a Licença MIT.