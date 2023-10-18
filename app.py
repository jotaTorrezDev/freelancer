#ler dados da planilha
# inserir cada célula de cada linha em um campo do sistema
import openpyxl

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)