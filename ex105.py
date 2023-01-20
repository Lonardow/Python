
def notas(*num, sit=False):
    """função para analisar notas e situações de vários alunos

    Args:
        sit (bool, optional): informa situação do aluno baseado na média. Defaults to False.

    Returns:
        _type_: retorna dicionario com notas medias e situação do aluno
    """
    dic = dict()
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['media'] = (sum(num)/len(num))
    if sit:
        if dic['media'] >= 7.0:
            dic['Situação'] = 'BOA'
        elif dic['media'] >= 6.0:
            dic['Situação'] = 'Razoavel'
        else:
            dic['Situação'] = 'RUIM'

    return dic


print(notas(5, 4, 5, 5.5, sit=True))
