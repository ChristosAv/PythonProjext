


#H synartisi ayth pairnei san orisma tin arxiki timh enos proiontos kai ypologizei to fpa toy kai sth synexeia ta apo8ikeuei se mia lista
#pou periexei mono tin kathari axia twn proiontwn.
def shopping_list(y): #(a:)allazw tin vallue me tin y.
    synoliki_axia = 0
    synoliki_VAT = 0
    axia = y/1.24
    synoliki_axia += axia
    value.append(axia) #prosthetei stin lista value tin timh toy proitnos apallagmeno apo to fpa
    VAT = y - axia
    synoliki_VAT += VAT
    print("Total cost of VAT: ",synoliki_VAT,".")
    print("Total cost of products: ",synoliki_axia,".")

#orizw 2 metablhtes typoy listas. Mia gia ton xaraktirismo twn proiontwn. Mia gia tin axia tous
#Se mia while loop dinw to dikaioma ston xristi na epilegei posa proionta 8a pros8esei sthn lista
product = []
value = []
Answer = "y"
while Answer == "y" :
    x = input("Add to cart.")
    y = float(input("It costs: "))
    shopping_list(y) #(a:)allazw tin vallue me tin y
    product.append(x)
    #value.append(y)
    Answer = input("Are there items to be added in the shopping list? Answer with y for yes or n for no :")
    

kalathi = {'item': product, 'price': value}
print(kalathi)
