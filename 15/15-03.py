def take_large_banknotes(banknotes):
    if banknotes == []:
        return ['Вы выиграли']
    return list(filter(lambda banknotes: banknotes > 10, banknotes))
