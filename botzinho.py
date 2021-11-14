#Importando todas as bibliotecas que iremos precisar
from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import tweepy
import time 
import schedule
from datetime import datetime 

#Informando as chaves de acesso à API do Twitter (obviamente não as colocarei aqui por se tratar de dados sensíveis)
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Autenticação no twitter com as chaves de acesso
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#Aqui crio a função principal que fará a mágica acontecer
def TweetDolar ():
    
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    #Faço a requisição de uma página do google com a cotação do dólar e a armazeno nas variáveis depois de tratar os dados
    page = requests.get('https://www.google.com/search?q=dolar', headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    #Aqui o BeautifulSoup procura dentro do HTML da página a span que armazena o valor do dólar pela classe especificada
    valor_dolar = soup.find_all('span', class_ = 'DFlfde SwHCTb')

    #Mrmazeno o valor do dólar extraído com o BeautifulSoup na variável de saida já com a mensagem pronta para o Tweet
    saida = 'O valor do dólar neste momento é R$' + (valor_dolar[0].get_text())

    #Mando a ordem para a API do Twitter fazer a publicação do tweet com o valor guardado dentro da variável
    api.update_status(saida) 

    #Mensagem básica para o terminal me avisar através de uma mensagem simples quando a função tiver sido executada
    horah = (datetime.now().time().strftime('%H:%M:%S'))
    print('Dólar executado com sucesso às', horah, 'HRs.')
    
#A função está pronta, mas necessita de uma ordem para ser executada. O Schedule fará isso no horário especificado, que neste caso são 18:00 HRs.
schedule.every().day.at("18:00").do(TweetDolar)

#Para que a função seja executada todos os dias no mesmo horário, crio um While que irá sempre executar as schedules que estiverem pendentes
while 1:
    schedule.run_pending()
    time.sleep(1)


#Este foi o meu primeiro projeto em Python. 
#Na base de muita pesquisa na internet, estudo de documentações e tutoriais de funções isoladas, consegui um Alpha do bot que já executava o básico (printar a cotação do dólar) em menos de 5 horas.
#Antes de 8 horas trabalhando consegui implementar o restante (mandar a cotação do dólar para o Twitter).
#Para que o bot trabalhe 24/7, sem que o computador esteja ligado e o executando, é necessário uma hospedagem de computação em Nuvem. Irei utilizar o Heroku.
#Sinta-se livre para utilizar este código ou partes dele em seus projetos.

#Para ver o bot em ação, acesse o link : https://twitter.com/pastelfarialima

#Futuras alterações relevantes serão enviadas para o repositório. O código usado para o bot que será colocado no ar será mais bem humorado :-)
