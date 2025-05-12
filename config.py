import json
#Токен
TOKEN = 'MTM2OTI0NTU1Nzg5MzEwMzY3Nw.GLFyCz.yGlDLuhA8gg2aNcDkLpJdrN0s-m00TY8sCUjdA'

# Список слов
word_list = []
for word in open('answers.txt', 'r', encoding='utf-8').readlines():
    word_list.append(word[:-1])

guesses_list = []
for word in open('guesses.txt', 'r', encoding='utf-8').readlines():
    guesses_list.append(word[:-1])

# База данных
with open('dataBase.json', 'r', encoding='utf-8') as file_json:
    players = json.load(file_json)


# Алфавит
emojis_letters = {
    '#': {'black': 'code', 'green': 'code'},
    '0': {'black': '', 'green': ''},
    '1': {'black': '', 'green': ''},
    '2': {'black': '', 'green': ''},

    'a': {
        'black': '<:bl_a:1369670025786556416>',
        'yellow':'<:y_a:1369671039872794638>',
        'green': '<:gr_a:1369670702113755216>'
    },
    'b': {
        'black': '<:bl_b:1369670054182129686>',
        'yellow':'<:y_b:1369671058130599966>',
        'green': '<:gr_b:1369670714956976159>'
    },
    'c': {
        'black': '<:bl_c:1369670066358190090>',
        'yellow':'<:y_c:1369671076010917918>',
        'green': '<:gr_c:1369670727623770273>'
    },
    'd': {
        'black': '<:bl_d:1369670086721536030>',
        'yellow':'<:y_d:1369671092737937419>',
        'green': '<:gr_d:1369670738650337420>'
    },
    'e': {
        'black': '<:bl_e:1369670101816574023>',
        'yellow':'<:y_e:1369671113046622429>',
        'green': '<:gr_e:1369670750298050651>'
    },
    'f': {
        'black': '<:bl_f:1369670114546421830>',
        'yellow':'<:y_f:1369671126246228149>',
        'green': '<:gr_f:1369670762243424286>'
    },
    'g': {
        'black': '<:y_g:1369671139076603935>',
        'yellow':'<:bl_g:1369670131323633735>',
        'green': '<:gr_g:1369670774851633274>'
    },
    'h': {
        'black': '<:bl_h:1369670143902486629>',
        'yellow':'<:y_h:1369671152049590282>',
        'green': '<:gr_h:1369670792077643786>'
    },
    'i': {
        'black': '<:bl_i:1369670156946640996>',
        'yellow':'<:y_i:1369671165760638997>',
        'green': '<:gr_i:1369670805864317081>'
    },
    'j': {
        'black': '<:bl_j:1369670168527114380>',
        'yellow':'<:y_j:1369671178092023940>',
        'green': '<:gr_j:1369670821706203187>'
    },
    'k': {
        'black': '<:bl_k:1369670181361549333>',
        'yellow':'<:y_k:1369671191111139338>',
        'green': '<:gr_k:1369670834842636370>'
    },
    'l': {
        'black': '<:bl_l:1369670194154311830>',
        'yellow':'<:y_l:1369671203999973530>',
        'green': '<:gr_l:1369670847861751864>'
    },
    'm': {
        'black': '<:bl_m:1369670204715438080>',
        'yellow':'<:y_m:1369671221091766292>',
        'green': '<:gr_m:1369670859563864114>'
    },
    'n': {
        'black': '<:bl_n:1369670216031801345>',
        'yellow':'<:y_n:1369671234228584478>',
        'green': '<:gr_n:1369670870305341490>'
    },
    'o': {
        'black': '<:bl_o:1369670225758519358>',
        'yellow':'<:y_o:1369671248946139197>',
        'green': '<:gr_o:1369670883471528056>'
    },
    'p': {
        'black': '<:bl_p:1369670522186760332>',
        'yellow':'<:y_p:1369671259750797434>',
        'green': '<:gr_p:1369670897249681539>'
    },
    'q': {
        'black': '<:bl_q:1369670538066395287>',
        'yellow':'<:y_q:1369671271574405230>',
        'green': '<:gr_q:1369670908666581063>'
    },
    'r': {
        'black': '<:bl_r:1369670557536223262>',
        'yellow':'<:y_r:1369671283863715940>',
        'green': '<:gr_r:1369670919932608593>'
    },
    's': {
        'black': '<:bl_s:1369670571473895558>',
        'yellow':'<:y_s:1369671297776488490>',
        'green': '<:gr_s:1369670934864072724>'
    },
    't': {
        'black': '<:bl_t:1369670584577036308>',
        'yellow':'<:y_t:1369671328982110308>',
        'green': '<:gr_t:1369670947350777956>'
    },
    'u': {
        'black': '<:bl_u:1369670597021532258>',
        'yellow':'<:y_u:1369671347885838468>',
        'green': '<:gr_u:1369670960193470484>'
    },
    'v': {
        'black': '<:bl_v:1369670616638292079>',
        'yellow':'<:y_v:1369671360833388654>',
        'green': '<:gr_v:1369670971719421982>'
    },
    'w': {
        'black': '<:bl_w:1369670637748097055>',
        'yellow':'<:y_w:1369671376377741392>',
        'green': '<:gr_w:1369670982197055559>'
    },
    'x': {
        'black': '<:bl_x:1369670653237788742>',
        'yellow':'<:y_x:1369671389556248748>',
        'green': '<:gr_x:1369670992523169823>'
    },
    'y': {
        'black': '<:bl_y:1369670666269229206>',
        'yellow':'<:y_y:1369671401501622312>',
        'green': '<:gr_y:1369671009925337209>'
    },
    'z': {
        'black': '<:bl_z:1369670683835240488>',
        'yellow':'<:y_z:1369671414365425735>',
        'green': '<:gr_z:1369671024169193673>'
    },
    'é': {
        'black': '<:bl_e_left:1369891736545132564>',
        'yellow':'<:y_e_left:1369891752735145994>',
        'green': '<:gr_e_left:1369891716835971144>'
    },
    'è': {
        'black': '<:bl_e_right:1369891789523124234>',
        'yellow':'<:y_e_right:1369891805155430400>',
        'green': '<:gr_e_right:1369891774734008402>'
    },
    'à': {
        'black': '<:bl_a_right:1369891839422763039>',
        'yellow':'<:y_a_right:1369891857148149891>',
        'green': '<:gr_a_right:1369891822599671890>'
    },
    'ù': {
        'black': '<:bl_u_right:1369891885291929731>',
        'yellow':'<:y_u_right:1369891903377510540>',
        'green': '<:gr_u_right:1369891871090020443>'
    },
    'ê': {
        'black': '<:bl_e_roof:1369891930527367248>',
        'yellow':'<:y_e_roof:1369891945186594866>',
        'green': '<:gr_e_roof:1369891916837027882>'
    },
    'â': {
        'black': '<:bl_a_roof:1369902214973362246>',
        'yellow':'<:y_a_roof:1369902230383230987>',
        'green': '<:gr_a_roof:1369902198783348827>'
    },
    'û': {
        'black': '<:bl_u_roof:1369891974240276510>',
        'yellow':'<:y_u_roof:1369891988073222186>',
        'green': '<:gr_u_roof:1369891957882490961>'
    },
    'ô': {
        'black': '<:bl_o_roof:1369892036970418246>',
        'yellow':'<:y_o_roof:1369892061872132157>',
        'green': '<:gr_o_roof:1369892015650771065>'
    },
    'î': {
        'black': '<:bl_i_roof:1369892116787888260>',
        'yellow':'<:y_i_roof:1369892136773877790>',
        'green': '<:gr_i_roof:1369892082956767333>'
    },
    'ë': {
        'black': '<:bl_e_dots:1369898528037540002>',
        'yellow':'<:y_e_dots:1369898545276260416>',
        'green': '<:gr_e_dots:1369898501776871514>'
    },
    'ï': {
        'black': '<:bl_i_dots:1369898581150138510>',
        'yellow':'<:y_i_dots:1369898605011406918>',
        'green': '<:gr_i_dots:1369898563726868645>'
    },
    'ü': {
        'black': '<:bl_u_dots:1369898642256691310>',
        'yellow':'<:y_u_dots:1369898672350957619>',
        'green': '<:gr_u_dots:1369898624812580964>'
    },
    'ç': {
        'black': '<:bl_c_tail:1369898710355542118>',
        'yellow':'<:y_c_tail:1369898730957836318>',
        'green': '<:gr_c_tail:1369898691686826024>'
    },
    'æ': {
        'black': '<:bl_ae_ligature:1369898761458942013>',
        'yellow':'<:y_ae_ligature:1369898779465224334>',
        'green': '<:gr_ae_ligature:1369898745566597220>'
    },
    'œ': {
        'black': '<:bl_oe_ligature:1369898817771536435>',
        'yellow':'<:y_oe_ligature:1369898834460938320>',
        'green': '<:gr_oe_ligature:1369898797060329542>'
    },

}

