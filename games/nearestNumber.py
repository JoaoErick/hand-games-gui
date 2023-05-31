
def nearest_number(guess_one: int, guess_two: int, value: int) -> str:
    """ Indica qual jogador chegou mais próximo do valor informado.

    Parameters
    ----------
    guess_one: :class:`int`
        Palpite do jogador 1.
    guess_two: :class:`int`
        Palpite do jogador 2.
    value: :class:`int`
        Valor a ser comparado.

    Returns
    -------
    :class:`str`
    """

    result_1: int = abs(value - guess_one)
    result_2: int = abs(value - guess_two)

    if(result_1 < result_2):
        return "Jogador 1 venceu!"
    elif(result_1 > result_2):
        return "Jogador 2 venceu!"

    return "Empate"