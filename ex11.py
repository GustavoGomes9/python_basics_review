# class multiple inheritance 
class Job:
    def __init__(self, salary, name, hours_work):
        self.sal = salary
        self.name = name
        self.hw = hours_work
    
    def going_work(self):
        return f'Going work!!'

class Designer(Job):
    def __init__(self, salary, name, hours_work):
        super().__init__(salary, name, hours_work)
    
    def style(self):
        return True 

class Web_dev(Job):
    def __init__(self, salary, name, hours_work):
        super().__init__(salary, name, hours_work)

    def development(self):
        return True

class Front_end(Web_dev, Designer):
    def __init__(self, salary, name, hours_work):
        super().__init__(salary, name, hours_work)
    
    def app(self):
        if self.sal < 3000:
            return f'Developing an app' 
        else:
            return f'Salary not worth it'

job = Job(1200, 'Balconist', '12')
print(job.sal, job.name, job.hw)
print(job.going_work())

john = Designer(3000, 'Designer', '8')
print(john.sal, john.name, john.hw, john.style())

daniel = Web_dev(4000,'Programmer', '6')
print(daniel.name, daniel.sal, daniel.hw, daniel.development())   

gustavo = Front_end(4000, 'Front-end', '6')
print(gustavo.name, gustavo.sal, gustavo.hw, gustavo.app(), gustavo.style(), gustavo.development())