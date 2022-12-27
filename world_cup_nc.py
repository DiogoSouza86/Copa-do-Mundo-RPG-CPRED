from random import choice, randint, choices

import unidecode as unidecode


def pontos():
    for c in range(1,4):
        if i[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            f_gols = choices(gols, weights=[0.5, 20.5, 25, 25, 10, 10])

        if i[c] in times_fracos:
            gols = [0, 1, 2, 3, 4, 5]
            f_gols = choices(gols, weights=[40, 30, 10, 10, 0.5, 0.5])

        if i[c] in times_medios:
            gols = [0, 1, 2, 3, 4, 5]
            f_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])

        return f_gols


def pontos2():
    for c in range(0, 4):
        if i[c] in (times_fortes) and i[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[0.5, 20.5, 25, 25, 10, 10])
            return ff_gols

        if i[c] in (times_fortes) and i[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols

        if i[c] in (times_fortes) and i[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols

        if i[c] in (times_medios) and i[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols
        if i[c] in (times_medios) and i[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols
        if i[c] in (times_medios) and i[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[10, 40, 30, 10, 10])
            return ff_gols

        if i[c] in (times_fracos) and i[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[40.5, 30, 10, 0.5, 0.5, 0.5])
            return ff_gols

        if i[c] in (times_fracos) and i[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 10, 10, 10, 0.5, 0.5])
            return ff_gols

        if i[c] in (times_fracos) and i[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30,30,20,10,0.5,0.5])
            return ff_gols


def pontos3(chave):
    for c in range(0, 4):
        if chave[c] in (times_fortes) and chave[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[0.5, 20.5, 25, 25, 10, 10])
            return ff_gols

        if chave[c] in (times_fortes) and chave[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols

        if chave[c] in (times_fortes) and chave[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols

        if chave[c] in (times_medios) and chave[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols
        if chave[c] in (times_medios) and chave[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
            return ff_gols
        if chave[c] in (times_medios) and chave[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[10, 40, 30, 10, 10])
            return ff_gols

        if chave[c] in (times_fracos) and chave[c] in (times_fortes):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[40.5, 30, 10, 0.5, 0.5, 0.5])
            return ff_gols

        if chave[c] in (times_fracos) and chave[c] in (times_medios):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30, 30, 10, 10, 10, 0.5, 0.5])
            return ff_gols

        if chave[c] in (times_fracos) and chave[c] in (times_fracos):
            gols = [0, 1, 2, 3, 4, 5]
            ff_gols = choices(gols, weights=[30,30,20,10,0.5,0.5])
            return ff_gols


def pontos4(time1, time2):
    if time1 in (times_fortes) and time2 in (times_fracos):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[0.5, 20.5, 25, 25, 10, 10])
        return ff_gols
    if time1 in (times_fortes) and time2 in (times_medios):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
        return ff_gols
    if time1 in (times_fortes) and time2 in (times_fortes):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
        return ff_gols

    if time1 in (times_medios) and time2 in (times_fortes):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
        return ff_gols
    if time1 in (times_medios) and time2 in (times_medios):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
        return ff_gols
    if time1 in (times_medios) and time2 in (times_fracos):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[10, 30, 30, 10, 10,10])
        return ff_gols

    if time1 in (times_fracos) and time2 in (times_fortes):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[40.5, 30, 10, 0.5, 0.5, 0.5])
        return ff_gols
    if time1 in (times_fracos) and time2 in (times_medios):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 10, 10, 10, 10])
        return ff_gols
    if time1 in (times_fracos) and time2 in (times_fracos):
        gols = [0, 1, 2, 3, 4, 5]
        ff_gols = choices(gols, weights=[30, 30, 20, 10, 0.5, 0.5])
        return ff_gols


def localizar(time):
    f = ''
    if time not in lista_oitavas:
        f = f'{time} foi eliminada na fase de grupos'
    elif time not in lista_quartas:
        f = f'{time} foi eliminada nas oitavas'
    elif time not in lista_semi_final:
        f =f'{time} foi eliminada nas quartas'
    elif time not in lista_final_terceiro and time not in lista_final:
        f = f'{time} foi eliminada na semi-final'
    return f


def salvar_titulo(txt):
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'\n{txt}\n')
    a.close()


def salvar_resultado(t1 , p1, t2, p2):
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{t1} {p1} X {p2} {t2}\n')
    a.close()


cup = ["França","Inglaterra", "Brasil", "Nigth City"]
w_cup = []
world_cup = []
lista_chave = []
tabela = {}
lista_tabela = []
sorteados = []

arquivo = open("paises.txt", encoding='utf-8', mode='r')
linha = []
for l in arquivo:
    l = l.strip()
    linha.append(l)
arquivo.close()

while len(w_cup)<32:
    cup.append(choice(linha))
    for e in cup:
        if e not in w_cup:
            w_cup.append(e)

# remove os acentos e adiciona ao self
for i in range(len(w_cup)):
    w_cup[i] = unidecode.unidecode(w_cup[i])
    world_cup.append(w_cup[i])

time1 = open('copa_do_mundo.txt', 'w', encoding='utf-8')
time1.write(f'{"TIMES CLASSIFICADOS"}\n\n')
time1.close()

for t in sorted(w_cup):
    time1 = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    time1.write(f'>{t}\n')
    time1.close()

for c in range(1, 9):
    tabela.clear()
    lista_chave.clear()
    while len(lista_chave) <= 3:
        time = choice(w_cup)
        if time not in sorteados:
            if time not in lista_chave:
                lista_chave.append(time)
                sorteados.append(time)
        else:
            continue

    tabela["Chave"] = lista_chave[:]
    lista_tabela.append(tabela.copy())

print(f'{"COPA DO MUNDO DE NIGHT CITY":^30}')
print('Sorteando...')
#sleep(2)
print(f'{len(w_cup)} times clasificados foram:\n{sorted(world_cup)}')

print()

times_fracos = []
times_medios = []
times_fortes = ["Nigth City"]
for f in w_cup:
    if f != "Nigth City":
        roll = randint(1,5)
        if roll == 1:
            times_fracos.append(f)
        elif roll == 4:
            times_fortes.append(f)
        else:
            times_medios.append(f)

print()
print(f'Times fracos:\n{sorted(times_fracos)}')
print(f'Times médios:\n{sorted(times_medios)}')
print(f'Times fortes:\n{sorted(times_fortes)}')

ff = open('copa_do_mundo.txt', 'a', encoding='utf-8')
print(f'\nTimes fracos: {sorted(times_fracos)}\nTimes médios{sorted(times_medios)}\nTimes fortes{sorted(times_fortes)}', file=ff)
ff.close()

time1 = open('copa_do_mundo.txt', 'a', encoding='utf-8')
time1.write(f'\n{"---TABELAS"}\n\n')
time1.close()

print(f'\n{"---CHAVES"}\n')
chave_a = []
chave_b = []
chave_c = []
chave_d = []
chave_e = []
chave_f = []
chave_g = []
chave_h = []
sorteados_chave = []

while len(chave_a) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_a:
            chave_a.append(time)
            sorteados_chave.append(time)

while len(chave_b) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_b:
            chave_b.append(time)
            sorteados_chave.append(time)

while len(chave_c) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_c:
            chave_c.append(time)
            sorteados_chave.append(time)

while len(chave_d) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_d:
            chave_d.append(time)
            sorteados_chave.append(time)
while len(chave_e) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_e:
            chave_e.append(time)
            sorteados_chave.append(time)

while len(chave_f) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_f:
            chave_f.append(time)
            sorteados_chave.append(time)

while len(chave_g) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_g:
            chave_g.append(time)
            sorteados_chave.append(time)

while len(chave_h) <= 3:
    time = choice(w_cup)
    if time not in sorteados_chave:
        if time not in chave_h:
            chave_h.append(time)
            sorteados_chave.append(time)

chaves_salva = open('copa_do_mundo.txt', 'a', encoding='utf-8')
chaves_salva.write(f'{"Chave A"}\n{chave_a}\n'
                   f'{"Chave B"}\n{chave_b}\n'
                   f'{"Chave C"}\n{chave_c}\n'
                   f'{"Chave D"}\n{chave_d}\n'
                   f'{"Chave E"}\n{chave_e}\n'
                   f'{"Chave F"}\n{chave_f}\n'
                   f'{"Chave G"}\n{chave_g}\n'
                   f'{"Chave H"}\n{chave_h}\n\n')
chaves_salva.close()

print(f'Chave A - {chave_a}')
print(f'Chave B - {chave_b}')
print(f'Chave C - {chave_c}')
print(f'Chave D - {chave_d}')
print(f'Chave E - {chave_e}')
print(f'Chave F - {chave_f}')
print(f'Chave G - {chave_g}')
print(f'Chave H - {chave_h}')
#Bibliotecas
#chave A biblios
biblio_chave_a_zero = {}
lista_pontos_zero = []
biblio_chave_a_um = {}
lista_pontos_um = []
biblio_chave_a_dois = {}
lista_pontos_dois = []
biblio_chave_a_tres = {}
lista_pontos_tres = []

#chave B biblios
biblio_chave_b_zero = {}
lista_pontos_b_zero = []
biblio_chave_b_um = {}
lista_pontos_b_um = []
biblio_chave_b_dois = {}
lista_pontos_b_dois = []
biblio_chave_b_tres = {}
lista_pontos_b_tres = []

#chave C biblios
biblio_chave_c_zero = {}
lista_pontos_c_zero = []
biblio_chave_c_um = {}
lista_pontos_c_um = []
biblio_chave_c_dois = {}
lista_pontos_c_dois = []
biblio_chave_c_tres = {}
lista_pontos_c_tres = []

#chave D biblios
biblio_chave_d_zero = {}
lista_pontos_d_zero = []
biblio_chave_d_um = {}
lista_pontos_d_um = []
biblio_chave_d_dois = {}
lista_pontos_d_dois = []
biblio_chave_d_tres = {}
lista_pontos_d_tres = []

#Chave E biblios
biblio_chave_e_zero = {}
lista_pontos_e_zero = []
biblio_chave_e_um = {}
lista_pontos_e_um = []
biblio_chave_e_dois = {}
lista_pontos_e_dois = []
biblio_chave_e_tres = {}
lista_pontos_e_tres = []

#chave F biblios
biblio_chave_f_zero = {}
lista_pontos_f_zero = []
biblio_chave_f_um = {}
lista_pontos_f_um = []
biblio_chave_f_dois = {}
lista_pontos_f_dois = []
biblio_chave_f_tres = {}
lista_pontos_f_tres = []

#chave G biblios
biblio_chave_g_zero = {}
lista_pontos_g_zero = []
biblio_chave_g_um = {}
lista_pontos_g_um = []
biblio_chave_g_dois = {}
lista_pontos_g_dois = []
biblio_chave_g_tres = {}
lista_pontos_g_tres = []

#chave H biblios
biblio_chave_h_zero = {}
lista_pontos_h_zero = []
biblio_chave_h_um = {}
lista_pontos_h_um = []
biblio_chave_h_dois = {}
lista_pontos_h_dois = []
biblio_chave_h_tres = {}
lista_pontos_h_tres = []

#saldo de gols
#chave A saldo de gols
chave_a_zero_gols = []
chave_a_zero_gols_sofridos = []
chave_a_um_gols = []
chave_a_um_gols_sofridos = []
chave_a_dois_gols = []
chave_a_dois_gols_sofridos = []
chave_a_tres_gols = []
chave_a_tres_gols_sofridos = []

#chave B saldo de gols
chave_b_zero_gols = []
chave_b_zero_gols_sofridos = []
chave_b_um_gols = []
chave_b_um_gols_sofridos = []
chave_b_dois_gols = []
chave_b_dois_gols_sofridos = []
chave_b_tres_gols = []
chave_b_tres_gols_sofridos = []

#Chave C saldo de gols
chave_c_zero_gols = []
chave_c_zero_gols_sofridos = []
chave_c_um_gols = []
chave_c_um_gols_sofridos = []
chave_c_dois_gols = []
chave_c_dois_gols_sofridos = []
chave_c_tres_gols = []
chave_c_tres_gols_sofridos = []

#chave D saldo de gols
chave_d_zero_gols = []
chave_d_zero_gols_sofridos = []
chave_d_um_gols = []
chave_d_um_gols_sofridos = []
chave_d_dois_gols = []
chave_d_dois_gols_sofridos = []
chave_d_tres_gols = []
chave_d_tres_gols_sofridos = []

#Chave E saldo de gols
chave_e_zero_gols = []
chave_e_zero_gols_sofridos = []
chave_e_um_gols = []
chave_e_um_gols_sofridos = []
chave_e_dois_gols = []
chave_e_dois_gols_sofridos = []
chave_e_tres_gols = []
chave_e_tres_gols_sofridos = []

#chave F saldo de gols
chave_f_zero_gols = []
chave_f_zero_gols_sofridos = []
chave_f_um_gols = []
chave_f_um_gols_sofridos = []
chave_f_dois_gols = []
chave_f_dois_gols_sofridos = []
chave_f_tres_gols = []
chave_f_tres_gols_sofridos = []

#chave G saldo de gols
chave_g_zero_gols = []
chave_g_zero_gols_sofridos = []
chave_g_um_gols = []
chave_g_um_gols_sofridos = []
chave_g_dois_gols = []
chave_g_dois_gols_sofridos = []
chave_g_tres_gols = []
chave_g_tres_gols_sofridos = []

#chave H saldo de gols
chave_h_zero_gols = []
chave_h_zero_gols_sofridos = []
chave_h_um_gols = []
chave_h_um_gols_sofridos = []
chave_h_dois_gols = []
chave_h_dois_gols_sofridos = []
chave_h_tres_gols = []
chave_h_tres_gols_sofridos = []

