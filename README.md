# Spark Template

Este repositório é um template para iniciar projetos de Engenharia de Dados utilizando PySpark, S3 OVH e PostgreSQL. Ele oferece uma estrutura modular, boas práticas e exemplos para acelerar o desenvolvimento.

## Estrutura do Projeto

```
├── Dockerfile
├── requirements.txt
├── src/
│   ├── upload_s3.py
│   └── utils/
│       ├── spark_handler.py
│       └── s3_handler.py
```

## Principais Recursos

- **PySpark 3.5.5**: Framework de processamento distribuído.
- **S3 OVH**: Armazenamento de dados, com funções para upload padronizado.
- **PostgreSQL**: Banco de dados relacional para destino dos dados.
- **Loguru & tqdm**: Logging colorido e barra de progresso em pipelines.
- **Docker**: Ambiente isolado e reprodutível.

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repo>
   cd spark-puro
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   # Instale também boto3, loguru e tqdm
   pip install boto3 loguru tqdm
   ```

3. **Configure variáveis:**
   - Edite os arquivos em `src/utils/` para definir credenciais, bucket, endpoint, áreas, projetos e caminhos de arquivos.
   - Exemplo de configuração no topo de `s3_handler.py`:
     ```python
     S3_BUCKET = 'drivalake'
     S3_ENDPOINT = 'https://s3.bhs.io.cloud.ovh.net/'
     AWS_ACCESS_KEY_ID = 'SUA_ACCESS_KEY'
     AWS_SECRET_ACCESS_KEY = 'SUA_SECRET_KEY'
     ```

4. **Execute scripts:**
   - Use os scripts de exemplo para upload de arquivos ao S3 ou inicialização do Spark.
   - Exemplo:
     ```bash
     python src/upload_s3.py
     ```

## Recomendações

- Declare todas as variáveis no início dos scripts para facilitar manutenção.
- Use funções modulares e tratamento de exceções.
- Estruture os caminhos S3 por camada, área, projeto e data (`YYYYMMDD`).
- Utilize f-strings e snake_case para variáveis e funções.

## Sobre

Este template foi criado para acelerar o início de projetos de dados, promovendo organização, clareza e boas práticas. Sinta-se livre para adaptar conforme sua necessidade!
