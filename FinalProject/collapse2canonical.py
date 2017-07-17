#!/usr/bin/env python

"""
Text normalization utilities and lists of words to count.

Does not usefully execute on its own; meant to be imported.  champ_list and item_list
are just meant to give you access to the lists.  champ_subs and item_subs shouldn't need
to be imported on their own, collapse_champ and collapse_item will run the substitution for you.  

Source for these nicknames is personal experience with nicknames used in in-game chat and on Reddit.
The full lists include all names, official and not, and the sub functions should get them back to one 
name per entity.  The lists assume everything has been lowercased, but not stripped of punctuation.

Lists are alphabetical (but see below).

Worth noting:
Where one word (separated by spaces) suffices to uniquely identify a multi-word name, I went down to that
word, as that's often abbreviated.  E.G. Lee Sin is listed under "lee" because that will catch both "lee" and 
"lee sin".  However, everything is still alphabetized under its canonical name.  This means for example that "yi" 
is in the M section because his full name is "master yi".  This is particularly obvious under the item section, which
I swear is actually alphabetical.

I included all nicknames that I felt uniquely pointed to one entity.  Some nicknames are shared (e.g. "bird" or "birb"
can mean Azir or Anivia) or overlap too heavily with other relevant words (e.g. "bear" can mean Volibear, but could also
refer to Udyr's Bear Stance) and these were omitted.  
"""


champ_subs = [('amumu', ['mumu', 'mummy']), \
    ('blitzcrank', ['blitz']),\
    ('caitlyn', ['cait']),\
    ('cho\'gath', ['cho']),\
    ('elise', ['spider']),\
    ('evelynn', ['eve']),\
    ('ezreal', ['ez']),\
    ('fiddlesticks', ['fids']),\
    ('gangplank', ['gp', 'plank', 'pirate']),\
    ('hecarim', ['hec']),\
    ('heimerdinger', ['donger']),\
    ('jarvan iv', ['j4']),\
    ('kalista', ['kali']),\
    ('karthus', ['karth']),\
    ('kassadin', ['kass']),\
    ('katarina', ['kat']),\
    ('kha\'zix', ['kha', 'khazix']),\
    ('kog\'maw', ['kog', 'kogmaw']),\
    ('leblanc', ['lb']),\
    ('leona', ['leo']),\
    ('lissandra', ['liss']),\
    ('malphite', ['malph']),\
    ('malzahar', ['malz']),\
    ('maokai', ['mao']),\
    ('miss fortune', ['mf']),\
    ('mordekaiser', ['morde']),\
    ('morgana', ['morg']),\
    ('nasus', ['doge']),\
    ('nidalee', ['nid']),\
    ('nocturne', ['noc']),\
    ('orianna', ['ori']),\
    ('rek\'sai', ['rek', 'reksai']),\
    ('renekton', ['renek', 'croc']),\
    ('shyvana', ['shyv']),\
    ('sivir', ['siv']),\
    ('soraka', ['raka']),\
    ('tristana', ['trist']),\
    ('tryndamere', ['tryn', 'trynd']),\
    ('twisted fate', ['tf']),\
    ('vel\'koz', ['vel', 'velkoz']),\
    ('vladimir', ['vlad']),\
    ('volibear', ['voli']),\
    ('warwick', ['ww']),\
    ('wukong', ['wu', 'monkey']),\
    ('yasuo', ['yas']),\
    ('zilean', ['zil'])]   
    