print(f'\n{"TABELA FASE DE GRUPOS":^60}\n\n{"PRIMEIRA RODADA - GRUPO A"}')

a0 = pontos4(chave_a[0], chave_a[1])
a1 = pontos4(chave_a[1], chave_a[0])
print(f'{chave_a[0]:<15} {a0}X {a1} {chave_a[1]:>15}')
if a0 > a1:
    biblio_chave_a_zero["Seleção"] = chave_a[0]
    lista_pontos_zero.append(3)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    biblio_chave_a_um["Seleção"]= chave_a[1]
    lista_pontos_um.append(0)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
elif a0 == a1:
    biblio_chave_a_zero["Seleção"] = chave_a[0]
    lista_pontos_zero.append(1)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    biblio_chave_a_um["Seleção"] = chave_a[1]
    lista_pontos_um.append(1)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
else:
    biblio_chave_a_zero["Seleção"] = chave_a[0]
    lista_pontos_zero.append(0)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    biblio_chave_a_um["Seleção"] = chave_a[1]
    lista_pontos_um.append(3)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
chave_a_zero_gols.append(a0)
chave_a_zero_gols_sofridos.append(a1)
chave_a_um_gols.append(a1)
chave_a_um_gols_sofridos.append(a0)
salvar_titulo("Primeira Rodada - Grupo A")
salvar_resultado(chave_a[0], a0, chave_a[1], a1)

a2 = pontos4(chave_a[2], chave_a[3])
a3 = pontos4(chave_a[3], chave_a[2])
print(f'{chave_a[2]:<15} {a2}X {a3} {chave_a[3]:>15}')
if a2 > a3:
    biblio_chave_a_dois["Seleção"] = chave_a[2]
    lista_pontos_dois.append(3)
    biblio_chave_a_dois["Pontos"] = lista_pontos_zero[:]
    biblio_chave_a_tres["Seleção"]= chave_a[3]
    lista_pontos_tres.append(0)
    biblio_chave_a_tres["Pontos"] = lista_pontos_um[:]
elif a2 == a3:
    biblio_chave_a_dois["Seleção"] = chave_a[2]
    lista_pontos_dois.append(1)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
    biblio_chave_a_tres["Seleção"] = chave_a[3]
    lista_pontos_tres.append(1)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
else:
    biblio_chave_a_dois["Seleção"] = chave_a[2]
    lista_pontos_dois.append(0)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
    biblio_chave_a_tres["Seleção"] = chave_a[3]
    lista_pontos_tres.append(3)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
chave_a_dois_gols.append(a2)
chave_a_dois_gols_sofridos.append(a3)
chave_a_tres_gols.append(a3)
chave_a_tres_gols_sofridos.append(a2)
salvar_resultado(chave_a[2], a2, chave_a[3], a3)


a4 = pontos4(chave_a[1], chave_a[2])
a5 = pontos4(chave_a[2], chave_a[1])
print(f'\n{"SEGUNDA RODADA - GRUPO A"}')
print(f'{chave_a[1]:<15} {a4}X {a5} {chave_a[2]:>15}')
if a4 > a5:
    lista_pontos_um.append(3)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
    lista_pontos_dois.append(0)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
elif a4 == a5:
    lista_pontos_um.append(1)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
    lista_pontos_dois.append(1)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
else:
    lista_pontos_um.append(0)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
    lista_pontos_dois.append(3)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
chave_a_um_gols.append(a4)
chave_a_um_gols_sofridos.append(a5)
chave_a_dois_gols.append(a5)
chave_a_dois_gols_sofridos.append(a4)
salvar_titulo("SEGUNDA RODADA - GRUPO A")
salvar_resultado(chave_a[1], a4, chave_a[2], a5)

a6 = pontos4(chave_a[3], chave_a[0])
a7 = pontos4(chave_a[0], chave_a[3])
print(f'{chave_a[3]:<15} {a6}X {a7} {chave_a[0]:>15}')
if a6 > a7:
    lista_pontos_tres.append(3)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
    lista_pontos_zero.append(0)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
elif a6 == a7:
    lista_pontos_tres.append(1)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
    lista_pontos_zero.append(1)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
else:
    lista_pontos_tres.append(0)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
    lista_pontos_zero.append(3)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
chave_a_zero_gols.append(a7)
chave_a_zero_gols_sofridos.append(a6)
chave_a_tres_gols.append(a6)
chave_a_tres_gols_sofridos.append(a7)
salvar_resultado(chave_a[3], a6, chave_a[0], a7)

print(f'\n{"TERCEIRA RODADA - GRUPO A"}')
a8 = pontos4(chave_a[1], chave_a[3])
a9 = pontos4(chave_a[3], chave_a[1])
print(f'{chave_a[1]:<15} {a8} X {a9} {chave_a[3]:>15}')
if a8 > a9:
    lista_pontos_um.append(3)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
    lista_pontos_tres.append(0)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
elif a8 == a9:
    lista_pontos_tres.append(1)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
    lista_pontos_um.append(1)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
else:
    lista_pontos_um.append(0)
    biblio_chave_a_um["Pontos"] = lista_pontos_um[:]
    lista_pontos_tres.append(3)
    biblio_chave_a_tres["Pontos"] = lista_pontos_tres[:]
chave_a_um_gols.append(a8)
chave_a_um_gols_sofridos.append(a9)
chave_a_tres_gols.append(a9)
chave_a_tres_gols_sofridos.append(a8)
salvar_titulo("TERCEIRA RODADA - GRUPO A")
salvar_resultado(chave_a[1], a8, chave_a[3], a9)

a10 = pontos4(chave_a[0], chave_a[2])
a11= pontos4(chave_a[2], chave_a[0])
print(f'{chave_a[0]:<15} {a10} X {a11} {chave_a[2]:>15}')
if a10 > a11:
    lista_pontos_zero.append(3)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    lista_pontos_dois.append(0)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
elif a10 == a11:
    lista_pontos_zero.append(1)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    lista_pontos_dois.append(1)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
else:
    lista_pontos_zero.append(0)
    biblio_chave_a_zero["Pontos"] = lista_pontos_zero[:]
    lista_pontos_dois.append(3)
    biblio_chave_a_dois["Pontos"] = lista_pontos_dois[:]
chave_a_zero_gols.append(a10)
chave_a_zero_gols_sofridos.append(a11)
chave_a_dois_gols.append(a11)
chave_a_dois_gols_sofridos.append(a10)
salvar_resultado(chave_a[0], a10, chave_a[2], a11)

print(f'\n{"PRIMEIRA RODADA - GRUPO B"}')
b0 = pontos4(chave_b[0], chave_b[1])
b1 = pontos4(chave_b[1], chave_b[0])
print(f'{chave_b[0]:<15} {b0}X {b1} {chave_b[1]:>15}')
if b0 > b1:
    biblio_chave_b_zero["Seleção"] = chave_b[0]
    lista_pontos_b_zero.append(3)
    biblio_chave_b_um["Seleção"] = chave_b[1]
    lista_pontos_b_um.append(0)
elif b0 == b1:
    biblio_chave_b_zero["Seleção"] = chave_b[0]
    lista_pontos_b_zero.append(1)
    biblio_chave_b_um["Seleção"] = chave_b[1]
    lista_pontos_b_um.append(1)
else:
    biblio_chave_b_zero["Seleção"] = chave_b[0]
    lista_pontos_b_zero.append(0)
    biblio_chave_b_um["Seleção"] = chave_b[1]
    lista_pontos_b_um.append(3)
chave_b_zero_gols.append(b0)
chave_b_zero_gols_sofridos.append(b1)
chave_b_um_gols.append(b1)
chave_b_um_gols_sofridos.append(b0)
salvar_titulo("PRIMEIRA RODADA - GRUPO B")
salvar_resultado(chave_b[0],b0, chave_b[1], b1)

b2 = pontos4(chave_b[2], chave_b[3])
b3 = pontos4(chave_b[3], chave_b[2])
print(f'{chave_b[2]:<15} {b2}X {b3} {chave_b[3]:>15}')
if b2 > b3:
    biblio_chave_b_dois["Seleção"] = chave_b[2]
    lista_pontos_b_dois.append(3)
    biblio_chave_b_tres["Seleção"] = chave_b[3]
    lista_pontos_b_tres.append(0)
elif b2 == b3:
    biblio_chave_b_dois["Seleção"] = chave_b[2]
    lista_pontos_b_dois.append(1)
    biblio_chave_b_tres["Seleção"] = chave_b[3]
    lista_pontos_b_tres.append(1)
else:
    biblio_chave_b_dois["Seleção"] = chave_b[2]
    lista_pontos_b_dois.append(0)
    biblio_chave_b_tres["Seleção"] = chave_b[3]
    lista_pontos_b_tres.append(3)
chave_b_dois_gols.append(b2)
chave_b_dois_gols_sofridos.append(b3)
chave_b_tres_gols.append(b3)
chave_b_tres_gols_sofridos.append(b2)
salvar_resultado(chave_b[2],b2, chave_b[3], b3)

b4 = pontos4(chave_b[1], chave_b[2])
b5 = pontos4(chave_b[2], chave_b[1])
print(f'\n{"SEGUNDA RODADA - GRUPO B"}')
print(f'{chave_b[1]:<15} {b4}X {b5} {chave_b[2]:>15}')
if b4 > b5:
    lista_pontos_b_um.append(3)
    lista_pontos_b_dois.append(0)
elif b4 == b5:
    lista_pontos_b_um.append(1)
    lista_pontos_b_dois.append(1)
else:
    lista_pontos_b_um.append(0)
    lista_pontos_b_dois.append(3)
chave_b_um_gols.append(b4)
chave_b_um_gols_sofridos.append(b5)
chave_b_dois_gols.append(b5)
chave_b_dois_gols_sofridos.append(b4)
salvar_titulo("SEGUNDA RODADA - GRUPO B")
salvar_resultado(chave_b[1],b4, chave_b[2], b5)

b6 = pontos4(chave_b[3], chave_b[0])
b7 = pontos4(chave_b[0], chave_b[3])
print(f'{chave_b[3]:<15} {b6}X {b7} {chave_b[0]:>15}')
if b6 > b7:
    lista_pontos_b_tres.append(3)
    lista_pontos_b_zero.append(0)
elif b6 == b7:
    lista_pontos_b_tres.append(1)
    lista_pontos_zero.append(1)
else:
    lista_pontos_tres.append(0)
    lista_pontos_zero.append(3)
    chave_b_zero_gols.append(b7)
chave_b_zero_gols_sofridos.append(b6)
chave_a_tres_gols.append(b6)
chave_a_tres_gols_sofridos.append(b7)
salvar_resultado(chave_b[3],b6, chave_b[0], b7)

print(f'\n{"TERCEIRA RODADA - GRUPO B"}')
b8 = pontos4(chave_b[1], chave_b[3])
b9 = pontos4(chave_b[3], chave_b[1])
print(f'{chave_b[1]:<15} {b8} X {b9} {chave_b[3]:>15}')
if b8 > b9:
    lista_pontos_b_um.append(3)
    lista_pontos_b_tres.append(0)
elif b8 == b9:
    lista_pontos_b_tres.append(1)
    lista_pontos_b_um.append(1)
else:
    lista_pontos_b_um.append(0)
    lista_pontos_b_tres.append(3)
chave_b_um_gols.append(b8)
chave_b_um_gols_sofridos.append(b9)
chave_a_tres_gols.append(b9)
chave_a_tres_gols_sofridos.append(b8)
salvar_titulo("TERCEIRA RODADA - GRUPO B")
salvar_resultado(chave_b[1],b8, chave_b[3], b9)

b10 = pontos4(chave_b[0], chave_b[2])
b11= pontos4(chave_b[2], chave_b[0])
print(f'{chave_b[0]:<15} {b10} X {b11} {chave_b[2]:>15}')
if b10 > b11:
    lista_pontos_b_zero.append(3)
    lista_pontos_b_dois.append(0)
elif b10 == b11:
    lista_pontos_b_zero.append(1)
    lista_pontos_b_dois.append(1)
else:
    lista_pontos_b_zero.append(0)
    lista_pontos_b_dois.append(3)
chave_b_zero_gols.append(b10)
chave_b_zero_gols_sofridos.append(b11)
chave_b_dois_gols.append(b11)
chave_b_dois_gols_sofridos.append(b10)
salvar_resultado(chave_b[0],b10, chave_b[2], b11)

print(f'\n{"PRIMEIRA RODADA - GRUPO C"}')
c0 = pontos4(chave_c[0], chave_c[1])
c1 = pontos4(chave_c[1], chave_c[0])
print(f'{chave_c[0]:<15} {c0}X {c1} {chave_c[1]:>15}')
if c0 > c1:
    biblio_chave_c_zero["Seleção"] = chave_c[0]
    lista_pontos_c_zero.append(3)
    biblio_chave_c_um["Seleção"]= chave_c[1]
    lista_pontos_c_um.append(0)
elif c0 == c1:
    biblio_chave_c_zero["Seleção"] = chave_c[0]
    lista_pontos_c_zero.append(1)
    biblio_chave_c_um["Seleção"] = chave_c[1]
    lista_pontos_c_um.append(1)
else:
    biblio_chave_c_zero["Seleção"] = chave_c[0]
    lista_pontos_c_zero.append(0)
    biblio_chave_c_um["Seleção"] = chave_c[1]
    lista_pontos_c_um.append(3)
chave_c_zero_gols.append(c0)
chave_c_zero_gols_sofridos.append(c1)
chave_c_um_gols.append(c1)
chave_c_um_gols_sofridos.append(c0)
salvar_titulo("PRIMEIRA RODADA - GRUPO C")
salvar_resultado(chave_c[0],c0, chave_c[1], c1)

