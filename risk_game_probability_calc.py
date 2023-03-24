
import numpy as np 
import random

##HU
##03/2023

#https://algebra.math.bme.hu/2018-19-1/BMETE91AM46-A1#5
#https://web.mit.edu/sp.268/www/risk.pdf

##Experimental probability calculation codes 
#-----------------------------------------------------------------------------------------------------------------#

def roll_dice(n): # dice are thrown imaginatively
    temp_dice=[]

    for i in range(n):
        temp_dice.append(int(random.random()*6)+1)
    
    temp_dice.sort(reverse=True) # array sorted in descending order
                                 # to reach first and second highest value
    return temp_dice


def lets_play(n):
    
    #total results
    
    #counters soldier losses
    att_loss_2s=0
    def_loss_2s=0
    one_on_one=0
    
    #counters of battle wins
    attacker_wins=0
    defender_wins=0
    draw=0
    
    for i in range (n):
        red_dices=roll_dice(3)  #attacker rolled dices array
        blue_dices=roll_dice(2) #defender rolled dices array
        
        att_soldier=3 # attacker soldier unit
        def_soldier=2 # defender soldier unit 
        
        # compare dices
        for i in range(2):
            
            if red_dices[i] > blue_dices[i]:
                def_soldier -=1
            else :
                att_soldier -=1 
   
 
        # determination of results        
        if def_soldier == 0 :  # If the remaining number of defender soldiers is zero, defender 2 soldiers are lost.
            def_loss_2s+=1     # So attacker wins
            attacker_wins+=1
        elif def_soldier == 1 : # If the remaining number of defender soldiers is oen, attacker and defender one soldier is lost.
            one_on_one+=1       # So with draw 
            draw+=1
        elif def_soldier == 2 : # If the remaining number of defender soldiers is two, attacker 2 soldiers are lost.
            att_loss_2s +=1     # So defender wins
            defender_wins+=1
            
    return [[attacker_wins,defender_wins,draw],[att_loss_2s,def_loss_2s,one_on_one]]
          


##Exact probability calculation codes 
#-----------------------------------------------------------------------------------------------------------------#

red_dices1=[1,2,3,4,5,6]
red_dices2=[1,2,3,4,5,6]
red_dices3=[1,2,3,4,5,6]

blue_dices1=[1,2,3,4,5,6]
blue_dices2=[1,2,3,4,5,6]

red_dices_sequence=[]
blue_dices_sequence=[]


for i in range(len(red_dices1)):
    for j in range(len(red_dices1)):
        for k in range(len(red_dices1)):
            temp_arr=[]
            temp_arr=[red_dices1[i],red_dices2[j],red_dices3[k]]
            red_dices_sequence.append(temp_arr)
            #red_dices_sequence.append()

for i in range(len(blue_dices1)):
    for j in range(len(red_dices1)):
        temp_arr=[]
        temp_arr=[blue_dices1[i],blue_dices2[j]]
        blue_dices_sequence.append(temp_arr)
        #red_dices_sequence.append()


 


def select_max_two_val(arr):#Choose the two with the highest value from the 3 red dice rolled
       
    red_max_selected_seq=arr
    
    for i in range(len(red_dices_sequence)):
            temp_arr=[]
            temp_arr=red_max_selected_seq[i]
            min_val=min(temp_arr)
            min_val_index=temp_arr.index(min_val)
            temp_arr.pop(min_val_index)
            red_max_selected_seq[i]=temp_arr

    
    return red_max_selected_seq     

       
def events_calc(red_arr,blue_arr):# calculate all possible events 

    attacker_wins_batt=0
    defender_wins_batt=0
    draw_=0
 
    for i in range(216):#6*6*6 dices combination
        red_temp_array=red_arr[i] 
        
        for j in range(36):#6*6 dices combination
            blue_temp_array=blue_arr[j]
            
            for k in range(1):# compare first dices values in first if block
                              # and compare seconds dices values in second if blocks and calculate results 
                    
                if red_temp_array[k]>blue_temp_array[k]: # highest value first red dice> highest value first blue dice
                    if red_temp_array[k+1]>blue_temp_array[k+1]: # compare second dices 
                        attacker_wins_batt+=1
                    elif red_temp_array[k+1]<blue_temp_array[k+1]:
                        draw_+=1
                        
                elif red_temp_array[k]<blue_temp_array[k]: # highest value first red dice< highest value first blue dice
                    if red_temp_array[k+1]<=blue_temp_array[k+1]: # compare second dices 
                        defender_wins_batt+=1
                    elif red_temp_array[k+1]>blue_temp_array[k+1]:
                        draw_+=1
                
                elif red_temp_array[k]==blue_temp_array[k]: # highest value first red dice= highest value first blue dice
                    if red_temp_array[k+1]>=blue_temp_array[k+1]: # compare second dices 
                        defender_wins_batt+=1
            
    return [attacker_wins_batt,defender_wins_batt,draw_]


##Invoke functions and calculate probability
#-----------------------------------------------------------------------------------------------------------------#

# Simulated 1000 times the experiment
iter_numb = 1000 # iteration number
results1=lets_play(iter_numb) 

# Simulated  1000000  times the experiment
iter_numb2 =  1000000  # iteration number
results2=lets_play(iter_numb2)    

#Exact Probability Calculate
max_val_selected_dice=select_max_two_val(red_dices_sequence)
#Chosen the two with the highest value from the 3 red dice rolled 
results_of_events=events_calc(max_val_selected_dice,blue_dices_sequence)
sum_of_all_events=results_of_events[0]+results_of_events[1]+results_of_events[2]


print('\n                     ','Attacker ','Draw     ','Defender   ')
print('1000 experiment      ',"{:.5f}".format(results1[0][0]/iter_numb),"  {:.5f}".format(results1[0][2]/iter_numb),
      "  {:.5f}".format(results1[0][1]/iter_numb))
print('1000000 experiment   ',"{:.5f}".format(results2[0][0]/iter_numb2),"  {:.5f}".format(results2[0][2]/iter_numb2),
      "  {:.5f}".format(results2[0][1]/iter_numb2))
print('Probability          ',"{:.5f}".format(results_of_events[0]/sum_of_all_events),"  {:.5f}".format(results_of_events[2]/sum_of_all_events),
"  {:.5f}".format(results_of_events[1]/sum_of_all_events))
