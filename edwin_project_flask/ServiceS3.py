import boto3
import requests

def cargarImagen(imagen):
    s3_client = boto3.client('s3', aws_acceskey_id="AKIAQ3F23Y03CPPUCK0J", aws_secret_acces_key="cSSwLTxGSi6q/n9jt/n5nLR19y0/Gges9fLL2utS" )

    response = s3_client.generate_presigned_post(
        Bucket='imageneschavo',
        key=imagen,
        ExpiresIn=10
    )

    files={'file':open(imagen, 'rb')}
    r=requests.post(response['url'],data=response['fields'],files=files)
    print(r.status_code)

cargarImagen()
