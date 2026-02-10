"""
Headcanon Generation Engine
Contains 200+ templates for generating unique character headcanons.
"""

import random
from typing import List, Optional

# Headcanon template categories by tone
TEMPLATES = {
    'wholesome': [
        "{character} always remembers everyone's birthdays and celebrates them with homemade cards",
        "{character} has a secret talent for baking and makes the best comfort food",
        "{character} gives the warmest, most genuine hugs that make everyone feel safe",
        "{character} keeps a gratitude journal and writes in it every night before bed",
        "{character} always carries tissues and band-aids, just in case someone needs them",
        "{character} has a playlist for every friend, filled with songs that remind them of that person",
        "{character} secretly waters their neighbors' plants when they're away",
        "{character} memorizes everyone's coffee orders and surprises them when they're having a bad day",
        "{character} has a collection of handwritten letters from loved ones that they treasure",
        "{character} always saves the last bite of dessert to share with someone else",
        "{character} names all the stray animals in their neighborhood and feeds them regularly",
        "{character} has a 'comfort item' from childhood they still sleep with sometimes",
        "{character} leaves encouraging post-it notes in library books for strangers to find",
        "{character} always notices when someone gets a haircut and compliments them",
        "{character} has memorized their best friend's favorite songs and hums them when they're sad",
        "{character} makes friendship bracelets during stressful times as a calming activity",
        "{character} always remembers the little details people tell them, even years later",
        "{character} has a 'happy folder' on their phone with screenshots of nice messages",
        "{character} volunteers at animal shelters on weekends without telling anyone",
        "{character} keeps a jar of happy memories written on paper slips",
        "{character} gives the best advice while making tea and listening patiently",
        "{character} has a special handshake with every close friend",
        "{character} always brings extra snacks to share with everyone",
        "{character} writes encouraging messages in steamy bathroom mirrors for roommates to find",
        "{character} has adopted every plant their friends couldn't keep alive",
        "{character} sends good morning texts to friends going through hard times",
        "{character} keeps a photo album of every important moment with friends",
        "{character} always offers their jacket to anyone who looks cold",
        "{character} has a 'self-care emergency kit' they share with struggling friends",
        "{character} remembers the exact date they met each of their close friends",
        "{character} makes personalized playlists for road trips with friends",
        "{character} always has hot chocolate ready for visitors on cold days",
        "{character} celebrates small victories like they're major achievements",
        "{character} reads bedtime stories to their younger siblings even as an adult",
        "{character} keeps a list of things that make their friends smile",
        "{character} always picks up litter when nobody is watching",
        "{character} sends handwritten thank-you notes for everything",
        "{character} has a tradition of baking cookies for new neighbors",
        "{character} remembers the names of everyone they meet",
        "{character} always checks in on friends who've been quiet lately",
        "{character} saves the funniest memes to share when someone needs cheering up",
        "{character} carries spare phone chargers for friends with dying batteries",
        "{character} gives the best pep talks before big events",
        "{character} always waits for the slowest person in the group",
        "{character} knows exactly how everyone takes their tea or coffee",
    ],
    'funny': [
        "{character} has an embarrassingly specific cereal ranking system they will defend to the death",
        "{character} talks to inanimate objects and apologizes when they bump into furniture",
        "{character} has a 3am personality that is completely different from their daytime self",
        "{character} cannot whisper to save their life - their whispers are just slightly quieter yelling",
        "{character} has strong opinions about the correct way to load a dishwasher",
        "{character} practices arguments in the shower and always wins",
        "{character} has a deeply personal beef with a specific household appliance",
        "{character} makes the weirdest food combinations but insists they're 'actually really good'",
        "{character} knows the lyrics to exactly one song perfectly and it's incredibly embarrassing",
        "{character} snorts when they laugh too hard and is completely unashamed of it",
        "{character} has been telling the same joke for years and still thinks it's peak comedy",
        "{character} cannot take a normal photo - every picture of them is slightly chaotic",
        "{character} has named their WiFi something passive-aggressive toward their neighbor",
        "{character} sets 47 alarms in the morning and sleeps through all of them",
        "{character} has very specific opinions about which direction toilet paper should hang",
        "{character} rehearses conversations in their head but panics when they actually happen",
        "{character} has a rivalry with one specific squirrel in their neighborhood",
        "{character} insists on reading the terms and conditions 'for fun'",
        "{character} has an irrational fear of a specific type of vegetable",
        "{character} waves back at people who weren't actually waving at them",
        "{character} cannot parallel park and has developed elaborate avoidance strategies",
        "{character} has accidentally liked a very old photo while stalking someone's profile",
        "{character} makes up elaborate backstories for random strangers they see",
        "{character} has a playlist called 'songs to overthink to' they listen to regularly",
        "{character} pronounces one common word wrong and refuses to be corrected",
        "{character} has absolutely no sense of direction and has gotten lost in a mall",
        "{character} takes very unflattering selfies of their friends as 'memories'",
        "{character} has an inexplicable talent that is completely useless",
        "{character} cannot remember which way to turn a screwdriver",
        "{character} has been pronouncing a friend's name wrong for years and it's too late to fix it",
        "{character} has a dramatic sigh for every minor inconvenience",
        "{character} thinks they're a good singer but everyone politely disagrees",
        "{character} always burns at least one thing when cooking",
        "{character} has an ongoing war with autocorrect that they keep losing",
        "{character} sends voice messages that are just them sighing",
        "{character} has memorized every commercial jingle from their childhood",
        "{character} trips on absolutely nothing at least once a week",
        "{character} cannot wink without their whole face contorting",
        "{character} has a very specific pizza order that takes five minutes to explain",
        "{character} makes dad jokes that are so bad they circle back to funny",
        "{character} has extremely strong opinions about which water brand tastes best",
        "{character} has an 'I told you so' dance that they use sparingly but devastatingly",
        "{character} cannot keep a straight face during serious moments",
        "{character} has accidentally walked into glass doors more than once",
        "{character} narrates their life in third person when doing mundane tasks",
    ],
    'dark': [
        "{character} hasn't slept properly in weeks and has accepted exhaustion as their baseline",
        "{character} keeps every promise they make because they know how it feels to be let down",
        "{character} has memorized all the exits in every room they enter",
        "{character} smiles less when they're actually happy - their real emotions are quiet",
        "{character} keeps their phone on silent because the sound of notifications triggers anxiety",
        "{character} has a 'go bag' packed and ready, just in case",
        "{character} never sits with their back to the door",
        "{character} practices conversations to ensure they don't accidentally reveal too much",
        "{character} can't remember the last time they cried, even when they needed to",
        "{character} keeps a mental list of everyone who has ever betrayed their trust",
        "{character} sleeps with a light on but will never admit why",
        "{character} has read their own obituary in their head more times than they'd like to admit",
        "{character} checks the locks exactly three times before they can sleep",
        "{character} has perfected the art of disappearing from social situations unnoticed",
        "{character} writes letters they never send to people who hurt them",
        "{character} has a 'public face' that is vastly different from how they actually feel",
        "{character} keeps their deepest thoughts in a journal hidden where no one will find it",
        "{character} can hear the difference between silence and someone trying to be quiet",
        "{character} has contingency plans for their contingency plans",
        "{character} learned to cook because they couldn't rely on anyone else to feed them",
        "{character} flinches at raised voices even when they know they're safe",
        "{character} counts heartbeats to calm down instead of counting sheep",
        "{character} has taught themselves to cry silently",
        "{character} knows exactly which lies are easiest for people to believe",
        "{character} remembers the exact moment they stopped asking for help",
        "{character} can tell when someone is about to leave before they even know it themselves",
        "{character} has a list of 'people who would notice if they disappeared'",
        "{character} sleeps in positions that allow for quick escape",
        "{character} never asks 'are you okay' because they know the answer is usually a lie",
        "{character} has accepted that some wounds don't heal - they just stop bleeding",
        "{character} watches people's hands during conversations out of habit",
        "{character} always knows where the nearest hospital is",
        "{character} keeps everything they might need in their pockets at all times",
        "{character} has trained themselves to wake up at any small sound",
        "{character} memorizes license plates without meaning to",
        "{character} never fully relaxes, even in safe places",
        "{character} knows exactly how long they can survive on their savings",
        "{character} has rehearsed goodbye speeches they hope they never have to give",
        "{character} trusts actions over words because words have failed them too many times",
        "{character} always sits in the seat closest to an exit",
        "{character} has comfort in routines because chaos once destroyed everything",
        "{character} learned to read emotions to survive, now they can't turn it off",
        "{character} keeps backup plans for their backup plans",
        "{character} remembers every unkind word ever said to them",
        "{character} learned to be self-sufficient because depending on others only brought pain",
    ],
    'emotional': [
        "{character} keeps old voicemails from loved ones just to hear their voices",
        "{character} has a box of things they can't throw away because of what they represent",
        "{character} writes poetry at 2am that they'll never show anyone",
        "{character} falls in love with small moments - the way someone laughs, hands that gesture while talking",
        "{character} has a song that makes them cry every single time without fail",
        "{character} remembers the last words of every important conversation",
        "{character} looks at old photos when they need to remember who they used to be",
        "{character} still has the first gift they ever received from their best friend",
        "{character} loves deeper than they'll ever admit out loud",
        "{character} has a place they go to think about people who are no longer in their life",
        "{character} keeps promises to the dead because breaking them feels like betrayal",
        "{character} re-reads old messages when they miss someone too much to call",
        "{character} has a specific sweater they wear when they need comfort",
        "{character} plants flowers for people they've lost as a way to remember them",
        "{character} falls asleep holding something that reminds them of someone they love",
        "{character} writes unsent letters to their future self",
        "{character} has conversations with the moon when they can't talk to anyone else",
        "{character} keeps a running list of 'things I want to tell you' for people far away",
        "{character} cries at commercials and is okay with being called sensitive",
        "{character} has a specific place where they feel closest to someone they miss",
        "{character} believes in signs from the universe and looks for meaning everywhere",
        "{character} can feel when someone they love is having a hard time, even from miles away",
        "{character} treasures handwritten notes more than expensive gifts",
        "{character} has a memory so precious they've never shared it with anyone",
        "{character} still looks for shooting stars because they made a wish as a child",
        "{character} keeps small mementos from every important day in their life",
        "{character} has loved and lost and would do it all over again",
        "{character} believes people deserve second chances, even when it hurts",
        "{character} whispers 'I love you' to people they care about when they're not listening",
        "{character} carries the weight of unspoken words everywhere they go",
        "{character} still celebrates anniversaries of friendships that ended",
        "{character} writes letters to people they've never met but feel connected to",
        "{character} keeps the ticket stubs from every meaningful experience",
        "{character} has a comfort movie they watch when they need to feel something",
        "{character} talks to old photographs like the people in them can hear",
        "{character} remembers exactly how everyone they love takes their coffee",
        "{character} holds onto hope for people who have long given up on themselves",
        "{character} sees beauty in broken things because they know what it feels like",
        "{character} collects sunset photos because each one feels like a goodbye",
        "{character} still believes in love letters even in the age of texting",
        "{character} has a box of things they're saving to give someone someday",
        "{character} can still smell their grandmother's perfume when they need comfort",
        "{character} writes the names of people they love in the margins of their favorite books",
        "{character} has a spot where they go to watch the rain when they need to think",
        "{character} believes every person they meet changes them in some small way",
    ],
}

