# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ethan Robitaille,  Rana Taunk, Prasidhaan Anandavimalana"

# Update "" with your team (e.g. T102)
__team__ = "T114"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(filename: str, school: str) -> list:
        """ 
     Returns a list of students, stored as a dictionary, that attended the 
    school mentioned in the parameters. 
    
    Precondition:
    filename == 'student-mat.csv'
    type(school) == str
    
    Examples:
    
    >>> student_school_list('student-mat.csv', 'GP')
    [{'Failures': 0.0, 'Age': 18.0, 'Studytime': 2.0, 'Health': 3.0, 'Absences': 6.0, 'G1': 5.0, 'G2': 6.0, 'G3': 6.0},
    {another element}, …]
    
    >>> student_school_list('student-mat.csv', 'MS')
    [{'Failures': 0.0, 'Age': 18.0, 'Studytime': 2.0, 'Health': 5.0, 'Absences': 2.0, 'G1': 11.0, 'G2': 11.0, 'G3': 11.0},
    {another element}, …]
    
    >>> student_school_list('student-mat.csv', 'BD')
    [{'Failures': 1.0, 'Age': 18.0, 'Studytime': 2.0, 'Health': 2.0, 'Absences': 0.0, 'G1': 7.0, 'G2': 7.0, 'G3': 0.0},
    {another element}, …]
    
    """
        student_list =[]
        file = open(filename,"r")
        for line in file:
                word_list = line.strip("\n").split(",")
                if word_list[0] == str(school):
                        studentDict = {}
                        studentDict['Failures'] = float(word_list[3])
                        studentDict['Age'] = float(word_list[1])
                        studentDict['Studytime'] = float(word_list[2])
                        studentDict['Health'] = float(word_list[4])
                        studentDict['Absences'] = float(word_list[5])
                        studentDict['G1'] = float(word_list[6])
                        studentDict['G2'] = float(word_list[7])
                        studentDict['G3'] = float(word_list[8])
                        student_list.append(studentDict)
                        continue
                else:
                        continue
        return student_list

#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename: str, num: int) -> list:
	
	"""
    Returns a list of students (stored as a dictionary) whos health equals 
    the value provided as an input parameter.
    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
    'G1': 9, 'G2': 11, 'G3': 7},
    {another element},
    …
    ]
    """
	file = open(filename, "r")
	student_info = []
	for line in file:
		eachline = line.strip().split(',')
		if eachline[4] == str(num):
			studentDict = {}
			studentDict['School'] = str(eachline[0])
			studentDict['Age'] = float(eachline[1])
			studentDict['Studytime'] = float(eachline[2])
			studentDict['Failures'] = float(eachline[3])
			studentDict['Absences'] = float(eachline[5])
			studentDict['G1'] = float(eachline[6])
			studentDict['G2'] = float(eachline[7])
			studentDict['G3'] = float(eachline[8])
			student_info.append(studentDict)
	return student_info

#==========================================#
# Place your student_age_list function after this line

def student_age_list(name: str,age: int) -> list:
	"""
     Returns a list of students, stored as a dictionary, that attended the 
    Age mentioned in the parameters. 
    
    Precondition:
    filename == 'student-mat.csv'
    age == int
    
    Examples:
    
    >>> student_age_list('student-mat.csv', 18)
    [{'School': 'MS', 'Failures': 0.0,, 'Studytime': 2.0, 'Health': 3.0, 'Absences': 6.0, 'G1': 5.0, 'G2': 6.0, 'G3': 6.0},
    {another element}, …]
    
    >>> student_age_list('student-mat.csv', 20)
    [{'School': 'GP', 'Failures': 2, 'Studytime': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 10, 'G3': 11},
    {another element}, …]
    
    """
	file = open(name, 'r')
	header = []
	a = file.readline()
	header= a.strip().split(',')
	b = header[-1]
	c = b.split("\n")
	header[-1] = c[0]
	dic={}
	lst = []
	for row in file:
		csvreader = row.strip().split(',')
		for ch in range(len(csvreader)):
			dic[header[ch]] = csvreader[ch]
		if int(csvreader[1]) == age:
			a = dict.copy(dic)
			a.pop('Age')
			lst.append(a)  
	return lst

