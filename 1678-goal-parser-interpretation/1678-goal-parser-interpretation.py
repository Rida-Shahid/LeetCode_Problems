class Solution:
    def interpret(self, command: str) -> str:
        new_str=""


        for i in range(0,len(command)):
            if(command[i]=="G"):
                new_str += 'G'
            elif(command[i]=='(' and command[i+1]==')'):
                new_str += 'o'
            elif (command[i]=='('and command[i+1]=='a' and command[i+2] =='l' and command[i+3]==')'):
                new_str += "al"
        return new_str
        