# Fandom-specific additions (expanded)
FANDOM_ADDITIONS = {
    'anime': [
        "{character} has a signature attack pose they practice in the mirror",
        "{character} dramatically announces their attacks even for mundane tasks",
        "{character} believes in the power of friendship solving literally everything",
        "{character} has an inner monologue that narrates their daily life dramatically",
        "{character} has flashbacks to training montages during stressful moments",
        "{character} eats their meals as if every bite is a spiritual experience",
        "{character} delivers motivational speeches at inappropriate times",
        "{character} has a transformation sequence for getting ready in the morning",
        "{character} strikes poses before and after completing any task",
        "{character} refers to their friends as their 'nakama' unironically",
    ],
    'books': [
        "{character} marks their favorite passages and loans books like treasure",
        "{character} judges people by their bookshelves and isn't ashamed of it",
        "{character} has specific reading spots for different genres",
        "{character} gets emotionally attached to fictional characters more than real people sometimes",
        "{character} has a 'to-read' pile that has become structurally concerning",
        "{character} annotates their books with arguments against the author",
        "{character} can recite the first lines of their favorite novels from memory",
        "{character} refuses to watch movie adaptations until they've read the book",
        "{character} has comfort books they've read so many times the pages are falling out",
        "{character} organizes their bookshelf by color, then by emotional impact",
    ],
    'movies': [
        "{character} quotes movies in everyday conversation and hopes someone gets the reference",
        "{character} has an opinion on every Oscar winner since 1990",
        "{character} always stays for the post-credits scenes, no matter what",
        "{character} has comfort movies they've watched over 50 times",
        "{character} mentally casts everyone they meet in hypothetical films",
        "{character} rates every movie they watch on a very specific rubric",
        "{character} can identify actors by their voice alone",
        "{character} has strong feelings about director's cuts versus theatrical releases",
        "{character} recreates movie scenes in their head starring themselves",
        "{character} considers movie soundtracks to be peak music",
    ],
    'games': [
        "{character} saves obsessively, even when the game auto-saves",
        "{character} has completed a game 100% and will never stop mentioning it",
        "{character} names their RPG characters the same thing every time",
        "{character} has a specific snack they only eat while gaming",
        "{character} talks to NPCs like they're real people",
        "{character} has emotional attachments to video game characters",
        "{character} refuses to skip cutscenes even on replays",
        "{character} spends more time customizing characters than actually playing",
        "{character} remembers video game lore better than real-world history",
        "{character} has a lucky controller they refuse to replace",
    ],
    'general': [
        "{character} has a comfort food they associate with a specific memory",
        "{character} remembers random facts about topics they cared about years ago",
        "{character} has a very specific morning routine they refuse to deviate from",
        "{character} collects something unusual that has sentimental value",
        "{character} has a superstition they don't actually believe but follow anyway",
        "{character} has a specific mug that is absolutely off-limits to everyone else",
        "{character} knows exactly which chair at every table is 'their' chair",
        "{character} has worn the same style of shoes for the past decade",
        "{character} always orders the same thing at their favorite restaurant",
        "{character} has a comfort show they've rewatched countless times",
    ],
}

