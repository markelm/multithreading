from time import perf_counter_ns
import simples as sp
import mtrhead as mt
import matplotlib.pyplot as plt

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))
data = data

def run_solution(data, n_threads):

    avg_simples = 0
    avg_mtthread = 0

    #print('\n\nanalise de %d valores\n\n'%(len(data)))

    for i in range(50):

        start1 = perf_counter_ns()
        primo_sp = sp.resolve_simples(data)
        finish1 = perf_counter_ns()

        start2 = perf_counter_ns()
        primo_mt = mt.resolve_thread(data, n_threads)
        finish2 = perf_counter_ns()

        avg_simples += (finish1-start1)/1000000
        avg_mtthread += (finish2-start2)/1000000

        speedup = avg_simples/avg_mtthread

        """ print('simples          > threads')
        print('%f ms   > %f ms  : tempo execucao'%((finish1-start1)/1000000,(finish2-start2)/1000000))
        print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt)) """

    """ print('simples          > threads')
    print('%f ms   > %f ms  : tempo execucao'%(avg_simples/1, avg_mtthread/1))
    print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt)) """

    return {'Numero de threads': n_threads,
            'SpeedUp': speedup,
            'Runtime simples': avg_simples/50,
            'Primos simples': primo_sp,
            'Runtime multithread': avg_mtthread/50,
            'Primos multithread': primo_mt
            }


#run_solution(data, 5)

def plot_graph(func, data, limit):

    result = list()
    for i in range(1, limit + 1):
        r = func(data, i)
        result.append(r)

    x = []
    y = []
    for i in range(len(result)):
        if i == 0:
            x.append(1)
            y.append(1)
        else:
            x.append(result[i]['Numero de threads'])
            y.append(result[i]['SpeedUp'])

    plt.plot(x, y)
    plt.show()

    print(result)

plot_graph(run_solution, data, 6)


