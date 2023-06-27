id_list =[ 19996,19995]
client_list = [ "MC MIQUEIAS" ,"MARCENARIA MAGNIFICA ALEXANDRE" ]

est_prod = ["RETIRADO", "PRODUÇÃO"]

# data = {id_list:id_list, client_list:client_list, est_prod:est_prod}

def criar_query_insercao(arr_id, arr_name, arr_est, tabela):
    # arr_id = data.id_list
    # arr_name = data.client_list
    # arr_est = data.est_prod

    if len(arr_id) != len(arr_name) or len(arr_id) != len(arr_est):
        raise ValueError("Os arrays devem ter o mesmo tamanho.")
    
    valores = []
    
    for i in range(len(arr_id)):
        id = arr_id[i]
        client = arr_name[i]
        estage = arr_est[i]
        if estage == 'PRODUÇÃO' or estage == '':
            is_ready = False
            destiny = 'Não informado'
        elif estage == 'EXPEDIÇÃO - ENTREGA':
            is_ready = True
            destiny = 'Entrega'
        elif estage == 'EXPEDIÇÃO - RETIRA':
            is_ready = True
            destiny = 'Retira'
        else:
            is_ready = True
            destiny = 'Não informado'
        
        valores.append(f"('{id}', '{client}', '{is_ready}', '{destiny}')")

    query = f"INSERT INTO {tabela} (id, client, is_ready, destiny) VALUES {', '.join(valores)};"
    
    return query

print(criar_query_insercao(id_list,client_list,est_prod, 'order_order'))