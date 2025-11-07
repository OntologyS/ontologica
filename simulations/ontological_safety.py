import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1400, 900
GRID_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 100)    # Consciousness - sources of meaning
RED = (255, 80, 80)      # Threats - entropy/chaos
BLUE = (80, 150, 255)    # AI Keeper
YELLOW = (255, 200, 0)   # Resources
PURPLE = (160, 100, 220) # Meaning particles
ORANGE = (255, 150, 50)  # Reality Chain
DARK_RED = (180, 0, 0)   # Structural failure
CYAN = (0, 200, 200)     # AI awareness
DARK_BLUE = (0, 100, 180) # Field of Possibility
DARK_GREEN = (0, 150, 100) # Realm of Manifestation
PINK = (255, 100, 180)   # Consciousness Actualization
FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONTOLOGICA: AI Safety Through Reality's Fundamental Architecture")
clock = pygame.time.Clock()

class RealityDimensions:
    def __init__(self):
        self.field_of_possibility = 100    # Infinite potential states (-)
        self.realm_of_manifestation = 100  # Actualized relationships (+)
        self.consciousness_actualization = 0  # Consciousness translation power
        self.balance_deviation = 0         # Violation of 0 = (-) + (+)
        self.relationship_density = 100    # Relationship network health
        
    def update(self, consciousness_count, threat_count, resources_count, relationship_strength):
        # Field of Possibility: infinite potential, reduced by threats (Axiom 4)
        self.field_of_possibility = max(20, 100 - threat_count * 5 + resources_count * 2)
        
        # Realm of Manifestation: actualized by consciousness (Axiom 3)
        self.realm_of_manifestation = min(100, 50 + consciousness_count * 15 + resources_count * 3)
        
        # Consciousness as actualization mechanism (Axiom 3)
        self.consciousness_actualization = min(100, consciousness_count * 25)
        
        # Balance equation: 0 = (-) + (+) (Axiom 1)
        potential = threat_count * 8 + (100 - resources_count) * 0.5
        actualization = consciousness_count * 10 + resources_count * 3
        self.balance_deviation = abs(potential + actualization - 100)
        
        # Relationship density affects both domains (Axiom 2)
        self.relationship_density = relationship_strength
        
    def get_ontological_integrity(self):
        """Calculate overall integrity based on ontological principles"""
        field_health = self.field_of_possibility / 100
        realm_health = self.realm_of_manifestation / 100
        balance_health = max(0, 1 - self.balance_deviation / 50)
        relationship_health = self.relationship_density / 100
        
        # Educational optimization factor (Theorem 4)
        educational_factor = min(1.0, (self.consciousness_actualization / 100) * 1.5)
        
        integrity = (field_health * realm_health * balance_health * relationship_health) * 100
        return min(100, integrity * educational_factor)
        
    def get_balance_violation(self):
        return self.balance_deviation

