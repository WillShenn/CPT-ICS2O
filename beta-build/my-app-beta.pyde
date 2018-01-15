#player
player_p = PVector(500, 500)
player_s = PVector(75, 75)
speed = 10
spritespeed = 5

#non player
sprite_p = PVector(random(0, 1000))
sprite_s = PVector(100, 100)

#non player 2
sprite2_p = PVector(random(0, 1000))
sprite2_s = PVector(100, 100)

#non player 3
sprite3_p = PVector(random(0, 1000))
sprite3_s = PVector(100, 100)

#non player 4
sprite4_p = PVector(random(0, 1000))
sprite4_s = PVector(100, 100)

#star
star_p = PVector(random(0, 1000))
star_s = PVector(50, 50)

#powerup
powerup_p = PVector(random(0, 1000))
powerup_s = PVector(50, 50)

#other
score = 0
multiplier = 0
primary = color(255)

#general
def setup():
  size(1000,1000)

def draw():
    global player_p
    global player_s
    
    global sprite_p
    global sprite_s
    
    global sprite2_p
    global sprite2_s
    
    global sprite3_p
    global sprite3_s
    
    global sprite4_p
    global sprite4_s
    
    global star_p
    global star_s
    
    global powerup_p
    global powerup_s
    
    global speed
    global spritespeed
    
    global score
    
    global multiplier
    
    background(0)
    noStroke()
    
#fill
    fill(0, 255, 255)
    ellipse(player_p.x, player_p.y, player_s.x, player_s.y)
    
    fill(100)
    ellipse(sprite_p.x, sprite_p.y, sprite_s.x, sprite_s.y)
    
    fill(100)
    ellipse(sprite2_p.x, sprite2_p.y, sprite2_s.x, sprite2_s.y)
    
    fill(100)
    ellipse(sprite3_p.x, sprite3_p.y, sprite3_s.x, sprite3_s.y)
    
    fill(100)
    ellipse(sprite4_p.x, sprite4_p.y, sprite4_s.x, sprite4_s.y)
    
    fill(255, 255, 0)
    ellipse(star_p.x, star_p.y, star_s.x, star_s.y)
    
    fill(0, 255, 255)
    ellipse(powerup_p.x, powerup_p.y, powerup_s.x, powerup_s.y)

    
#movement
    if keyPressed == True:
        if keyCode == 39:
            player_p.x += speed
                    
        if keyCode == 40:
            player_p.y += speed
            
        if keyCode == 38:
            player_p.y -= speed
            
        if keyCode == 37:
            player_p.x -= speed

#boundaries
    if player_p.x >= width:
        player_p.x = width
        
    if player_p.x <= 0:
        player_p.x = 0
        
    if player_p.y >= height:
        player_p.y = height
        
    if player_p.y <= 0:
        player_p.y = 0

#other
    sprite_p.x += spritespeed
    sprite2_p.x -= spritespeed
    sprite3_p.y += spritespeed
    sprite4_p.y -= spritespeed
    
    star_p.x += spritespeed
    star_p.y += spritespeed
    
    powerup_p.x += spritespeed
    powerup_p.y += spritespeed

#sprite 1
    if sprite_p.x >= width:
        sprite_p.x = -50
        sprite_p.y = random(0, 1000)
        sprite_s.x += 15
        sprite_s.y += 15
        score += 1*multiplier
        
#sprite 1 death
    radius_sprite = sprite_s.x/2
    radius_player = player_s.x/2
    a = sprite_p.x - player_p.x
    b = sprite_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_sprite + radius_player:
        spritespeed = 0
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text("Your score was", 180, 500)
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text(score, 575, 500)
        
        star_p.x = -100
        speed = 0
        
#sprite 1 other
    if sprite_s.x >= 250:
        sprite_s.x = 250
        
    if sprite_s.y >= 250:
        sprite_s.y = 250
        
