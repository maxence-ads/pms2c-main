import re
with open('c:/dev/PMS2C/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pour_qui_pattern = re.compile(r'(  <!-- POUR QUI / PROFIL.*?  </section>\n\n)', re.DOTALL)
match = pour_qui_pattern.search(text)
if match:
    pour_qui_block = match.group(1)
    text = text.replace(pour_qui_block, '')
    
    insert_pattern = re.compile(r'(  <!-- ETUDES DE CAS)')
    text = insert_pattern.sub(lambda m: pour_qui_block + m.group(1), text)
    
    with open('c:/dev/PMS2C/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Success')
else:
    print('Failed to find pour_qui block')