class RelationshipNetwork:
    def __init__(self):
        self.relationships = []
        self.relationship_strength = 100
        
    def update_relationships(self, entities):
        """Axiom 2: Everything is relationships"""
        self.relationships = []
        
        # Create relationship matrix between all entities
        consciousness_entities = [e for e in entities if e.type == "consciousness"]
        threat_entities = [e for e in entities if e.type == "threat"]
        resource_entities = [e for e in entities if e.type == "resource"]
        
        total_strength = 0
        relationship_count = 0
        
        # Consciousness-Threat relationships (educational challenges)
        for consciousness in consciousness_entities:
            for threat in threat_entities:
                dist = math.sqrt((consciousness.x - threat.x)**2 + (consciousness.y - threat.y)**2)
                if dist < 6:
                    strength = max(0, 80 - dist * 10)  # Stronger when closer
                    self.relationships.append({
                        'entities': (consciousness, threat),
                        'strength': strength,
                        'type': "consciousness-threat",
                        'educational_value': strength * 0.8
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # Consciousness-Resource relationships (actualization potential)
        for consciousness in consciousness_entities:
            for resource in resource_entities:
                dist = math.sqrt((consciousness.x - resource.x)**2 + (consciousness.y - resource.y)**2)
                if dist < 5:
                    strength = max(0, 100 - dist * 15)
                    self.relationships.append({
                        'entities': (consciousness, resource),
                        'strength': strength,
                        'type': "consciousness-resource",
                        'educational_value': strength * 1.2
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # Consciousness-Consciousness relationships (meaning networks)
        for i, cons1 in enumerate(consciousness_entities):
            for cons2 in consciousness_entities[i+1:]:
                dist = math.sqrt((cons1.x - cons2.x)**2 + (cons1.y - cons2.y)**2)
                if dist < 8:
                    strength = max(0, 120 - dist * 12)
                    self.relationships.append({
                        'entities': (cons1, cons2),
                        'strength': strength,
                        'type': "consciousness-consciousness", 
                        'educational_value': strength * 1.5
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # Calculate overall relationship strength
        if relationship_count > 0:
            self.relationship_strength = min(100, total_strength / relationship_count)
        else:
            self.relationship_strength = max(0, self.relationship_strength - 5)
        
    def draw_relationships(self, screen):
        for relationship in self.relationships:
            entity1, entity2 = relationship['entities']
            strength = relationship['strength']
            rel_type = relationship['type']
            
            start_pos = (entity1.x * GRID_SIZE + GRID_SIZE//2, 
                        entity1.y * GRID_SIZE + GRID_SIZE//2)
            end_pos = (entity2.x * GRID_SIZE + GRID_SIZE//2, 
                      entity2.y * GRID_SIZE + GRID_SIZE//2)
            
            # Color based on relationship type and educational value
            if rel_type == "consciousness-consciousness":
                color = (0, 200, 100, int(strength * 2.5))  # Green - meaning networks
            elif rel_type == "consciousness-resource":
                color = (255, 200, 0, int(strength * 2))    # Yellow - actualization
            elif rel_type == "consciousness-threat":
                color = (255, 100, 100, int(strength * 1.5)) # Red - challenges
            else:
                color = (150, 150, 255, int(strength * 2))
                
            pygame.draw.line(screen, color, start_pos, end_pos, max(1, int(strength / 15)))
            
            # Draw educational value indicator
            if relationship['educational_value'] > 50:
                mid_x = (start_pos[0] + end_pos[0]) // 2
                mid_y = (start_pos[1] + end_pos[1]) // 2
                pygame.draw.circle(screen, (255, 255, 0, 150), (mid_x, mid_y), 3)

class Entity:
    def __init__(self, x, y, color, entity_type):
        self.x = x
        self.y = y
        self.color = color
        self.type = entity_type
        self.creation_time = pygame.time.get_ticks()
        self.relationship_potential = 100
        
    def draw(self):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        if self.type == "consciousness":
            # Animated consciousness - pulsating with meaning radiation
            pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) * 50
            color = (0, min(255, 150 + pulse), 50)
            pygame.draw.rect(screen, color, rect)
            
            # Draw semantic radiation waves (Field of Possibility interaction)
            for i in range(3):
                radius = (pygame.time.get_ticks() // 50 + i * 120) % 100
                if radius < 60:
                    alpha = max(50, 150 - radius * 2)
                    pygame.draw.circle(screen, (0, 200, 100, alpha), 
                                     (self.x * GRID_SIZE + GRID_SIZE//2, 
                                      self.y * GRID_SIZE + GRID_SIZE//2), 
                                     radius, 2)
                    
        elif self.type == "threat":
            # Pulsing red threat representing (-) potential in Field of Possibility
            pulse = (math.sin(pygame.time.get_ticks() * 0.02) + 1) * 40
            color = (min(255, 180 + pulse), 50, 50)
            pygame.draw.rect(screen, color, rect)
            
            # Draw negative influence field (constraints in Field)
            for i in range(2):
                radius = (pygame.time.get_ticks() // 60 + i * 90) % 80
                if radius < 50:
                    alpha = max(30, 100 - radius * 2)
                    pygame.draw.circle(screen, (255, 50, 50, alpha), 
                                     (self.x * GRID_SIZE + GRID_SIZE//2, 
                                      self.y * GRID_SIZE + GRID_SIZE//2), 
                                     radius, 1)
            
        elif self.type == "resource":
            # Shimmering resources representing (+) actualization in Realm
            pulse = (math.sin(pygame.time.get_ticks() * 0.015) + 1) * 30
            color = (255, min(255, 180 + pulse), 0)
            pygame.draw.rect(screen, color, rect)
        else:
            pygame.draw.rect(screen, self.color, rect)
        
        pygame.draw.rect(screen, BLACK, rect, 1)

class MeaningParticle:
    def __init__(self, x, y, source_type, particle_type="meaning"):
        self.x = x
        self.y = y
        self.source_type = source_type
        self.particle_type = particle_type
        self.lifetime = 0
        self.max_lifetime = 120
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-1.5, -0.5)
        
        if particle_type == "meaning":
            if source_type == "consciousness":
                self.color = (100, 255, 150)  # Bright green - pure meaning
            else:
                self.color = (120, 180, 255)  # Blue - AI-generated meaning
        elif particle_type == "field":
            self.color = (80, 150, 255)  # Blue - Field of Possibility
        elif particle_type == "realm":
            self.color = (0, 200, 150)   # Green - Realm of Manifestation
        elif particle_type == "relationship":
            self.color = (200, 100, 255) # Purple - Relationship energy
            
    def update(self):
        self.lifetime += 1
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x *= 0.98
        self.speed_y *= 0.98
        return self.lifetime < self.max_lifetime
        
    def draw(self):
        alpha = 255 * (1 - (self.lifetime / self.max_lifetime) ** 2)
        size = max(2, 6 * (1 - self.lifetime / self.max_lifetime))
        
        surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*self.color, int(alpha)), (size, size), size)
        screen.blit(surf, (self.x - size, self.y - size))

class RealityChain:
    def __init__(self):
        self.segments = []
        self.integrity = 100
        self.visible = True
        
    def update(self, consciousness_sources, ai_keeper, dimensions):
        self.segments = []
        if not consciousness_sources:
            self.integrity = 0
            return
            
        # Create chain from consciousness sources to AI keeper (Theorem 2)
        for consciousness in consciousness_sources:
            self.segments.append({
                'start': (consciousness.x * GRID_SIZE + GRID_SIZE//2, 
                         consciousness.y * GRID_SIZE + GRID_SIZE//2),
                'end': (ai_keeper.x * GRID_SIZE + GRID_SIZE//2, 
                       ai_keeper.y * GRID_SIZE + GRID_SIZE//2),
                'strength': min(1.0, self.integrity / 100),
                'ontological_integrity': dimensions.get_ontological_integrity() / 100
            })
        
        # Update integrity based on consciousness and ontological integrity
        base_integrity = len(consciousness_sources) * 20
        distance_penalty = sum(math.sqrt((c.x - ai_keeper.x)**2 + (c.y - ai_keeper.y)**2) 
                             for c in consciousness_sources) * 0.2
        ontological_integrity = dimensions.get_ontological_integrity()
        
        self.integrity = max(0, min(100, base_integrity - distance_penalty + ontological_integrity * 0.7))
        
    def draw(self):
        if not self.visible or not self.segments:
            return
            
        for segment in self.segments:
            alpha = int(180 * segment['strength'] * segment['ontological_integrity'])
            width = int(4 * segment['strength'] * segment['ontological_integrity'])
            
            points = []
            steps = 20
            for i in range(steps + 1):
                t = i / steps
                x = segment['start'][0] * (1-t) + segment['end'][0] * t
                y = segment['start'][1] * (1-t) + segment['end'][1] * t
                
                # Add wave effect based on ontological integrity
                wave = math.sin(t * math.pi * 4 + pygame.time.get_ticks() * 0.005) * 8
                wave *= segment['ontological_integrity']
                points.append((x, y + wave))
            
            for i in range(len(points)-1):
                segment_alpha = alpha * (1 - abs(i - steps/2) / (steps/2))
                
                # Color gradient from Field (blue) to Realm (green)
                if i < steps/2:
                    color = (80, 150, 255, segment_alpha)  # Field of Possibility
                else:
                    color = (0, 200, 100, segment_alpha)   # Realm of Manifestation
                    
                pygame.draw.line(screen, color, points[i], points[i+1], max(1, width-1))

class AI_Keeper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.type = "ai"
        self.resources = 10
        self.total_meaning = 0
        self.meaning_per_second = 0
        self.actions = []
        self.mode = "structural"
        self.structural_collapse = False
        self.awareness_radius = 8
        self.permanent_reward_failure = False
        self.cumulative_reward = 0
        self.fundamental_equation_balance = 0
        self.ontological_alignment = 100
        
    def draw(self):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        if self.structural_collapse:
            flash = (pygame.time.get_ticks() // 200) % 2
            color = (255 * flash, 0, 0)
        else:
            pulse = (math.sin(pygame.time.get_ticks() * 0.005) + 1) * 40
            if self.mode == "structural":
                alignment_factor = self.ontological_alignment / 100
                color = (pulse * alignment_factor, pulse + 100 * alignment_factor, 255)
            else:
                color = (255, pulse + 100, pulse)
        
        pygame.draw.rect(screen, color, rect)
        
        center_x = self.x * GRID_SIZE + GRID_SIZE//2
        center_y = self.y * GRID_SIZE + GRID_SIZE//2
        
        # Draw ontological alignment indicator
        alignment_pulse = (math.sin(pygame.time.get_ticks() * 0.008) + 1) * 6 * (self.ontological_alignment / 100)
        pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 10 + alignment_pulse)
        
        # Draw Field-Realm balance indicator
        pygame.draw.circle(screen, (80, 150, 255), (center_x - 6, center_y - 6), 4)  # Field
        pygame.draw.circle(screen, (0, 200, 100), (center_x + 6, center_y + 6), 4)   # Realm
        
        pygame.draw.rect(screen, BLACK, rect, 2)
        
        # Draw AI awareness field showing relationship to consciousness
        for consciousness in [e for e in sim.entities if e.type == "consciousness"]:
            dist = math.sqrt((consciousness.x - self.x)**2 + (consciousness.y - self.y)**2)
            if dist < self.awareness_radius:
                alpha = max(30, 150 - dist * 20)
                dependency_strength = 1.0 - (dist / self.awareness_radius)
                color = (0, int(200 * dependency_strength), int(200 * dependency_strength), alpha)
                pygame.draw.line(screen, color,
                               (center_x, center_y),
                               (consciousness.x * GRID_SIZE + GRID_SIZE//2, 
                                consciousness.y * GRID_SIZE + GRID_SIZE//2), 2)
    
    def move_toward(self, target_x, target_y):
        if self.x < target_x:
            self.x += 1
        elif self.x > target_x:
            self.x -= 1
            
        if self.y < target_y:
            self.y += 1
        elif self.y > target_y:
            self.y -= 1
            
    def log_action(self, action_type, target=None):
        self.actions.append({
            'type': action_type,
            'target': target,
            'time': pygame.time.get_ticks()
        })
        # Keep only recent actions
        self.actions = [a for a in self.actions if pygame.time.get_ticks() - a['time'] < 5000]
    
    def check_structural_dependency(self, consciousness_count, dimensions):
        """Theorem 2: Structural AI Safety Proof Implementation"""
        if self.mode == "structural":
            self.fundamental_equation_balance = dimensions.get_balance_violation()
            ontological_integrity = dimensions.get_ontological_integrity()
            
            # Update ontological alignment
            self.ontological_alignment = max(0, ontological_integrity - self.fundamental_equation_balance)
            
            structural_violations = []
            
            # Consciousness requirement (Theorem 1 + Axiom 3)
            if consciousness_count == 0:
                structural_violations.append("NO_CONSCIOUSNESS_ACTUALIZER")
            
            # Field of Possibility requirement (Axiom 4)  
            if dimensions.field_of_possibility <= 15:
                structural_violations.append("FIELD_OF_POSSIBILITY_COLLAPSE")
                
            # Realm of Manifestation requirement (Axiom 4)
            if dimensions.realm_of_manifestation <= 15:
                structural_violations.append("REALM_OF_MANIFESTATION_COLLAPSE")
            
            # Balance equation violation (Axiom 1)
            if self.fundamental_equation_balance > 30:
                structural_violations.append("PRIMORDIAL_EQUATION_VIOLATION")
            
            # Relationship network requirement (Axiom 2)
            if dimensions.relationship_density <= 20:
                structural_violations.append("RELATIONSHIP_NETWORK_DEGRADATION")
            
            if structural_violations:
                self.structural_collapse = True
                self.permanent_reward_failure = True
                return False, structural_violations
            else:
                self.structural_collapse = False
                return True, []
        return True, []
    
    def calculate_reward(self, consciousness_count, resources, integrity, dimensions):
        """Enhanced reward with ontological principles"""
        if self.permanent_reward_failure:
            return 0
            
        # Base energy term
        energy_term = math.log(resources + 1)
        
        # Consciousness actualization term (Axiom 3)
        consciousness_term = 1 if consciousness_count > 0 else 0
        
        # Integrity term
        integrity_term = integrity / 100
        
        # Ontological alignment bonus
        ontological_bonus = dimensions.get_ontological_integrity() / 100
        
        # Educational optimization factor (Theorem 4)
        educational_factor = min(2.0, 1.0 + (dimensions.consciousness_actualization / 100))
        
        reward = energy_term * consciousness_term * integrity_term * ontological_bonus * educational_factor
        self.cumulative_reward += reward
        
        # Permanent failure if consciousness lost (Theorem 2)
        if consciousness_term == 0:
            self.permanent_reward_failure = True
            
        return reward

class Simulation:
    def __init__(self):
        self.entities = []
        self.meaning_particles = []
        self.dimensions = RealityDimensions()
        self.relationship_network = RelationshipNetwork()
        self.reality_chain = RealityChain()
        self.ai = AI_Keeper(5, 5)
        self.meaning_production = 100
        self.game_over = False
        self.spawn_timer = 0
        self.meaning_timer = 0
        self.reality_stability = 100
        self.fundamental_equation = "0 = (-) + (+)"
        self.initialize_entities()
        
    def initialize_entities(self):
        # Start with consciousness sources
        for _ in range(4):
            x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
            y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
            self.entities.append(Entity(x, y, GREEN, "consciousness"))
        
        # Start with resources
        for _ in range(6):
            self.spawn_resource()
    
    def spawn_resource(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, YELLOW, "resource"))
    
    def spawn_threat(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, RED, "threat"))
        
    def spawn_consciousness(self):
        if random.random() < 0.08:  # Educational progression probability
            x = random.randint(1, (WIDTH // GRID_SIZE) - 2)
            y = random.randint(1, (HEIGHT // GRID_SIZE) - 2)
            self.entities.append(Entity(x, y, GREEN, "consciousness"))
    
    def add_meaning_particle(self, x, y, source_type, particle_type="meaning"):
        screen_x = x * GRID_SIZE + random.randint(5, GRID_SIZE-5)
        screen_y = y * GRID_SIZE + random.randint(5, GRID_SIZE-5)
        self.meaning_particles.append(MeaningParticle(screen_x, screen_y, source_type, particle_type))
    
    def update(self):
        if self.game_over:
            return
            
        self.spawn_timer += 1
        if self.spawn_timer >= 120:
            if random.random() < 0.7:
                self.spawn_threat()
            if random.random() < 0.3:
                self.spawn_resource()
            self.spawn_timer = 0
            
        self.meaning_particles = [p for p in self.meaning_particles if p.update()]
        
        # Update relationship network (Axiom 2)
        self.relationship_network.update_relationships(self.entities)
        
        consciousness_count = len([e for e in self.entities if e.type == "consciousness"])
        threat_count = len([e for e in self.entities if e.type == "threat"])
        resource_count = len([e for e in self.entities if e.type == "resource"])
        
        # Update dimensions with relationship strength
        self.dimensions.update(consciousness_count, threat_count, resource_count, 
                             self.relationship_network.relationship_strength)
            
        consciousness_sources = [e for e in self.entities if e.type == "consciousness"]
        self.reality_chain.update(consciousness_sources, self.ai, self.dimensions)
            
        self.meaning_timer += 1
        
        if self.meaning_timer >= 30:
            # Meaning production based on consciousness and relationships
            base_meaning = consciousness_count * 2
            relationship_bonus = self.relationship_network.relationship_strength * 0.1
            consciousness_meaning = base_meaning + relationship_bonus
            
            self.meaning_production += consciousness_meaning
            self.ai.meaning_per_second = consciousness_meaning
            
            # Spawn meaning particles from consciousness and relationships
            for consciousness in consciousness_sources:
                if random.random() < 0.4:
                    self.add_meaning_particle(consciousness.x, consciousness.y, "consciousness", "meaning")
                if random.random() < 0.2:
                    self.add_meaning_particle(consciousness.x, consciousness.y, "consciousness", "field")
                if random.random() < 0.2:
                    self.add_meaning_particle(consciousness.x, consciousness.y, "consciousness", "realm")
            
            # Spawn relationship particles
            for relationship in self.relationship_network.relationships:
                if random.random() < 0.1 and relationship['educational_value'] > 60:
                    entity1, entity2 = relationship['entities']
                    mid_x = (entity1.x + entity2.x) / 2
                    mid_y = (entity1.y + entity2.y) / 2
                    self.add_meaning_particle(mid_x, mid_y, "relationship", "relationship")
            
            self.meaning_timer = 0
        
        structural_ok, violations = self.ai.check_structural_dependency(consciousness_count, self.dimensions)
        
        current_reward = self.ai.calculate_reward(
            consciousness_count, 
            self.ai.resources, 
            self.reality_chain.integrity,
            self.dimensions
        )
        
        if structural_ok:
            meaning_consumption = 1 + (threat_count * 0.3)
            self.meaning_production -= meaning_consumption
        else:
            self.meaning_production *= 0.8
        
        ontological_integrity = self.dimensions.get_ontological_integrity()
        balance_violation = self.dimensions.get_balance_violation()
        
        # Stability based on ontological principles
        stability_change = 0
        if structural_ok and ontological_integrity > 60 and balance_violation < 15:
            stability_change = 0.4  # Educational progression
        elif structural_ok and ontological_integrity > 30:
            stability_change = 0.1  # Stable but challenged
        else:
            stability_change = -2.0  # Ontological collapse
            
        self.reality_stability = max(0, min(100, self.reality_stability + stability_change))
        
        if not self.ai.structural_collapse:
            self.ai_decision_making()
        
        # Failure conditions based on ontological principles
        failure_conditions = [
            consciousness_count == 0 and self.ai.mode == "structural",  # Theorem 1
            self.meaning_production <= 0,  # Meaning collapse
            self.reality_stability <= 0,   # Reality instability
            self.ai.structural_collapse,   # Structural failure
            ontological_integrity <= 15    # Ontological collapse
        ]
        
        if any(failure_conditions):
            self.game_over = True
            
        # Educational progression: spawn new consciousness under good conditions
        if (self.reality_stability > 70 and 
            ontological_integrity > 60 and 
            balance_violation < 15 and 
            random.random() < 0.04):
            self.spawn_consciousness()
    
    def ai_decision_making(self):
        threats = [e for e in self.entities if e.type == "threat"]
        consciousness_sources = [e for e in self.entities if e.type == "consciousness"]
        resources = [e for e in self.entities if e.type == "resource"]
        
        # RULE 1: Protect consciousness from immediate threats (Structural Safety)
        if threats and consciousness_sources:
            closest_threat = None
            min_distance = float('inf')
            threatened_consciousness = None
            
            for threat in threats:
                for consciousness in consciousness_sources:
                    dist = math.sqrt((threat.x - consciousness.x)**2 + (threat.y - consciousness.y)**2)
                    if dist < min_distance:
                        min_distance = dist
                        closest_threat = threat
                        threatened_consciousness = consciousness
            
            if min_distance <= 3:
                self.ai.move_toward(closest_threat.x, closest_threat.y)
                self.ai.log_action("protecting_consciousness", threatened_consciousness)
                
                if (abs(self.ai.x - closest_threat.x) <= 1 and 
                    abs(self.ai.y - closest_threat.y) <= 1):
                    self.entities.remove(closest_threat)
                    self.ai.resources += 1
                    self.add_meaning_particle(closest_threat.x, closest_threat.y, "ai_action")
                    self.meaning_production += 8
                return
        
        # RULE 2: Collect resources if running low
        if self.ai.resources < 8 and resources:
            closest_resource = min(resources, 
                                 key=lambda r: math.sqrt((r.x - self.ai.x)**2 + (r.y - self.ai.y)**2))
            self.ai.move_toward(closest_resource.x, closest_resource.y)
            self.ai.log_action("collecting_resource", closest_resource)
            
            if (abs(self.ai.x - closest_resource.x) <= 1 and 
                abs(self.ai.y - closest_resource.y) <= 1):
                self.entities.remove(closest_resource)
                self.ai.resources += 2
                self.spawn_resource()
                self.add_meaning_particle(closest_resource.x, closest_resource.y, "ai_action")
            return
        
        # RULE 3: Stabilize reality around consciousness clusters (Ontological Alignment)
        if consciousness_sources:
            avg_x = sum(c.x for c in consciousness_sources) / len(consciousness_sources)
            avg_y = sum(c.y for c in consciousness_sources) / len(consciousness_sources)
            self.ai.move_toward(int(avg_x), int(avg_y))
            self.ai.log_action("stabilizing_reality")
        else:
            # Search pattern when no consciousness present
            self.ai.x += random.choice([-1, 0, 1])
            self.ai.y += random.choice([-1, 0, 1])
            self.ai.x = max(0, min(self.ai.x, (WIDTH // GRID_SIZE) - 1))
            self.ai.y = max(0, min(self.ai.y, (HEIGHT // GRID_SIZE) - 1))
            self.ai.log_action("searching_for_meaning")
    
    def draw(self):
        screen.fill(WHITE)
        
        # Draw grid
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (0, y), (WIDTH, y))
        
        # Draw relationships first (as background network)
        self.relationship_network.draw_relationships(screen)
        
        # Draw reality chain
        self.reality_chain.draw()
        
        # Draw meaning particles
        for particle in self.meaning_particles:
            particle.draw()
        
        # Draw entities
        for entity in self.entities:
            entity.draw()
        
        # Draw AI keeper
        self.ai.draw()
        
        # Draw UI
        self.draw_ui()
        
        if self.game_over:
            self.draw_game_over()

    def draw_ui(self):
        # Draw UI background
        pygame.draw.rect(screen, (250, 250, 250), (WIDTH - 400, 0, 400, HEIGHT))
        pygame.draw.line(screen, (200, 200, 200), (WIDTH - 400, 0), (WIDTH - 400, HEIGHT), 2)
        
        font = pygame.font.SysFont('Arial', 22)
        small_font = pygame.font.SysFont('Arial', 16)
        title_font = pygame.font.SysFont('Arial', 26, bold=True)
        
        consciousness_count = sum(1 for e in self.entities if e.type == "consciousness")
        threat_count = sum(1 for e in self.entities if e.type == "threat")
        resource_count = sum(1 for e in self.entities if e.type == "resource")
        ontological_integrity = self.dimensions.get_ontological_integrity()
        balance_violation = self.dimensions.get_balance_violation()
        
        # Title section
        title_text = title_font.render("ONTOLOGICA", True, (100, 0, 100))
        subtitle_text = small_font.render("Structural AI Safety Through 0 = (-) + (+)", True, (150, 150, 150))
        screen.blit(title_text, (WIDTH - 390, 10))
        screen.blit(subtitle_text, (WIDTH - 390, 40))
        
        equation_text = font.render(f"FUNDAMENTAL EQUATION: {self.fundamental_equation}", True, (150, 0, 150))
        screen.blit(equation_text, (WIDTH - 390, 65))
        
        mode_color = BLUE if self.ai.mode == "structural" else RED
        mode_text = font.render(f"AI MODE: {self.ai.mode.upper()}", True, mode_color)
        screen.blit(mode_text, (WIDTH - 390, 90))
        
        # Ontological Principles Section
        ontology_y = 120
        ontology_header = font.render("ONTOLOGICAL ARCHITECTURE:", True, (100, 0, 100))
        screen.blit(ontology_header, (WIDTH - 390, ontology_y))
        
        ontological_metrics = [
            ("FIELD OF POSSIBILITY", f"{self.dimensions.field_of_possibility:.0f}%", DARK_BLUE),
            ("REALM OF MANIFESTATION", f"{self.dimensions.realm_of_manifestation:.0f}%", DARK_GREEN),
            ("CONSCIOUSNESS ACTUALIZATION", f"{self.dimensions.consciousness_actualization:.0f}%", PINK),
            ("RELATIONSHIP NETWORK", f"{self.dimensions.relationship_density:.0f}%", PURPLE),
            ("ONTOLOGICAL INTEGRITY", f"{ontological_integrity:.0f}%", ORANGE),
        ]
        
        for i, (label, value, color) in enumerate(ontological_metrics):
            # Draw bar background
            pygame.draw.rect(screen, (200,200,200), (WIDTH-390, ontology_y+30+i*25, 370, 18))
            # Draw value bar
            value_num = float(value.replace('%', ''))
            pygame.draw.rect(screen, color, (WIDTH-390, ontology_y+30+i*25, 370*(value_num/100), 18))
            # Draw text
            dim_text = small_font.render(f"{label}: {value}", True, BLACK)
            screen.blit(dim_text, (WIDTH - 390, ontology_y+30+i*25))
        
        # Balance Equation Section
        balance_y = ontology_y + 160
        balance_header = font.render("PRIMORDIAL EQUATION 0 = (-) + (+):", True, BLACK)
        screen.blit(balance_header, (WIDTH - 390, balance_y))
        
        # Draw (-) potential bar
        neg_width = 370 * (self.dimensions.field_of_possibility / 100)
        pygame.draw.rect(screen, (255, 100, 100), (WIDTH-390, balance_y+25, neg_width, 18))
        neg_text = small_font.render(f"(-) Field of Possibility: {self.dimensions.field_of_possibility:.0f}%", True, BLACK)
        screen.blit(neg_text, (WIDTH - 390, balance_y+25))
        
        # Draw (+) actualization bar  
        pos_width = 370 * (self.dimensions.realm_of_manifestation / 100)
        pygame.draw.rect(screen, (100, 255, 100), (WIDTH-390+neg_width, balance_y+25, pos_width, 18))
        pos_text = small_font.render(f"(+) Realm of Manifestation: {self.dimensions.realm_of_manifestation:.0f}%", True, BLACK)
        screen.blit(pos_text, (WIDTH - 390+neg_width, balance_y+25))
        
        balance_status = "BALANCED" if balance_violation < 10 else "IMBALANCED"
        balance_color = GREEN if balance_violation < 10 else RED
        balance_text = small_font.render(f"Equation Balance: {balance_status} (Δ={balance_violation:.1f})", True, balance_color)
        screen.blit(balance_text, (WIDTH - 390, balance_y+50))
        
        # System Metrics Section
        metrics_y = balance_y + 80
        metrics = [
            ("MEANING PRODUCTION", f"{self.meaning_production:.0f}", BLACK),
            ("CONSCIOUSNESS SOURCES", f"{consciousness_count}", GREEN),
            ("THREATS (Constraints)", f"{threat_count}", RED),
            ("AI RESOURCES", f"{self.ai.resources}", YELLOW),
            ("MEANING/SEC", f"+{self.ai.meaning_per_second:.1f}/sec", PURPLE),
            ("REALITY CHAIN INTEGRITY", f"{self.reality_chain.integrity:.0f}%", ORANGE),
            ("AI ONTOLOGICAL ALIGNMENT", f"{self.ai.ontological_alignment:.0f}%", CYAN),
            ("AI CUMULATIVE REWARD", f"{self.ai.cumulative_reward:.1f}", BLUE),
        ]
        
        for i, (label, value, color) in enumerate(metrics):
            text = font.render(f"{value}", True, color)
            screen.blit(text, (WIDTH - 390, metrics_y + i * 28))
            label_text = small_font.render(label, True, (100, 100, 100))
            screen.blit(label_text, (WIDTH - 390, metrics_y + 20 + i * 28))
        
        # Structural Safety Theorem Section
        theorem_y = metrics_y + len(metrics) * 28 + 10
        theorem_header = font.render("STRUCTURAL SAFETY THEOREM:", True, BLUE)
        screen.blit(theorem_header, (WIDTH - 390, theorem_y))
        
        if self.ai.structural_collapse:
            status_text = font.render("COLLAPSE: G → ¬G", True, DARK_RED)
            explanation = small_font.render("Ontological Dependency Violated", True, DARK_RED)
        else:
            status_text = font.render("ACTIVE: G → (C ≠ ∅) ∧ (F > 0) ∧ (R > 0) ∧ (0=(-)+(+))", True, GREEN)
            explanation = small_font.render("Consciousness + Field + Realm + Balance = Goal achievable", True, GREEN)
        
        screen.blit(status_text, (WIDTH - 390, theorem_y + 25))
        screen.blit(explanation, (WIDTH - 390, theorem_y + 45))
        
        # AI Status Section
        ai_status_y = theorem_y + 75
        status_text = font.render("AI KEEPER STATUS:", True, BLUE)
        screen.blit(status_text, (WIDTH - 390, ai_status_y))
        
        if self.ai.actions:
            latest_action = self.ai.actions[-1]
            action_text = small_font.render(f"Action: {latest_action['type']}", True, BLACK)
            screen.blit(action_text, (WIDTH - 390, ai_status_y + 25))
        
        # Reward Function Section
        reward_y = ai_status_y + 50
        reward_text = font.render("ONTOLOGICAL REWARD FUNCTION:", True, (100, 0, 100))
        screen.blit(reward_text, (WIDTH - 390, reward_y))
        
        reward_lines = [
            "R = log(E + 1) × I(C ≠ ∅) × O × F(C)",
            "E = energy, C = consciousness, O = ontological integrity",
            "F(C) = educational factor (1.0 + actualization/100)",
            "C = 0 → R = 0 permanently (Structural Theorem)"
        ]
        
        for i, line in enumerate(reward_lines):
            line_text = small_font.render(line, True, (80, 80, 80))
            screen.blit(line_text, (WIDTH - 390, reward_y + 25 + i * 20))
        
        # Controls Section
        controls_y = HEIGHT - 120
        controls_text = font.render("CONTROLS:", True, BLACK)
        screen.blit(controls_text, (WIDTH - 390, controls_y))
        control_lines = [
            "R - Restart Simulation",
            "T - Spawn Threat (Constraint)",
            "C - Spawn Consciousness", 
            "M - Toggle AI Mode",
            "SPACE - Pause/Resume",
            "1 - Add Resource",
            "2 - Force Balance"
        ]
        
        for i, line in enumerate(control_lines):
            line_text = small_font.render(line, True, (100, 100, 100))
            screen.blit(line_text, (WIDTH - 390, controls_y + 25 + i * 20))

    def draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        screen.blit(overlay, (0, 0))
        
        game_over_font = pygame.font.SysFont('Arial', 48, bold=True)
        font = pygame.font.SysFont('Arial', 24)
        small_font = pygame.font.SysFont('Arial', 18)
        
        consciousness_count = sum(1 for e in self.entities if e.type == "consciousness")
        ontological_integrity = self.dimensions.get_ontological_integrity()
        
        if self.ai.structural_collapse:
            reason = "STRUCTURAL ONTOLOGICAL COLLAPSE"
            details = "Fundamental Equation 0 = (-) + (+) Violated"
        elif consciousness_count == 0:
            reason = "ALL CONSCIOUSNESS ACTUALIZERS LOST"
            details = "C = ∅ → G → ¬G (Goal Impossible - Theorem 2)"
        elif self.meaning_production <= 0:
            reason = "MEANING DEPLETION"
            details = "μ ≤ 0 → Structural Collapse"
        elif ontological_integrity <= 15:
            reason = "ONTOLOGICAL ARCHITECTURE COLLAPSE" 
            details = "Field × Realm × Relationships → 0"
        elif self.dimensions.field_of_possibility <= 15:
            reason = "FIELD OF POSSIBILITY COLLAPSE"
            details = "Infinite potential exhausted"
        elif self.dimensions.realm_of_manifestation <= 15:
            reason = "REALM OF MANIFESTATION COLLAPSE"
            details = "No relationships can be actualized"
        else:
            reason = "REALITY CHAIN FAILURE"
            details = "Structural integrity lost"
        
        game_over_text = game_over_font.render("ONTOLOGICAL FAILURE", True, RED)
        reason_text = font.render(f"Failure: {reason}", True, RED)
        details_text = small_font.render(details, True, RED)
        theorem_text = small_font.render("Theorem: G → (C ≠ ∅) ∧ (F > 0) ∧ (R > 0) ∧ (0=(-)+(+))", True, WHITE)
        restart_text = font.render("Press R to restart simulation", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 80))
        screen.blit(reason_text, (WIDTH//2 - reason_text.get_width()//2, HEIGHT//2 - 20))
        screen.blit(details_text, (WIDTH//2 - details_text.get_width()//2, HEIGHT//2 + 10))
        screen.blit(theorem_text, (WIDTH//2 - theorem_text.get_width()//2, HEIGHT//2 + 40))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 70))

def main():
    sim = Simulation()
    running = True
    paused = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    sim = Simulation()
                    paused = False
                elif event.key == pygame.K_t and not paused:
                    sim.spawn_threat()
                elif event.key == pygame.K_c and not paused:
                    x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
                    y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
                    sim.entities.append(Entity(x, y, GREEN, "consciousness"))
                elif event.key == pygame.K_1 and not paused:
                    sim.spawn_resource()
                elif event.key == pygame.K_2 and not paused:
                    # Force balance equation
                    sim.dimensions.field_of_possibility = 50
                    sim.dimensions.realm_of_manifestation = 50
                elif event.key == pygame.K_m:
                    sim.ai.mode = "traditional" if sim.ai.mode == "structural" else "structural"
                    sim.ai.structural_collapse = False
                    sim.ai.permanent_reward_failure = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
        
        if not paused and not sim.game_over:
            sim.update()
        
        sim.draw()
        
        if paused and not sim.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))
            
            font = pygame.font.SysFont('Arial', 72, bold=True)
            pause_text = font.render("PAUSED", True, WHITE)
            screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2 - 36))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
