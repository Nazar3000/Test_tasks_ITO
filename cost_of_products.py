
input={
"products": [
{
"id": 1,
"title": "Product 1",
"net_cost": 100
},
{
"id": 2,
"title": "Product 2",
"net_cost": 200
}
],
"tax": 0.1,
"margin": 0.2
}



def new_prises(input):

    tax = input["tax"]+1
    margin = input["margin"]+1
    products_list=[]
    total_price = 0

    for dict in input["products"]:
        dict.update({"price": dict["net_cost"]})
        new_dict = {key: value*margin*tax if key is "price" else value for key, value in
                    dict.items()}
        new_dict.pop("title")
        total_price += new_dict["price"]
        new_dict.pop("net_cost")
        products_list.append(new_dict)

    output= {"products": products_list, "total_price": total_price }

    print(output)
    return output


new_prises(input)



# Output={
# "products": [
# {
# "id": 0,
# "title": "string",
# "price": 0
# }
# ],
# "total_price": 0
# }

