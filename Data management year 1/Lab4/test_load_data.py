# ECOR 1042 Lab 4 - team submission

#import check module here

#import load_data module here

# Update "" with your the name of the active members of the team
__author__ = "Ethan Robitaille, Rana Taunk, Prasidhaan Anandaviamalan"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)
    
    check.equal(isinstance(student_school_list('student-test.csv', 'MS'), list), True)
    
    check.equal(isinstance(student_school_list('student-test.csv', 'BD'), list), True)
    
    check.equal(isinstance(student_school_list('student-test.csv', 'CF'), list), True)
    
    #test that student_age_list returns a list (3 different test cases required)
    
    check.equal(isinstance(student_age_list('student-test.csv', 15), list), True)
    
    check.equal(isinstance(student_age_list('student-test.csv', 18), list), True)
    
    check.equal(isinstance(student_age_list('student-test.csv', 17), list), True)
    
    #test that student_health_list returns a list (3 different test cases required)
    
    check.equal(isinstance(student_health_list('student-test.csv', 2), list), True)
    
    check.equal(isinstance(student_health_list('student-test.csv', 4), list), True)
    
    check.equal(isinstance(student_health_list('student-test.csv', 3), list), True)
    
    #test that student_failures_list returns a list (3 different test cases required)
    
    check.equal(isinstance(student_failures_list('student-test.csv', 0), list), True)
    
    check.equal(isinstance(student_failures_list('student-test.csv', 2), list), True)
    
    check.equal(isinstance(student_failures_list('student-test.csv', 3), list), True)
    
    #test that load_data returns a list (6 different test cases required)
    
    check.equal(isinstance(load_data('student-test.csv', ('School', 'MB')), list), True)
    
    check.equal(isinstance(load_data('student-test.csv', ('Age', 15)), list), True)
    
    check.equal(isinstance(load_data('student-test.csv', ('Health', 3)), list), True)
    
    check.equal(isinstance(load_data('student-test.csv', ('Failures', 0)), list), True)
    
    check.equal(isinstance(load_data('student-test.csv', ('Failures', 69)), list), True)
    
    check.equal(isinstance(load_data('student-test.csv', ('All', -1)), list), True)
    
    #test that add_average returns a list (3 different test cases required)
    
    check.equal(isinstance(add_average(load_data('student-test.csv', ('Age', 15))), list), True)
    
    check.equal(isinstance(add_average(load_data('student-test.csv', ('Health', 3))), list), True)
    
    check.equal(isinstance(add_average(load_data('student-test.csv', ('All', -1))), list), True)
    
    check.summary()

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list("student-test.csv", "A")), 0)
    check.equal(len(student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(student_school_list("student-test.csv", "MS")), 4)
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 16)), 2)
    check.equal(len(student_age_list("student-test.csv", 15)), 3)
    check.equal(len(student_age_list("student-test.csv", 7)), 0)    
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 777)), 0)     
    
    #test that student_failures_list returns a list  with the correct lenght(3 different test cases required)
    check.equal(len(student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(student_failures_list("student-test.csv", 3)), 1)
    check.equal(len(student_failures_list("student-test.csv", 400)), 0)     
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data("student-test.csv", ("ALL", -60))), 15) 
    check.equal(len(load_data("student-test.csv", ("school", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("age", 15))), 3)
    check.equal(len(load_data("student-test.csv", ("health", 3))), 8)
    check.equal(len(load_data("student-test.csv", ("failures", 0))), 11)
    check.equal(len(load_data("student-test.csv", ("failures", 8))), 0)
    
    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(add_average([])), 0)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("ALL", -60))), 15)
    
    check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    testfile = "student-test.csv"
    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_school_list(testfile,"GP")[0], {'Age': 18, 'StudyTime': 2, 'Failures':0, 'Health': 3, 'Absences': 6, 'G1':5, 'G2':6, 'G3':6})
    check.equal(load_data.student_school_list(testfile,"GP")[-1], {'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health':3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_school_list(testfile,"GP")[1], {'Age':17 , 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
        
    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_age_list(testfile,15)[0],{'School': 'GP' , 'StudyTime': 2 , 'Failures': 3 , 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_age_list(testfile,15)[-1],{'School': 'CF' , 'StudyTime': 5, 'Failures': 2 , 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    check.equal(load_data.student_age_list(testfile,15)[1],{'School': 'MB' , 'StudyTime': 1, 'Failures': 0 , 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12})
        
    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_health_list(testfile,3)[0],{'School': 'GB', 'Age': 2, 'StudyTime': 0, 'Failures': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_health_list(testfile,3)[-1],{'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences':1, 'G1':13, 'G2': 12, 'G3': 12})
    check.equal(load_data.student_health_list(testfile,3)[1],{'School': 'GB', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_failures_list(testfile, 1)[0],{'School': 'CF','Age': 16,'StudyTime': 2.0,'Health': 5,'Absences': 4,'G1': 10,'G2': 12,'G3': 12})
    check.equal(load_data.student_failures_list(testfile, 2)[0],{'School': 'CF','Age': 15,'StudyTime': 5.0,'Health': 3,'Absences': 6,'G1': 5,'G2': 9,'G3': 7})
    check.equal(load_data.student_failures_list(testfile, 0)[0],{'School': 'GP','Age': 18,'StudyTime': 2.0,'Health': 3,'Absences': 6,'G1': 5,'G2': 6,'G3': 6})

    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data.load_data(testfile, ('School', 'GP'))[0],{'Age': 18,'StudyTime': 2.0,'Failures': 0,'Health': 3,'Absences': 6,'G1': 5,'G2': 6,'G3': 6})
    check.equal(load_data.load_data(testfile, ('Age', 17))[0],{'School': 'GP','StudyTime': 2.0,'Failures': 0,'Health': 3,'Absences': 4,'G1': 5,'G2': 5,'G3': 6})
    check.equal(load_data.load_data(testfile, ('Health', 1))[0],{'School': 'MS','Age': 17,'StudyTime': 3.0,'Failures': 0,'Absences': 7,'G1': 10,'G2': 9,'G3': 9})
    check.equal(load_data.load_data(testfile, ('Failures', 1))[0],{'School': 'CF','Age': 16,'StudyTime': 2.0,'Health': 5,'Absences': 4,'G1': 10,'G2': 12,'G3': 12})
    check.equal(load_data.load_data(testfile, ('All', 6))[0],{'School': 'GP','Age': 18,'StudyTime': 2.0,'Failures': 0,'Health': 3,'Absences': 6,'G1': 5,'G2': 6,'G3': 6})
    check.equal(load_data.load_data(testfile, ('This doesnt work', 6)),[])

     #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    check.equal(load_data.add_average(load_data.load_data(testfile, ('School', 'GP')))[0],{'Age': 18,'StudyTime': 2.0,'Failures': 0,'Health': 3,'Absences': 6,'G1': 5,'G2': 6,'G3': 6, 'G_Avg': 5.67 })
    check.equal(load_data.add_average(load_data.student_failures_list(testfile, 1))[0],{'School': 'CF','Age': 16,'StudyTime': 2.0,'Health': 5,'Absences': 4,'G1': 10,'G2': 12,'G3': 12, 'G_Avg': 11.33 })
    check.equal(load_data.add_average(load_data.student_age_list(testfile, 15))[0],{'School': 'GP','StudyTime': 2.0,'Failures': 3,'Health': 3,'Absences': 10,'G1': 7,'G2': 8,'G3': 10, 'G_Avg': 8.33 })
    
    check.summary()

#Place test_add_average function here
def test_add_average():
    #Complete the function with your test cases
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))), len(student_school_list("student-test.csv", "GP")))
    check.equal(len(add_average(student_age_list("student-test.csv", 18))), len(student_age_list("student-test.csv", 18)))
    check.equal(len(add_average(student_health_list("student-test.csv", 5))), len(student_health_list("student-test.csv", 5)))
    check.equal(len(add_average(student_failures_list("student-test.csv", 3))), len(student_failures_list("student-test.csv", 3)))
    check.equal(len(add_average(load_data("student-test.csv", ("ALL", -60)))), len(load_data("student-test.csv", ("ALL", -60))))
    
    #test that the function returns an empty list when it is called whith an empty list
    check.equal(len(add_average(student_school_list("student-test.csv", "A"))), 0)
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))[1].keys()), len(student_school_list("student-test.csv", "GP")[1].keys())+1)
    check.equal(len(add_average(student_age_list("student-test.csv", 18))[1].keys()), len(student_age_list("student-test.csv", 18)[1].keys())+1)
    check.equal(len(add_average(student_health_list("student-test.csv", 5))[0].keys()), len(student_health_list("student-test.csv", 5)[0].keys())+1)
    check.equal(len(add_average(student_failures_list("student-test.csv", 3))[0].keys()), len(student_failures_list("student-test.csv", 3)[0].keys())+1)
    check.equal(len(add_average(load_data("student-test.csv", ("School", 'GP')))[0].keys()), len(load_data("student-test.csv", ("School", 'GP'))[0].keys())+1)
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(add_average(student_school_list("student-test.csv", "GP"))[0]['G_Avg'], 5.67)
    check.equal(add_average(student_age_list("student-test.csv", 18))[2]['G_Avg'], 12.33)
    check.equal(add_average(student_health_list("student-test.csv", 5))[1]['G_Avg'], 4.33)
    check.equal(add_average(student_failures_list("student-test.csv", 3))[0]['G_Avg'], 8.33)
    check.equal(add_average(student_school_list("student-test.csv", "GP"))[2]['G_Avg'], 8.33)
   
    
    check.summary()


# Do NOT include a main script in your submission