champs = ['aatrox', 'ahri', 'akali', 'alistar',\
          'amumu', 'mumu', 'mummy',\
          'anivia', 'annie', 'ashe', 'aurelion sol', 'azir',\
          'bard',\
          'blitzcrank', 'blitz',\
          'brand', 'braum',\
          'caitlyn', 'cait',\
          'cassiopeia', 'cass',\
          'cho\'gath', 'cho',\
          'corki',\
          'darius', 'diana',
           'mundo',\
          'draven',\
          'ekko',\
          'elise', 'spider',\
          'evelynn', 'eve',\
          'ezreal', 'ez',\
          'fiddlesticks', 'fids',\
          'fiora', 'fizz', \
          'galio', \
          'gangplank', 'gp', 'plank', 'pirate',\
          'garen', 'gnar', 'gragas', 'graves', \
          'hecarim', 'hec'\
          'heimerdinger', 'donger'\
          'illaoi', 'irelia', \
          'janna',\
          'jarvan iv', 'j4',\
          'jax', 'jayce', 'jhin', 'jinx',\
          'kalista', 'kali',\
          'karma',\
          'karthus', 'karth',\
          'kassadin', 'kass',\
          'katarina', 'kat',\
          'kayle', 'kennen',
          'kha\'zix', 'kha', 'khazix',\
          'kindred',\
          'kog\'maw', 'kog', 'kogmaw',\
          'leblanc', 'lb'\
          'lee',\
          'leona', 'leo'\
          'lissandra', 'liss'\
          'lulu', 'lux',\
          'malphite', 'malph',\
          'fiora', 'fizz', \
          'galio', \
          'gangplank', 'gp', 'plank', 'pirate',\
          'garen', 'gnar', 'gragas', 'graves', \
          'hecarim', 'hec',\
          'heimerdinger', 'donger',\
          'illaoi', 'irelia', \
          'janna',\
          'jarvan iv', 'j4',\
          'jax', 'jayce', 'jhin', 'jinx',\
          'kalista', 'kali',\
          'karma',\
          'karthus', 'karth',\
          'kassadin', 'kass',\
          'katarina', 'kat',\
          'kayle', 'kennen',
          'kha\'zix', 'kha', 'khazix',\
          'kindred',\
          'kog\'maw', 'kog', 'kogmaw',\
          'leblanc', 'lb',\
          'lee',\
          'leona', 'leo',\
          'lissandra', 'liss',\
          'lucian', 'lulu', 'lux',\
          'malphite', 'malph',\
          'malzahar', 'malz',\
          'maokai', 'mao',\
          'yi',\
          'miss fortune', 'mf',\
          'mordekaiser', 'morde',\
          'morgana', 'morg',\
          'nami',\
          'nasus', 'doge',\
          'nautilus', 'naut',\
          'nidalee', 'nid',\
          'nocturne', 'noc',\
          'nunu', \
          'olaf',\
          'orianna', 'ori',\
          'pantheon', 'panth',\
          'poppy',\
          'quinn',\
          'rammus',\
          'rek\'sai', 'rek', 'reksai'\
          'renekton', 'renek', 'croc',\
          'rengar', 'riven', 'rumble', 'ryze',\
          'sejuani', 'sej',\
          'shaco', 'shen',\
          'shyvana', 'shyv',\
          'singed', 'sion',\
          'sivir', 'siv',\
          'skarner', 'sona',\
          'soraka', 'raka',\
          'swain', 'syndra',\
          'tahm', 'taliyah', 'talon', 'taric', 'teemo', 'thresh',\
          'tristana', 'trist',\
          'trundle',\
          'tryndamere', 'tryn', 'trynd',\
          'twisted fate', 'tf',\
          'twitch',\
          'udyr', 'urgot',\
          'varus', 'vayne', 'veigar',\
          'vel\'koz', 'vel', 'velkoz',\
          'vi', 'viktor',\
          'vladimir', 'vlad',\
          'volibear', 'voli', \
          'warwick', 'ww',\
          'wukong', 'wu', 'monkey',\
          'xerath',
          'xin',\
          'yasuo', 'yas',\
          'yorick',\
          'zac', 'zed', 'ziggs',\
          'zilean', 'zil',\
          'zyra']

item_subs = [('bf sword', ['b.f. sword']),\
        ('blade of the ruined king', ['bork']),\
        ('boots of swiftness', ['swifties']),\
        ('dead man\'s plate', ['dmp']),\
        ('face of the mountain', ['fotm']),\
        ('iceborn gauntlet', ['frozen fist']),\
        ('infinity edge', ['ie']),\
        ('lich bane', ['lichbane']),\
        ('mercury\'s treads', ['mercs']),\
        ('needlessly large rod', ['nlr']),\
        ('quicksilver sash', ['qss']),\
        ('rod of ages', ['roa']),\
        ('sorcerer\'s shoes', ['sorcs']),\
        ('talisman of ascension', ['shureliya\'s']),\
        ('bloodthirster',['bt']),\
        ('trinity force', ['triforce'])]


