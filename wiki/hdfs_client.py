"""
from hdfs import InsecureClient
client = InsecureClient('http://localhost:9870', user='Drach', timeout=10)
try:
    #client.makedirs('/carpeta_1')
    #client.makedirs('/carpeta_2')
    print(client.write('/carpeta_1',data='./carpeta_1/Documento_1.txt'))
    print(client.list('/home'))
except Exception as e:
    print(f"Error: {e}")
"""
from pywebhdfs.webhdfs import PyWebHdfsClient

client = PyWebHdfsClient(host='localhost',port='9000')

client.create_file('/carpeta_1',"file_data")
