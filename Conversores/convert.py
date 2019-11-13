doc = open("./doctor.csv", "r")
#hosp = open("./hospital.csv", "r")
xml_doc = open("./doctor_final.xml", "w")
#xml_hosp = open("./hospital_mini.xml", "w")

# def find_ind(lista, name):
#     for x in range(len(lista)):
#         if lista[x] == name:
#             return x
    

doc2 = doc.read().splitlines()

doc3 = []
for x in doc2:
    doc3.append(x.split(","))


#print (doc3[0])

ind_NPI = doc3[0].index("NPI")
ind_first_name = doc3[0].index("First Name")
ind_middle_name = doc3[0].index("Middle Name")
ind_last_name = doc3[0].index("Last Name")
ind_primary_speciality = doc3[0].index("Primary specialty")
ind_city = doc3[0].index("City")
ind_state = doc3[0].index("State")
ind_hospital_name1 = doc3[0].index("Hospital affiliation LBN 1")
ind_hospital_name2 = doc3[0].index("Hospital affiliation LBN 2")


dic = dict()
for especialidade_ind in range(len(doc3)):
    if especialidade_ind == 0:
        continue
    especialidade = doc3[especialidade_ind][ind_primary_speciality]
    if especialidade not in dic:
        dic[especialidade] = []
    dic[especialidade].append(doc3[especialidade_ind])

xml = ""

xml += '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<especialidades>\n'
for x in dic:
    xml += '\t<especialidade nome="{especialidade}">\n'.format(especialidade=x.replace('"', ''))
    xml += '\t\t<medicos>'
    aux = ""
    for y in dic[x]:
        if y[ind_NPI] != aux:
            aux = y[ind_NPI]
            xml += '''
\t\t\t<medico id="{NPI}">
\t\t\t\t<primeiro_nome>"{first_name}"</primeiro_nome>
\t\t\t\t<segundo_nome>"{middle_name}"</segundo_nome>
\t\t\t\t<terceiro_nome>"{last_name}"</terceiro_nome>
\t\t\t\t<cidade>"{city}"</cidade>
\t\t\t\t<estado>"{state}"</estado>
\t\t\t\t<hospital1>"{hospital_name1}"</hospital1>
\t\t\t\t<hospital2>"{hospital_name2}"</hospital2>
\t\t\t</medico>
'''.format  (
            NPI=y[ind_NPI].replace("&", "&amp;").replace('"', ''), 
            first_name=y[ind_first_name].replace("&", "&amp;").replace('"', ''), 
            middle_name=y[ind_middle_name].replace("&", "&amp;").replace('"', ''),
            last_name=y[ind_last_name].replace("&", "&amp;").replace('"', ''),
            city=y[ind_city].replace("&", "&amp;").replace('"', ''),
            state=y[ind_state].replace("&", "&amp;").replace('"', ''),
            hospital_name1=y[ind_hospital_name1].replace("&", "&amp;").replace('"', ''),
            hospital_name2=y[ind_hospital_name2]
            )
    xml += '\t\t</medicos>\n'
    xml += '\t</especialidade>\n'
xml += '</especialidades>'

xml_doc.write(xml) 
xml_doc.close()

        






#RESTON HOSPITAL CENTER
#CJW MEDICAL CENTER
#EMERGENCY MEDICINE ASSOCIATES PA PC


#State , Organization legal name