c2 = pontos4(chave_c[2], chave_c[3])
c3 = pontos4(chave_c[3], chave_c[2])
print(f'{chave_c[2]:<15} {c2}X {c3} {chave_c[3]:>15}')
if c2 > c3:
    biblio_chave_c_dois["Seleção"] = chave_c[2]
    lista_pontos_c_dois.append(3)
    biblio_chave_c_tres["Seleção"]= chave_c[3]
    lista_pontos_c_tres.append(0)
elif c2 == c3:
    biblio_chave_c_dois["Seleção"] = chave_c[2]
    lista_pontos_c_dois.append(1)
    biblio_chave_c_tres["Seleção"] = chave_c[3]
    lista_pontos_c_tres.append(1)
else:
    biblio_chave_c_dois["Seleção"] = chave_c[2]
    lista_pontos_c_dois.append(0)
    biblio_chave_c_tres["Seleção"] = chave_c[3]
    lista_pontos_c_tres.append(3)
chave_c_dois_gols.append(c2)
chave_c_dois_gols_sofridos.append(c3)
chave_c_tres_gols.append(c3)
chave_c_tres_gols_sofridos.append(c2)
salvar_resultado(chave_c[2],c2, chave_c[3], c3)

c4 = pontos4(chave_c[1], chave_c[2])
c5 = pontos4(chave_c[2], chave_c[1])
print(f'\n{"SEGUNDA RODADA - GRUPO C"}')
print(f'{chave_c[1]:<15} {c4}X {c5} {chave_c[2]:>15}')
if c4 > c5:
    lista_pontos_c_um.append(3)
    lista_pontos_c_dois.append(0)
elif c4 == c5:
    lista_pontos_c_um.append(1)
    lista_pontos_c_dois.append(1)
else:
    lista_pontos_c_um.append(0)
    biblio_chave_c_um["Pontos"] = lista_pontos_c_um[:]
    lista_pontos_c_dois.append(3)
    biblio_chave_c_dois["Pontos"] = lista_pontos_c_dois[:]
chave_c_um_gols.append(c4)
chave_c_um_gols_sofridos.append(c5)
chave_c_dois_gols.append(c5)
chave_c_dois_gols_sofridos.append(c4)
salvar_titulo("SEGUNDA RODADA - GRUPO C")
salvar_resultado(chave_c[1],c4, chave_c[2], c5)

c6 = pontos4(chave_c[3], chave_c[0])
c7 = pontos4(chave_c[0], chave_c[3])
print(f'{chave_c[3]:<15} {c6}X {c7} {chave_c[0]:>15}')
if c6 > c7:
    lista_pontos_c_tres.append(3)
    lista_pontos_c_zero.append(0)
elif c6 == c7:
    lista_pontos_c_tres.append(1)
    lista_pontos_c_zero.append(1)
else:
    lista_pontos_c_tres.append(0)
    lista_pontos_c_zero.append(3)
chave_c_zero_gols.append(c7)
chave_c_zero_gols_sofridos.append(c6)
chave_c_tres_gols.append(c6)
chave_c_tres_gols_sofridos.append(c7)
salvar_resultado(chave_c[3],c6, chave_c[0], c7)

print(f'\n{"TERCEIRA RODADA - GRUPO C"}')
c8 = pontos4(chave_c[1], chave_c[3])
c9 = pontos4(chave_c[3], chave_c[1])
print(f'{chave_c[1]:<15} {c8} X {c9} {chave_c[3]:>15}')
if c8 > c9:
    lista_pontos_c_um.append(3)
    lista_pontos_c_tres.append(0)
elif c8 == c9:
    lista_pontos_c_tres.append(1)
    lista_pontos_c_um.append(1)
else:
    lista_pontos_c_um.append(0)
    lista_pontos_c_tres.append(3)
chave_c_um_gols.append(c8)
chave_c_um_gols_sofridos.append(c9)
chave_c_tres_gols.append(c9)
chave_c_tres_gols_sofridos.append(c8)
salvar_titulo("TERCEIRA RODADA - GRUPO C")
salvar_resultado(chave_c[1],c8, chave_c[3], c9)

c10 = pontos4(chave_c[0], chave_c[2])
c11 = pontos4(chave_c[2], chave_c[0])
print(f'{chave_c[0]:<15} {c10} X {c11} {chave_c[2]:>15}')
if c10 > c11:
    lista_pontos_c_zero.append(3)
    lista_pontos_c_dois.append(0)
elif c10 == c11:
    lista_pontos_c_zero.append(1)
    lista_pontos_c_dois.append(1)
else:
    lista_pontos_c_zero.append(0)
    lista_pontos_c_dois.append(3)
chave_c_zero_gols.append(c10)
chave_c_zero_gols_sofridos.append(c11)
chave_c_dois_gols.append(c11)
chave_c_dois_gols_sofridos.append(c10)
salvar_resultado(chave_c[0],c10, chave_c[2], c11)

print(f'\n{"PRIMEIRA RODADA - GRUPO D"}')
d0 = pontos4(chave_d[0], chave_d[1])
d1 = pontos4(chave_d[1], chave_d[0])
print(f'{chave_d[0]:<15} {d0}X {d1} {chave_d[1]:>15}')
if d0 > d1:
    biblio_chave_d_zero["Seleção"] = chave_d[0]
    lista_pontos_d_zero.append(3)
    biblio_chave_d_um["Seleção"]= chave_d[1]
    lista_pontos_d_um.append(0)
elif d0 == d1:
    biblio_chave_d_zero["Seleção"] = chave_d[0]
    lista_pontos_d_zero.append(1)
    biblio_chave_d_um["Seleção"] = chave_d[1]
    lista_pontos_d_um.append(1)
else:
    biblio_chave_d_zero["Seleção"] = chave_d[0]
    lista_pontos_d_zero.append(0)
    biblio_chave_d_um["Seleção"] = chave_d[1]
    lista_pontos_d_um.append(3)
chave_d_zero_gols.append(d0)
chave_d_zero_gols_sofridos.append(d1)
chave_d_um_gols.append(d1)
chave_d_um_gols_sofridos.append(d0)
salvar_titulo("PRIMEIRA RODADA - GRUPO D")
salvar_resultado(chave_d[0],d0, chave_d[1], d1)

d2 = pontos4(chave_d[2], chave_d[3])
d3 = pontos4(chave_d[3], chave_d[2])
print(f'{chave_d[2]:<15} {d2}X {d3} {chave_d[3]:>15}')
if d2 > d3:
    biblio_chave_d_dois["Seleção"] = chave_d[2]
    lista_pontos_d_dois.append(3)
    biblio_chave_d_tres["Seleção"]= chave_d[3]
    lista_pontos_d_tres.append(0)
elif d2 == d3:
    biblio_chave_d_dois["Seleção"] = chave_d[2]
    lista_pontos_d_dois.append(1)
    biblio_chave_d_tres["Seleção"] = chave_d[3]
    lista_pontos_d_tres.append(1)
else:
    biblio_chave_d_dois["Seleção"] = chave_d[2]
    lista_pontos_d_dois.append(0)
    biblio_chave_d_tres["Seleção"] = chave_d[3]
    lista_pontos_d_tres.append(3)
chave_d_dois_gols.append(d2)
chave_d_dois_gols_sofridos.append(d3)
chave_d_tres_gols.append(d3)
chave_d_tres_gols_sofridos.append(d2)
salvar_resultado(chave_d[2],d2, chave_d[3], d3)

d4 = pontos4(chave_d[1], chave_d[2])
d5 = pontos4(chave_d[2], chave_d[1])
print(f'\n{"SEGUNDA RODADA - GRUPO D"}')
print(f'{chave_d[1]:<15} {d4}X {d5} {chave_d[2]:>15}')
if d4 > d5:
    lista_pontos_d_um.append(3)
    lista_pontos_d_dois.append(0)
elif d4 == d5:
    lista_pontos_d_um.append(1)
    lista_pontos_d_dois.append(1)
else:
    lista_pontos_d_um.append(0)
    biblio_chave_d_um["Pontos"] = lista_pontos_d_um[:]
    lista_pontos_d_dois.append(3)
    biblio_chave_d_dois["Pontos"] = lista_pontos_d_dois[:]
chave_d_um_gols.append(d4)
chave_d_um_gols_sofridos.append(d5)
chave_d_dois_gols.append(d5)
chave_d_dois_gols_sofridos.append(d4)
salvar_titulo("SEGUNDA RODADA - GRUPO D")
salvar_resultado(chave_d[1],d4, chave_d[2], d5)

d6 = pontos4(chave_d[3], chave_d[0])
d7 = pontos4(chave_d[0], chave_d[3])
print(f'{chave_d[3]:<15} {d6}X {d7} {chave_d[0]:>15}')
if d6 > c7:
    lista_pontos_d_tres.append(3)
    lista_pontos_d_zero.append(0)
elif d6 == c7:
    lista_pontos_d_tres.append(1)
    lista_pontos_d_zero.append(1)
else:
    lista_pontos_d_tres.append(0)
    lista_pontos_d_zero.append(3)
chave_d_zero_gols.append(d7)
chave_d_zero_gols_sofridos.append(d6)
chave_d_tres_gols.append(d6)
chave_d_tres_gols_sofridos.append(d7)
salvar_resultado(chave_d[3],d6, chave_d[0], d7)

print(f'\n{"TERCEIRA RODADA - GRUPO D"}')
d8 = pontos4(chave_d[1], chave_d[3])
d9 = pontos4(chave_d[3], chave_d[1])
print(f'{chave_d[1]:<15} {d8} X {d9} {chave_d[3]:>15}')
if d8 > d9:
    lista_pontos_d_um.append(3)
    lista_pontos_d_tres.append(0)
elif d8 == d9:
    lista_pontos_d_tres.append(1)
    lista_pontos_d_um.append(1)
else:
    lista_pontos_d_um.append(0)
    lista_pontos_d_tres.append(3)
chave_d_um_gols.append(d8)
chave_d_um_gols_sofridos.append(d9)
chave_d_tres_gols.append(d9)
chave_d_tres_gols_sofridos.append(d8)
salvar_titulo("TERCEIRA RODADA - GRUPO D")
salvar_resultado(chave_d[1],d8, chave_d[3], d9)

d10 = pontos4(chave_d[0], chave_d[2])
d11= pontos4(chave_d[2], chave_d[0])
print(f'{chave_d[0]:<15} {d10} X {d11} {chave_d[2]:>15}')
if d10 > d11:
    lista_pontos_d_zero.append(3)
    lista_pontos_d_dois.append(0)
elif d10 == d11:
    lista_pontos_d_zero.append(1)
    lista_pontos_d_dois.append(1)
else:
    lista_pontos_d_zero.append(0)
    lista_pontos_d_dois.append(3)
chave_d_zero_gols.append(d10)
chave_d_zero_gols_sofridos.append(d11)
chave_d_dois_gols.append(d11)
chave_d_dois_gols_sofridos.append(d10)
salvar_resultado(chave_d[0],d10, chave_d[2], d11)

print(f'\n{"PRIMEIRA RODADA - GRUPO E"}')
e0 = pontos4(chave_e[0], chave_e[1])
e1 = pontos4(chave_e[1], chave_e[0])
print(f'{chave_e[0]:<15} {e0}X {e1} {chave_e[1]:>15}')
if e0 > e1:
    biblio_chave_e_zero["Seleção"] = chave_e[0]
    lista_pontos_e_zero.append(3)
    biblio_chave_e_um["Seleção"]= chave_e[1]
    lista_pontos_e_um.append(0)
elif e0 == e1:
    biblio_chave_e_zero["Seleção"] = chave_e[0]
    lista_pontos_e_zero.append(1)
    biblio_chave_e_um["Seleção"] = chave_e[1]
    lista_pontos_e_um.append(1)
else:
    biblio_chave_e_zero["Seleção"] = chave_e[0]
    lista_pontos_e_zero.append(0)
    biblio_chave_e_um["Seleção"] = chave_e[1]
    lista_pontos_e_um.append(3)
chave_e_zero_gols.append(e0)
chave_e_zero_gols_sofridos.append(e1)
chave_e_um_gols.append(e1)
chave_e_um_gols_sofridos.append(e0)
salvar_titulo("PRIMEIRA RODADA - GRUPO E")
salvar_resultado(chave_e[0], e0, chave_e[1], e1)

e2 = pontos4(chave_e[2], chave_e[3])
e3 = pontos4(chave_e[3], chave_e[2])
print(f'{chave_e[2]:<15} {e2}X {e3} {chave_e[3]:>15}')
if e2 > e3:
    biblio_chave_e_dois["Seleção"] = chave_e[2]
    lista_pontos_e_dois.append(3)
    biblio_chave_e_tres["Seleção"]= chave_e[3]
    lista_pontos_e_tres.append(0)
elif e2 == e3:
    biblio_chave_e_dois["Seleção"] = chave_e[2]
    lista_pontos_e_dois.append(1)
    biblio_chave_e_tres["Seleção"] = chave_e[3]
    lista_pontos_e_tres.append(1)
else:
    biblio_chave_e_dois["Seleção"] = chave_e[2]
    lista_pontos_e_dois.append(0)
    biblio_chave_e_tres["Seleção"] = chave_e[3]
    lista_pontos_e_tres.append(3)
chave_e_dois_gols.append(e2)
chave_e_dois_gols_sofridos.append(e3)
chave_e_tres_gols.append(e3)
chave_e_tres_gols_sofridos.append(e2)
salvar_resultado(chave_e[2], e2, chave_e[3], e3)

