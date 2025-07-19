import streamlit as st

import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Hogwarts Characters",
    page_icon="🧙‍♂️",
    layout="wide"
)

# Custom CSS for characters page
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
    }
    
    .page-header {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #d4af37, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
    }
    
    .character-card {
        background: linear-gradient(145deg, rgba(139, 0, 0, 0.15), rgba(0, 0, 139, 0.15));
        border: 2px solid #ffd700;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .character-card:hover {
        transform: translateY(-5px);
        border-color: #ffed4e;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4);
    }
    
    .character-name {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffd700;
        margin-bottom: 0.5rem;
    }
    
    .character-house {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .gryffindor { color: #dc143c; }
    .slytherin { color: #00ff00; }
    .ravenclaw { color: #0066cc; }
    .hufflepuff { color: #ffcc00; }
    .none { color: #888888; }
    
    .character-role {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        display: inline-block;
    }
    
    .hero { background: linear-gradient(45deg, #ffd700, #ffed4e); color: #000; }
    .villain { background: linear-gradient(45deg, #8b0000, #dc143c); color: #fff; }
    .anti-hero { background: linear-gradient(45deg, #4b0082, #8a2be2); color: #fff; }
    .mentor { background: linear-gradient(45deg, #0066cc, #4169e1); color: #fff; }
    
    .character-description {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.1rem;
        color: #e8e8e8;
        line-height: 1.6;
        text-align: justify;
    }
    
    .filter-section {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(212, 175, 55, 0.3);
    }
    
    .stats-card {
        background: rgba(139, 0, 0, 0.1);
        border: 1px solid #ffd700;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 0.5rem;
    }
    
    .stats-number {
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #ffd700;
    }
    
    .stats-label {
        font-family: 'Cormorant Garamond', serif;
        color: #e8e8e8;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Character data
CHARACTERS = [
    {
        "name": "Harry Potter",
        "house": "Gryffindor",
        "role": "Hero",
        "description": "The Boy Who Lived, Harry Potter is the main protagonist of the series. Born with a lightning bolt scar and the burden of defeating the Dark Lord, Harry grows from an orphaned boy into a brave wizard who values friendship, loyalty, and sacrifice above all else.",
        "year": "Same age as Harry (Year 1-7)",
        "patronus": "Stag"
    },
    {
        "name": "Hermione Granger",
        "house": "Gryffindor", 
        "role": "Hero",
        "description": "The brightest witch of her age, Hermione is Harry's loyal friend and the brains of the trio. Born to Muggle parents, she proves that magical ability comes from within, not bloodline. Her vast knowledge and quick thinking save the day countless times.",
        "year": "Same age as Harry (Year 1-7)",
        "patronus": "Otter"
    },
    {
        "name": "Ron Weasley",
        "house": "Gryffindor",
        "role": "Hero", 
        "description": "Harry's first friend and loyal companion, Ron comes from a large pure-blood wizarding family. Though sometimes overshadowed by his friends, his bravery, loyalty, and strategic mind (especially at wizard's chess) prove invaluable in their adventures.",
        "year": "Same age as Harry (Year 1-7)",
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Albus Dumbledore",
        "house": "Gryffindor",
        "role": "Mentor",
        "description": "The wise and powerful Headmaster of Hogwarts, considered the greatest wizard of his time. Dumbledore guides Harry through his journey, though his methods are sometimes questionable. His past holds dark secrets that ultimately help defeat Voldemort.",
        "year": "Headmaster",
        "patronus": "Phoenix"
    },
    {
        "name": "Severus Snape",
        "house": "Slytherin",
        "role": "Anti-Hero",
        "description": "The complex Potions Master whose true loyalties remain hidden until the very end. Snape's love for Lily Potter drives him to protect Harry, despite his hatred for James Potter. His story is one of redemption, love, and ultimate sacrifice.",
        "year": "Professor",
        "patronus": "Doe"
    },
    {
        "name": "Lord Voldemort",
        "house": "Slytherin",
        "role": "Villain",
        "description": "Born Tom Marvolo Riddle, Voldemort is the Dark Lord who seeks immortality and pure-blood supremacy. His fear of death leads him to split his soul into Horcruxes, making him less human with each piece. He represents everything evil in the wizarding world.",
        "year": "Former Student (1938-1945)",
        "patronus": "Cannot produce one"
    },
    {
        "name": "Rubeus Hagrid",
        "house": "Gryffindor",
        "role": "Mentor",
        "description": "The lovable half-giant Keeper of Keys and Grounds at Hogwarts, and later Care of Magical Creatures professor. Hagrid introduces Harry to the wizarding world and remains a loyal friend throughout. His love for dangerous creatures often leads to trouble.",
        "year": "Expelled in 3rd Year (1943)",
        "patronus": "Unknown"
    },
    {
        "name": "Draco Malfoy",
        "house": "Slytherin",
        "role": "Anti-Hero",
        "description": "Harry's school rival from a wealthy pure-blood supremacist family. Initially a bully and antagonist, Draco struggles with the expectations of his family and the Dark Lord. His character shows the complexity of choice versus circumstance.",
        "year": "Same age as Harry (Year 1-7)",
        "patronus": "Unknown"
    },
    {
        "name": "Minerva McGonagall",
        "house": "Gryffindor",
        "role": "Mentor",
        "description": "The stern but fair Transfiguration professor and Head of Gryffindor House. An Animagus who can transform into a cat, McGonagall is fiercely protective of her students and plays a crucial role in the fight against Voldemort.",
        "year": "Professor & Deputy Headmistress",
        "patronus": "Cat"
    },
    {
        "name": "Sirius Black",
        "house": "Gryffindor",
        "role": "Hero",
        "description": "Harry's godfather and James Potter's best friend. Wrongly imprisoned in Azkaban for twelve years, Sirius escaped to help Harry. As an Animagus who transforms into a black dog, he represents the loyal companion Harry never had.",
        "year": "James Potter's generation",
        "patronus": "Unknown (Animagus: Dog)"
    },
    {
        "name": "Remus Lupin",
        "house": "Gryffindor", 
        "role": "Mentor",
        "description": "The best Defense Against the Dark Arts teacher Harry ever had, Lupin is a werewolf who struggles with his condition. One of the Marauders and Harry's father's friend, he provides guidance and teaches Harry the Patronus charm.",
        "year": "James Potter's generation",
        "patronus": "Wolf"
    },
    {
        "name": "Bellatrix Lestrange",
        "house": "Slytherin",
        "role": "Villain", 
        "description": "Voldemort's most devoted and dangerous Death Eater, Bellatrix is Sirius Black's cousin. Her fanatical loyalty to the Dark Lord and sadistic nature make her one of the most feared witches. She killed Sirius Black and tortured Neville's parents into insanity.",
        "year": "Graduated before Harry's time",
        "patronus": "Cannot produce one"
    }
]

def get_house_color_class(house):
    return house.lower() if house in ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'] else 'none'

def get_role_class(role):
    role_map = {
        'Hero': 'hero',
        'Villain': 'villain', 
        'Anti-Hero': 'anti-hero',
        'Mentor': 'mentor'
    }
    return role_map.get(role, 'hero')

def main():
    load_css()
    
    st.markdown('<h1 class="page-header">🧙‍♂️ Characters of the Wizarding World</h1>', unsafe_allow_html=True)
    
    # Character statistics
    st.markdown("### 📊 Character Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{len(CHARACTERS)}</div>
            <div class="stats-label">Total Characters</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        heroes = len([c for c in CHARACTERS if c['role'] == 'Hero'])
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{heroes}</div>
            <div class="stats-label">Heroes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        villains = len([c for c in CHARACTERS if c['role'] == 'Villain'])
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{villains}</div>
            <div class="stats-label">Villains</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        gryffindors = len([c for c in CHARACTERS if c['house'] == 'Gryffindor'])
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{gryffindors}</div>
            <div class="stats-label">Gryffindors</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Filters
    st.markdown("### 🔍 Filter Characters")
    
    with st.container():
        st.markdown('<div class="filter-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            house_filter = st.selectbox(
                "🏠 Filter by House:",
                options=['All Houses'] + sorted(list(set([c['house'] for c in CHARACTERS]))),
                key="house_filter"
            )
        
        with col2:
            role_filter = st.selectbox(
                "⚔️ Filter by Role:",
                options=['All Roles'] + sorted(list(set([c['role'] for c in CHARACTERS]))),
                key="role_filter"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter characters
    filtered_characters = CHARACTERS
    
    if house_filter != 'All Houses':
        filtered_characters = [c for c in filtered_characters if c['house'] == house_filter]
    
    if role_filter != 'All Roles':
        filtered_characters = [c for c in filtered_characters if c['role'] == role_filter]
    
    # Display characters
    st.markdown(f"### 📚 Found {len(filtered_characters)} Characters")
    
    # Display in columns
    for i in range(0, len(filtered_characters), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            if i < len(filtered_characters):
                char = filtered_characters[i]
                display_character(char)
        
        with col2:
            if i + 1 < len(filtered_characters):
                char = filtered_characters[i + 1]
                display_character(char)

def display_character(char):
    house_class = get_house_color_class(char['house'])
    role_class = get_role_class(char['role'])
    
    st.markdown(f"""
    <div class="character-card">
        <div class="character-name">{char['name']}</div>
        <div class="character-house {house_class}">🏠 {char['house']}</div>
        <div class="character-role {role_class}">{char['role']}</div>
        <div class="character-description">{char['description']}</div>
        <br>
        <small style="color: #aaa; font-family: 'Cormorant Garamond', serif;">
            <strong>School Years:</strong> {char['year']}<br>
            <strong>Patronus:</strong> {char['patronus']}
        </small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Hogwarts Spell Practice",
    page_icon="🪄",
    layout="wide"
)

# Custom CSS for spells page
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
    }
    
    .page-header {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #d4af37, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
    }
    
    .spell-card {
        background: linear-gradient(145deg, rgba(139, 0, 0, 0.15), rgba(0, 0, 139, 0.15));
        border: 2px solid #ffd700;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .spell-card:hover {
        transform: translateY(-5px);
        border-color: #ffed4e;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4);
    }
    
    .spell-name {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffd700;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .spell-pronunciation {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        color: #ffed4e;
        text-align: center;
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .spell-description {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.1rem;
        color: #e8e8e8;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 1rem;
    }
    
    .spell-type {
        display: inline-block;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-family: 'Cormorant Garamond', serif;
        font-size: 0.9rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    .charm { background: linear-gradient(45deg, #4169e1, #0066cc); color: white; }
    .curse { background: linear-gradient(45deg, #8b0000, #dc143c); color: white; }
    .transfiguration { background: linear-gradient(45deg, #9932cc, #8a2be2); color: white; }
    .defense { background: linear-gradient(45deg, #ffd700, #ffed4e); color: black; }
    .healing { background: linear-gradient(45deg, #00ff7f, #32cd32); color: black; }
    .utility { background: linear-gradient(45deg, #ff8c00, #ffa500); color: black; }
    
    .practice-section {
        background: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid rgba(212, 175, 55, 0.3);
    }
    
    .casting-result {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    .success {
        background: linear-gradient(45deg, #00ff7f, #32cd32);
        color: #000;
        animation: glow-green 2s ease-in-out;
    }
    
    .partial {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #000;
        animation: glow-yellow 2s ease-in-out;
    }
    
    .failure {
        background: linear-gradient(45deg, #8b0000, #dc143c);
        color: #fff;
        animation: glow-red 2s ease-in-out;
    }
    
    @keyframes glow-green {
        0%, 100% { box-shadow: 0 0 5px #32cd32; }
        50% { box-shadow: 0 0 20px #32cd32, 0 0 30px #32cd32; }
    }
    
    @keyframes glow-yellow {
        0%, 100% { box-shadow: 0 0 5px #ffd700; }
        50% { box-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700; }
    }
    
    @keyframes glow-red {
        0%, 100% { box-shadow: 0 0 5px #dc143c; }
        50% { box-shadow: 0 0 20px #dc143c, 0 0 30px #dc143c; }
    }
    
    .lumos-effect {
        background: radial-gradient(circle, #ffffff, #ffff99, transparent);
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 300px;
        height: 300px;
        border-radius: 50%;
        opacity: 0;
        pointer-events: none;
        z-index: 1000;
        animation: lumos-flash 2s ease-out;
    }
    
    @keyframes lumos-flash {
        0% { opacity: 0; transform: translate(-50%, -50%) scale(0); }
        50% { opacity: 0.8; transform: translate(-50%, -50%) scale(1); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(1.2); }
    }
    
    .movie-tab {
        background: rgba(139, 0, 0, 0.2);
        border: 2px solid #ffd700;
        color: white;
        padding: 0.8rem 1.5rem;
        font-family: 'Cinzel', serif;
        font-weight: 600;
        margin: 0.2rem;
        border-radius: 25px;
        transition: all 0.3s ease;
    }
    
    .movie-tab:hover {
        background: rgba(139, 0, 0, 0.4);
        transform: translateY(-2px);
    }
    
    .active-tab {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# Spells database organized by movie/book
SPELLS_BY_MOVIE = {
    "Philosopher's Stone": [
        {
            "name": "Alohomora",
            "pronunciation": "ah-LOH-ho-MOR-ah",
            "description": "The Unlocking Charm opens locked doors, windows, and other objects. Hermione uses this spell to unlock doors throughout Hogwarts during their first year adventures.",
            "type": "charm"
        },
        {
            "name": "Lumos",
            "pronunciation": "LOO-mos",
            "description": "The Wand-Lighting Charm produces a bright light from the tip of the wand. Essential for navigating dark corridors and mysterious places in the castle.",
            "type": "charm"
        },
        {
            "name": "Nox",
            "pronunciation": "noks",
            "description": "The Wand-Extinguishing Charm extinguishes the light produced by Lumos. Always remember to turn off your magical light when you're done!",
            "type": "charm"
        },
        {
            "name": "Wingardium Leviosa",
            "pronunciation": "win-GAR-dee-um lev-ee-OH-sah",
            "description": "The Levitation Charm makes objects fly. It's swish and flick, not swish and flick! This spell helped Harry and friends get past Fluffy.",
            "type": "charm"
        }
    ],
    "Chamber of Secrets": [
        {
            "name": "Expelliarmus",
            "pronunciation": "ex-pel-ee-AR-mus",
            "description": "The Disarming Charm forces an opponent to release whatever they're holding, often their wand. Harry's signature spell that he uses throughout the series.",
            "type": "defense"
        },
        {
            "name": "Obliviate",
            "pronunciation": "oh-BLIV-ee-ate",
            "description": "The Memory Charm erases specific memories from the target's mind. Gilderoy Lockhart attempts to use this on Harry and Ron, but it backfires spectacularly.",
            "type": "charm"
        },
        {
            "name": "Rictusempra",
            "pronunciation": "rik-tu-SEM-pra",
            "description": "The Tickling Charm causes the victim to buckle over with laughter. Harry uses this against Draco during their duel in the Dueling Club.",
            "type": "charm"
        }
    ],
    "Prisoner of Azkaban": [
        {
            "name": "Expecto Patronum",
            "pronunciation": "ex-PEK-toh pa-TROH-num",
            "description": "The Patronus Charm conjures a guardian against Dementors. The caster must focus on their happiest memory to produce a silver, animal-shaped protector.",
            "type": "defense"
        },
        {
            "name": "Riddikulus",
            "pronunciation": "ri-dik-YOU-lus",
            "description": "The Boggart-Banishing Spell transforms a Boggart into something amusing, weakening it through laughter. Think of something funny about your worst fear!",
            "type": "defense"
        },
        {
            "name": "Mobiliarbus",
            "pronunciation": "mo-bil-ee-AR-bus",
            "description": "This spell animates trees, causing them to move and attack. Used by Professor Lupin during his demonstration of defensive magic.",
            "type": "transfiguration"
        }
    ],
    "Goblet of Fire": [
        {
            "name": "Avada Kedavra",
            "pronunciation": "ah-VAH-də kə-DAV-rə",
            "description": "The Killing Curse is one of the three Unforgivable Curses. It causes instant death with no known counter-curse. Voldemort's favorite spell.",
            "type": "curse"
        },
        {
            "name": "Crucio",
            "pronunciation": "KROO-see-oh",
            "description": "The Cruciatus Curse is an Unforgivable Curse that inflicts excruciating pain on the victim. Mad-Eye Moody (Barty Crouch Jr.) demonstrates this on a spider.",
            "type": "curse"
        },
        {
            "name": "Imperio",
            "pronunciation": "im-PEER-ee-oh",
            "description": "The Imperius Curse is an Unforgivable Curse that controls the victim's actions. The victim feels a sense of euphoria and loses their free will.",
            "type": "curse"
        },
        {
            "name": "Accio",
            "pronunciation": "AK-see-oh",
            "description": "The Summoning Charm brings an object to the caster. Harry uses this to summon his Firebolt during the first task of the Triwizard Tournament.",
            "type": "charm"
        }
    ],
    "Order of the Phoenix": [
        {
            "name": "Stupefy",
            "pronunciation": "STOO-pə-fy",
            "description": "The Stunning Spell renders the victim unconscious. A red light shoots from the wand, and it's commonly used by Aurors and in magical duels.",
            "type": "defense"
        },
        {
            "name": "Protego",
            "pronunciation": "pro-TAY-go",
            "description": "The Shield Charm creates a magical barrier that deflects hexes, jinxes, and curses back at the attacker. Essential for any dueling situation.",
            "type": "defense"
        },
        {
            "name": "Reducto",
            "pronunciation": "re-DUK-toh",
            "description": "The Reductor Curse blasts solid objects apart. Ginny uses this spell effectively during the Department of Mysteries battle.",
            "type": "curse"
        }
    ],
    "Half-Blood Prince": [
        {
            "name": "Sectumsempra",
            "pronunciation": "sec-tum-SEM-pra",
            "description": "A dark spell invented by Severus Snape that slashes the victim as if cut by an invisible sword. Harry uses this on Draco with devastating results.",
            "type": "curse"
        },
        {
            "name": "Vulnera Sanentur",
            "pronunciation": "VUL-ner-ah sah-NEN-tur",
            "description": "A healing spell that counters the effects of Sectumsempra. Snape uses this three-part incantation to save Draco's life.",
            "type": "healing"
        },
        {
            "name": "Muffliato",
            "pronunciation": "muf-lee-AH-to",
            "description": "A spell that fills the ears of nearby people with an unidentifiable buzzing sound, preventing them from overhearing conversations. Another Snape invention.",
            "type": "utility"
        }
    ],
    "Deathly Hallows Part 1": [
        {
            "name": "Confringo",
            "pronunciation": "con-FRIN-go",
            "description": "The Blasting Curse creates explosions. Hermione uses this spell to destroy the horcrux locket after they retrieve it from Umbridge.",
            "type": "curse"
        },
        {
            "name": "Polyjuice Potion",
            "pronunciation": "POL-ee-juice",
            "description": "While not a spell, this complex potion allows the drinker to assume the appearance of another person. Used for the Seven Potters mission.",
            "type": "utility"
        }
    ],
    "Deathly Hallows Part 2": [
        {
            "name": "Fianto Duri",
            "pronunciation": "fee-AN-toh DOO-ree",
            "description": "A protective charm that strengthens shield spells and other defensive enchantments. Used to defend Hogwarts during the final battle.",
            "type": "defense"
        },
        {
            "name": "Protego Maxima",
            "pronunciation": "pro-TAY-go MAX-ih-ma",
            "description": "A powerful version of the Shield Charm that creates a large protective barrier. McGonagall uses this to protect Hogwarts Castle.",
            "type": "defense"
        },
        {
            "name": "Piertotum Locomotor",
            "pronunciation": "peer-TOH-tum lo-co-MOH-tor",
            "description": "The spell that animates statues and suits of armor. McGonagall uses this to bring the castle's defenses to life: 'I've always wanted to use that spell!'",
            "type": "transfiguration"
        }
    ]
}

def get_spell_type_class(spell_type):
    return spell_type.lower()

def cast_spell_feedback(spell_name, user_input):
    """Generate feedback for spell casting attempts"""
    spell_name_clean = spell_name.lower().replace(" ", "")
    user_input_clean = user_input.lower().replace(" ", "").replace("!", "").replace(".", "")
    
    # Perfect match
    if user_input_clean == spell_name_clean:
        success_messages = [
            f"🌟 Perfect! You've successfully cast {spell_name}! The spell glows brilliantly!",
            f"✨ Excellent work! {spell_name} was cast flawlessly! You're a natural wizard!",
            f"🎯 Magnificent! Your pronunciation of {spell_name} was spot on! The magic flows through you!",
            f"⭐ Outstanding! {spell_name} worked perfectly! Professor Flitwick would be proud!"
        ]
        return "success", random.choice(success_messages)
    
    # Close match (80% similarity)
    elif len(user_input_clean) > 0 and (len(set(spell_name_clean) & set(user_input_clean)) / len(set(spell_name_clean))) > 0.6:
        partial_messages = [
            f"⚡ Close! Your {spell_name} almost worked. Try focusing on the pronunciation!",
            f"💫 Not bad! {spell_name} flickered but didn't quite take hold. Practice makes perfect!",
            f"🌙 You're getting there! {spell_name} showed some magical sparks. Keep trying!",
            f"✨ Almost! Your wand trembled with {spell_name}. Just need a bit more confidence!"
        ]
        return "partial", random.choice(partial_messages)
    
    # Poor attempt
    else:
        failure_messages = [
            f"💥 Oops! Your wand just made some sparks. {spell_name} needs more practice!",
            f"🌪️ Hmm, that didn't work. Try saying {spell_name} more clearly!",
            f"⚡ Your spell fizzled out! Remember, it's {spell_name} - pronunciation is key!",
            f"🔥 Nice try! But {spell_name} requires precise incantation. Don't give up!",
            f"💨 Your wand seems confused! Focus on {spell_name} and try again!",
            f"🎪 Well, that was... interesting! But it wasn't {spell_name}. Keep practicing!"
        ]
        return "failure", random.choice(failure_messages)

def create_lumos_effect():
    """Create a light effect for Lumos spell"""
    st.markdown("""
    <div class="lumos-effect"></div>
    <script>
        setTimeout(function() {
            var elements = document.getElementsByClassName('lumos-effect');
            if (elements.length > 0) {
                elements[0].remove();
            }
        }, 2000);
    </script>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    st.markdown('<h1 class="page-header">🪄 Hogwarts Spell Practice</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; color: #e8e8e8; margin-bottom: 2rem;">
        Welcome to the Hogwarts Spell Practice Room!<br>
        <em>"It's LeviOsa, not LeviosA!"</em> - Hermione Granger
    </div>
    """, unsafe_allow_html=True)
    
    # Movie/Year selection
    st.markdown("### 🎬 Choose Your Year at Hogwarts")
    
    # Create tabs for each movie
    movie_tabs = st.tabs(list(SPELLS_BY_MOVIE.keys()))
    
    for i, (movie, spells) in enumerate(SPELLS_BY_MOVIE.items()):
        with movie_tabs[i]:
            st.markdown(f"""
            <div style="text-align: center; margin: 1rem 0;">
                <h3 style="color: #ffd700; font-family: 'Cinzel', serif;">✨ {movie} Spells ✨</h3>
                <p style="color: #ccc; font-family: 'Cormorant Garamond', serif;">Master the spells from this magical year</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display spells in a grid
            cols = st.columns(2)
            for idx, spell in enumerate(spells):
                with cols[idx % 2]:
                    display_spell(spell, f"{movie}_{idx}")
    
    # Spell casting practice section
    st.markdown("---")
    st.markdown("### 🎯 Practice Spell Casting")
    
    with st.container():
        st.markdown('<div class="practice-section">', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; color: #ffd700; font-family: 'Cinzel', serif; font-size: 1.5rem; margin-bottom: 1rem;">
            🧙‍♂️ Spell Casting Challenge 🧙‍♀️
        </div>
        <div style="text-align: center; color: #ccc; font-family: 'Cormorant Garamond', serif; margin-bottom: 1.5rem;">
            Choose a spell from above and try to cast it by typing its name below!
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            user_spell = st.text_input(
                "🪄 Cast your spell here:",
                placeholder="Type the spell name (e.g., Expelliarmus, Lumos, Alohomora...)",
                key="spell_input"
            )
        
        with col2:
            cast_button = st.button("✨ Cast Spell!", key="cast_spell", type="primary")
        
        if cast_button and user_spell:
            # Find matching spell
            spell_found = None
            for spells in SPELLS_BY_MOVIE.values():
                for spell in spells:
                    if spell['name'].lower() in user_spell.lower() or user_spell.lower() in spell['name'].lower():
                        spell_found = spell
                        break
                if spell_found:
                    break
            
            if spell_found:
                result_type, message = cast_spell_feedback(spell_found['name'], user_spell)
                
                # Special effect for Lumos
                if spell_found['name'].lower() == 'lumos' and result_type == 'success':
                    create_lumos_effect()
                
                st.markdown(f'<div class="casting-result {result_type}">{message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="casting-result failure">🤔 Hmm, "{user_spell}" isn\'t a spell I recognize! Try one from the spells above.</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Random spell generator
    st.markdown("### 🎲 Random Spell Challenge")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🔮 Give me a random spell to practice!", key="random_spell"):
            all_spells = []
            for spells in SPELLS_BY_MOVIE.values():
                all_spells.extend(spells)
            
            random_spell = random.choice(all_spells)
            st.session_state['random_spell'] = random_spell
    
    with col2:
        if 'random_spell' in st.session_state:
            spell = st.session_state['random_spell']
            st.markdown(f"""
            <div style="background: rgba(139, 0, 0, 0.2); border: 2px solid #ffd700; border-radius: 10px; padding: 1rem; text-align: center;">
                <div style="color: #ffd700; font-family: 'Cinzel', serif; font-size: 1.5rem; font-weight: 700;">
                    {spell['name']}
                </div>
                <div style="color: #ffed4e; font-family: 'Cormorant Garamond', serif; font-style: italic; margin: 0.5rem 0;">
                    {spell['pronunciation']}
                </div>
                <div style="color: #ccc; font-family: 'Cormorant Garamond', serif; font-size: 0.9rem;">
                    Try to cast this spell!
                </div>
            </div>
            """, unsafe_allow_html=True)

def display_spell(spell, unique_key):
    type_class = get_spell_type_class(spell['type'])
    
    st.markdown(f"""
    <div class="spell-card">
        <div class="spell-name">{spell['name']}</div>
        <div class="spell-pronunciation">{spell['pronunciation']}</div>
        <div class="spell-type {type_class}">{spell['type'].title()}</div>
        <div class="spell-description">{spell['description']}</div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