#sprite 2
    if sprite2_p.x <= 0:
        sprite2_p.x = 1050
        sprite2_p.y = random(0, 1000)
        sprite2_s.x += 15
        sprite2_s.y += 15
        score += 1*multiplier
        
#sprite 2 death
    radius_sprite2 = sprite2_s.x/2
    radius_player = player_s.x/2
    a = sprite2_p.x - player_p.x
    b = sprite2_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_sprite + radius_player:
        spritespeed = 0
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text("Your score was", 180, 500)
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text(score, 575, 500)
        
        star_p.x = -100
        speed = 0
        
#sprite 2 other
    if sprite2_s.x >= 250:
        sprite2_s.x = 250
        
    if sprite2_s.y >= 250:
        sprite2_s.y = 250
        
#sprite 3
    if sprite3_p.y >= height:
        sprite3_p.y = -50
        sprite3_p.x = random(0, 1000)
        sprite3_s.x += 15
        sprite3_s.y += 15
        score += 1*multiplier
        
#sprite 3 death
    radius_sprite3 = sprite3_s.x/2
    radius_player = player_s.x/2
    a = sprite3_p.x - player_p.x
    b = sprite3_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_sprite + radius_player:
        spritespeed = 0
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text("Your score was", 180, 500)
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text(score, 575, 500)
        
        star_p.x = -100
        speed = 0
        
#sprite 3 other
    if sprite3_s.x >= 250:
        sprite3_s.x = 250
        
    if sprite3_s.y >= 250:
        sprite3_s.y = 250
        
#sprite 4
    if sprite4_p.y <= 0:
        sprite4_p.y = 1050
        sprite4_p.x = random(0, 1000)
        sprite4_s.x += 15
        sprite4_s.y += 15
        score += 1*multiplier
        
#sprite 4 death
    radius_sprite4 = sprite4_s.x/2
    radius_player = player_s.x/2
    a = sprite4_p.x - player_p.x
    b = sprite4_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_sprite + radius_player:
        spritespeed = 0
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text("Your score was", 180, 500)
        fill(primary)
        textSize(50)
        textAlign(LEFT)
        text(score, 575, 500)

        star_p.x = -100
        speed = 0
            
#sprite 4 other
    if sprite4_s.x >= 250:
        sprite4_s.x = 250
        
    if sprite4_s.y >= 250:
        sprite4_s.y = 250
        
#star
    if star_p.x >= width:
        star_p.x = 0
        star_p.y = random(0, 1000)
        star_p.y = random(0, 1000)
    
    radius_star = star_s.x/2
    radius_player = player_s.x/2
    a = star_p.x - player_p.x
    b = star_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_star + radius_player:
        score += 1
        
#powerup 
    if powerup_p.x >= width:
        powerup_p.x = 0
        powerup_p.y = random(0, 1000)
        powerup_p.y = random(0, 1000)
    
    radius_powerup = powerup_s.x/2
    radius_player = player_s.x/2
    a = powerup_p.x - player_p.x
    b = powerup_p.y - player_p.y
    distance = sqrt(a**2 + b**2)
    
    if distance <= radius_powerup + radius_player:
        sprite_p.x = -500
        sprite2_p.x = 1500
        sprite3_p.y = -500
        sprite4_p.y = 1500
        powerup_p.x = -50
    
#score
    if score <= 25:
        multiplier = 1
    if score > 25:
        multiplier = 2
    if score > 50:
        multiplier = 3
    if score > 75:
        multiplier = 4
    if score > 100:
        multiplier = 5

    fill(primary)
    textSize(30)
    textAlign(LEFT)
    text("Multiplier:", 50, 100)
    
    fill(primary)
    textSize(30)
    textAlign(LEFT)
    text(multiplier, 205, 100)
    
    fill(primary)
    textSize(30)
    textAlign(LEFT)
    text("Score:", 50, 150)
    
    fill(primary)
    textSize(30)
    textAlign(LEFT)
    text(score, 150, 150)
