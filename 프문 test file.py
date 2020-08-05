class person: 
    def __init__(self, name):
        sena = name
    
    def say_hello(self, to_name): ##메소드 정의
        print("안녕!" +to_name + " 나는 " + sena)

luna = person("Luna")  ##인스턴스 생성
joy = person("Joy")
jenny = person("Jenny")
lisa = person("Lisa")

luna.say_hello("Joy")  ##메소드 호출
joy.say_hello("Luna")
jenny.say_hello("Lisa")
lisa.say_hello("jenny")

