"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    new_list=[]
    for score in student_scores:
        new_list.append(round(score))
    return new_list

def count_failed_students(student_scores):
    count=0
    for score in student_scores:
        if score<=40:
            count+=1
    return count

def above_threshold(student_scores, threshold):
    new_list=[]
    for score in student_scores:
        if score>=threshold:
            new_list.append(score)
    return new_list

def letter_grades(highest):
    interval=round((highest-40)/4)
    return [41,41+interval,41+(interval*2),41+(interval*3)]

def student_ranking(student_scores, student_names):
    new_list=[]
    for i in range(0,len(student_scores)):
        new_list.append(str(i+1)+'. '+ student_names[i]+': '+str(student_scores[i])) 
    return new_list



def perfect_score(student_info): 
    list_100=[]
    for eachlist in student_info:
        if eachlist[1]==100:
            list_100=eachlist
            break
    return list_100
    