# Additional personality traits to mix in
PERSONALITY_TRAITS = [
    "fiercely loyal to those they consider family",
    "secretly incredibly competitive about random things",
    "terrible at accepting compliments but loves giving them",
    "has very specific music for every mood and activity",
    "believes in always keeping their word, no matter the cost",
    "notices the small things others overlook",
    "acts tough but is incredibly soft underneath",
    "would rather be honest and hurt feelings than lie and be comfortable",
    "keeps their promises even when it's inconvenient",
    "falls asleep anywhere when they feel safe",
    "has very strong opinions about things that don't matter",
    "treats strangers with unexpected kindness",
    "remembers insults forever but forgets compliments instantly",
    "is actually really good at something they pretend to be bad at",
    "speaks several languages but switches when frustrated",
]


def generate_headcanons(
    character: str,
    fandom: Optional[str] = None,
    tone: str = 'random',
    count: int = 4
) -> List[str]:
    """
    Generate unique headcanons for a character.
    
    Args:
        character: The character's name
        fandom: Optional fandom (anime, books, movies, games, or custom)
        tone: One of 'wholesome', 'funny', 'dark', 'emotional', or 'random'
        count: Number of headcanons to generate (3-5)
    
    Returns:
        List of generated headcanon strings
    """
    # Clamp count between 3 and 5
    count = max(3, min(5, count))
    
    # Collect available templates
    if tone == 'random':
        available_templates = []
        for tone_templates in TEMPLATES.values():
            available_templates.extend(tone_templates)
    else:
        available_templates = TEMPLATES.get(tone, TEMPLATES['wholesome']).copy()
    
    # Add fandom-specific templates if applicable
    fandom_key = 'general'
    if fandom:
        fandom_lower = fandom.lower()
        if 'anime' in fandom_lower or 'manga' in fandom_lower:
            fandom_key = 'anime'
        elif 'book' in fandom_lower or 'novel' in fandom_lower or 'literature' in fandom_lower:
            fandom_key = 'books'
        elif 'movie' in fandom_lower or 'film' in fandom_lower or 'cinema' in fandom_lower:
            fandom_key = 'movies'
        elif 'game' in fandom_lower or 'gaming' in fandom_lower or 'video' in fandom_lower:
            fandom_key = 'games'
    
    available_templates.extend(FANDOM_ADDITIONS.get(fandom_key, FANDOM_ADDITIONS['general']))
    
    # Shuffle and select unique templates
    random.shuffle(available_templates)
    selected_templates = available_templates[:count]
    
    # Generate headcanons
    headcanons = []
    for template in selected_templates:
        headcanon = template.format(character=character)
        headcanons.append(headcanon)
    
    return headcanons


