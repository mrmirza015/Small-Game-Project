Questions=[
    ["What is the capital of India ? ","Delhi","Mumbai","Kolkata","Chennai",1],
    ["What is the capital of Maharashtra ? ","Delhi","Mumbai","Kolkata","Chennai",2],
    ["What is the capital of West Bengal ? ","Delhi","Mumbai","Kolkata","Chennai",3],
    ["What is the capital of Tamilnadu ? ","Delhi","Mumbai","Kolkata","Chennai",4]        
    ]
Levels=[1000,2000,4000,8000]
i=0
money=0
for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"\n\nQuestion for Rs.{Levels[i]}\n\n")
    print(f"Question {i+1}.{Question[0]}")
    print(f"a.{ Question[1]}         b.{Question[2]}")
    print(f"c.{ Question[3]}       d.{Question[4]}")
    reply=int(input("Enter your choice as 1-4\n"))
    if(reply==Question[-1]):
        print(f"Correct answer, You won Rs.{Levels[i]}")
        money=Levels[i]
    else:
        print("Wrong answer")
        break
print(f"You won total Rs. {money}")