e4 = pontos4(chave_e[1], chave_e[2])
e5 = pontos4(chave_e[2], chave_e[1])
print(f'\n{"SEGUNDA RODADA - GRUPO E"}')
print(f'{chave_e[1]:<15} {e4}X {e5} {chave_e[2]:>15}')
if e4 > e5:
    lista_pontos_e_um.append(3)
    lista_pontos_e_dois.append(0)
elif e4 == e5:
    lista_pontos_e_um.append(1)
    lista_pontos_e_dois.append(1)
else:
    lista_pontos_e_um.append(0)
    biblio_chave_e_um["Pontos"] = lista_pontos_e_um[:]
    lista_pontos_e_dois.append(3)
    biblio_chave_e_dois["Pontos"] = lista_pontos_e_dois[:]
chave_e_um_gols.append(e4)
chave_e_um_gols_sofridos.append(e5)
chave_e_dois_gols.append(e5)
chave_e_dois_gols_sofridos.append(e4)
salvar_titulo("SEGUNDA RODADA - GRUPO E")
salvar_resultado(chave_e[1], e4, chave_e[2], e5)

e6 = pontos4(chave_e[3], chave_e[0])
e7 = pontos4(chave_e[0], chave_e[3])
print(f'{chave_e[3]:<15} {e6}X {e7} {chave_e[0]:>15}')
if e6 > c7:
    lista_pontos_e_tres.append(3)
    lista_pontos_e_zero.append(0)
elif e6 == c7:
    lista_pontos_e_tres.append(1)
    lista_pontos_e_zero.append(1)
else:
    lista_pontos_e_tres.append(0)
    lista_pontos_e_zero.append(3)
chave_e_zero_gols.append(e7)
chave_e_zero_gols_sofridos.append(e6)
chave_e_tres_gols.append(e6)
chave_e_tres_gols_sofridos.append(e7)
salvar_resultado(chave_e[3], e6, chave_e[0], e7)

print(f'\n{"TERCEIRA RODADA - GRUPO E"}')
e8 = pontos4(chave_e[1], chave_e[3])
e9 = pontos4(chave_e[3], chave_e[1])
print(f'{chave_e[1]:<15} {e8} X {e9} {chave_e[3]:>15}')
if e8 > e9:
    lista_pontos_e_um.append(3)
    lista_pontos_e_tres.append(0)
elif e8 == e9:
    lista_pontos_e_tres.append(1)
    lista_pontos_e_um.append(1)
else:
    lista_pontos_e_um.append(0)
    lista_pontos_e_tres.append(3)
chave_e_um_gols.append(e8)
chave_e_um_gols_sofridos.append(e9)
chave_e_tres_gols.append(e9)
chave_e_tres_gols_sofridos.append(e8)
salvar_titulo("TERCEIRA RODADA - GRUPO E")
salvar_resultado(chave_e[1], e8, chave_e[3], e9)

e10 = pontos4(chave_e[0], chave_e[2])
e11= pontos4(chave_e[2], chave_e[0])
print(f'{chave_e[0]:<15} {e10} X {e11} {chave_e[2]:>15}')
if e10 > e11:
    lista_pontos_e_zero.append(3)
    lista_pontos_e_dois.append(0)
elif e10 == e11:
    lista_pontos_e_zero.append(1)
    lista_pontos_e_dois.append(1)
else:
    lista_pontos_e_zero.append(0)
    lista_pontos_e_dois.append(3)
chave_e_zero_gols.append(e10)
chave_e_zero_gols_sofridos.append(e11)
chave_e_dois_gols.append(e11)
chave_e_dois_gols_sofridos.append(e10)
salvar_resultado(chave_e[0], e10, chave_e[2], e11)

print(f'\n{"PRIMEIRA RODADA - GRUPO F"}')
f0 = pontos4(chave_f[0], chave_f[1])
f1 = pontos4(chave_f[1], chave_f[0])
print(f'{chave_f[0]:<15} {f0}X {f1} {chave_f[1]:>15}')
if f0 > f1:
    biblio_chave_f_zero["Seleção"] = chave_f[0]
    lista_pontos_f_zero.append(3)
    biblio_chave_f_um["Seleção"]= chave_f[1]
    lista_pontos_f_um.append(0)
elif f0 == f1:
    biblio_chave_f_zero["Seleção"] = chave_f[0]
    lista_pontos_f_zero.append(1)
    biblio_chave_f_um["Seleção"] = chave_f[1]
    lista_pontos_f_um.append(1)
else:
    biblio_chave_f_zero["Seleção"] = chave_f[0]
    lista_pontos_f_zero.append(0)
    biblio_chave_f_um["Seleção"] = chave_f[1]
    lista_pontos_f_um.append(3)
chave_f_zero_gols.append(f0)
chave_f_zero_gols_sofridos.append(f1)
chave_f_um_gols.append(f1)
chave_f_um_gols_sofridos.append(f0)
salvar_titulo("PRIMEIRA RODADA - GRUPO F")
salvar_resultado(chave_f[0], f0, chave_f[1], f1)

f2 = pontos4(chave_f[2], chave_f[3])
f3 = pontos4(chave_f[3], chave_f[2])
print(f'{chave_f[2]:<15} {f2}X {f3} {chave_f[3]:>15}')
if f2 > f3:
    biblio_chave_f_dois["Seleção"] = chave_f[2]
    lista_pontos_f_dois.append(3)
    biblio_chave_f_tres["Seleção"]= chave_f[3]
    lista_pontos_f_tres.append(0)
elif f2 == f3:
    biblio_chave_f_dois["Seleção"] = chave_f[2]
    lista_pontos_f_dois.append(1)
    biblio_chave_f_tres["Seleção"] = chave_f[3]
    lista_pontos_f_tres.append(1)
else:
    biblio_chave_f_dois["Seleção"] = chave_f[2]
    lista_pontos_f_dois.append(0)
    biblio_chave_f_tres["Seleção"] = chave_f[3]
    lista_pontos_f_tres.append(3)
chave_f_dois_gols.append(f2)
chave_f_dois_gols_sofridos.append(f3)
chave_f_tres_gols.append(f3)
chave_f_tres_gols_sofridos.append(f2)
salvar_resultado(chave_f[2], f2, chave_f[3], f3)

f4 = pontos4(chave_f[1], chave_f[2])
f5 = pontos4(chave_f[2], chave_f[1])
print(f'\n{"SEGUNDA RODADA - GRUPO F"}')
print(f'{chave_f[1]:<15} {f4}X {f5} {chave_f[2]:>15}')
if f4 > f5:
    lista_pontos_f_um.append(3)
    lista_pontos_f_dois.append(0)
elif f4 == f5:
    lista_pontos_f_um.append(1)
    lista_pontos_f_dois.append(1)
else:
    lista_pontos_f_um.append(0)
    biblio_chave_f_um["Pontos"] = lista_pontos_f_um[:]
    lista_pontos_f_dois.append(3)
    biblio_chave_f_dois["Pontos"] = lista_pontos_f_dois[:]
chave_f_um_gols.append(f4)
chave_f_um_gols_sofridos.append(f5)
chave_f_dois_gols.append(f5)
chave_f_dois_gols_sofridos.append(f4)
salvar_titulo("SEGUNDA RODADA - GRUPO F")
salvar_resultado(chave_f[1], f4, chave_f[2], f5)

f6 = pontos4(chave_f[3], chave_f[0])
f7 = pontos4(chave_f[0], chave_f[3])
print(f'{chave_f[3]:<15} {f6}X {f7} {chave_f[0]:>15}')
if f6 > c7:
    lista_pontos_f_tres.append(3)
    lista_pontos_f_zero.append(0)
elif f6 == c7:
    lista_pontos_f_tres.append(1)
    lista_pontos_f_zero.append(1)
else:
    lista_pontos_f_tres.append(0)
    lista_pontos_f_zero.append(3)
chave_f_zero_gols.append(f7)
chave_f_zero_gols_sofridos.append(f6)
chave_f_tres_gols.append(f6)
chave_f_tres_gols_sofridos.append(f7)
salvar_resultado(chave_f[3], f6, chave_f[0], f7)

print(f'\n{"TERCEIRA RODADA - GRUPO F"}')
f8 = pontos4(chave_f[1], chave_f[3])
f9 = pontos4(chave_f[3], chave_f[1])
print(f'{chave_f[1]:<15} {f8} X {f9} {chave_f[3]:>15}')
if f8 > f9:
    lista_pontos_f_um.append(3)
    lista_pontos_f_tres.append(0)
elif f8 == f9:
    lista_pontos_f_tres.append(1)
    lista_pontos_f_um.append(1)
else:
    lista_pontos_f_um.append(0)
    lista_pontos_f_tres.append(3)
chave_f_um_gols.append(f8)
chave_f_um_gols_sofridos.append(f9)
chave_f_tres_gols.append(f9)
chave_f_tres_gols_sofridos.append(f8)
salvar_titulo("TERCEIRA RODADA - GRUPO F")
salvar_resultado(chave_f[1], f8, chave_f[3], f9)

f10 = pontos4(chave_f[0], chave_f[2])
f11= pontos4(chave_f[2], chave_f[0])
print(f'{chave_f[0]:<15} {f10} X {f11} {chave_f[2]:>15}')
if f10 > f11:
    lista_pontos_f_zero.append(3)
    lista_pontos_f_dois.append(0)
elif f10 == f11:
    lista_pontos_f_zero.append(1)
    lista_pontos_f_dois.append(1)
else:
    lista_pontos_f_zero.append(0)
    lista_pontos_f_dois.append(3)
chave_f_zero_gols.append(f10)
chave_f_zero_gols_sofridos.append(f11)
chave_f_dois_gols.append(f11)
chave_f_dois_gols_sofridos.append(f10)
salvar_resultado(chave_f[0], f10, chave_f[2], f11)

print(f'\n{"PRIMEIRA RODADA - GRUPO G"}')
g0 = pontos4(chave_g[0], chave_g[1])
g1 = pontos4(chave_g[1], chave_g[0])
print(f'{chave_g[0]:<15} {g0}X {g1} {chave_g[1]:>15}')
if g0 > g1:
    biblio_chave_g_zero["Seleção"] = chave_g[0]
    lista_pontos_g_zero.append(3)
    biblio_chave_g_um["Seleção"]= chave_g[1]
    lista_pontos_g_um.append(0)
elif g0 == g1:
    biblio_chave_g_zero["Seleção"] = chave_g[0]
    lista_pontos_g_zero.append(1)
    biblio_chave_g_um["Seleção"] = chave_g[1]
    lista_pontos_g_um.append(1)
else:
    biblio_chave_g_zero["Seleção"] = chave_g[0]
    lista_pontos_g_zero.append(0)
    biblio_chave_g_um["Seleção"] = chave_g[1]
    lista_pontos_g_um.append(3)
chave_g_zero_gols.append(g0)
chave_g_zero_gols_sofridos.append(g1)
chave_g_um_gols.append(g1)
chave_g_um_gols_sofridos.append(g0)
salvar_titulo("PRIMEIRA RODADA - GRUPO G")
salvar_resultado(chave_g[0], g0, chave_g[1], g1)

g2 = pontos4(chave_g[2], chave_g[3])
g3 = pontos4(chave_g[3], chave_g[2])
print(f'{chave_g[2]:<15} {g2}X {g3} {chave_g[3]:>15}')
if g2 > g3:
    biblio_chave_g_dois["Seleção"] = chave_g[2]
    lista_pontos_g_dois.append(3)
    biblio_chave_g_tres["Seleção"]= chave_g[3]
    lista_pontos_g_tres.append(0)
elif g2 == g3:
    biblio_chave_g_dois["Seleção"] = chave_g[2]
    lista_pontos_g_dois.append(1)
    biblio_chave_g_tres["Seleção"] = chave_g[3]
    lista_pontos_g_tres.append(1)
else:
    biblio_chave_g_dois["Seleção"] = chave_g[2]
    lista_pontos_g_dois.append(0)
    biblio_chave_g_tres["Seleção"] = chave_g[3]
    lista_pontos_g_tres.append(3)
chave_g_dois_gols.append(g2)
chave_g_dois_gols_sofridos.append(g3)
chave_g_tres_gols.append(g3)
chave_g_tres_gols_sofridos.append(g2)
salvar_resultado(chave_g[2], g2, chave_g[3], g3)

g4 = pontos4(chave_g[1], chave_g[2])
g5 = pontos4(chave_g[2], chave_g[1])
print(f'\n{"SEGUNDA RODADA - GRUPO G"}')
print(f'{chave_g[1]:<15} {g4}X {g5} {chave_g[2]:>15}')
if g4 > g5:
    lista_pontos_g_um.append(3)
    lista_pontos_g_dois.append(0)
elif g4 == g5:
    lista_pontos_g_um.append(1)
    lista_pontos_g_dois.append(1)
else:
    lista_pontos_g_um.append(0)
    biblio_chave_g_um["Pontos"] = lista_pontos_g_um[:]
    lista_pontos_g_dois.append(3)
    biblio_chave_g_dois["Pontos"] = lista_pontos_g_dois[:]
chave_g_um_gols.append(g4)
chave_g_um_gols_sofridos.append(g5)
chave_g_dois_gols.append(g5)
chave_g_dois_gols_sofridos.append(g4)
salvar_titulo("SEGUNDA RODADA - GRUPO G")
salvar_resultado(chave_g[1], g4, chave_g[2], g5)

g6 = pontos4(chave_g[3], chave_g[0])
g7 = pontos4(chave_g[0], chave_g[3])
print(f'{chave_g[3]:<15} {g6}X {g7} {chave_g[0]:>15}')
if g6 > c7:
    lista_pontos_g_tres.append(3)
    lista_pontos_g_zero.append(0)
