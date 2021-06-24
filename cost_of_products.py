
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

    tax = input["tax"]
    margin = input["margin"]
    products_list = []
    total_price = 0

    for dict in input["products"]:
        net_cost = dict["net_cost"]
        price = net_cost*(margin+1)*(tax+1)
        first_tax = net_cost*(margin+1)*tax
        second_tax = price*tax

        dict.update({"price": price})

        new_dict = {
            key: round(value+(second_tax-first_tax), 2)
            if key is "price"
            else value for key, value in
                    dict.items()}

        total_price += new_dict["price"]
        new_dict.pop("net_cost")
        products_list.append(new_dict)

    output = {"products": products_list, "total_price": round(total_price, 2)}

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