def get_tone_options() -> List[dict]:
    """Return available tone options for the UI."""
    return [
        {'value': 'wholesome', 'label': 'Wholesome', 'emoji': '💖', 'description': 'Heartwarming and comforting'},
        {'value': 'funny', 'label': 'Funny', 'emoji': '😂', 'description': 'Quirky and comedic'},
        {'value': 'dark', 'label': 'Dark', 'emoji': '🖤', 'description': 'Mysterious and angsty'},
        {'value': 'emotional', 'label': 'Emotional', 'emoji': '🥺', 'description': 'Deep and meaningful'},
        {'value': 'random', 'label': 'Random', 'emoji': '🎲', 'description': 'Mix of all tones'},
    ]


# Ship/Relationship headcanon templates
SHIP_TEMPLATES = {
    'wholesome': [
        "{character1} and {character2} have a secret handshake that took them months to perfect",
        "{character1} always knows when {character2} needs a hug without being told",
        "{character1} leaves little love notes in {character2}'s pockets and bags",
        "{character1} and {character2} have matching phone wallpapers but pretend it's a coincidence",
        "{character1} memorized {character2}'s coffee order on their second meeting",
        "{character1} and {character2} share a playlist they add songs to when thinking of each other",
        "{character1} always saves the last bite of their favorite food for {character2}",
        "{character1} and {character2} have inside jokes nobody else understands",
        "{character1} gets jealous when {character2} laughs at someone else's jokes",
        "{character1} and {character2} finish each other's sentences constantly",
        "{character1} always notices when {character2} gets a haircut first",
        "{character1} and {character2} have a tradition of watching the sunrise together",
        "{character1} keeps a folder of {character2}'s best photos on their phone",
        "{character1} and {character2} have matching scars from an adventure gone wrong",
        "{character1} unconsciously gravitates toward {character2} in group settings",
    ],
    'funny': [
        "{character1} and {character2} have an ongoing prank war that's lasted years",
        "{character1} roasts {character2} constantly but won't let anyone else do it",
        "{character1} and {character2} argue about who falls asleep first (both claim the other does)",
        "{character1} steals {character2}'s hoodies so often they've given up reclaiming them",
        "{character1} and {character2} have a competition for who can embarrass the other more in public",
        "{character1} sends {character2} ugly photos of themselves at 3am",
        "{character1} and {character2} have different versions of how they met and both insist theirs is correct",
        "{character1} knows exactly which buttons to push to annoy {character2} (and pushes them regularly)",
        "{character1} and {character2} fight over the aux cord like their lives depend on it",
        "{character1} has an entire camera roll of unflattering photos of {character2}",
        "{character1} and {character2} have a running bet that neither remembers the stakes of anymore",
        "{character1} finishes {character2}'s food without asking and acts innocent",
        "{character1} and {character2} are competitive about everything, even deciding where to eat",
        "{character1} mocks {character2}'s music taste but secretly adds their songs to their playlist",
        "{character1} and {character2} have developed their own language of weird noises",
    ],
    'emotional': [
        "{character1} can tell something is wrong with {character2} just from their texting patterns",
        "{character1} would burn the world down for {character2} without hesitation",
        "{character1} and {character2} have a 'if we're both single at 40' pact they joke about but secretly mean",
        "{character1} still gets butterflies around {character2} after all this time",
        "{character1} and {character2} have a song that makes them cry together",
        "{character1} keeps every gift {character2} has ever given them, no matter how small",
        "{character1} and {character2} have grown into better people because of each other",
        "{character1} would wait a lifetime for {character2}, and {character2} knows it",
        "{character1} and {character2} have a 'we'll get through this together' that has never failed",
        "{character1} sees {character2}'s flaws and loves them anyway—maybe even because of them",
        "{character1} and {character2} are each other's emergency contacts, metaphorically and literally",
        "{character1} wrote their feelings for {character2} in a letter they never sent",
        "{character1} and {character2} have survived things that would have broken them alone",
        "{character1} trusts {character2} with secrets they've never told anyone else",
        "{character1} and {character2} communicate entire conversations through eye contact",
    ],
    'dark': [
        "{character1} and {character2} have a secret only they share—and will take to their graves",
        "{character1} would lie, cheat, and steal for {character2} without a second thought",
        "{character1} and {character2} are each other's alibis, no questions asked",
        "{character1} knows exactly where {character2} would hide a body (and vice versa)",
        "{character1} and {character2} have trust that was forged in a crisis",
        "{character1} would choose {character2} over doing the 'right' thing every time",
        "{character1} and {character2} have matching scars from protecting each other",
        "{character1} has killed for {character2} and would do it again",
        "{character1} and {character2} are toxic for everyone except each other",
        "{character1} keeps a mental list of everyone who's ever wronged {character2}",
        "{character1} and {character2} understand each other's darkness without judgment",
        "{character1} is the only person {character2} can be truly vulnerable with",
        "{character1} and {character2} have survived trauma that bonded them permanently",
        "{character1} and {character2} are partners in crimes they'll never speak of",
        "{character1} saw {character2} at their absolute worst and didn't flinch",
    ],
}


