# 7. Tente adicionar a cor "laranja" à tupla "cores" e observe o resultado. Explique o motivo pelo qual ocorreu um erro fazendo um comentário no código.
cores.append("laranja");

print("Cores: ", cores);
print();

""" RESULTADO (TERMINAL):

AttributeError: 'tuple' object has no attribute 'append'

    MOTIVO: Porque objeto "tupla" não tem um método "append()" para adicionar os elementos, por isso é imutável! 

"""