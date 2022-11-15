
### Pré-requisitos:
- Recomendado `python v3.10.0` ou mais recente.

### Instalação:
- Clone o repositório principal para acessar todos os arquivos e versões de dependência
- Use `python -m venv venv` para criar um ambiente virtual
- Ative o ambiente virtual:
  - [LINUX]   -> `.\venv\bin\activate`
  - [WINDOWS] -> `.\venv\Scripts\activate`

- Use `pip install -r .\requirements.txt ` para instalar as bibliotecas necessárias


### Informações:
- Para realização deste teste foi populado um banco com alguns dados de partidas de Counter Strike para um banco de dados (MYSQL), use as seguintes credenciais para acessar estes dados.\
LOGIN= “candidato”\
SENHA = ‘’********”\
HOST = '***********'\
SCHEMA = 'CSGO'

### Objetivos:
- Escreva um script em python que consuma cada uma das tabelas no schema e transforme-as em dataframes, ao transforma-los podemos notar que as colunas dos dataframes estão nomeadas no padrão camel case, passe-as para snake case.

- Faça uma query em SQL que retorne uma tabela com Id do player, taxa de vitória e número de partidas dos jogadores que tiverem acima de 10 partidas, selecione os jogadores com as 50 maiores taxas de vitória.

- Uma das métricas para medir o desempenho do jogador é o rating “K/D” que consiste no número de eliminações realizadas dividido pelo número de vezes que o jogador foi eliminado, Faça uma query em SQL e selecione o id do player, país de origem, idade e rating kd.
