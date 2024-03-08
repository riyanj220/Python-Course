import re

pattern = f"[A-Z]+kynet"
text = """Terminator 2: Judgment Day is a 1991 
American science fiction action film directed 
by James Cameron, who co-wrote the script with
 William Wisher. Starring Arnold Schwarzenegger, 
Linda Hamilton, Robert Patrick (pictured), and
Edward Furlong, it is the sequel to The Terminator 
(1984). In the film, Skynet, Mkynet ,Ikynet a malevolent artificial
intelligence, sends a Terminator android (Patrick)
back in time to 1995 to kill the young John Connor 
(Furlong), the future leader of the human resistance. 
The resistance sends back a less-advanced Terminator (Schwarzenegger), 
reprogrammed to protect Connor. The film had an estimated $94–
102 million budget, making it the most expensive film made up to that time. 
Industrial Light & Magic created a

"""
# match = re.search(pattern, text)
# print(match)
matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0] : match.span()[1]])
