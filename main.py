groceries = {}
cate = ["diary_products", "meat_products", "snacks", "grains"]


while True:
    print("Menu:\n\n1.Add\n2.Remove\n3.View\n4.Exit")

    op = int(input("Choose an option:"))
    if op == 1:
        # add screen
        print("\nIn which of the below categories you want to add?")
        for i, k in enumerate(cate):
            print(str(i + 1) + "." + k)
        print (str(i+2)+"."+"add_category")
        add_op = int(input("Choose an option:"))
        if add_op==(i+2):
           new_cat= input("Enter the name of the category:")
           cate.append(new_cat)
        else:
            print(
                "What "
                + cate[add_op - 1].replace("_", " ").removesuffix("s")
                + " you want to add?\n"
            )
            item =list(map(str,input("Enter your items:").split()))
            if cate[add_op - 1] in groceries:
                temp = groceries[cate[add_op - 1]]
                temp.extend(item)
                groceries[cate[add_op - 1]] = temp
                del temp
            else:
                groceries[cate[add_op - 1]] = item

    if op == 2:
        # remove screen
        items = []
        for key in  groceries:
            for item in groceries[key]:
                items.append((key, item))
        
        if len(items) == 0:
            print("\nThere are no items to remove")
        else:
            print("\nWhat all do you want to remove?")
        for idx, item in enumerate(items):
            print(f"{idx+1}.{item[1]}")
        if len(items) != 0:
             print(idx+2,'.'+'remove all', sep="")
              
        item_no = list(map(int, input().split()))
        for idx, item in enumerate(items):
            if idx+1 in item_no:
                temp = groceries[item[0]]
                temp.remove(item[1])
                groceries[item[0]] = temp
        if idx+2 == item_no[0]:
            groceries.clear()
            

    if op == 3:
        # view screen
        print(groceries)
    if op == 4:
        break
