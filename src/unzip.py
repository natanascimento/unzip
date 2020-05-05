import os, zipfile, datetime 
import schedule, time

def zipando():
    directory = "C:\\dev\\CiscoDevNet\\learninglabs\\Meraki\\BIC\\testzip"
    ex = ".zip"

    os.chdir(directory)

    currentDt = datetime.datetime.now()

    for item in os.listdir(directory):
        if item.endswith(ex):
            filename = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(filename)
            zip_ref.extractall(directory)
            zip_ref.close()
            os.remove(filename)
            print("Extração concluido em ", currentDt.strftime("%d-%m-%Y %H:%M:%S"))

zipando()
#schedule para verificação de novos arquivos no diretório (opcional)
schedule.every(15).seconds.do(zipando)

while 1:
    schedule.run_pending()
    time.sleep(1)