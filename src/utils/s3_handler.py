from loguru import logger
from tqdm import tqdm
from datetime import datetime
import boto3
import os

logger.remove()
logger.add(lambda msg: tqdm.write(msg, end=''), colorize=True)


# =====================
# Variáveis de configuração
# =====================
S3_BUCKET: str = 'drivalake'  # Nome do bucket S3
S3_ENDPOINT: str = 'https://s3.bhs.io.cloud.ovh.net/'  # Endpoint OVH
AWS_ACCESS_KEY_ID: str = 'SUA_ACCESS_KEY'  # Substitua pela sua access key
AWS_SECRET_ACCESS_KEY: str = 'SUA_SECRET_KEY'  # Substitua pela sua secret key

# Parâmetros do upload (edite conforme necessário)
LAYER: str = 'raw'            # raw, trusted, refined, service
DATA_AREA: str = 'ambiental'  # financas, ambiental, features...
PROJECT: str = 'perdcomp'     # projeto específico
FILENAME: str = 'raw_perdcomp.parquet'  # nome do arquivo
LOCAL_FILE_PATH: str = f'/caminho/para/{FILENAME}'  # caminho local do arquivo

def build_s3_path(layer: str, area: str, project: str, filename: str) -> str:
    """
    Gera o caminho S3 padronizado com data do dia.
    Exemplo: raw/ambiental/perdcomp/20250728/raw_perdcomp.parquet
    Args:
        layer (str): Camada do pipeline (raw, trusted, refined, service)
        area (str): Área de negócio (ambiental, financas, etc)
        project (str): Projeto específico
        filename (str): Nome do arquivo
    Returns:
        str: Caminho S3 completo
    """
    today = datetime.today().strftime('%Y%m%d')
    s3_path = f'{layer}/{area}/{project}/{today}/{filename}'
    return s3_path

def upload_to_s3(
    local_path: str,
    s3_path: str,
    bucket: str = S3_BUCKET,
    endpoint: str = S3_ENDPOINT,
    access_key: str = AWS_ACCESS_KEY_ID,
    secret_key: str = AWS_SECRET_ACCESS_KEY
) -> None:
    """
    Faz upload de um arquivo local para o S3 OVH.
    Args:
        local_path (str): Caminho local do arquivo
        s3_path (str): Caminho destino no S3
        bucket (str): Nome do bucket
        endpoint (str): Endpoint OVH
        access_key (str): AWS Access Key
        secret_key (str): AWS Secret Key
    """
    try:
        session = boto3.session.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        s3 = session.client('s3', endpoint_url=endpoint)
        with tqdm(total=os.path.getsize(local_path), unit='B', unit_scale=True, desc=f'Upload {os.path.basename(local_path)}') as pbar:
            def progress_hook(bytes_amount):
                pbar.update(bytes_amount)
            s3.upload_file(local_path, bucket, s3_path, Callback=progress_hook)
        logger.success(f'Arquivo enviado para s3://{bucket}/{s3_path}')
    except Exception as e:
        logger.error(f'Erro no upload: {e}')

if __name__ == '__main__':
    # Basta editar as variáveis acima para controlar o destino e nome do arquivo
    s3_path = build_s3_path(LAYER, DATA_AREA, PROJECT, FILENAME)
    upload_to_s3(LOCAL_FILE_PATH, s3_path)
