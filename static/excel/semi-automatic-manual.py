big_string = """Nro Orc	Situação	Nome / Razão Cliente	Vlr.	Vendedor	Vlr.Faturado	Saldo Faturar	Dt.Cadastro	Dt.Prev.Entrega	Fone	Celular	No.Ped. Temp.	Fone 2	Endereco	Nro.Casa	Bairro	UF	Cidade	Cod Ref.	Confi. Temp.	Dt.Venda	Dt.Fatur.	Email	Estagio Produção	Markup Total	Data Cancelado	Motivo Cancelamento	Motivo de Cancelamento	Entregue em:	Dt.Aprovação Cliente	Dt.Garantia Perfis	Dt.Garantia Acessorios	Dt.Garantia Serviços	Dt.Garantia Vidro	Cliente Codigo	Como Conheceu	Complemento	Dt.Validade
20173	FATURADO	JAPA VIDROS	433,68	STEFANE CRISTINA	433,68	0	27/06/2023		(12)98823-8283      	(12)98823-8283      	0	(12)98823-8283      	AV. ADEMAR PEREIRA DE BARROS, 712 - STA MARIA/JACAREI	712	JARDIM SANTA MARIA	SP	JACAREI		Não Enviado	27/06/2023	27/06/2023			0										2272			
20172	FATURADO	IN VITRO SOLUCOES EM VIDROS.	145	STEFANE CRISTINA	145	0	27/06/2023		(12)3308-9116       		0		R. MARIA APARECIDA DO CARMO SILVA, N° 25	'-	 RES CALIFÓRNIA	SP	SAO JOSE DOS CAMPOS		Não Enviado	27/06/2023	27/06/2023	financeiro@invitrosolucoes.com.br		0										36			
20160	FATURADO	JEFFERSON CUNHADO 	50,48	STEFANE CRISTINA	50,48	0	26/06/2023		                    	(12)9408-4211       	0	                    				SP	SAO JOSE DOS CAMPOS		Não Enviado	26/06/2023	26/06/2023		PRODUÇÃO	0										335			
20159	FATURADO	COMERCIAL ANDRADE MAT CONSTRUÇÃO	0,06	STEFANE CRISTINA	0,06	0	26/06/2023		(12)3929-2988       	(12)94404-0295      	0		RUA JOSÉ ALVES DE PAIVA, N°777	'-	JARDIM SANTA INÊS	SP	SAO JOSE DOS CAMPOS		Não Enviado	26/06/2023	26/06/2023		PRODUÇÃO	0										1937			"""



queryable_fields = ['Nro Orc', 'Nome / Razão Cliente', 'Vendedor', 'Estagio Produção']
queryable_database_fields = ['id', 'client', 'seller', 'is_ready', 'destiny']
queryable_fields_index = []




def organize():
    big_list = big_string.split('\n')

    first_row = big_list.pop(0)
    for index, field in enumerate(first_row.split('\t')):
        if field in queryable_fields:
            queryable_fields_index.append(index)
    values_list = []  # Lista para armazenar os valores de todas as linhas
    for row in big_list:
        index = 0
        values = []
        campos = row.split('\t')
        for campo in campos:
            if queryable_fields_index.__contains__(index):
                values.append(campo)
            index = index + 1
        values_list.append(values)

    query_values = []
    for values in values_list:
        query_values.append("({})".format(', '.join(["'{}'".format(value) for value in values])))

    # Concatenar todos os valores em uma única query
    query = "INSERT INTO tabela ({}) VALUES {};".format(', '.join(queryable_fields), ', '.join(query_values))
    print(query)
organize()