elif g6 == c7:
    lista_pontos_g_tres.append(1)
    lista_pontos_g_zero.append(1)
else:
    lista_pontos_g_tres.append(0)
    lista_pontos_g_zero.append(3)
chave_g_zero_gols.append(g7)
chave_g_zero_gols_sofridos.append(g6)
chave_g_tres_gols.append(g6)
chave_g_tres_gols_sofridos.append(g7)
salvar_resultado(chave_g[3], g6, chave_g[0], g7)

print(f'\n{"TERCEIRA RODADA - GRUPO G"}')
g8 = pontos4(chave_g[1], chave_g[3])
g9 = pontos4(chave_g[3], chave_g[1])
print(f'{chave_g[1]:<15} {g8} X {g9} {chave_g[3]:>15}')
if g8 > g9:
    lista_pontos_g_um.append(3)
    lista_pontos_g_tres.append(0)
elif g8 == g9:
    lista_pontos_g_tres.append(1)
    lista_pontos_g_um.append(1)
else:
    lista_pontos_g_um.append(0)
    lista_pontos_g_tres.append(3)
chave_g_um_gols.append(g8)
chave_g_um_gols_sofridos.append(g9)
chave_g_tres_gols.append(g9)
chave_g_tres_gols_sofridos.append(g8)
salvar_titulo("TERCEIRA RODADA - GRUPO G")
salvar_resultado(chave_g[1], g8, chave_g[3], g9)

g10 = pontos4(chave_g[0], chave_g[2])
g11= pontos4(chave_g[2], chave_g[0])
print(f'{chave_g[0]:<15} {g10} X {g11} {chave_g[2]:>15}')
if g10 > g11:
    lista_pontos_g_zero.append(3)
    lista_pontos_g_dois.append(0)
elif g10 == g11:
    lista_pontos_g_zero.append(1)
    lista_pontos_g_dois.append(1)
else:
    lista_pontos_g_zero.append(0)
    lista_pontos_g_dois.append(3)
chave_g_zero_gols.append(g10)
chave_g_zero_gols_sofridos.append(g11)
chave_g_dois_gols.append(g11)
chave_g_dois_gols_sofridos.append(g10)
salvar_resultado(chave_g[0], g10, chave_g[2], g11)

print(f'\n{"PRIMEIRA RODADA - GRUPO H"}')
h0 = pontos4(chave_h[0], chave_h[1])
h1 = pontos4(chave_h[1], chave_h[0])
print(f'{chave_h[0]:<15} {h0}X {h1} {chave_h[1]:>15}')
if h0 > h1:
    biblio_chave_h_zero["Seleção"] = chave_h[0]
    lista_pontos_h_zero.append(3)
    biblio_chave_h_um["Seleção"]= chave_h[1]
    lista_pontos_h_um.append(0)
elif h0 == h1:
    biblio_chave_h_zero["Seleção"] = chave_h[0]
    lista_pontos_h_zero.append(1)
    biblio_chave_h_um["Seleção"] = chave_h[1]
    lista_pontos_h_um.append(1)
else:
    biblio_chave_h_zero["Seleção"] = chave_h[0]
    lista_pontos_h_zero.append(0)
    biblio_chave_h_um["Seleção"] = chave_h[1]
    lista_pontos_h_um.append(3)
chave_h_zero_gols.append(h0)
chave_h_zero_gols_sofridos.append(h1)
chave_h_um_gols.append(h1)
chave_h_um_gols_sofridos.append(h0)
salvar_titulo("PRIMEIRA RODADA - GRUPO H")
salvar_resultado(chave_h[0], h0, chave_h[1], h1)

h2 = pontos4(chave_h[2], chave_h[3])
h3 = pontos4(chave_h[3], chave_h[2])
print(f'{chave_h[2]:<15} {h2}X {h3} {chave_h[3]:>15}')
if h2 > h3:
    biblio_chave_h_dois["Seleção"] = chave_h[2]
    lista_pontos_h_dois.append(3)
    biblio_chave_h_tres["Seleção"]= chave_h[3]
    lista_pontos_h_tres.append(0)
elif h2 == h3:
    biblio_chave_h_dois["Seleção"] = chave_h[2]
    lista_pontos_h_dois.append(1)
    biblio_chave_h_tres["Seleção"] = chave_h[3]
    lista_pontos_h_tres.append(1)
else:
    biblio_chave_h_dois["Seleção"] = chave_h[2]
    lista_pontos_h_dois.append(0)
    biblio_chave_h_tres["Seleção"] = chave_h[3]
    lista_pontos_h_tres.append(3)
chave_h_dois_gols.append(h2)
chave_h_dois_gols_sofridos.append(h3)
chave_h_tres_gols.append(h3)
chave_h_tres_gols_sofridos.append(h2)
salvar_resultado(chave_h[2], h2, chave_h[3], h3)

h4 = pontos4(chave_h[1], chave_h[2])
h5 = pontos4(chave_h[2], chave_h[1])
print(f'\n{"SEGUNDA RODADA - GRUPO H"}')
print(f'{chave_h[1]:<15} {h4}X {h5} {chave_h[2]:>15}')
if h4 > h5:
    lista_pontos_h_um.append(3)
    lista_pontos_h_dois.append(0)
elif h4 == h5:
    lista_pontos_h_um.append(1)
    lista_pontos_h_dois.append(1)
else:
    lista_pontos_h_um.append(0)
    biblio_chave_h_um["Pontos"] = lista_pontos_h_um[:]
    lista_pontos_h_dois.append(3)
    biblio_chave_h_dois["Pontos"] = lista_pontos_h_dois[:]
chave_h_um_gols.append(h4)
chave_h_um_gols_sofridos.append(h5)
chave_h_dois_gols.append(h5)
chave_h_dois_gols_sofridos.append(h4)
salvar_titulo("SEGUNDA RODADA - GRUPO H")
salvar_resultado(chave_h[1], h4, chave_h[2], h5)

h6 = pontos4(chave_h[3], chave_h[0])
h7 = pontos4(chave_h[0], chave_h[3])
print(f'{chave_h[3]:<15} {h6}X {h7} {chave_h[0]:>15}')
if h6 > c7:
    lista_pontos_h_tres.append(3)
    lista_pontos_h_zero.append(0)
elif h6 == c7:
    lista_pontos_h_tres.append(1)
    lista_pontos_h_zero.append(1)
else:
    lista_pontos_h_tres.append(0)
    lista_pontos_h_zero.append(3)
chave_h_zero_gols.append(h7)
chave_h_zero_gols_sofridos.append(h6)
chave_h_tres_gols.append(h6)
chave_h_tres_gols_sofridos.append(h7)
salvar_resultado(chave_h[3], h6, chave_h[0], h7)

print(f'\n{"TERCEIRA RODADA - GRUPO H"}')
h8 = pontos4(chave_h[1], chave_h[3])
h9 = pontos4(chave_h[3], chave_h[1])
print(f'{chave_h[1]:<15} {h8} X {h9} {chave_h[3]:>15}')
if h8 > h9:
    lista_pontos_h_um.append(3)
    lista_pontos_h_tres.append(0)
elif h8 == h9:
    lista_pontos_h_tres.append(1)
    lista_pontos_h_um.append(1)
else:
    lista_pontos_h_um.append(0)
    lista_pontos_h_tres.append(3)
chave_h_um_gols.append(h8)
chave_h_um_gols_sofridos.append(h9)
chave_h_tres_gols.append(h9)
chave_h_tres_gols_sofridos.append(h8)
salvar_titulo("TERCEIRA RODADA - GRUPO H")
salvar_resultado(chave_h[1], h8, chave_h[3], h9)

h10 = pontos4(chave_h[0], chave_h[2])
h11= pontos4(chave_h[2], chave_h[0])
print(f'{chave_h[0]:<15} {h10} X {h11} {chave_h[2]:>15}')
if h10 > h11:
    lista_pontos_h_zero.append(3)
    lista_pontos_h_dois.append(0)
elif h10 == h11:
    lista_pontos_h_zero.append(1)
    lista_pontos_h_dois.append(1)
else:
    lista_pontos_h_zero.append(0)
    lista_pontos_h_dois.append(3)
chave_h_zero_gols.append(h10)
chave_h_zero_gols_sofridos.append(h11)
chave_h_dois_gols.append(h11)
chave_h_dois_gols_sofridos.append(h10)
salvar_resultado(chave_h[0], h10, chave_h[2], h11)
#resultado
#chave A classificação chave de grupos
soma_gols_a_zero = 0
soma_gols_sofridos_a_zero = 0
soma_gols_a_um = 0
soma_gols_sofridos_a_um = 0
soma_gols_a_dois = 0
soma_gols_sofridos_a_dois = 0
soma_gols_a_tres = 0
soma_gols_sofridos_a_tres = 0

for n in chave_a_zero_gols:
    soma_gols_a_zero += sum(n)
for num in chave_a_zero_gols_sofridos:
    soma_gols_sofridos_a_zero += sum(num)
saldo_a_zero = soma_gols_a_zero - soma_gols_sofridos_a_zero

for n in chave_a_um_gols:
    soma_gols_a_um += sum(n)
for num in chave_a_um_gols_sofridos:
    soma_gols_sofridos_a_um += sum(num)
saldo_a_um = soma_gols_a_um - soma_gols_sofridos_a_um

for n in chave_a_dois_gols:
    soma_gols_a_dois += sum(n)
for num in chave_a_dois_gols_sofridos:
    soma_gols_sofridos_a_dois += sum(num)
saldo_a_dois = soma_gols_a_dois - soma_gols_sofridos_a_dois

for n in chave_a_tres_gols:
    soma_gols_a_tres += sum(n)
for num in chave_a_tres_gols_sofridos:
    soma_gols_sofridos_a_tres += sum(num)
saldo_a_tres = soma_gols_a_tres - soma_gols_sofridos_a_tres

biblio_chave_a_zero["Total"] = sum(lista_pontos_zero)
biblio_chave_a_zero["Saldo de Gols"] = saldo_a_zero
biblio_chave_a_um["Total"] = sum(lista_pontos_um)
biblio_chave_a_um["Saldo de Gols"] = saldo_a_um
biblio_chave_a_dois["Total"] = sum(lista_pontos_dois)
biblio_chave_a_dois["Saldo de Gols"] = saldo_a_dois
biblio_chave_a_tres["Total"] = sum(lista_pontos_tres)
biblio_chave_a_tres["Saldo de Gols"] = saldo_a_tres

lista_a = []
lista_a.append(biblio_chave_a_zero)
lista_a.append(biblio_chave_a_um)
lista_a.append(biblio_chave_a_dois)
lista_a.append(biblio_chave_a_tres)

#chave B classificação chave de grupos
soma_gols_b_zero = 0
soma_gols_sofridos_b_zero = 0
soma_gols_b_um = 0
soma_gols_sofridos_b_um = 0
soma_gols_b_dois = 0
soma_gols_sofridos_b_dois = 0
soma_gols_b_tres = 0
soma_gols_sofridos_b_tres = 0

for n in chave_b_zero_gols:
    soma_gols_b_zero += sum(n)
for num in chave_b_zero_gols_sofridos:
    soma_gols_sofridos_b_zero += sum(num)
saldo_b_zero = soma_gols_b_zero - soma_gols_sofridos_b_zero

for n in chave_b_um_gols:
    soma_gols_b_um += sum(n)
for num in chave_b_um_gols_sofridos:
    soma_gols_sofridos_b_um += sum(num)
saldo_b_um = soma_gols_b_um - soma_gols_sofridos_b_um

for n in chave_b_dois_gols:
    soma_gols_b_dois += sum(n)
for num in chave_b_dois_gols_sofridos:
    soma_gols_sofridos_b_dois += sum(num)
saldo_b_dois = soma_gols_b_dois - soma_gols_sofridos_b_dois

for n in chave_b_tres_gols:
    soma_gols_b_tres += sum(n)
for num in chave_b_tres_gols_sofridos:
    soma_gols_sofridos_b_tres += sum(num)
saldo_b_tres = soma_gols_b_tres - soma_gols_sofridos_b_tres

biblio_chave_b_zero["Pontos"] = lista_pontos_b_zero[:]
biblio_chave_b_zero["Total"] = sum(lista_pontos_b_zero)
biblio_chave_b_zero["Saldo de Gols"] = saldo_b_zero
biblio_chave_b_um["Pontos"] = lista_pontos_b_um[:]
biblio_chave_b_um["Total"] = sum(lista_pontos_b_um)
biblio_chave_b_um["Saldo de Gols"] = saldo_b_um
biblio_chave_b_dois["Pontos"] = lista_pontos_b_dois[:]
biblio_chave_b_dois["Total"] = sum(lista_pontos_b_dois)
biblio_chave_b_dois["Saldo de Gols"] = saldo_b_dois
biblio_chave_b_tres["Pontos"] = lista_pontos_b_tres[:]
biblio_chave_b_tres["Total"] = sum(lista_pontos_b_tres)
biblio_chave_b_tres["Saldo de Gols"] = saldo_b_tres

lista_b = []
lista_b.append(biblio_chave_b_zero)
lista_b.append(biblio_chave_b_um)
lista_b.append(biblio_chave_b_dois)
lista_b.append(biblio_chave_b_tres)

#chave c classificação chave de grupos
soma_gols_c_zero = 0
soma_gols_sofridos_c_zero = 0
soma_gols_c_um = 0
soma_gols_sofridos_c_um = 0
soma_gols_c_dois = 0
soma_gols_sofridos_c_dois = 0
soma_gols_c_tres = 0
soma_gols_sofridos_c_tres = 0

for n in chave_c_zero_gols:
    soma_gols_c_zero += sum(n)
