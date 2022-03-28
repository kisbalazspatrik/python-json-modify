import os.path
import json

filename = 'in.json'

jsonArr = []

with open(filename) as data_file:
    data = json.load(data_file)

for x in range(1,641):
    atk = 0
    defense = 0
    hp = 0

    # Back (2. attribute)
    match data[x]['attributes'][1]['value']:
      case "SMG":
        atk += 2
        defense += 0
        hp += 0
      case "Avery Bow":
        atk += 3
        defense += 2
        hp += 1
      case "Bunny Backpack":
        atk += 1
        defense += 0
        hp += 1
      case "Dragon Scrolls":
        atk += 1
        defense += 1
        hp += 0
      case "Purple Katana":
        atk += 2
        defense += 0
        hp += 0
      case "Fusion Rifle":
        atk += 2
        defense += 0
        hp += 0
      case "Pulse Rifle":
        atk += 1
        defense += 1
        hp += 0
      case "Sniper Rifle":
        atk += 2
        defense += 0
        hp += 0
      case "White Sword":
        atk += 1
        defense += 0
        hp += 1
      case "Cyber Blade":
        atk += 2
        defense += 1
        hp += 0
      case "Gianna Greatsword":
        atk += 3
        defense += 1
        hp += 2
      case "Energy Sword":
        atk += 2
        defense += 0
        hp += 0
      case "Plasma Rifle":
        atk += 2
        defense += 0
        hp += 1
      case "Alien Backpack":
        atk += 1
        defense += 0
        hp += 1
      case "Cyber Bow":
        atk += 2
        defense += 0
        hp += 0
      case "Scorpion Tails":
        atk += 2
        defense += 1
        hp += 1
      case "Cyber Dragon":
        atk += 1
        defense += 2
        hp += 1
      case "Thermal Cannon":
        atk += 3
        defense += 1
        hp += 0
      case "Galaxy Backpack":
        atk += 1
        defense += 1
        hp += 0
      case "Meta Claymore":
        atk += 2
        defense += 0
        hp += 0
      case "Field Generator":
        atk += 1
        defense += 0
        hp += 1
      case _:
          pass

    # Skin (3. attribute)
    match data[x]['attributes'][2]['value']:
      case "Prime Lilian":
        atk += 1
        defense += 0
        hp += 1
      case "Prime Avery":
        atk += 2
        defense += 2
        hp += 2
      case "Prime Serenity":
        atk += 0
        defense += 1
        hp += 1
      case "Prime Adalyn":
        atk += 1
        defense += 1
        hp += 0
      case "Prime Melody":
        atk += 1
        defense += 0
        hp += 1
      case "Prime Ruby":
        atk += 1
        defense += 2
        hp += 1
      case "Prime Stella":
        atk += 0
        defense += 1
        hp += 1
      case "Prime Ivy":
        atk += 1
        defense += 1
        hp += 1
      case "Prime Harper":
        atk += 1
        defense += 0
        hp += 1
      case "Prime Daisy":
        atk += 0
        defense += 1
        hp += 1
      case "Nova Juniper":
        atk += 1
        defense += 1
        hp += 0
      case "Nova Cora":
        atk += 1
        defense += 0
        hp += 1
      case "Nova Gianna":
        atk += 3
        defense += 2
        hp += 1
      case "Nova Valery":
        atk += 0
        defense += 1
        hp += 1
      case "Nova Violet":
        atk += 2
        defense += 0
        hp += 0
      case "Nova Charlotte":
        atk += 1
        defense += 1
        hp += 0
      case "Nova Jade":
        atk += 0
        defense += 0
        hp += 2
      case "Nova Scarlett":
        atk += 2
        defense += 1
        hp += 1
      case "Nova Phoebe":
        atk += 0
        defense += 2
        hp += 0
      case "Nova Sky":
        atk += 1
        defense += 2
        hp += 0
      case _:
          pass

    # Clothes (4. attribute)
    match data[x]['attributes'][3]['value']:
        case "Cyberbunny Outfit":
          atk += 1
          defense += 1
          hp += 2
        case "Avery Outfit":
          atk += 2
          defense += 1
          hp += 3
        case "Cherry Outfit":
          atk += 0
          defense += 1
          hp += 0
        case "Samurai Outfit":
          atk += 1
          defense += 1
          hp += 2
        case "UFO Outfit":
          atk += 1
          defense += 0
          hp += 1
        case "Street Outfit":
          atk += 0
          defense += 0
          hp += 1
        case "Seethrough Coat":
          atk += 0
          defense += 1
          hp += 0
        case "Kimono":
          atk += 1
          defense += 1
          hp += 1
        case "Ninja Outfit":
          atk += 1
          defense += 1
          hp += 0
        case "Gianna Outfit":
          atk += 2
          defense += 1
          hp += 3
        case "Strapless Top":
          atk += 0
          defense += 0
          hp += 1
        case "Infinity Outfit":
          atk += 0
          defense += 1
          hp += 1
        case "Mathematic Top":
          atk += 0
          defense += 0
          hp += 2
        case "Astronaut Suit":
          atk += 1
          defense += 1
          hp += 2
        case "Black Bra":
          atk += 0
          defense += 0
          hp += 1
        case "Nie Outfit":
          atk += 0
          defense += 1
          hp += 0
        case "Pard Bra":
          atk += 1
          defense += 0
          hp += 1
        case "Suntouched Outfit":
          atk += 0
          defense += 1
          hp += 2
        case "Casual Seethrough Outfit":
          atk += 0
          defense += 1
          hp += 0
        case "Pink Seethrough Outfit":
          atk += 1
          defense += 1
          hp += 1
        case "Pink Bra":
          atk += 0
          defense += 1
          hp += 0
        case "Red Bra":
          atk += 0
          defense += 0
          hp += 1
        case "Black Crop Top":
          atk += 0
          defense += 1
          hp += 1
        case "Racing Suit":
          atk += 1
          defense += 0
          hp += 2
        case "Wicked Lady Outfit":
          atk += 0
          defense += 1
          hp += 1
        case "Chinese Outfit":
          atk += 0
          defense += 1
          hp += 2
        case "Cutout Outfit":
          atk += 0
          defense += 1
          hp += 1
        case "Casual Top":
          atk += 0
          defense += 1
          hp += 0
        case "Sports Outfit":
          atk += 0
          defense += 0
          hp += 1
        case "Assymetric Black Outfit":
          atk += 0
          defense += 1
          hp += 1
        case "Nano Outfit":
          atk += 1
          defense += 0
          hp += 1
        case _:
            pass

    # Mask (5. attribute)
    match data[x]['attributes'][4]['value']:
        case "Headset":
            atk += 0
            defense += 1
            hp += 0
        case "Avery Mask":
            atk += 2
            defense += 3
            hp += 1
        case "Kiss Mask":
            atk += 1
            defense += 2
            hp += 1
        case "Gas Mask":
            atk += 0
            defense += 1
            hp += 1
        case "Butterfly Glasses":
            atk += 1
            defense += 0
            hp += 1
        case "White Mask":
            atk += 0
            defense += 1
            hp += 0
        case "Cigarette":
            atk += 1
            defense += 0
            hp += 0
        case "Kunai":
            atk += 2
            defense += 0
            hp += 0
        case "Fox Mask":
            atk += 1
            defense += 0
            hp += 0
        case "Gianna Mask":
            atk += 2
            defense += 2
            hp += 2
        case "Sports Mask":
            atk += 1
            defense += 1
            hp += 0
        case "Robotic Mask":
            atk += 2
            defense += 2
            hp += 0
        case "Pipe":
            atk += 0
            defense += 1
            hp += 1
        case "Astronaut Mask":
            atk += 1
            defense += 2
            hp += 0
        case "Implant":
            atk += 1
            defense += 0
            hp += 0
        case "Robodragon Mask":
            atk += 1
            defense += 2
            hp += 1
        case "Pilot Mask":
            atk += 2
            defense += 1
            hp += 0
        case "Gold Chain":
            atk += 0
            defense += 1
            hp += 1
        case "Silver Chain":
            atk += 0
            defense += 1
            hp += 0
        case "Piercings":
            atk += 1
            defense += 0
            hp += 0
        case "Retro Glasses":
            atk += 1
            defense += 0
            hp += 1
        case "Cyberpunk Glasses":
            atk += 1
            defense += 2
            hp += 1
        case "Toothpick":
            atk += 0
            defense += 0
            hp += 1
        case "Cherry":
            atk += 0
            defense += 0
            hp += 2
        case "Bamboo Mask":
            atk += 0
            defense += 1
            hp += 1
        case "Black Mask":
            atk += 2
            defense += 0
            hp += 0
        case "Skull Eyepatch":
            atk += 1
            defense += 1
            hp += 1
        case "Pocky":
            atk += 0
            defense += 0
            hp += 2
        case "Blindfold":
            atk += 1
            defense += 0
            hp += 1
        case "Wheat":
            atk += 0
            defense += 0
            hp += 1
        case "Bandages":
            atk += 1
            defense += 0
            hp += 1
        case "Bend-Aid":
            atk += 0
            defense += 0
            hp += 2
        case "Fish":
            atk += 1
            defense += 0
            hp += 1
        case "Steampunk Glasses":
            atk += 1
            defense += 1
            hp += 0
        case "Destroyer Mask":
            atk += 2
            defense += 2
            hp += 0
        case "Gum":
            atk += 0
            defense += 0
            hp += 1
        case _:
            pass

    # Hairstyle (6. attribute)
    match data[x]['attributes'][5]['value']:
        case "Black Bunny Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "Pink Bunny Hairstyle":
            atk += 1
            defense += 0
            hp += 1
        case "Avery Hairstyle":
            atk += 1
            defense += 2
            hp += 3
        case "Heart Hairstyle":
            atk += 0
            defense += 1
            hp += 1
        case "Short Purple Wave Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Short Blue Wave Hairstyle":
            atk += 1
            defense += 0
            hp += 0
        case "Short Pink Wave Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case "Purple Ponytail Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "White Kunoichi Hairstyle":
            atk += 2
            defense += 1
            hp += 1
        case "Afro Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case "Geisha Hairstyle":
            atk += 1
            defense += 0
            hp += 1
        case "Japanese Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "Tomboy Black Hairstyle":
            atk += 2
            defense += 0
            hp += 0
        case "Tomboy Purple Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "Pink Bun Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Blue Bun Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case "Black Bun Hairstyle":
            atk += 1
            defense += 0
            hp += 0
        case "Pink Mousse Roll Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case "Brown Mousse Roll Hairstyle":
            atk += 1
            defense += 0
            hp += 0
        case "White Mousse Roll Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Shinobi Hairstyle":
            atk += 1
            defense += 1
            hp += 1
        case "Gianna Hairstyle":
            atk += 3
            defense += 1
            hp += 2
        case "Blonde Robotic Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "Infinity Hairstyle":
            atk += 1
            defense += 1
            hp += 2
        case "Horned Hairstyle":
            atk += 1
            defense += 1
            hp += 1
        case "Galactic Halo":
            atk += 2
            defense += 0
            hp += 2
        case "Devil Halo":
            atk += 2
            defense += 2
            hp += 0
        case "Robotic Ponytail":
            atk += 2
            defense += 1
            hp += 0
        case "Bow Hairstyle":
            atk += 1
            defense += 2
            hp += 1
        case "Ghost Hairstyle":
            atk += 0
            defense += 1
            hp += 1
        case "Purple YGG Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case "Blonde YGG Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Pink AK Hairstyle":
            atk += 1
            defense += 2
            hp += 0
        case "Blonde AK Hairstyle":
            atk += 1
            defense += 1
            hp += 1
        case "White EV Hairstyle":
            atk += 1
            defense += 1
            hp += 0
        case "Pink EV Hairstyle":
            atk += 0
            defense += 1
            hp += 1
        case "Long Braid Hairstyle":
            atk += 1
            defense += 0
            hp += 1
        case "White Long Wave Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Pink Long Wave Hairstyle":
            atk += 0
            defense += 1
            hp += 0
        case "Zero Hairstyle":
            atk += 0
            defense += 0
            hp += 1
        case _:
            pass

    # Earring (7. attribute)
    match data[x]['attributes'][6]['value']:
        case "Cyberbunny Earring":
            atk += 1
            defense += 1
            hp += 2
        case "Avery Earring":
            atk += 2
            defense += 2
            hp += 2
        case "UFO Earring":
            atk += 1
            defense += 0
            hp += 0
        case "Wave Earring":
            atk += 0
            defense += 1
            hp += 0
        case "Circle Earring":
            atk += 0
            defense += 0
            hp += 1
        case "Spaceship Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Bullet Earring":
            atk += 2
            defense += 0
            hp += 0
        case "Bell Earring":
            atk += 0
            defense += 1
            hp += 2
        case "Planet Earring":
            atk += 0
            defense += 1
            hp += 3
        case "Robodragon Earring":
            atk += 0
            defense += 3
            hp += 0
        case "Blacksteel Earring":
            atk += 0
            defense += 2
            hp += 2
        case "Triforce Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Spaceelf Earring":
            atk += 0
            defense += 2
            hp += 1
        case "Triangle Earring":
            atk += 0
            defense += 1
            hp += 0
        case "Mood Earring":
            atk += 0
            defense += 0
            hp += 1
        case "Gianna Earring":
            atk += 2
            defense += 3
            hp += 1
        case "Shide Paper Earring":
            atk += 1
            defense += 0
            hp += 0
        case "Mayan Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Alignment Earring":
            atk += 0
            defense += 1
            hp += 1
        case "Pink Gemstone Earring":
            atk += 0
            defense += 2
            hp += 0
        case "Blue Gemstone Earring":
            atk += 0
            defense += 0
            hp += 2
        case "Love Earring":
            atk += 1
            defense += 1
            hp += 2
        case "Silver Earring":
            atk += 1
            defense += 0
            hp += 0
        case "Gold Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Heart Earring":
            atk += 0
            defense += 1
            hp += 1
        case "Boss Earring":
            atk += 1
            defense += 1
            hp += 1
        case "Stylish Earring":
            atk += 0
            defense += 1
            hp += 0
        case "Simple Earring":
            atk += 0
            defense += 0
            hp += 1
        case "Aztec Earring":
            atk += 1
            defense += 0
            hp += 0
        case "Simple Heart Earring":
            atk += 0
            defense += 1
            hp += 1
        case "Sad Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Butterfly Earring":
            atk += 0
            defense += 1
            hp += 1
        case "Donut Earring":
            atk += 0
            defense += 1
            hp += 0
        case "Golden Sun Earring":
            atk += 1
            defense += 0
            hp += 1
        case "Silver Sun Earring":
            atk += 1
            defense += 1
            hp += 0
        case "Giant Earring":
            atk += 0
            defense += 1
            hp += 1
        case "Thunder Earring":
            atk += 3
            defense += 0
            hp += 1
        case "Rose Earring":
            atk += 0
            defense += 2
            hp += 2
        case _:
            pass

    # Effect (8. attribute)
    match data[x]['attributes'][7]['value']:
        case "3D Globes":
            atk += 0
            defense += 1
            hp += 0
        case "Holy Light":
            atk += 0
            defense += 0
            hp += 1
        case "Lightning":
            atk += 1
            defense += 0
            hp += 0
        case "Sakura Blossom":
            atk += 0
            defense += 1
            hp += 0
        case "Bubbles":
            atk += 0
            defense += 0
            hp += 1
        case "Wind":
            atk += 1
            defense += 0
            hp += 0
        case  _:
            pass
        
    data[x]['Attack'] = atk
    data[x]['Defense'] = defense
    data[x]['Health'] = hp
        
jsonArr.append(data)
with open("out.json", "w") as outf:
    json.dump(jsonArr, outf, indent=4)