def generate_ship_headcanons(
    character1: str,
    character2: str,
    tone: str = 'random',
    count: int = 4
) -> List[str]:
    """
    Generate unique headcanons for a ship/pairing.

    Args:
        character1: First character's name
        character2: Second character's name
        tone: One of 'wholesome', 'funny', 'dark', 'emotional', or 'random'
        count: Number of headcanons to generate (3-5)

    Returns:
        List of generated headcanon strings
    """
    count = max(3, min(5, count))

    if tone == 'random':
        available_templates = []
        for tone_templates in SHIP_TEMPLATES.values():
            available_templates.extend(tone_templates)
    else:
        available_templates = SHIP_TEMPLATES.get(tone, SHIP_TEMPLATES['wholesome']).copy()

    random.shuffle(available_templates)
    selected_templates = available_templates[:count]

    headcanons = []
    for template in selected_templates:
        headcanon = template.format(character1=character1, character2=character2)
        headcanons.append(headcanon)

    return headcanons


def get_popular_fandoms() -> List[str]:
    """Return list of popular fandoms for the dropdown."""
    return [
        "Anime/Manga",
        "Harry Potter",
        "Marvel",
        "DC Comics",
        "Star Wars",
        "Lord of the Rings",
        "Stranger Things",
        "Game of Thrones",
        "Percy Jackson",
        "Attack on Titan",
        "My Hero Academia",
        "Demon Slayer",
        "Naruto",
        "One Piece",
        "Genshin Impact",
        "Minecraft",
        "The Hunger Games",
        "Twilight",
        "Disney",
        "Studio Ghibli",
        "K-Pop",
        "Video Games",
        "Books/Literature",
        "Movies/Cinema",
        "TV Shows",
        "Original Characters",
        "Other",
    ]
