import pandas as pd
import tweepy as tw
from sqlalchemy import create_engine
import os
import logging
from datetime import datetime
import pymysql


def conexaotweet():
    consumer_key= 'Sg6ASDPot7uYbmXQ3ksqIvd5N'
    consumer_secret = 's7nlTBSUeWYmWpL42b9X7feMnLhfZjlpDomhTB3PakY40XlxfP'
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAC4ofgEAAAAA6cha%2B5oOuOPRzEI2ska58Pvpqsc%3DAAM5eMGMWZjcbplPfhEMwdRKgQU8UPUt8rftEqaw7EUnSZfSbD'
    acess_token = '1487773725034520585-laR8tyP0HOdpNvG4f2vesCBsgM3jy4'
    acess_token_secret= 'KFUBFfpte6Zmp2rbYdCKgiq7YEgjgjbbhe9nRQLTCWvWT'

    cliente = tw.Client(bearer_token, consumer_key, consumer_secret, acess_token, acess_token_secret)

    return cliente


def retornar_tweet(resposta):

    tweets= resposta.search_recent_tweets(query='Bolsonario', max_results=100)

    dados = tweets.data

    return dados

def tratamento(dados):
    id = [] 
    texto= [] 
    rt = []

    for dado in dados:
        id.append(dado.id)
        texto.append(dado.text)

    for i in texto:
        if (i[:2]) == 'RT':
            RT = 'retweet'
        else:
            RT = 'tweet'
        rt.append(RT)

    df = pd.DataFrame(list(zip(id, texto, rt)),columns= ['ID', 'Texto', 'tipo'])
    df['scrapy_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    return df


def conexao(df):
    mysql = create_engine('mysql+pymysql://wrweb301_well:well1003@wrweb.net.br/wrweb301_olist')
    df.to_sql('tweets', con=mysql, if_exists= 'append', index=False)



if __name__ == '__main__':

    path = '/home/wellington/Documentos/'
    logging.basicConfig(
        filename= path + 'Logs/tweets.log',
        level = logging.DEBUG,
        format= '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt= '%Y-%m-%d %H:%M:%S',)

    logger = logging.getLogger('tweets')

    
    resposta = conexaotweet()
    logger.info('Conexao com Tweets')

    dados = retornar_tweet(resposta)
    logger.info('Baixando os Tweets')

    df = tratamento(dados)
    logger.info('Criação da Tabela')

    conexao(df)
    logger.info('Carregado com sucesso no Banco de dados')