items = ['abyssal', 'aegis', 'wisp', 'tome', 'coin', 'archangel\'s', 'censer', 'athene\'s', \
         'bf sword', 'b.f. sword',\
         'cinder', 'banner', 'banshee\'s', 'berserker\'s greaves', 'cutlass',\
         'blade of the ruined king', 'bork', \
         'blasting wand', 'boots of speed', \
         'boots of swiftness', 'swifties',\
         'brawler\'s gloves',\
         'catalyst', 'caulfield\'s warhammer', 'chain vest', 'chalice', 'cloak of agility', 'cloth',\
         'corrupting', 'crystalline bracer', 'cull', \
         'dagger', \
         'dead man\'s plate', 'dmp',\
         'death\'s dance', 'dervish blade', 'doran\'s blade', 'doran\'s ring', 'doran\'s shield',\
         'duskblade',\
         'elixir of iron', 'elixir of sorcery', 'elixir of wrath', 'entropy', 'essence reaver', 'executioner\'s calling' \
         'eye of the equinox', 'eye of the oasis', 'eye of the watchers',\
         'face of the mountain', 'fotm',\
         'faerie charm', 'fiendish codex', 'forbidden idol', 'frost queen\'s', 'frostfang'\
         'frozen heart', 'frozen mallet', 'giant slayer', 'giant\'s belt' 'glacial shroud', 'guardian', 'guinsoo\'s'\
         'haunting guise', 'health potion', 'hexdrinker', 'hextech glp-800', 'hextech gunblade', 'hextech protobelt-01'\
         'hextech revolver', 'hunter\'s machete', 'hunter\'s potion', 'hunter\'s talisman'\
         'iceborn gauntlet', 'frozen fist',\
         'infinity edge', 'ie',\
         'ionian boots of lucidity'\
         'jaurim\'s fist',\
         'kindlegem', 'shard', \
         'last whisper', 'liandry\'s', 
         'lich bane', 'lichbane',\
         'locket', 'long sword', 'dominik\'s'\
         'lost chapter', 'luden\'s', \
         'manamune', 'maw', 'mejai\'s', 'mercurial scimitar', 
         'mercury\'s treads', 'mercs',\
         'mikael\'s',\
         'morellonomicon', 'mortal reminder', 'muramana', \
         'nashor\'s', \
         'nlr', 'needlessly large rod',\
         'negatron cloak', 'tabi', 'medallion', 'null-magic mantle',\
         'ohmwrecker', 'orb of winter',\
         'phage', 'phantom dancer', 'pickaxe'\
         'qss', 'quicksilver sash',\
         'deathcap', 'randuin\'s', 'firecannon', 'raptor cloak', 'ravenous hydra', 'recurve bow', 'refillable potion',\
         'rejuvenation bead', 'relic shield', 'righteous glory',\
         'rod of ages', 'roa',\
         'ruby crystal', 'ruby sightstone',\
         'runaan\'s', 'rylai\'s', 'sapphire crystal', 'seeker\'s', 'seraph\'s', 'dirk', 'sheen', 'sightstone'\
         'skirmisher\'s',\
         'sorcerer\'s shoes', 'sorcs',\
         'spectre\'s', 'spellthief\'s', 'spirit visage', 'stalker\'s',\
         'statikk', 'sterak\'s', 'stinger', 'sunfire',\
         'talisman of ascension', 'shureliya\'s',\
         'targon\'s', 'tear', 'black cleaver',
         'bloodthirster', 'bt',\
         'dark seal', 'thornmail',\
         'tiamat', 'titanic hydra', 'tracker\'s knife', 
         'trinity', 'triforce',\
         'vampiric', 'void staff',\
         'warden\'s', 'warmog\'s', 'wit\'s end', \
         'youmuu\'s', \
         'zeal', 'zeke\'s', 'zhonya\'s', 'zz\'rot']
         
def champ_list():
    return(set(champs))

def item_list():
    return(set(items))
    
def collapse_champ(word):
    for (real_name, nicknames) in champ_subs:
        if word in nicknames:
            word = real_name
    return word

def collapse_item(word):
    for (real_name, nicknames) in item_subs:
        if word in nicknames:
            word = real_name
    return word