for num in chave_c_zero_gols_sofridos:
    soma_gols_sofridos_c_zero += sum(num)
saldo_c_zero = soma_gols_c_zero - soma_gols_sofridos_c_zero

for n in chave_c_um_gols:
    soma_gols_c_um += sum(n)
for num in chave_c_um_gols_sofridos:
    soma_gols_sofridos_c_um += sum(num)
saldo_c_um = soma_gols_c_um - soma_gols_sofridos_c_um

for n in chave_c_dois_gols:
    soma_gols_c_dois += sum(n)
for num in chave_c_dois_gols_sofridos:
    soma_gols_sofridos_c_dois += sum(num)
saldo_c_dois = soma_gols_c_dois - soma_gols_sofridos_c_dois

for n in chave_c_tres_gols:
    soma_gols_c_tres += sum(n)
for num in chave_c_tres_gols_sofridos:
    soma_gols_sofridos_c_tres += sum(num)
saldo_c_tres = soma_gols_c_tres - soma_gols_sofridos_c_tres

biblio_chave_c_zero["Pontos"] = lista_pontos_c_zero[:]
biblio_chave_c_zero["Total"] = sum(lista_pontos_c_zero)
biblio_chave_c_zero["Saldo de Gols"] = saldo_c_zero
biblio_chave_c_um["Pontos"] = lista_pontos_c_um[:]
biblio_chave_c_um["Total"] = sum(lista_pontos_c_um)
biblio_chave_c_um["Saldo de Gols"] = saldo_c_um
biblio_chave_c_dois["Pontos"] = lista_pontos_c_dois[:]
biblio_chave_c_dois["Total"] = sum(lista_pontos_c_dois)
biblio_chave_c_dois["Saldo de Gols"] = saldo_c_dois
biblio_chave_c_tres["Pontos"] = lista_pontos_c_tres[:]
biblio_chave_c_tres["Total"] = sum(lista_pontos_c_tres)
biblio_chave_c_tres["Saldo de Gols"] = saldo_c_tres

lista_c = []
lista_c.append(biblio_chave_c_zero)
lista_c.append(biblio_chave_c_um)
lista_c.append(biblio_chave_c_dois)
lista_c.append(biblio_chave_c_tres)

#chave D classificaçao chave de grupos
soma_gols_d_zero = 0
soma_gols_sofridos_d_zero = 0
soma_gols_d_um = 0
soma_gols_sofridos_d_um = 0
soma_gols_d_dois = 0
soma_gols_sofridos_d_dois = 0
soma_gols_d_tres = 0
soma_gols_sofridos_d_tres = 0

for n in chave_d_zero_gols:
    soma_gols_d_zero += sum(n)
for num in chave_d_zero_gols_sofridos:
    soma_gols_sofridos_d_zero += sum(num)
saldo_d_zero = soma_gols_d_zero - soma_gols_sofridos_d_zero

for n in chave_d_um_gols:
    soma_gols_d_um += sum(n)
for num in chave_d_um_gols_sofridos:
    soma_gols_sofridos_d_um += sum(num)
saldo_d_um = soma_gols_d_um - soma_gols_sofridos_d_um

for n in chave_d_dois_gols:
    soma_gols_d_dois += sum(n)
for num in chave_d_dois_gols_sofridos:
    soma_gols_sofridos_d_dois += sum(num)
saldo_d_dois = soma_gols_d_dois - soma_gols_sofridos_d_dois

for n in chave_d_tres_gols:
    soma_gols_d_tres += sum(n)
for num in chave_d_tres_gols_sofridos:
    soma_gols_sofridos_d_tres += sum(num)
saldo_d_tres = soma_gols_d_tres - soma_gols_sofridos_d_tres

biblio_chave_d_zero["Pontos"] = lista_pontos_d_zero[:]
biblio_chave_d_zero["Total"] = sum(lista_pontos_d_zero)
biblio_chave_d_zero["Saldo de Gols"] = saldo_d_zero
biblio_chave_d_um["Pontos"] = lista_pontos_d_um[:]
biblio_chave_d_um["Total"] = sum(lista_pontos_d_um)
biblio_chave_d_um["Saldo de Gols"] = saldo_d_um
biblio_chave_d_dois["Pontos"] = lista_pontos_d_dois[:]
biblio_chave_d_dois["Total"] = sum(lista_pontos_d_dois)
biblio_chave_d_dois["Saldo de Gols"] = saldo_d_dois
biblio_chave_d_tres["Pontos"] = lista_pontos_d_tres[:]
biblio_chave_d_tres["Total"] = sum(lista_pontos_d_tres)
biblio_chave_d_tres["Saldo de Gols"] = saldo_d_tres

lista_d = []
lista_d.append(biblio_chave_d_zero)
lista_d.append(biblio_chave_d_um)
lista_d.append(biblio_chave_d_dois)
lista_d.append(biblio_chave_d_tres)

#chave E classificação chave de grupos
soma_gols_e_zero = 0
soma_gols_sofridos_e_zero = 0
soma_gols_e_um = 0
soma_gols_sofridos_e_um = 0
soma_gols_e_dois = 0
soma_gols_sofridos_e_dois = 0
soma_gols_e_tres = 0
soma_gols_sofridos_e_tres = 0

for n in chave_e_zero_gols:
    soma_gols_e_zero += sum(n)
for num in chave_e_zero_gols_sofridos:
    soma_gols_sofridos_e_zero += sum(num)
saldo_e_zero = soma_gols_e_zero - soma_gols_sofridos_e_zero

for n in chave_e_um_gols:
    soma_gols_e_um += sum(n)
for num in chave_e_um_gols_sofridos:
    soma_gols_sofridos_e_um += sum(num)
saldo_e_um = soma_gols_e_um - soma_gols_sofridos_e_um

for n in chave_e_dois_gols:
    soma_gols_e_dois += sum(n)
for num in chave_e_dois_gols_sofridos:
    soma_gols_sofridos_e_dois += sum(num)
saldo_e_dois = soma_gols_e_dois - soma_gols_sofridos_e_dois

for n in chave_e_tres_gols:
    soma_gols_e_tres += sum(n)
for num in chave_e_tres_gols_sofridos:
    soma_gols_sofridos_e_tres += sum(num)
saldo_e_tres = soma_gols_e_tres - soma_gols_sofridos_e_tres

biblio_chave_e_zero["Pontos"] = lista_pontos_e_zero[:]
biblio_chave_e_zero["Total"] = sum(lista_pontos_e_zero)
biblio_chave_e_zero["Saldo de Gols"] = saldo_e_zero
biblio_chave_e_um["Pontos"] = lista_pontos_e_um[:]
biblio_chave_e_um["Total"] = sum(lista_pontos_e_um)
biblio_chave_e_um["Saldo de Gols"] = saldo_e_um
biblio_chave_e_dois["Pontos"] = lista_pontos_e_dois[:]
biblio_chave_e_dois["Total"] = sum(lista_pontos_e_dois)
biblio_chave_e_dois["Saldo de Gols"] = saldo_e_dois
biblio_chave_e_tres["Pontos"] = lista_pontos_e_tres[:]
biblio_chave_e_tres["Total"] = sum(lista_pontos_e_tres)
biblio_chave_e_tres["Saldo de Gols"] = saldo_e_tres

lista_e = []
lista_e.append(biblio_chave_e_zero)
lista_e.append(biblio_chave_e_um)
lista_e.append(biblio_chave_e_dois)
lista_e.append(biblio_chave_e_tres)

#chave F classificação chave de grupos
soma_gols_f_zero = 0
soma_gols_sofridos_f_zero = 0
soma_gols_f_um = 0
soma_gols_sofridos_f_um = 0
soma_gols_f_dois = 0
soma_gols_sofridos_f_dois = 0
soma_gols_f_tres = 0
soma_gols_sofridos_f_tres = 0

for n in chave_f_zero_gols:
    soma_gols_f_zero += sum(n)
for num in chave_f_zero_gols_sofridos:
    soma_gols_sofridos_f_zero += sum(num)
saldo_f_zero = soma_gols_f_zero - soma_gols_sofridos_f_zero

for n in chave_f_um_gols:
    soma_gols_f_um += sum(n)
for num in chave_f_um_gols_sofridos:
    soma_gols_sofridos_f_um += sum(num)
saldo_f_um = soma_gols_f_um - soma_gols_sofridos_f_um

for n in chave_f_dois_gols:
    soma_gols_f_dois += sum(n)
for num in chave_f_dois_gols_sofridos:
    soma_gols_sofridos_f_dois += sum(num)
saldo_f_dois = soma_gols_f_dois - soma_gols_sofridos_f_dois

for n in chave_f_tres_gols:
    soma_gols_f_tres += sum(n)
for num in chave_f_tres_gols_sofridos:
    soma_gols_sofridos_f_tres += sum(num)
saldo_f_tres = soma_gols_f_tres - soma_gols_sofridos_f_tres

biblio_chave_f_zero["Pontos"] = lista_pontos_f_zero[:]
biblio_chave_f_zero["Total"] = sum(lista_pontos_f_zero)
biblio_chave_f_zero["Saldo de Gols"] = saldo_f_zero
biblio_chave_f_um["Pontos"] = lista_pontos_f_um[:]
biblio_chave_f_um["Total"] = sum(lista_pontos_f_um)
biblio_chave_f_um["Saldo de Gols"] = saldo_f_um
biblio_chave_f_dois["Pontos"] = lista_pontos_f_dois[:]
biblio_chave_f_dois["Total"] = sum(lista_pontos_f_dois)
biblio_chave_f_dois["Saldo de Gols"] = saldo_f_dois
biblio_chave_f_tres["Pontos"] = lista_pontos_f_tres[:]
biblio_chave_f_tres["Total"] = sum(lista_pontos_f_tres)
biblio_chave_f_tres["Saldo de Gols"] = saldo_f_tres

lista_f = []
lista_f.append(biblio_chave_f_zero)
lista_f.append(biblio_chave_f_um)
lista_f.append(biblio_chave_f_dois)
lista_f.append(biblio_chave_f_tres)

#chave G classificação chave de grupos
soma_gols_g_zero = 0
soma_gols_sofridos_g_zero = 0
soma_gols_g_um = 0
soma_gols_sofridos_g_um = 0
soma_gols_g_dois = 0
soma_gols_sofridos_g_dois = 0
soma_gols_g_tres = 0
soma_gols_sofridos_g_tres = 0

for n in chave_g_zero_gols:
    soma_gols_g_zero += sum(n)
for num in chave_g_zero_gols_sofridos:
    soma_gols_sofridos_g_zero += sum(num)
saldo_g_zero = soma_gols_g_zero - soma_gols_sofridos_g_zero

for n in chave_g_um_gols:
    soma_gols_g_um += sum(n)
for num in chave_g_um_gols_sofridos:
    soma_gols_sofridos_g_um += sum(num)
saldo_g_um = soma_gols_g_um - soma_gols_sofridos_g_um

for n in chave_g_dois_gols:
    soma_gols_g_dois += sum(n)
for num in chave_g_dois_gols_sofridos:
    soma_gols_sofridos_g_dois += sum(num)
saldo_g_dois = soma_gols_g_dois - soma_gols_sofridos_g_dois

for n in chave_g_tres_gols:
    soma_gols_g_tres += sum(n)
for num in chave_g_tres_gols_sofridos:
    soma_gols_sofridos_g_tres += sum(num)
saldo_g_tres = soma_gols_g_tres - soma_gols_sofridos_g_tres

biblio_chave_g_zero["Pontos"] = lista_pontos_g_zero[:]
biblio_chave_g_zero["Total"] = sum(lista_pontos_g_zero)
biblio_chave_g_zero["Saldo de Gols"] = saldo_g_zero
biblio_chave_g_um["Pontos"] = lista_pontos_g_um[:]
biblio_chave_g_um["Total"] = sum(lista_pontos_g_um)
biblio_chave_g_um["Saldo de Gols"] = saldo_g_um
biblio_chave_g_dois["Pontos"] = lista_pontos_g_dois[:]
biblio_chave_g_dois["Total"] = sum(lista_pontos_g_dois)
biblio_chave_g_dois["Saldo de Gols"] = saldo_g_dois
biblio_chave_g_tres["Pontos"] = lista_pontos_g_tres[:]
biblio_chave_g_tres["Total"] = sum(lista_pontos_g_tres)
biblio_chave_g_tres["Saldo de Gols"] = saldo_g_tres

lista_g = []
lista_g.append(biblio_chave_g_zero)
lista_g.append(biblio_chave_g_um)
lista_g.append(biblio_chave_g_dois)
lista_g.append(biblio_chave_g_tres)

#chave H classificação chave de grupos
soma_gols_h_zero = 0
soma_gols_sofridos_h_zero = 0
soma_gols_h_um = 0
soma_gols_sofridos_h_um = 0
soma_gols_h_dois = 0
soma_gols_sofridos_h_dois = 0
soma_gols_h_tres = 0
soma_gols_sofridos_h_tres = 0

for n in chave_h_zero_gols:
    soma_gols_h_zero += sum(n)
for num in chave_h_zero_gols_sofridos:
    soma_gols_sofridos_h_zero += sum(num)
saldo_h_zero = soma_gols_h_zero - soma_gols_sofridos_h_zero

for n in chave_h_um_gols:
    soma_gols_h_um += sum(n)
for num in chave_h_um_gols_sofridos:
    soma_gols_sofridos_h_um += sum(num)
saldo_h_um = soma_gols_h_um - soma_gols_sofridos_h_um

for n in chave_h_dois_gols:
    soma_gols_h_dois += sum(n)
for num in chave_h_dois_gols_sofridos:
    soma_gols_sofridos_h_dois += sum(num)
