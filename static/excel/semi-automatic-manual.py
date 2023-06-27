big_string = ""
queryable_fields = ['Nro Orc', 'Nome / Razão Cliente', 'Estagio Produção']
queryable_fields_index = [0,1]

def organize():
    big_list = big_string.split('\n')
    for row in big_list:
        index = 0
        values = []
        campos = row.split('\t')
        for campo in campos:
            if queryable_fields_index.__contains__(index):
                values.append(campo)
            index = index + 1
            print(campos)
        print(values)

organize()