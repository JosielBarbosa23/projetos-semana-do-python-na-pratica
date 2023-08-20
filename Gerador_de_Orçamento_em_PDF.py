#Entrada de dados do orçamento;

projeto = input('Digite a descrição do projeto: ')
horas_estimadas = input('Informe o total de horas estimadas: ')
valor_hora = input('Digite o valor da hora trabalhada: ')
prazo = input('Informe o prazo estimado: ')

total_orcamento = int(horas_estimadas) * int(valor_hora)
print(total_orcamento)

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
#Colocar um template em toda extensao por isso x e y é 0;
pdf.image("template.png", x= 0, y = 0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
#Converter o total para texto;
pdf.text(115, 205, str(total_orcamento))

#Salvando e criando o arquivo;
pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
