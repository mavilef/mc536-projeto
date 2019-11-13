doc = open("./hospital.csv", "r")
xml_doc = open("./hospital2.xml", "w")

def convert(a):
    try:
        int(a)
        return a
    except:
        return "0"
    

doc2 = doc.read().splitlines()

doc3 = []
for x in doc2:
    doc3.append(x.split(","))

ind_facility_id = doc3[0].index("Facility ID")
ind_facility_name = doc3[0].index("Facility Name")
ind_city = doc3[0].index("City")
ind_state = doc3[0].index("State")
ind_hosp_rat = doc3[0].index("Hospital overall rating")
ind_mortality = doc3[0].index("Mortality national comparison")
ind_safety = doc3[0].index("Safety of care national comparison")
ind_readmission = doc3[0].index("Readmission national comparison")
ind_patient = doc3[0].index("Patient experience national comparison")
ind_effectiveness = doc3[0].index("Effectiveness of care national comparison")
ind_timeliness = doc3[0].index("Timeliness of care national comparison")
ind_imaging = doc3[0].index("Efficient use of medical imaging national comparison")

dic = dict()

for estado_ind in range(len(doc3)):
    if estado_ind == 0:
        continue
    estado = doc3[estado_ind][ind_state]
    cidade = doc3[estado_ind][ind_city]
    if estado not in dic:
        dic[estado] = dict()
    if cidade not in dic[estado]: 
        dic[estado][cidade] = []
    dic[estado][cidade].append(doc3[estado_ind])

xml = ""

xml += '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<estados>\n'
for x in dic:
    xml += '\t<estado nome="{estado}">\n'.format(estado=x.replace('"', '').replace("&", "&amp;")) 
    xml += '\t\t<cidades>\n'
    for y in dic[x]:
        xml += '\t\t\t<cidade nome="{cidade}">\n'.format(cidade=y.replace('"', '').replace("&", "&amp;") )
        xml += '\t\t\t\t<hospitais>'
        for z in dic[x][y]:
            xml += '''
\t\t\t\t\t<hospital id="{facility_id}">
\t\t\t\t\t\t<facility_name>"{facility_name}"</facility_name>
\t\t\t\t\t\t<hospital_rating>{hosp_rat}</hospital_rating>
\t\t\t\t\t\t<mortality>"{mortality}"</mortality>
\t\t\t\t\t\t<safety>"{safety}"</safety>
\t\t\t\t\t\t<readmission>"{readmission}"</readmission>
\t\t\t\t\t\t<patient_experience>"{patient}"</patient_experience>
\t\t\t\t\t\t<effectiveness>"{effectiveness}"</effectiveness>
\t\t\t\t\t\t<timeliness_rate>"{timeliness}"</timeliness_rate>
\t\t\t\t\t\t<imaging_rate>"{imaging}"</imaging_rate>
\t\t\t\t\t</hospital>
'''.format(
                                facility_id=z[ind_facility_id].replace("&", "&amp;").replace('"', ''), 
                                facility_name=z[ind_facility_name].replace("&", "&amp;").replace('"', ''), 
                                hosp_rat=convert(z[ind_hosp_rat].replace("&", "&amp;").replace('"', '')),
                                mortality=z[ind_mortality].replace("&", "&amp;").replace('"', ''),
                                safety=z[ind_safety].replace("&", "&amp;").replace('"', ''),
                                readmission=z[ind_readmission].replace("&", "&amp;").replace('"', ''),
                                patient=z[ind_patient].replace("&", "&amp;").replace('"', ''),
                                effectiveness=z[ind_effectiveness].replace("&", "&amp;").replace('"', ''),
                                timeliness=z[ind_timeliness].replace("&", "&amp;").replace('"', ''),
                                imaging=z[ind_imaging].replace("&", "&amp;").replace('"', '')
                            )
        xml += '\t\t\t\t</hospitais>\n'
        xml += '\t\t\t</cidade>\n'
    xml += '\t\t</cidades>\n'
    xml += '\t</estado>\n'
xml += '</estados>'

xml_doc.write(xml) 
xml_doc.close()