# Сообщения
msg_start = '''Wordly game started!
Send a message which length is equal to 5
    Rule:
    Black - wrong letter
    Yellow - correct letter but wrong position
    Green - correct letter and correct position
Bonne chance,'''

msg_win = '''Good job!'''

msg_lose = '''Next time. Word was'''

msg_wrong_letters = ''', your word has the wrong length! It should be 5'''

msg_help = '''
1. `w!play` - starts new Wordle game
2. `w!stop` - stops current game
3. `w!alphabet` - shows letters that you can use
4. `w!stats` - shows your score and statistics
5. `w!reset` - resets your score and statictics
6. `w!help` - shows available commands
7. `w!rules` - explains rules and how to play
'''

msg_alphabet = '''
é è à ù ê â û ô î ë ï ü ç æ œ
a b c d e f g h i j k l m
n o p q r s t u v w x y z'''

msg_rules = ''' 
- Guess a secret five-letter word in **eight** tries or less.

- Each guess must be a **valid** five-letter French word.

- After each guess, the game gives feedback:

- - **Green**: letter is **correct** and in the **right position**.

- - **Yellow**: letter is **correct** but in the **wrong position**.

- - **Black**: letter is **incorrect**.

- Letters can appear more than once in the answer.

- You win by guessing the word within six attempts, or lose if you run out of guesses'''
