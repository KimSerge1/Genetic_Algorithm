import math
import random
import pylab
import os
from matplotlib import mlab

def file_is_empty():
    return os.stat('/home/sergey/Documents/GA/lab1/pokolenie.txt').st_size==0

def IntToByte(n):
    b = 16384
    bit=''
    while b > 0:
        z = n & b
        if z == 0:
            bit=bit+'0'
        else:
            bit=bit+'1'
        b = b >> 1
    return bit

def func (x):
    if x==0:
        return 1.0
    return math.cos(x)/(1+math.exp(-x))
iii=0
population=2000
maksimum=open('pokolenie.txt','r')
xmin = 0.5
xmax = 10.0
dx=0.1
xlist = mlab.frange (xmin, xmax, dx)
ylist1 = [func (x) for x in xlist]
osobi=1
cross_mass2=[]
while iii<population:
    if population!= (population%2):
        xlist2=[]
        zip_mass=[]
        zip_mass2=[]
        zip_mass_temp=[]
        generation=[]
        if file_is_empty()==True:
            while osobi<=population:
                argument=random.randint(0,16384)
                zip_mass_temp.append(argument)
                peremennaya = 0.5+argument*((10-0.5)/(16384))
                gen_predok=peremennaya
                ylist2 = func(gen_predok)
                pylab.scatter (gen_predok,func(gen_predok),color="red")
                generation.append(ylist2)
                xlist2.append(gen_predok)
                osobi = osobi+1
            zip_mass=sorted(zip(zip_mass_temp,generation),key=lambda item : item[1],reverse=True)   
            print(zip_mass)
            pylab.plot (xlist, ylist1)
            pylab.show()
        else:
            file_file=open("pokolenie.txt","r")
            cross_mass2=[line.strip() for line in file_file]
            population=int(len(cross_mass2))
            osobii=1
            generation_second=[]
            ylist2_second=[]
            xlist2_second=[]
            print(cross_mass2)
            while osobii<=population:
                argument=int(cross_mass2[osobii-1])
                zip_mass_temp.append(argument)
                peremennaya = 0.5+argument*((10-0.5)/(16384))
                gen_predok=peremennaya
                ylist2_second = func(gen_predok)
                ylist2=ylist2_second
                pylab.scatter (gen_predok,func(gen_predok),color="red")
                generation_second.append(ylist2)
                generation=generation_second
                xlist2_second.append(gen_predok)
                xlist2=xlist2_second
                osobii = osobii+1
            zip_mass=sorted(zip(zip_mass_temp,generation),key=lambda item : item[1],reverse=True)   
            print(zip_mass)
            print(generation)
            pylab.plot (xlist, ylist1)
            pylab.show()
        print(generation)
    else:
        print("Maksimum :")
        print(maksimum.read())
        maksimum.close()
        break
    population=int(len(zip_mass))
    reproduction=population/2
    population=reproduction
    reproduction_generation=[]
    repro=0
    while repro<reproduction:
        reproduction_generation.append(zip_mass[repro])
        repro=repro+1
    print(reproduction_generation)

    cross_mass=zip_mass
    cross_mass111=[]
    cross_mass222=[]
    cr_mass=[]

    cross_mass111,cross_mass222=zip(*zip_mass)

    repro=0
    while repro<reproduction:
        cr_mass.append(IntToByte(cross_mass111[repro]))
        repro=repro+1
    cross_mass2=cr_mass


    repro=0
    maybe_cross=random.randint(0,1)
    if maybe_cross==1:
        while repro<reproduction:
            crossingover_point=random.randint(0,15)
            cross1=cross_mass2[repro]
            if len(cross_mass2)>1:
                cross2=cross_mass2[repro+1]
            else:
                print("Find maksimum!")
                break
            cross11=cross1[0:crossingover_point]
            cross22=cross2[0:crossingover_point]
            cross12=cross2[crossingover_point:15]
            cross21=cross1[crossingover_point:15]
            cross_one=cross11+cross12
            cross_two=cross22+cross21
            cross_mass2.append(cross_one)
            cross_mass2.append(cross_two)
            repro=repro+3

    maybe_mutation=random.random()

    if maybe_mutation<=0.001:
        change_hromosoma=random.randint(0,len(cross_mass2)-1)
        change_genom=random.randint(0,15)
        mutation=cross_mass2[change_hromosoma]
        mutation_genom=[]

        mut=0
        while mut<15:
            mutation_genom.append(mutation[mut])
            mut=mut+1 
        mut=0

        if mutation[change_genom-1]=='1':
            mutation_genom[change_genom-1]='0'
            cross_mass2[change_hromosoma-1]=mutation_genom[0]+mutation_genom[1]+mutation_genom[2]+mutation_genom[3]+mutation_genom[4]+mutation_genom[5]+mutation_genom[6]+mutation_genom[7]+mutation_genom[8]+mutation_genom[9]+mutation_genom[10]+mutation_genom[11]+mutation_genom[12]+mutation_genom[13]+mutation_genom[14]

            len_mass=0
            while len_mass<len(cross_mass2):
                cross_mass2[len_mass]=int((cross_mass2[len_mass]),2)
                len_mass=len_mass+1
            len_mass=0
            while len_mass<len(cross_mass2):
                cross_mass2[len_mass]=str(cross_mass2[len_mass])
                len_mass=len_mass+1
            len_mass=0
            my_file=open("pokolenie.txt","w")
            while len_mass<len(cross_mass2):    
                my_file.write(str(cross_mass2[len_mass])+'\n')
                len_mass=len_mass+1
            my_file.close()
        else:
            mutation_genom[change_genom-1]='1'
            cross_mass2[change_hromosoma-1]=mutation_genom[0]+mutation_genom[1]+mutation_genom[2]+mutation_genom[3]+mutation_genom[4]+mutation_genom[5]+mutation_genom[6]+mutation_genom[7]+mutation_genom[8]+mutation_genom[9]+mutation_genom[10]+mutation_genom[11]+mutation_genom[12]+mutation_genom[13]+mutation_genom[14]
            len_mass=0
            while len_mass<len(cross_mass2):
                cross_mass2[len_mass]=int(cross_mass2[len_mass],2)
                len_mass=len_mass+1
            len_mass=0
            while len_mass<len(cross_mass2):
                cross_mass2[len_mass]=str(cross_mass2[len_mass])
                len_mass=len_mass+1
            len_mass=0
            my_file=open("pokolenie.txt","w")
            while len_mass<len(cross_mass2):    
                my_file.write(str(cross_mass2[len_mass])+'\n')
                len_mass=len_mass+1
            my_file.close()

    else:
        len_mass=0
        temp_mass=[]
        while len_mass<len(cross_mass2):
            temp_mass.append(int(cross_mass2[len_mass],2))
            len_mass=len_mass+1
        cross_mass2=temp_mass
        temp_mass=[]
        len_mass=0
        while len_mass<len(cross_mass2):
            temp_mass.append(str(cross_mass2[len_mass]))
            len_mass=len_mass+1
        cross_mass2=temp_mass
        temp_mass=[]
        len_mass=0
        my_file=open("pokolenie.txt","w")
        while len_mass<len(cross_mass2):    
            my_file.write(str(cross_mass2[len_mass])+'\n')
            len_mass=len_mass+1
        my_file.close()
iii=iii+1