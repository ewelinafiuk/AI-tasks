#Ewelina Fiuk, 304037
from Bayesian_Network import BayesianNetwork
import random

def main():

        net = BayesianNetwork()
        a = "Minus"
        b = "Snieg"
        c = "Narty"
        d = "Oblodzenie"
        e = "Wypadki"
        
        net.add_variable(a)
        net.add_variable(b)
        net.add_variable(c)
        net.add_variable(d)
        net.add_variable(e)
        
        net.add_edge(a,b)
        net.add_edge(b,c)
        net.add_edge(b,d)
        net.add_edge(c,e)
        net.add_edge(d,e)
        
        n1 = [0.3]
        n2 = [0.2, 0.1]
        n3 = [0.8,0.3]
        n4 = [0.6,0.1]
        n5 = [0.3,0.1,0.2,0.05]

        net.set_probabilities(a, n1)
        net.set_probabilities(b, n2)
        net.set_probabilities(c, n3)
        net.set_probabilities(d, n4)
        net.set_probabilities(e, n5)

        A = random.choice([True, False])
        B = random.choice([True, False])
        C = random.choice([True, False])
        D = random.choice([True, False])
        E = random.choice([True, False])
        

        print(f"{a} is", A)
        print(f"{b} is", B)
        print(f"{c} is", C)
        print(f"{d} is", D)
        print(f"{e} is", E)


        r1 = net.gibbs_sampling(a, {b:B, c: C, d: D, e:E}, 100)
        r2 = net.gibbs_sampling(b, {a:A,  c: C, d: D, e:E }, 100)
        r3 = net.gibbs_sampling(c, {a:A, b:B,  d: D,  e:E}, 100)
        r4 = net.gibbs_sampling(d, {a:A, b:B, c: C,  e:E}, 100)
        r5 = net.gibbs_sampling(e, {a:A, b:B, c: C, d: D}, 100)


        results = {a:r1, b:r2, c:r3, d:r4, e:r5}

        print(f"Probability for {a}: " + str(r1))
        print(f"Probability for {b}: " + str(r2))
        print(f"Probability for {c}: " + str(r3))
        print(f"Probability for {d}: " + str(r4))
        print(f"Probability for {e}: " + str(r5))

        for r in results.items():
                if r[1] > 0.5:
                        print(r[0], "Is probably gonna happen")
        

if __name__ == '__main__':
    main()