saldo_h_dois = soma_gols_h_dois - soma_gols_sofridos_h_dois

for n in chave_h_tres_gols:
    soma_gols_h_tres += sum(n)
for num in chave_h_tres_gols_sofridos:
    soma_gols_sofridos_h_tres += sum(num)
saldo_h_tres = soma_gols_h_tres - soma_gols_sofridos_h_tres

biblio_chave_h_zero["Pontos"] = lista_pontos_h_zero[:]
biblio_chave_h_zero["Total"] = sum(lista_pontos_h_zero)
biblio_chave_h_zero["Saldo de Gols"] = saldo_h_zero
biblio_chave_h_um["Pontos"] = lista_pontos_h_um[:]
biblio_chave_h_um["Total"] = sum(lista_pontos_h_um)
biblio_chave_h_um["Saldo de Gols"] = saldo_h_um
biblio_chave_h_dois["Pontos"] = lista_pontos_h_dois[:]
biblio_chave_h_dois["Total"] = sum(lista_pontos_h_dois)
biblio_chave_h_dois["Saldo de Gols"] = saldo_h_dois
biblio_chave_h_tres["Pontos"] = lista_pontos_h_tres[:]
biblio_chave_h_tres["Total"] = sum(lista_pontos_h_tres)
biblio_chave_h_tres["Saldo de Gols"] = saldo_h_tres

lista_h = []
lista_h.append(biblio_chave_h_zero)
lista_h.append(biblio_chave_h_um)
lista_h.append(biblio_chave_h_dois)
lista_h.append(biblio_chave_h_tres)

print(f'\n{"Resultado final da Chave de Grupos"}\n')
print(f'{"Grupo A"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'\n{"Classificação das seleções na Fase de Grupos"}\n'
        f'{"Grupo A"}\n')
a.close()
ordem_a = sorted(lista_a, key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_a):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c+1} - {selecao}\n')
    a.close()
print(f'{"Grupo B"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo B"}\n')
a.close()
ordem_b = sorted(lista_b,key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_b):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo C"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo C"}\n')
a.close()
ordem_c = sorted(lista_c,key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_c):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo D"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo D"}\n')
a.close()
ordem_d = sorted(lista_d,key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_d):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo E"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo E"}\n')
a.close()
ordem_e = sorted(lista_e,key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_e):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo F"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo F"}\n')
a.close()
ordem_f = sorted(lista_f,key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_f):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo G"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo G"}\n')
a.close()
ordem_g = sorted(lista_g, key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_g):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()
print(f'{"Grupo H"}')
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'{"Grupo H"}\n')
a.close()
ordem_h = sorted(lista_h, key=lambda contact: contact["Total"], reverse=True)
for c, selecao in enumerate(ordem_h):
    print(f'{c+1} - {selecao}')
    a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
    a.write(f'{c + 1} - {selecao}\n')
    a.close()

#oitavas de final
print(f'{"OITAVAS DE FINAL"}')
lista_oitavas = []
lista_oitavas.append(ordem_a[0]["Seleção"])
lista_oitavas.append(ordem_a[1]["Seleção"])
lista_oitavas.append(ordem_b[0]["Seleção"])
lista_oitavas.append(ordem_b[1]["Seleção"])
lista_oitavas.append(ordem_c[0]["Seleção"])
lista_oitavas.append(ordem_c[1]["Seleção"])
lista_oitavas.append(ordem_d[0]["Seleção"])
lista_oitavas.append(ordem_d[1]["Seleção"])
lista_oitavas.append(ordem_e[0]["Seleção"])
lista_oitavas.append(ordem_e[1]["Seleção"])
lista_oitavas.append(ordem_f[0]["Seleção"])
lista_oitavas.append(ordem_f[1]["Seleção"])
lista_oitavas.append(ordem_g[0]["Seleção"])
lista_oitavas.append(ordem_g[1]["Seleção"])
lista_oitavas.append(ordem_h[0]["Seleção"])
lista_oitavas.append(ordem_h[1]["Seleção"])
print(lista_oitavas)
a = open('copa_do_mundo.txt', 'a', encoding='utf-8')
a.write(f'\n{"Seleções classificadas para Oitavas de final"}\n'
        f'{lista_oitavas}\n')
a.close()

#tabela oitavas
lista_quartas = []
print(f'\n{"TABELA OITAVAS DE FINAL"}')
salvar_titulo("OITAVAS DE FINAL")
salvar_titulo("Partida 01")
oi1 = pontos4(ordem_a[0]["Seleção"], ordem_b[1]["Seleção"])
oi2= pontos4(ordem_b[1]["Seleção"], ordem_a[0]["Seleção"])
print(f'01 -  {ordem_a[0]["Seleção"]} {oi1} X {oi2} {ordem_b[1]["Seleção"]}')
if oi1 > oi2:
    lista_quartas.append(ordem_a[0]["Seleção"])
    salvar_resultado(ordem_a[0]["Seleção"],oi1, ordem_b[1]["Seleção"],oi2)
