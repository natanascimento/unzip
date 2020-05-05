import os, zipfile, datetime 
import schedule, time

def zipando():
    #Diretório onde os arquivos se encontram
    directory = "C:\\dev\\unzip\\src\\test"
    extension = ".zip"

    os.chdir(directory)
    
    #Captando a hora exata
    currentDt = datetime.datetime.now()

    for item in os.listdir(directory):
        if item.endswith(extension):
            filename = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(filename)
            #Extraindo todos os arquivos com base no diretorio
            zip_ref.extractall(directory)
            zip_ref.close()
            #Removendo os arquivos originais do diretório
            os.remove(filename)
            print("Extração concluido em ", currentDt.strftime("%d-%m-%Y %H:%M:%S"))

zipando()
#schedule para verificação de novos arquivos no diretório (opcional)
schedule.every(15).seconds.do(zipando)

while 1:
    schedule.run_pending()
    time.sleep(1)