#pip install mysql-connector-python
import mysql.connector
import pandas as pd
import re
from datetime import datetime, date
from openpyxl.workbook import Workbook


cnx = mysql.connector.connect(user='candidato', password='analista_atmo',
                              host='atmo-db.cncfsgdjnfjz.sa-east-1.rds.amazonaws.com',
                              database='CSGO')

query_1 = "select * from tb_lobby_stats_player"
df_lobby = pd.read_sql(query_1, cnx)

query_2 = "select * from tb_medalha"
df_med = pd.read_sql(query_2, cnx)

query_3 = "select * from tb_players"
df_player = pd.read_sql(query_3, cnx)

query_4 = "select * from tb_players_medalha"
df_plamedalha = pd.read_sql(query_3, cnx)


def camel(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower().replace(" ","")


def col_correct(dataframe):
    x = len(dataframe.columns)
    cont = 0
    while cont <= x-1:
        dados_col = dataframe.columns.values[cont]
        dataframe.columns.values[cont] = dados_col.replace(dados_col,camel(dados_col))
        cont += 1
    return dataframe


dfs = [df_lobby, df_med, df_player, df_plamedalha]

for i in dfs:
    col_correct(i)

query_lobby = "select idPlayer, count(idPlayer) as QTD_Partidas from tb_lobby_stats_player tlsp group by idPlayer "
df_qlobby = pd.read_sql(query_lobby,cnx)

query_vict = "select idPlayer , count(idPlayer) as QTD_Vitorias from tb_lobby_stats_player tlsp where flWinner = 1 group by idPlayer "
df_query = pd.read_sql(query_vict,cnx)

df_merge = pd.merge(df_qlobby, df_query, on=['idPlayer'], how='left')

df_merge['Win Rate'] = round(df_merge['QTD_Vitorias'] / df_merge['QTD_Partidas'], 2)

df_trat = df_merge.query('QTD_Partidas > 10')
df_trat.sort_values(by='Win Rate', ascending=False, inplace=True)

df_final = df_trat.head(50)
df_final = df_final.reset_index(drop=True)

query_plr = "select idPlayer,descCountry ,dtBirth  from tb_players"
df_plr = pd.read_sql(query_plr,cnx)
df_plr['dtBirth'] = pd.to_datetime(df_plr['dtBirth']).dt.strftime('%d/%m/%Y')

query_kd = "select idPlayer,sum(qtKill) / sum(qtDeath) as KD from tb_lobby_stats_player tlsp group by idPlayer"
df_kd = pd.read_sql(query_kd,cnx)

df_status = pd.merge(df_plr, df_kd, on=['idPlayer'], how='left')


def age(born):
    born = datetime.strptime(born, "%d/%m/%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month,
                                      today.day) < (born.month,
                                                    born.day))


df_st_tratado = df_status.copy()
df_st_tratado = df_st_tratado.dropna()
df_st_tratado['Idade'] = df_st_tratado['dtBirth'].apply(age)

col_correct(df_final)
col_correct(df_status)
col_correct(df_st_tratado)

df_final.to_excel("exercicio_2.xlsx", index=False)
df_status.to_excel("dados.xlsx")
df_st_tratado.to_excel("exercicio_3.xlsx", index=False)