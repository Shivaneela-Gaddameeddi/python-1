data={
    'neela':{'status':True,'python':96,'mysql':95,'fastapi':93},
    'shiva':{'status':True,'python':76,'mysql':75,'fastapi':73},
    'shivani':{'status':True,'python':66,'mysql':55,'fastapi':53},
    'shivanee':{'status':True,'python':66,'mysql':55,'fastapi':53},
    'nainaaa':{'status':False,'python':None,'mysql':None,'fastapi':None},

}
name = input("Enter the name:")
if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['fastapi']
        avg = total/3
        if avg > 80:
            print(f"{name}, congrates you got the first grade")
        elif  avg > 60:
            print(f'{name}, Good work hard next time') 
        elif avg > 40:
            print(f'{name}, Better luck next time ')
        elif avg > 35:
            print(f'{name}, You just passed, work hard')
        else:
            print(f"{name} you failed   the exam bring your parents")
    else:   
        print(f"{name}, didn't attented the exam. Bring your parents") 
else:
    print(f"{name}, is not found in data ") 

