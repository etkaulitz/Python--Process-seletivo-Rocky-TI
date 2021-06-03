import json
from operator import itemgetter

#função responsável por ler o Json
def read_json():
    with open('broken-database.json', 'r', encoding="utf8") as f:
        return json.load(f)


#função responsável por arrumar o nome
def reverse_name(data):
    for i in range(len(data)):
        data[i]['name'] = data[i]['name'].replace('æ', 'a').replace('ß', 'b').replace('¢', 'c').replace('ø', 'o')
    print('Arrumando nome: ')
    print(data)
    print()
    return data


#função responsável por alterar preço de String para Float
def convert_price(data):
    for i in range(len(data)):
        data[i]['price'] = float(data[i]['price'])
    print ('Arrumando valor: ')
    print(data)
    print()
    return data


#verifica se não tem o campo 'quantity', caso não tenha é acrescentado o campo com valor 0
def add_quantity(data):
    for i in range(len(data)):
        if not ('quantity' in data[i]):
            data[i] = {
                'id': data[i]['id'],
                'name': data[i]['name'],
                'quantity': 0,
                'price': data[i]['price'],
                'category': data[i]['category']
            }
    print('Arrumando quantidade: ')
    print(data)
    print()
    return data


#função que salva os dados atualizados em um Json
def save_json(data):
    with open('saida.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data



#função cria lista para armazenar os campos necessários
def category_ordering(data):
    for i in range(len(data)):
        list_category = list()
        list_name = list()
        list_id = list()

        list_category.append(data[i]['category'])
        list_name.append(data[i]['name'])
        list_id.append((data[i]['id']))

#ordenado por categoria
        category_ord = sorted(data, key=itemgetter('category'))

    print()
    print('Listando nomes ordenados de acordo com ordem alfabética da categoria: ')
    print()
    for i in range(len(category_ord)):
        category_name = category_ord[i]
        for i in range(len(category_name['name'])):
            list_names = list()
            list_names.append(category_name['name'])
        print(list_names)
            

#ordenado por id de forma crescente
    id_ordering = sorted(data, key=itemgetter('id'))
    print()
    print('Listando nomes ordenados de acordo com id em ordem crescente: ')
    print()

    for i in range(len(id_ordering)):
        names = id_ordering[i]
        for i in range(len(names['name'])):
            list_names = list()
            list_names.append(names['name'])
        print(list_names)
    return data


#função que soma o total dos produtos de acordo com a categoria
def qtd_tot(data):
    category = list()
    qtd_total = list()
    for i in range(len(data)):
        if data[i]['category'] in category:
            qtd = data[i]['price'] * data[i]['quantity']
            qtd_total[category.index(data[i]['category'])] = qtd_total[category.index(data[i]['category'])] + qtd
        else:
            category.append(data[i]['category'])
            qtd_total.append(data[i]['price'] * data[i]['quantity'])

    print()
    print('Quantidade total separada por categoria: ')
    for i in range(len(category)):  
        print(category[i], ':', qtd_total[i])
            

#função principal chamando todas as funções
def main():
    data = read_json()
    dados = reverse_name(data)
    convert = convert_price(data)
    add = add_quantity(data)
    jsonSave = save_json(data)
    result = category_ordering(data)
    totCategory = qtd_tot(data)

main()

