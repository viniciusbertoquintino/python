import requests
from bs4 import BeautifulSoup

def obter_resultados_mega_sena():
    url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        resultados = []

        # Encontrar a tabela de resultados
        tabela_resultados = soup.find("table", class_="simple-table")
        
        # Iterar sobre as linhas da tabela
        for linha in tabela_resultados.find_all("tr")[1:]:
            colunas = linha.find_all("td")
            concurso = colunas[0].text.strip()
            numeros = [numero.text.strip() for numero in colunas[1:7]]
            resultado = {"Concurso": concurso, "Numeros": numeros}
            resultados.append(resultado)

        return resultados
    else:
        print("Erro ao obter dados do site da Caixa.")
        return None

# Exemplo de uso
resultados = obter_resultados_mega_sena()

if resultados:
    for resultado in resultados:
        print(f"Concurso: {resultado['Concurso']}, Números: {', '.join(resultado['Numeros'])}")