elif oi1 < oi2:
    lista_quartas.append(ordem_b[1]["Seleção"])
    salvar_resultado(ordem_a[0]["Seleção"],oi1, ordem_b[1]["Seleção"],oi2)
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    salvar_resultado(ordem_a[0]["Seleção"],oi1,ordem_b[1]["Seleção"],oi2)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_a[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_b[1]["Seleção"]}')
        lista_quartas.append(ordem_a[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_a[0]["Seleção"], penalti_t1, ordem_b[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_a[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_b[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_a[0]["Seleção"]}')
        lista_quartas.append(ordem_b[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_a[0]["Seleção"], penalti_t1, ordem_b[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_b[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_a[0]["Seleção"], ordem_b[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))


#segunda partida
oi3 = pontos4(ordem_c[0]["Seleção"], ordem_d[1]["Seleção"])
oi4= pontos4(ordem_d[1]["Seleção"], ordem_c[0]["Seleção"])
salvar_titulo("Partida 02")
print(f'02 - {ordem_c[0]["Seleção"]} {oi3} X {oi4} {ordem_d[1]["Seleção"]}')
if oi3 > oi4:
    lista_quartas.append(ordem_c[0]["Seleção"])
    salvar_resultado(ordem_c[0]["Seleção"],oi3, ordem_d[1]["Seleção"],oi4)
elif oi3 < oi4:
    lista_quartas.append(ordem_d[1]["Seleção"])
    salvar_resultado(ordem_c[0]["Seleção"],oi3, ordem_d[1]["Seleção"],oi4)
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    salvar_resultado(ordem_c[0]["Seleção"],oi3, ordem_d[1]["Seleção"],oi4)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_c[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_d[1]["Seleção"]}')
        lista_quartas.append(ordem_c[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_c[0]["Seleção"], penalti_t1, ordem_d[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_c[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_d[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_c[0]["Seleção"]}')
        lista_quartas.append(ordem_d[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_c[0]["Seleção"], penalti_t1, ordem_d[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_d[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_c[0]["Seleção"], ordem_d[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))

#terceura partida
oi5 = pontos4(ordem_e[0]["Seleção"], ordem_f[1]["Seleção"])
oi6= pontos4(ordem_f[1]["Seleção"], ordem_e[0]["Seleção"])
salvar_titulo("Partida 03")
print(f'03 - {ordem_e[0]["Seleção"]} {oi5} X {oi6} {ordem_f[1]["Seleção"]}')
if oi5 > oi6:
    lista_quartas.append(ordem_e[0]["Seleção"])
    salvar_resultado(ordem_e[0]["Seleção"], oi5, ordem_f[1]["Seleção"], oi6)
elif oi5 < oi6:
    lista_quartas.append(ordem_f[1]["Seleção"])
    salvar_resultado(ordem_e[0]["Seleção"], oi5, ordem_f[1]["Seleção"], oi6)
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    salvar_resultado(ordem_e[0]["Seleção"],oi5, ordem_f[1]["Seleção"],oi6)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_e[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_f[1]["Seleção"]}')
        lista_quartas.append(ordem_e[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_e[0]["Seleção"], penalti_t1, ordem_f[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_e[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_f[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_e[0]["Seleção"]}')
        lista_quartas.append(ordem_f[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_e[0]["Seleção"], penalti_t1, ordem_f[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_f[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_e[0]["Seleção"], ordem_f[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#quarta partida
oi7 = pontos4(ordem_g[0]["Seleção"], ordem_h[1]["Seleção"])
oi8= pontos4(ordem_h[1]["Seleção"], ordem_g[0]["Seleção"])
print(f'04 - {ordem_g[0]["Seleção"]} {oi7} X {oi8} {ordem_h[1]["Seleção"]}')
salvar_titulo("Partida 04")
if oi7 > oi8:
    lista_quartas.append(ordem_g[0]["Seleção"])
    salvar_resultado(ordem_g[0]["Seleção"], oi7, ordem_h[1]["Seleção"], oi8)
elif oi7 < oi8:
    lista_quartas.append(ordem_h[1]["Seleção"])
    salvar_resultado(ordem_g[0]["Seleção"], oi7, ordem_h[1]["Seleção"], oi8)
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    salvar_resultado(ordem_g[0]["Seleção"], oi7, ordem_h[1]["Seleção"], oi8)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_g[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_h[1]["Seleção"]}')
        lista_quartas.append(ordem_g[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_g[0]["Seleção"], penalti_t1, ordem_h[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_g[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_h[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_g[0]["Seleção"]}')
        lista_quartas.append(ordem_h[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_g[0]["Seleção"], penalti_t1, ordem_h[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_h[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_g[0]["Seleção"], ordem_h[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#quinta partida
oi9 = pontos4(ordem_b[0]["Seleção"], ordem_a[1]["Seleção"])
oi10= pontos4(ordem_a[1]["Seleção"], ordem_b[0]["Seleção"])
print(f'05 - {ordem_b[0]["Seleção"]} {oi9} X {oi10} {ordem_a[1]["Seleção"]}')
salvar_titulo("Partida 05")
if oi9 > oi10:
    lista_quartas.append(ordem_b[0]["Seleção"])
    salvar_resultado(ordem_b[0]["Seleção"], oi9, ordem_a[1]["Seleção"], oi10)
elif oi9 < oi10:
    lista_quartas.append(ordem_a[1]["Seleção"])
    salvar_resultado(ordem_b[0]["Seleção"], oi9, ordem_a[1]["Seleção"], oi10)
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    salvar_resultado(ordem_b[0]["Seleção"], oi9, ordem_a[1]["Seleção"], oi10)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_b[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_a[1]["Seleção"]}')
        lista_quartas.append(ordem_b[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_b[0]["Seleção"], penalti_t1, ordem_a[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_b[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_a[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_b[0]["Seleção"]}')
        lista_quartas.append(ordem_a[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_b[0]["Seleção"], penalti_t1, ordem_a[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_a[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_b[0]["Seleção"], ordem_a[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#sexta partida
oi11 = pontos4(ordem_d[0]["Seleção"], ordem_c[1]["Seleção"])
oi12= pontos4(ordem_c[1]["Seleção"], ordem_d[0]["Seleção"])
print(f'06 - {ordem_d[0]["Seleção"]} {oi11} X {oi12} {ordem_c[1]["Seleção"]}')
salvar_titulo("Partida 06")
salvar_resultado(ordem_d[0]["Seleção"], oi11, ordem_c[1]["Seleção"], oi12)
if oi11 > oi12:
    lista_quartas.append(ordem_d[0]["Seleção"])
elif oi11 < oi12:
    lista_quartas.append(ordem_c[1]["Seleção"])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_d[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_c[1]["Seleção"]}')
        lista_quartas.append(ordem_d[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_d[0]["Seleção"], penalti_t1, ordem_c[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_d[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_c[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_d[0]["Seleção"]}')
        lista_quartas.append(ordem_c[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_d[0]["Seleção"], penalti_t1, ordem_c[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_c[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_d[0]["Seleção"], ordem_c[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#setima partida
oi13 = pontos4(ordem_f[0]["Seleção"], ordem_e[1]["Seleção"])
oi14= pontos4(ordem_e[1]["Seleção"], ordem_f[0]["Seleção"])
print(f'07 - {ordem_f[0]["Seleção"]} {oi13} X {oi14} {ordem_e[1]["Seleção"]}')
salvar_titulo("Partida 07")
salvar_resultado(ordem_f[0]["Seleção"], oi13, ordem_e[1]["Seleção"], oi14)
if oi13 > oi14:
    lista_quartas.append(ordem_f[0]["Seleção"])
elif oi13 < oi14:
    lista_quartas.append(ordem_e[1]["Seleção"])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_f[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_e[1]["Seleção"]}')
        lista_quartas.append(ordem_f[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_f[0]["Seleção"], penalti_t1, ordem_e[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_f[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_e[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_f[0]["Seleção"]}')
        lista_quartas.append(ordem_e[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_f[0]["Seleção"], penalti_t1, ordem_e[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_e[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_f[0]["Seleção"], ordem_e[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#oitava partida
oi15 = pontos4(ordem_h[0]["Seleção"], ordem_g[1]["Seleção"])
oi16= pontos4(ordem_g[1]["Seleção"], ordem_h[0]["Seleção"])
print(f'08 - {ordem_h[0]["Seleção"]} {oi15} X {oi16} {ordem_g[1]["Seleção"]}')
salvar_titulo("Partida 08")
salvar_resultado(ordem_h[0]["Seleção"], oi15, ordem_g[1]["Seleção"], oi16)
if oi15 > oi16:
    lista_quartas.append(ordem_h[0]["Seleção"])
elif oi15 < oi16:
    lista_quartas.append(ordem_g[1]["Seleção"])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {ordem_h[0]["Seleção"]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {ordem_g[1]["Seleção"]}')
        lista_quartas.append(ordem_h[0]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_h[0]["Seleção"], penalti_t1, ordem_g[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_h[0]["Seleção"]))
    elif penalti_t1 < penalti_t2:
        print(f'    {ordem_g[1]["Seleção"]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {ordem_h[0]["Seleção"]}')
        lista_quartas.append(ordem_g[1]["Seleção"])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(ordem_h[0]["Seleção"], penalti_t1, ordem_g[1]["Seleção"], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(ordem_g[1]["Seleção"]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [ordem_h[0]["Seleção"], ordem_g[1]["Seleção"]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_quartas.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))

print(f'\n{"Seleções classificadas para as Quartas de Final:"}\n{lista_quartas}')
salvar_titulo(f'{"Times classificados para Quartas de Final"}\n>>{lista_quartas}')

#QUARTAS DE FINAL
lista_semi_final = []

#partida 01 das quartas
print(f'\n{"QUARTAS DE FINAL"}')
salvar_titulo("QUARTAS DE FINAL")
qr1 = pontos4(lista_quartas[4], lista_quartas[5])
qr2= pontos4(lista_quartas[5], lista_quartas[4])
print(f'01 - {lista_quartas[4]} {qr1} X {qr2} {lista_quartas[5]}')
salvar_titulo("Partida 01 - Quartas de Final")
salvar_resultado(lista_quartas[4], qr1, lista_quartas[5], qr2)
if qr1 > qr2:
    lista_semi_final.append(lista_quartas[4])
elif qr1 < qr2:
    lista_semi_final.append(lista_quartas[5])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_quartas[4]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_quartas[5]}')
        lista_semi_final.append(lista_quartas[4])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[4], penalti_t1, lista_quartas[5], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[4]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_quartas[4]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_quartas[5]}')
        lista_semi_final.append(lista_quartas[5])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[4], penalti_t1, lista_quartas[5], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[5]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_quartas[4], lista_quartas[5]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_semi_final.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#partida 02 da quartas
qr3 = pontos4(lista_quartas[0], lista_quartas[1])
qr4= pontos4(lista_quartas[1], lista_quartas[0])
print(f'02 - {lista_quartas[0]} {qr3} X {qr4} {lista_quartas[1]}')
salvar_titulo("Partida 02 - Quartas de Final")
salvar_resultado(lista_quartas[0], qr3, lista_quartas[1], qr4)
if qr3 > qr4:
    lista_semi_final.append(lista_quartas[0])
elif qr3 < qr4:
    lista_semi_final.append(lista_quartas[1])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_quartas[0]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_quartas[1]}')
        lista_semi_final.append(lista_quartas[0])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[0], penalti_t1, lista_quartas[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[0]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_quartas[1]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_quartas[0]}')
        lista_semi_final.append(lista_quartas[1])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[0], penalti_t1, lista_quartas[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[1]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_quartas[0], lista_quartas[1]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_semi_final.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#partida 03 das quartas de final
qr5 = pontos4(lista_quartas[6], lista_quartas[7])
qr6= pontos4(lista_quartas[7], lista_quartas[6])
print(f'03 - {lista_quartas[6]} {qr5} X {qr6} {lista_quartas[7]}')
salvar_titulo("Partida 03 - Quartas de Final")
salvar_resultado(lista_quartas[6], qr5, lista_quartas[7], qr6)
if qr5 > qr6:
    lista_semi_final.append(lista_quartas[6])
elif qr5 < qr6:
    lista_semi_final.append(lista_quartas[7])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_quartas[6]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_quartas[7]}')
        lista_semi_final.append(lista_quartas[6])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[6], penalti_t1, lista_quartas[7], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[6]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_quartas[7]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_quartas[6]}')
        lista_semi_final.append(lista_quartas[7])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[6], penalti_t1, lista_quartas[7], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[7]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_quartas[6], lista_quartas[7]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_semi_final.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#partida 04 das quartas
qr7 = pontos4(lista_quartas[2], lista_quartas[3])
qr8= pontos4(lista_quartas[3], lista_quartas[2])
print(f'04 - {lista_quartas[2]} {qr7} X {qr8} {lista_quartas[3]}')
salvar_titulo("Partida 04 - Quartas de Final")
salvar_resultado(lista_quartas[2], qr7, lista_quartas[3], qr8)
if qr7 > qr8:
    lista_semi_final.append(lista_quartas[2])
elif qr7 < qr8:
    lista_semi_final.append(lista_quartas[3])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_quartas[2]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_quartas[3]}')
        lista_semi_final.append(lista_quartas[2])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[2], penalti_t1, lista_quartas[3], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[2]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_quartas[3]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_quartas[2]}')
        lista_semi_final.append(lista_quartas[3])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_quartas[2], penalti_t1, lista_quartas[3], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_quartas[3]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_quartas[2], lista_quartas[3]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_semi_final.append(empate_penal)
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
print(lista_semi_final)

#SEMI FINAL
print("SEMI FINAL")
salvar_titulo("SEMI FINAL")
lista_final = []
lista_final_terceiro = []
sm1 = pontos4(lista_semi_final[1], lista_semi_final[0])
sm2= pontos4(lista_semi_final[0], lista_semi_final[1])
print(f'01 - {lista_semi_final[1]} {sm1} X {sm2} {lista_semi_final[0]}')
salvar_titulo("Partida 01 - SEMI FINAL")
salvar_resultado(lista_semi_final[1], sm1, lista_semi_final[0], sm2)
if sm1 > sm2:
    lista_final.append(lista_semi_final[1])
    lista_final_terceiro.append(lista_semi_final[0])
elif sm1 < sm2:
    lista_final.append(lista_semi_final[0])
    lista_final_terceiro.append(lista_semi_final[1])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_semi_final[1]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_semi_final[0]}')
        lista_final.append(lista_semi_final[0])
        lista_final_terceiro.append(lista_semi_final[1])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_semi_final[1], penalti_t1, lista_semi_final[0], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_semi_final[1]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_semi_final[0]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_semi_final[1]}')
        lista_final.append(lista_semi_final[0])
        lista_final_terceiro.append(lista_semi_final[1])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_semi_final[1], penalti_t1, lista_semi_final[0], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_semi_final[0]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_semi_final[1], lista_semi_final[0]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_final.append(empate_penal)
        if lista_semi_final[1] == empate_penal:
            lista_final_terceiro.append(lista_semi_final[0])
        if lista_semi_final[0] == empate_penal:
            lista_final_terceiro.append(lista_semi_final[1])
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))
#partida 02 semi final
sm3 = pontos4(lista_semi_final[3], lista_semi_final[2])
sm4= pontos4(lista_semi_final[2], lista_semi_final[3])
print(f'02 - {lista_semi_final[3]} {sm3} X {sm4} {lista_semi_final[2]}')
salvar_titulo("Partida 02 - SEMI FINAL")
salvar_resultado(lista_semi_final[3], sm3, lista_semi_final[2], sm4)
if sm3 > sm4:
    lista_final.append(lista_semi_final[3])
    lista_final_terceiro.append(lista_semi_final[2])
elif sm3 < sm4:
    lista_final.append(lista_semi_final[2])
    lista_final_terceiro.append(lista_semi_final[3])
else:
    print("     Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_semi_final[3]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_semi_final[2]}')
        lista_final.append(lista_semi_final[3])
        lista_final_terceiro.append(lista_semi_final[2])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_semi_final[3], penalti_t1, lista_semi_final[2], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_semi_final[3]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_semi_final[2]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_semi_final[3]}')
        lista_final.append(lista_semi_final[2])
        lista_final_terceiro.append(lista_semi_final[3])
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_semi_final[3], penalti_t1, lista_semi_final[2], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_semi_final[2]))
    else:
        print("     Empate nos penlties!")
        lista_emp_penal = [lista_semi_final[3], lista_semi_final[2]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        lista_final.append(empate_penal)
        if lista_semi_final[3] == empate_penal:
            lista_final_terceiro.append(lista_semi_final[2])
        if lista_semi_final[2] == empate_penal:
            lista_final_terceiro.append(lista_semi_final[3])
        salvar_titulo("Empate nos penaltes!")
        salvar_titulo("{} venceu a disputa".format(empate_penal))

#FINAL!
campeao = ""
vice = " "
terceiro = " "
print(f"\n{'FINAL'}!")
salvar_titulo("FINAL!")

fn1 = pontos4(lista_final[0], lista_final[1])
fn2 = pontos4(lista_final[1], lista_final[0])
soma_gols_final = fn1 + fn2
print(f'FINAL - {lista_final[0]} {fn1} X {fn2} {lista_final[1]}')
salvar_titulo("FINAL")
salvar_resultado(lista_final[0], fn1, lista_final[1], fn2)
lista_derrota_zero = ["Um dos times resolveu não entrar em campo hoje Arnaldo", "Partida disputada, ambos os times se esforçaram muito",
                      "Vitória merecida!", "A seleção vitoriosa jogou muito hoje Galvão, mereceu levar essa" ]
if fn1 > fn2:
    campeao = lista_final[0]
    vice = lista_final[1]

elif fn1 < fn2:
    campeao = lista_final[1]
    vice = lista_final[0]
else:
    print("    Partida empatada!A disputa será nos penalties")
    roll_t1 = [1, 2, 3, 4, 5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1, 2, 3, 4, 5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_final[0]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_final[1]}')
        campeao = lista_final[0]
        vice = lista_final[1]
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_final[0], penalti_t1, lista_semi_final[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_final[0]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_final[1]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_final[0]}')
        campeao = lista_final[1]
        vice = lista_final[0]
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_final[0], penalti_t1, lista_final[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_final[1]))
    else:
        print(f'    {lista_final[0]} e {lista_final[1]} empataram com {penalti_t1} conversões cada!')
        print("     Empate novamente!pode isso Arnaldo?!")
        salvar_titulo("Empate nos penaltes, pode isso Arnaldo?!!")
        lista_emp_penal = [lista_final[0], lista_final[1]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        if lista_final[0] == empate_penal:
            campeao = lista_final[0]
            vice = lista_final[1]
            salvar_titulo("{} levou o ouro. É a seleção campeã!!!!!".format(campeao))
            salvar_titulo("{} leva a medalha de prata!".format(vice))
        if lista_final[1] == empate_penal:
            campeao = lista_final[1]
            vice = lista_final[0]
            salvar_titulo("{} levou o ouro. É a seleção campeã!!!!!".format(campeao))
            salvar_titulo("{} leva a medalha de prata!".format(vice))

#TERCEIRO COLOCADO
fn3 = pontos4(lista_final_terceiro[0], lista_final_terceiro[1])
fn4= pontos4(lista_final_terceiro[1], lista_final_terceiro[0])
print(f'SEMI-FINAL - {lista_final_terceiro[0]} {fn3} X {fn4} {lista_final_terceiro[1]}')
salvar_titulo("SEMI - FINAL")
salvar_resultado(lista_final_terceiro[0], fn3, lista_final_terceiro[1], fn4)
if fn3 > fn4:
    terceiro = lista_final_terceiro[0]
elif fn3 < fn4:
    terceiro = lista_final_terceiro[1]
else:
    print("    Partida empatada!A disputa será nos penalties")
    roll_t1 = [1,2,3,4,5]
    penalti_t1 = choice(roll_t1)
    roll_t2 = [1,2,3,4,5]
    penalti_t2 = choice(roll_t2)
    if penalti_t1 > penalti_t2:
        print(f'    {lista_final_terceiro[0]} venceu marcando {penalti_t1} gols nos penalties\n'
              f'    contra {penalti_t2} da seleção {lista_final_terceiro[1]}')
        terceiro = lista_final_terceiro[0]
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_final_terceiro[0], penalti_t1, lista_final_terceiro[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_final_terceiro[0]))
    elif penalti_t1 < penalti_t2:
        print(f'    {lista_final_terceiro[1]} venceu marcando {penalti_t2} gols nos penalties\n'
              f'    contra {penalti_t1} da seleção {lista_final_terceiro[0]}')
        terceiro = lista_final_terceiro[1]
        salvar_titulo("Disputa de penaltes!")
        salvar_resultado(lista_final_terceiro[0], penalti_t1, lista_final_terceiro[1], penalti_t2)
        salvar_titulo("{} venceu a disputa".format(lista_final_terceiro[1]))
    else:
        print("     Empate nos penlties, pode isso Arnaldo?!")
        salvar_titulo("Empate nos penaltes, pode isso Arnaldo?!!")
        lista_emp_penal = [lista_final_terceiro[0], lista_final_terceiro[1]]
        empate_penal = choice(lista_emp_penal)
        print(f'A seleção {empate_penal} venceu a disputa!')
        if lista_final_terceiro[0] == empate_penal:
            terceiro = lista_final_terceiro[0]
            salvar_titulo("{} levou o bronze pra casa!!!!!".format(terceiro))
        if lista_final_terceiro[1] == empate_penal:
            terceiro = lista_final_terceiro[1]
            salvar_titulo("{} levou o bronze pra casa!!!!!".format(terceiro))

print(f'\nA seleção {campeao} levou o ouro!!! É CAMPEÃ!')
print(f'A medalha de prata fica com a seleção {vice}!')
print("{} levou o bronze pra casa!!!!!".format(terceiro))
salvar_titulo(f'\nA seleção {campeao} levou o ouro!!! É CAMPEÃ!')
salvar_titulo(f'A medalha de prata fica com a seleção {vice}!')
salvar_titulo("{} levou o bronze pra casa!!!!!".format(terceiro))


print()
print(localizar("França"))
salvar_titulo(localizar("França"))
print(localizar("Inglaterra"))
salvar_titulo(localizar("Inglaterra"))
print(localizar("Nigth City"))
salvar_titulo(localizar("Nigth City"))


