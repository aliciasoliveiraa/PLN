#Aula3

import re

# group 1 - (.*) - este apanha as palavras iniciais
# group 2 - (\n.+) - apanha cada uma das linhas das descrições sucessivamente
# group 3 - ((\n.+)+) - junta todas as linhas do grupo anterior
# como tem três grupos de captura, o resultado vai ter uma lista de tuplos com 3 partes
# o ?: serve para silenciar o grupo de captura 2 porque ele ajuda-me a ir buscar as descrições corretas mas eu não quero imprimir

# 3 capture group -> \n\n(.+)((\n.+)+) 
    #1 (.+)  para termos
    #2 (\n.+) para as descrições 
    #3 ((\n.+)+) para a descrição total mas marcamos este com ?: para o silenciar, ou seja, nao o guarda
    
file = open("dicionario_medico.txt", encoding= "utf-8")
text = file.read()
entries = re.findall(r"\n\n(.+)((?:\n.+)+)", text)
#print(entries[10])

remove_ff = re.sub(r"\f", "", text) # Retirar \f do documento (FF - form feed (FFvermelho))
mark_designations = re.sub(r"\n\n(.+)", r"\n\n#T=\1", remove_ff) # Mark with #T (term) the designations
mark_descriptions = re.sub(r"\n([^#\s].+)", r"\n#E=\1", mark_designations) # Mark with #E (explication) the descriptions
descriptions = re.sub(r"(#T=.+)\n\n#T=(.+)", r"\1\n#E=\2", mark_descriptions) # Remove \n between designation and description
remove_new_lines = re.sub(r"(#E=.+)(?:\n#E=(.+))+", r"\1 \2", descriptions) # Remove new lines
remove_marks = re.sub(r"#[TE]=", r"", remove_new_lines) # Remove marks #T and #E
new_entries = re.findall(r"\n\n(.+)\n(.+)", remove_marks)

file.close()
    
html = open("dicionario_medico.html", "w", encoding='utf-8')

header = '''<html>
<head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #E0FFFF;
}
</style>
<met charset = 'utf-8'/>
</head>
<body>
<h1> Medical dictionary </h1>           
<p>This document is used to support medical diagnosis. The document consists of designations and their descriptions.</p> 
'''

list_dic=list(new_entries)
list_dic.insert(0,("Designation", "Description"))

# Create the HTML table
table = "<table frame='hsides' bgcolor='B0E0E6'>\n"
for i, row in enumerate(list_dic):
    table += "<tr>"
    for j, item in enumerate(row):
        if i == 0: # if first row, add bold style
            table += "<th style='font-weight:bold'>{}</th>".format(item)
        else:
            table += "<td>{}</td>".format(item)
    table += "</tr>\n"
table += "</table>"


footer = '''</body>
</html>
'''

html.write(header+table+footer)


html.close()