def display_best_portfolio(portfolio):
    print(f"\nLe meilleur portefeuille trouvé : \n \nComposition: \n \n{portfolio} \nPour un prix total de {portfolio.price} \nPour un profit total de {portfolio.profit}")


def display_best_branch(branch):
    composition = ""
    for action in branch.composition:
        composition += f"{action} \n"
    print(f"\nLe meilleur portefeuille trouvé : \n \nComposition: \n \n{composition} \nPour un prix total de {branch.price} \nPour un profit total de {branch.net_profit}")
