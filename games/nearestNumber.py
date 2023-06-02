
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

def validation(guess_one: str, guess_two: str) -> str:
    """ Faz a validação dos campos utilizados para o jogo nearest number.
    
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

    if(guess_one == None or guess_two == None):
        return "Preencha os campos!"

    try:
        guess_one_int = int(guess_one)
        guess_two_int = int(guess_two)
    except:
        return "Erro! Devem ser informados somente números inteiros."

    if(guess_one_int < 0 or guess_two_int < 0):
        return "Não são permitidos números negativos!"

    if(guess_one_int == guess_two_int):
        return "Escolham números diferentes!"

    if(guess_one_int > 20 or guess_two_int > 20):
        return "O palpite máximo é 20!"

    return None