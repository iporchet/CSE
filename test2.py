alice_text = """Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do: once or twice she had peeped into the book her sister was reading, 
but it had no pictures or conversations in it, `and what is the use of a book,' 
thought Alice `without pictures or conversation?'"""


dickens_text = """My father’s family name being Pirrip, and my Christian name Philip, 
my infant tongue could make of both names nothing longer or more explicit than Pip. 
So, I called myself Pip, and came to be called Pip.I give Pirrip as my father’s family name, 
on the authority of his tombstone and my sister,—Mrs. Joe Gargery, who married the blacksmith. 
As I never saw my father or my mother, and never saw any likeness of either of them 
(for their days were long before the days of photographs), my first fancies regarding what they 
were like were unreasonably derived from their tombstones. 
The shape of the letters on my father’s, gave me an odd idea that he was a square, stout, 
dark man, with curly black hair. From the character and turn of the inscription, 
“Also Georgiana Wife of the Above,” I drew a childish conclusion that my mother was freckled and sickly. 
To five little stone lozenges, each about a foot and a half long, which were arranged in a neat 
row beside their grave, and were sacred to the memory of five little brothers of mine,—who gave up trying to 
get a living, exceedingly early in that universal struggle,—I am indebted for a belief I religiously 
entertained that they had all been born on their backs with their hands in their trousers-pockets, 
and had never taken them out in this state of existence."""

counter = 0

for x in set(alice_text):
    for y in set(dickens_text):

        if x == y:
            counter += 1

print(counter)