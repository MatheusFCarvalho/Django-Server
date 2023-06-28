import re
input_data = """Nro Orc	Situação	Nome / Razão Cliente	Vlr.	Vendedor	Vlr.Faturado	Saldo Faturar	Dt.Cadastro	Dt.Prev.Entrega	Fone	Celular	No.Ped. Temp.	Fone 2	Endereco	Nro.Casa	Bairro	UF	Cidade	Cod Ref.	Confi. Temp.	Dt.Venda	Dt.Fatur.	Email	Estagio Produção	Markup Total	Data Cancelado	Motivo Cancelamento
20197	FATURADO	 VEZZANO MOVEIS E DESIGN	224	VALTER NETO	224	0	27/06/2023		(12)99131-7139      	(12)99714-3299      	0		RUA ANTÔNIO DE DEUS ANDRADE - 290	290	JARDIM BARONESA	SP	TAUBATE		Não Enviado	27/06/2023	27/06/2023			0		
20194	FATURADO	AUTENTIC MOVELARIA	197,49	STEFANE CRISTINA	197,49	0	27/06/2023		(12)98806-7652      		0		RUA ALCIDES SALGADO	162	CAMPOS DE SÃO JOSÉ	SP	SAO JOSE DOS CAMPOS		Não Enviado	27/06/2023	27/06/2023		PRODUÇÃO	0		
20193	FATURADO	FAGUNDES AMBIENTES PLANEJADOS	528,24	MICHELLE BOSCHETTI	528,24	0	27/06/2023		(12)3917-8091       	(12)99739-8655      	0		 RUA FIALHO 	111	JARDIM SANTA LUCIA	SP	SAO JOSE DOS CAMPOS		Não Enviado	27/06/2023	27/06/2023	marcenariafagundes2015@hotmail.com	PRODUÇÃO	0		
"""
# id_list =[ 19996,19995]
# client_list = [ "MC MIQUEIAS" ,"MARCENARIA MAGNIFICA ALEXANDRE" ]
# seller_list = [""]
# est_prod = ["RETIRADO", "PRODUÇÃO"]

# data = {id_list:id_list, client_list:client_list, est_prod:est_prod}



def extract_data(input_str):
    lines = input_str.strip().split('\n')
    headers = lines[0].split('\t')
    data = [line.split('\t') for line in lines[1:]]

    id_list = []
    client_list = []
    seller_list = []
    est_prod = []

    for row in data:
        id_list.append(int(row[0]))
        client_list.append(row[2])
        seller_list.append(row[4])
        est_prod.append(row[23])

    return {
        'id_list': id_list,
        'client_list': client_list,
        'seller_list': seller_list,
        'est_prod': est_prod
    }


# print(output)

def seller_name_to_id(stringo):
    obj = {'LUCIANA ROCHA': 3, 'STEFANE CRISTINA': 2, 'MICHELLE BOSCHETTI': 5, 'VALTER NETO': 4, 'TATIANE BROCKYELD': 6}
    return obj.get(stringo, None)


def criar_query_insercao(data_extracted):
    print(data_extracted)
    id_list = data_extracted['id_list']
    client_list = data_extracted['client_list']
    seller_list = data_extracted['seller_list']
    est_prod = data_extracted['est_prod']
    # id_list = data.id_list
    # client_list = data.client_list
    # est_prod = data.est_prod

    if len(id_list) != len(client_list) or len(id_list) != len(est_prod) or len(id_list) != len(seller_list):
        raise ValueError("Os arrays devem ter o mesmo tamanho.")
    
    valores = []
    
    for i in range(len(id_list)):
        id = id_list[i]
        client = client_list[i]
        estage = est_prod[i]
        seller_id = seller_name_to_id(seller_list[i])

        if estage == 'PRODUÇÃO' or estage == '':
            is_ready = False
            destiny = 'Nao informado'
        elif estage == 'EXPEDIÇÃO - ENTREGA':
            is_ready = True
            destiny = 'Entrega'
        elif estage == 'EXPEDIÇÃO - RETIRA':
            is_ready = True
            destiny = 'Retira'
        else:
            is_ready = True
            destiny = 'Nao informado'
        

        valores.append(f"('{id}', '{client}', '{seller_id}', '{is_ready}', '{destiny}')")

    query = f"INSERT INTO order_order (id, client, seller_id, is_ready, destiny) VALUES {', '.join(valores)};"
    
    return query

# print(criar_query_insercao(id_list,client_list,est_prod, 'order_order'))

def write_query_to_file(query, file_path):
    with open(file_path, 'w') as file:
        file.write(query)
    print(f"Arquivo '{file_path}' criado com sucesso.")

# Exemplo de uso

formated_data = extract_data(input_data)
query = criar_query_insercao(formated_data)
write_query_to_file(query,'static/querys/poppoco.sql')