#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, num: int) -> list[dict]:
	""" 
	Return a list that contains dicitionaries with the information on the
    students who have the number of failures specified by the user. 
    
    Precondition: num >= 0 
    
    >>> student_failures_list('student-mat.csv',0)
    [{'School": "GP", 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6,
    'G1': 5, 'G2': 6, 'G3':6},
    {another element}, ...]
    
    >>> student_failures_list('student-mat.csv',2)
    [{'School": "GP", 'Age': 16, 'StudyTime': 1, 'Health': 5, 'Absences': 14,
    'G1': 6, 'G2': 9, 'G3':8},
    {another element}, ...]
    
    >>> student_failures_list('student-mat.csv', 100)
    [] 
    """   
	student_list = []
	with open(filename, "r") as file:
		header = file.readline().strip().split(",")
		for line in file:
			word_list = line.strip().split(",")
			student_dict = {}
			if int(word_list[3]) == num:
				#student_dict = {}
				for i in range(len(header)):
					if header[i] != "Failures":
						if i==0:
							student_dict[header[i]] = word_list[i]
						elif i==2:
							student_dict[header[i]] = float(word_list[i])
						else:
							student_dict[header[i]] = int(word_list[i])
			if len(student_dict) > 0:
				student_list.append(student_dict)
	return student_list


#==========================================#
# Place your load_data function after this line
def load_data(name:str, filter1:tuple)->list:
	"""
	Inputs a file name and a key filter that returns a 
	list of dictionaries without the filter key.
	
	Precondition:
	
	name == 'student-mat.csv'
	filter1 is a tuple with a string from the key list and an int
	
	Example:
	
       >>>load_data('student-mat.csv', ('all', -1))
       [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
       'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
       {another element},
       ]
       >>> load_data('student-mat.csv', ('failures', 0))
       [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {another element}, …]

       """
	
	file = open(name, "r")
	header = []
	a = file.readline()
	header= a.strip().split(',')
	b = header[-1]
	c = b.split("\n")
	header[-1] = c[0]  
	dic={}
	lst = []
	for i in range(len(header)):
		if filter1[0].lower() == header[i].lower():
			pos = i
		elif filter1[0].lower() == "all":
			pos = 1
	for i in range(len(header)):
		for row in file:
			dic={}
			csvreader= row.strip().split(',')                                  	 
			for ch in range(len(csvreader)):
				dic[header[ch].lower()] = csvreader[ch]
			if csvreader[pos] == str(filter1[1]):
				a = dict.copy(dic)
				a.pop(filter1[0].lower())
				lst.append(a)	
			
	if filter1[0].lower() == 'all':		
		lst=[]
		file = open(name, "r")
		for i in range(len(header)):
			for row in file:
				dic={}
				csvreader= row.strip().split(',')            	 
				for ch in range(len(csvreader)):
					dic[header[ch]] = csvreader[ch]  
				a = dict.copy(dic)
				lst.append(a)
		lst.pop(0)
		return lst
	return lst  

#==========================================#
# Place your add_average function after this line
def add_average(inpu:list)->list:
	"""
	Returns the sum of the average of the student’s grades (G1, G2 and G3) as an
	additional attribute to the dictionary
	
	Precondition:
	
	type(inpu) == list 
	
	Examples:
	
        >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,'Failures': 1, 'Health': 3, 'Absences': 7,'G1': 5, 'G2': 6, 'G3': 6}, {another element}, … ] )

        [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 }, {another element}, … ]
	
	>>> add_average([{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])

        [{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33 }, {another element}, … ]

	"""
	
	lst = []
	for i in range(len(inpu)):
		c = list(inpu[i].keys())[-1]
		b = list(inpu[i].keys())[-2]
		a = list(inpu[i].keys())[-3]
		avg = round((int(inpu[i][c]) + int(inpu[i][b]) + int(inpu[i][a])) / 3, 2)
		inpu[i]['G_Avg'] = avg
		temp = {}
		temp = dict.copy(inpu[i])
		lst.append(temp)
	return lst

# Do NOT include a main script in your submission


