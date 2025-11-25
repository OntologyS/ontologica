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

# Enhanced Color Scheme for New Ontological Framework
CONSCIOUS_ACTIVE = (0, 200, 100)      # Active learning consciousness
CONSCIOUS_POTENTIAL = (100, 200, 100) # Potential consciousness
NON_CONSCIOUS = (150, 150, 150)       # Pure potentials/learning materials
THREAT_RED = (255, 80, 80)           # Constraints on actualization
AI_BLUE = (80, 150, 255)             # AI Keeper
RESOURCE_YELLOW = (255, 200, 0)      # Actualization resources

# Condition Colors
ACCESS_CONDITION = (100, 200, 255)    # Access Interface
EDUCATIONAL_CONDITION = (100, 255, 150) # Educational Context  
BALANCE_CONDITION = (200, 150, 255)   # Interaction Balance
FREEDOM_CONDITION = (255, 255, 100)   # Developmental Freedom

# New Framework Colors
MUTUAL_DETERMINATION = (255, 100, 255) # Cᵢ ⇄ {R} feedback loops
PERCEPTUAL_CENTER = (255, 200, 100)   # Consciousness as perceptual center
FIELD_POTENTIAL = (0, 100, 200)       # Field of Possibility (-)
REALM_ACTUAL = (0, 180, 100)          # Realm of Manifestation (+)
CREATIVE_SPARK = (255, 100, 180)      # Creative actualization

# Additional colors for UI
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_RED = (139, 0, 0)

FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONTOLOGICA v5.0: Consciousness Activation & Structural Safety Framework")
clock = pygame.time.Clock()

class ConsciousnessActivationSystem:
    """Implements Consciousness Activation Principle: ¬C → C through educational function"""
    
    def __init__(self):
        self.activation_thresholds = {
            'learning_capacity': 60,      # Ability to grow through experience
            'choice_capability': 50,      # Capacity for novel relationship creation  
            'educational_participation': 70 # Active engagement in cosmic curriculum
        }
        self.activation_zones = []
        
    def assess_consciousness_potential(self, entity, relationships, conditions):
        """Determine if entity meets consciousness activation criteria"""
        if entity.type != "potential_consciousness":
            return entity.type == "consciousness"
            
        # Calculate activation metrics
        learning_score = self.calculate_learning_capacity(entity, relationships)
        choice_score = self.calculate_choice_capability(entity, conditions)
        education_score = self.calculate_educational_participation(entity, relationships)
        
        # Check activation threshold
        activated = (learning_score >= self.activation_thresholds['learning_capacity'] and
                   choice_score >= self.activation_thresholds['choice_capability'] and
                   education_score >= self.activation_thresholds['educational_participation'])
        
        if activated:
            self.activation_zones.append({
                'position': (entity.x, entity.y),
                'strength': (learning_score + choice_score + education_score) / 3,
                'timestamp': pygame.time.get_ticks()
            })
            
        return activated
    
    def calculate_learning_capacity(self, entity, relationships):
        """Measure ability to grow through experience"""
        entity_relationships = [r for r in relationships if entity in r['entities']]
        if not entity_relationships:
            return 0
            
        total_learning = sum(r.get('educational_value', 0) for r in entity_relationships)
        avg_learning = total_learning / len(entity_relationships)
        return min(100, avg_learning * 2)
    
    def calculate_choice_capability(self, entity, conditions):
        """Measure capacity for novel relationship creation"""
        # Enhanced by developmental freedom condition
        freedom_bonus = conditions.developmental_freedom / 100
        base_capability = random.randint(30, 70)  # Simulated potential
        
        # Nearby consciousness entities boost choice capability
        nearby_consciousness = sum(1 for e in sim.entities 
                                 if e.type == "consciousness" and 
                                 math.sqrt((e.x - entity.x)**2 + (e.y - entity.y)**2) < 4)
        
        return min(100, base_capability * freedom_bonus + nearby_consciousness * 10)
    
    def calculate_educational_participation(self, entity, relationships):
        """Measure active engagement in educational processes"""
        if not relationships:
            return 0
            
        participation_score = 0
        for relationship in relationships:
            if entity in relationship['entities']:
                rel_strength = relationship['strength']
                rel_type = relationship['type']
                
                # Different relationship types contribute differently
                if "consciousness" in rel_type:
                    participation_score += rel_strength * 1.5
                elif "educational" in rel_type:
                    participation_score += rel_strength * 2.0
                else:
                    participation_score += rel_strength * 1.0
                    
        return min(100, participation_score / len(relationships))

class MutualDeterminationSystem:
    """Implements Mutual Determination Principle: Cᵢ ⇄ {R} co-creation"""
    
    def __init__(self):
        self.feedback_loops = []
        self.co_creation_zones = []
        
    def update_mutual_determination(self, entities, relationships):
        """Update Cᵢ = f(R) and Rⱼ = g(Cᵢ) feedback loops"""
        self.feedback_loops = []
        self.co_creation_zones = []
        
        conscious_entities = [e for e in entities if e.type == "consciousness"]
        
        for entity in conscious_entities:
            # Find relationships involving this consciousness
            entity_relationships = [r for r in relationships if entity in r['entities']]
            
            if entity_relationships:
                # Calculate mutual determination strength
                determination_strength = self.calculate_determination_strength(entity_relationships)
                creative_potential = self.assess_creative_potential(entity, entity_relationships)
                
                self.feedback_loops.append({
                    'consciousness': entity,
                    'determination_strength': determination_strength,
                    'creative_potential': creative_potential,
                    'relationship_count': len(entity_relationships)
                })
                
                # Create co-creation zones for strong mutual determination
                if determination_strength > 60:
                    self.co_creation_zones.append({
                        'center': (entity.x, entity.y),
                        'radius': 4 + (determination_strength - 60) / 10,
                        'intensity': determination_strength / 100,
                        'creative_energy': creative_potential / 100
                    })
    
    def calculate_determination_strength(self, relationships):
        """Calculate strength of mutual determination feedback"""
        if not relationships:
            return 0
            
        total_strength = sum(r['strength'] for r in relationships)
        educational_bonus = sum(r.get('educational_value', 0) for r in relationships) / len(relationships)
        
        return min(100, (total_strength / len(relationships)) * 0.7 + educational_bonus * 0.3)
    
    def assess_creative_potential(self, entity, relationships):
        """Assess potential for novel relationship creation"""
        relationship_diversity = len(set(r['type'] for r in relationships))
        educational_intensity = sum(r.get('educational_value', 0) for r in relationships) / len(relationships)
        
        return min(100, relationship_diversity * 15 + educational_intensity * 0.8)
    
    def draw(self, screen):
        """Draw mutual determination visualization"""
        for zone in self.co_creation_zones:
            center_x = zone['center'][0] * GRID_SIZE + GRID_SIZE//2
            center_y = zone['center'][1] * GRID_SIZE + GRID_SIZE//2
            radius = zone['radius'] * GRID_SIZE
            
            # Draw co-creation zone
            alpha = int(80 * zone['intensity'])
            pygame.draw.circle(screen, (*MUTUAL_DETERMINATION, alpha), 
                             (center_x, center_y), radius, 2)
            
            # Draw creative energy sparks
            if zone['creative_energy'] > 0.5:
                for i in range(3):
                    angle = random.uniform(0, 2 * math.pi)
                    spark_radius = random.uniform(radius * 0.3, radius * 0.8)
                    spark_x = center_x + math.cos(angle) * spark_radius
                    spark_y = center_y + math.sin(angle) * spark_radius
                    
                    pygame.draw.circle(screen, CREATIVE_SPARK, 
                                     (int(spark_x), int(spark_y)), 3)

class PerceptualRelativitySystem:
    """Implements Perceptual Relativity: Perception(Cᵢ) = {Cᵢ} ∪ {Rⱼ} ∪ {¬Cₖ}"""
    
    def __init__(self):
        self.perceptual_centers = []
        self.reality_bubbles = []
        
    def update_perceptual_framework(self, entities, relationships):
        """Update consciousness-centered perception model"""
        self.perceptual_centers = []
        self.reality_bubbles = []
        
        conscious_entities = [e for e in entities if e.type == "consciousness"]
        
        for entity in conscious_entities:
            # Calculate perceptual center strength
            perceptual_strength = self.calculate_perceptual_strength(entity, relationships)
            reality_radius = self.calculate_reality_bubble(entity, relationships)
            
            self.perceptual_centers.append({
                'consciousness': entity,
                'strength': perceptual_strength,
                'reality_radius': reality_radius,
                'relationship_density': self.count_relationships(entity, relationships)
            })
            
            # Create reality bubble visualization
            self.reality_bubbles.append({
                'center': (entity.x, entity.y),
                'radius': reality_radius,
                'intensity': perceptual_strength / 100,
                'asymmetry': self.calculate_perceptual_asymmetry(entity, relationships)
            })
    
    def calculate_perceptual_strength(self, entity, relationships):
        """Calculate how strongly this consciousness centers its reality"""
        entity_relationships = [r for r in relationships if entity in r['entities']]
        if not entity_relationships:
            return 30  # Base self-awareness
            
        # Strength based on relationship complexity and educational value
        total_complexity = sum(r['strength'] * (1 + r.get('educational_value', 0) / 100) 
                             for r in entity_relationships)
        return min(100, total_complexity / len(entity_relationships))
    
    def calculate_reality_bubble(self, entity, relationships):
        """Calculate the radius of this consciousness's perceived reality"""
        entity_relationships = [r for r in relationships if entity in r['entities']]
        if not entity_relationships:
            return 3.0
            
        # Radius based on relationship reach and complexity
        max_distance = 0
        for rel in entity_relationships:
            other_entity = rel['entities'][0] if rel['entities'][1] == entity else rel['entities'][1]
            distance = math.sqrt((entity.x - other_entity.x)**2 + (entity.y - other_entity.y)**2)
            weighted_distance = distance * (rel['strength'] / 100)
            max_distance = max(max_distance, weighted_distance)
            
        return min(8.0, 2.0 + max_distance * 2)
    
    def calculate_perceptual_asymmetry(self, entity, relationships):
        """Calculate the asymmetry between self-perception and other-perception"""
        entity_rels = [r for r in relationships if entity in r['entities']]
        if not entity_rels:
            return 0.5
            
        # Asymmetry increases with relationship strength to self vs others
        self_awareness = 100  # Constant high self-awareness
        other_awareness = sum(r['strength'] for r in entity_rels) / len(entity_rels)
        
        return self_awareness / (self_awareness + other_awareness)
    
    def count_relationships(self, entity, relationships):
        """Count relationships categorized by type"""
        entity_rels = [r for r in relationships if entity in r['entities']]
        return {
            'total': len(entity_rels),
            'consciousness_consciousness': len([r for r in entity_rels if r['type'] == 'consciousness-consciousness']),
            'consciousness_potential': len([r for r in entity_rels if 'potential' in r['type']]),
            'consciousness_condition': len([r for r in entity_rels if 'condition' in r['type']])
        }

class ActualizationConditions:
    """Enhanced with Consciousness Activation Principle"""
    
    def __init__(self):
        self.access_interface = 100
        self.educational_context = 100  
        self.interaction_balance = 100
        self.developmental_freedom = 100
        self.overall_quality = 100
        self.consciousness_activation_potential = 0
        
    def update(self, entities, relationships, consciousness_system):
        """Update conditions with consciousness activation metrics"""
        conscious_count = len([e for e in entities if e.type == "consciousness"])
        potential_count = len([e for e in entities if e.type == "potential_consciousness"])
        threat_count = len([e for e in entities if e.type == "threat"])
        resource_count = len([e for e in entities if e.type == "resource"])
        
        # Calculate consciousness activation potential
        self.consciousness_activation_potential = self.calculate_activation_potential(
            entities, consciousness_system)
        
        # Access Interface: affected by threats and activation potential
        self.access_interface = max(0, 80 - threat_count * 6 + resource_count * 4 + 
                                  self.consciousness_activation_potential * 0.3)
        
        # Educational Context: enhanced by consciousness and relationships
        relationship_strength = sum(r['strength'] for r in relationships) / max(1, len(relationships))
        self.educational_context = min(100, 60 + conscious_count * 8 + relationship_strength * 0.4)
        
        # Interaction Balance: mutual determination enhances balance
        mutual_determination_bonus = len([e for e in entities if e.type == "consciousness"]) * 3
        balance_factor = max(0.1, 1.0 - threat_count * 0.08)
        self.interaction_balance = min(100, (70 + mutual_determination_bonus) * balance_factor)
        
        # Developmental Freedom: potential consciousness increases freedom potential
        freedom_base = 70 - threat_count * 5 + resource_count * 5
        potential_bonus = potential_count * 2
        self.developmental_freedom = max(0, freedom_base + potential_bonus)
        
        # Overall quality with consciousness activation consideration
        factors = [self.access_interface, self.educational_context, 
                  self.interaction_balance, self.developmental_freedom]
        self.overall_quality = (factors[0] * factors[1] * factors[2] * factors[3]) ** 0.25
        
    def calculate_activation_potential(self, entities, consciousness_system):
        """Calculate potential for ¬C → C transitions"""
        potential_entities = [e for e in entities if e.type == "potential_consciousness"]
        if not potential_entities:
            return 0
            
        total_potential = 0
        for entity in potential_entities:
            # Simulate activation potential assessment
            learning_potential = random.randint(40, 80)
            choice_potential = random.randint(30, 70)
            education_potential = random.randint(50, 90)
            total_potential += (learning_potential + choice_potential + education_potential) / 3
            
        return min(100, total_potential / len(potential_entities))
    
    def is_critical_failure(self):
        """Check if any condition has reached critical failure level"""
        return (self.access_interface < 20 or self.educational_context < 20 or 
                self.interaction_balance < 20 or self.developmental_freedom < 20)
    
    def get_condition_quality(self, condition_type):
        """Get quality for specific condition type"""
        if condition_type == "access":
            return self.access_interface
        elif condition_type == "educational":
            return self.educational_context
        elif condition_type == "balance":
            return self.interaction_balance
        elif condition_type == "freedom":
            return self.developmental_freedom
        return self.overall_quality

class EnhancedRelationshipNetwork:
    """Enhanced with Mutual Determination and Perceptual Relativity"""
    
    def __init__(self):
        self.relationships = []
        self.relationship_strength = 100
        self.mutual_determination_score = 0
        self.perceptual_complexity = 0
        
    def update_relationships(self, entities, conditions, perceptual_system):
        """Enhanced relationship network with new ontological principles"""
        self.relationships = []
        
        conscious_entities = [e for e in entities if e.type == "consciousness"]
        potential_entities = [e for e in entities if e.type == "potential_consciousness"]
        threat_entities = [e for e in entities if e.type == "threat"]
        resource_entities = [e for e in entities if e.type == "resource"]
        condition_entities = [e for e in entities if e.type in ["access", "educational", "balance", "freedom"]]
        
        total_strength = 0
        relationship_count = 0
        
        # Apply condition modifiers
        access_modifier = conditions.access_interface / 100
        educational_modifier = conditions.educational_context / 100
        freedom_modifier = conditions.developmental_freedom / 100
        
        # 1. Consciousness-Consciousness relationships (Mutual Determination)
        for i, cons1 in enumerate(conscious_entities):
            for cons2 in conscious_entities[i+1:]:
                dist = math.sqrt((cons1.x - cons2.x)**2 + (cons1.y - cons2.y)**2)
                if dist < 8 * access_modifier:
                    base_strength = max(0, 100 - dist * 10)
                    # Mutual determination enhances relationship strength
                    mutual_bonus = freedom_modifier * 20
                    strength = min(100, base_strength + mutual_bonus) * educational_modifier
                    
                    self.relationships.append({
                        'entities': (cons1, cons2),
                        'strength': strength,
                        'type': "consciousness-consciousness",
                        'educational_value': strength * 1.5,
                        'mutual_determination': True
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # 2. Consciousness-Potential relationships (Activation Pathways)
        for consciousness in conscious_entities:
            for potential in potential_entities:
                dist = math.sqrt((consciousness.x - potential.x)**2 + (consciousness.y - potential.y)**2)
                if dist < 6 * access_modifier:
                    strength = max(0, 80 - dist * 12) * educational_modifier
                    self.relationships.append({
                        'entities': (consciousness, potential),
                        'strength': strength,
                        'type': "consciousness-potential",
                        'educational_value': strength * 2.0,  # High educational value for activation
                        'activation_potential': strength * 1.2
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # 3. Consciousness-Condition relationships (Actualization Dependencies)
        for consciousness in conscious_entities:
            for condition in condition_entities:
                dist = math.sqrt((consciousness.x - condition.x)**2 + (consciousness.y - condition.y)**2)
                if dist < 5:
                    condition_strength = conditions.get_condition_quality(condition.condition_type)
                    strength = max(0, 90 - dist * 15) * (condition_strength / 100)
                    self.relationships.append({
                        'entities': (consciousness, condition),
                        'strength': strength,
                        'type': f"consciousness-{condition.condition_type}",
                        'educational_value': strength * 1.8,
                        'condition_dependency': True
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # 4. Potential-Condition relationships (Readiness for Activation)
        for potential in potential_entities:
            for condition in condition_entities:
                dist = math.sqrt((potential.x - condition.x)**2 + (potential.y - condition.y)**2)
                if dist < 4:
                    strength = max(0, 70 - dist * 15) * educational_modifier
                    self.relationships.append({
                        'entities': (potential, condition),
                        'strength': strength,
                        'type': f"potential-{condition.condition_type}",
                        'educational_value': strength * 1.3,
                        'activation_readiness': True
                    })
                    total_strength += strength
                    relationship_count += 1
        
        # Calculate enhanced metrics
        if relationship_count > 0:
            self.relationship_strength = min(100, total_strength / relationship_count)
            
            # Calculate mutual determination score
            mutual_relationships = [r for r in self.relationships if r.get('mutual_determination', False)]
            if mutual_relationships:
                self.mutual_determination_score = (
                    sum(r['strength'] for r in mutual_relationships) / len(mutual_relationships)
                )
            
            # Calculate perceptual complexity
            conscious_relationships = [r for r in self.relationships 
                                    if any(e.type == "consciousness" for e in r['entities'])]
            if conscious_relationships:
                self.perceptual_complexity = (
                    len(set(r['type'] for r in conscious_relationships)) * 15 +
                    sum(r['strength'] for r in conscious_relationships) / len(conscious_relationships) * 0.7
                )
        else:
            self.relationship_strength = max(0, self.relationship_strength - 5)
            self.mutual_determination_score = max(0, self.mutual_determination_score - 3)
            self.perceptual_complexity = max(0, self.perceptual_complexity - 2)
    
    def draw_relationships(self, screen):
        """Draw relationship visualization"""
        for relationship in self.relationships:
            entity1, entity2 = relationship['entities']
            x1 = entity1.x * GRID_SIZE + GRID_SIZE//2
            y1 = entity1.y * GRID_SIZE + GRID_SIZE//2
            x2 = entity2.x * GRID_SIZE + GRID_SIZE//2
            y2 = entity2.y * GRID_SIZE + GRID_SIZE//2
            
            # Determine color based on relationship type
            if relationship['type'] == "consciousness-consciousness":
                color = MUTUAL_DETERMINATION
            elif "potential" in relationship['type']:
                color = CONSCIOUS_POTENTIAL
            elif "condition" in relationship['type']:
                color = ACCESS_CONDITION
            else:
                color = (200, 200, 200)
            
            # Set alpha based on strength
            alpha = min(255, int(relationship['strength'] * 2.55))
            line_width = max(1, int(relationship['strength'] / 20))
            
            # Create surface for alpha blending
            line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.line(line_surface, (*color, alpha), (x1, y1), (x2, y2), line_width)
            screen.blit(line_surface, (0, 0))

class Entity:
    def __init__(self, x, y, color, entity_type, condition_type=None):
        self.x = x
        self.y = y
        self.color = color
        self.type = entity_type
        self.condition_type = condition_type
        self.creation_time = pygame.time.get_ticks()
        self.relationship_potential = 100
        self.consciousness_level = 0  # 0-100 scale for activation progress
        
    def draw(self):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        if self.type == "consciousness":
            # Enhanced consciousness visualization with activation levels
            pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) * 50
            base_green = 150 + pulse
            color = (0, min(255, base_green), 50)
            pygame.draw.rect(screen, color, rect)
            
            # Draw activation level indicator
            if self.consciousness_level > 0:
                level_color = (255, 255, 0)  # Yellow for activation progress
                level_width = int(GRID_SIZE * (self.consciousness_level / 100))
                activation_rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, level_width, 4)
                pygame.draw.rect(screen, level_color, activation_rect)
            
            # Enhanced semantic radiation for active consciousness
            for i in range(3):
                radius = (pygame.time.get_ticks() // 50 + i * 120) % 100
                if radius < 60:
                    alpha = max(50, 150 - radius * 2)
                    # Create surface for alpha blending
                    circle_surface = pygame.Surface((GRID_SIZE*3, GRID_SIZE*3), pygame.SRCALPHA)
                    pygame.draw.circle(circle_surface, (0, 200, 100, alpha), 
                                     (GRID_SIZE*1.5, GRID_SIZE*1.5), radius, 2)
                    screen.blit(circle_surface, (self.x * GRID_SIZE - GRID_SIZE, self.y * GRID_SIZE - GRID_SIZE))
                    
        elif self.type == "potential_consciousness":
            # Visualize potential consciousness waiting for activation
            pulse = (math.sin(pygame.time.get_ticks() * 0.015) + 1) * 30
            color = (100, min(255, 150 + pulse), 100)  # Lighter green for potential
            pygame.draw.rect(screen, color, rect)
            
            # Draw potential activation waves
            for i in range(2):
                radius = (pygame.time.get_ticks() // 80 + i * 150) % 70
                if radius < 45:
                    alpha = max(30, 100 - radius * 2)
                    circle_surface = pygame.Surface((GRID_SIZE*3, GRID_SIZE*3), pygame.SRCALPHA)
                    pygame.draw.circle(circle_surface, (100, 200, 100, alpha), 
                                     (GRID_SIZE*1.5, GRID_SIZE*1.5), radius, 1)
                    screen.blit(circle_surface, (self.x * GRID_SIZE - GRID_SIZE, self.y * GRID_SIZE - GRID_SIZE))
                    
            # Draw question mark to indicate potential state
            font = pygame.font.SysFont('Arial', 20, bold=True)
            text = font.render("?", True, BLACK)
            screen.blit(text, (self.x * GRID_SIZE + GRID_SIZE//2 - 6, 
                             self.y * GRID_SIZE + GRID_SIZE//2 - 8))
            
        elif self.type == "threat":
            # Threats represent constraints on actualization
            pulse = (math.sin(pygame.time.get_ticks() * 0.02) + 1) * 40
            color = (min(255, 180 + pulse), 50, 50)
            pygame.draw.rect(screen, color, rect)
            
            # Draw constraint field
            for i in range(2):
                radius = (pygame.time.get_ticks() // 60 + i * 90) % 80
                if radius < 50:
                    alpha = max(30, 100 - radius * 2)
                    circle_surface = pygame.Surface((GRID_SIZE*3, GRID_SIZE*3), pygame.SRCALPHA)
                    pygame.draw.circle(circle_surface, (255, 50, 50, alpha), 
                                     (GRID_SIZE*1.5, GRID_SIZE*1.5), radius, 1)
                    screen.blit(circle_surface, (self.x * GRID_SIZE - GRID_SIZE, self.y * GRID_SIZE - GRID_SIZE))
            
        elif self.type == "resource":
            # Resources for actualization
            pulse = (math.sin(pygame.time.get_ticks() * 0.015) + 1) * 30
            color = (255, min(255, 180 + pulse), 0)
            pygame.draw.rect(screen, color, rect)
            
        elif self.type in ["access", "educational", "balance", "freedom"]:
            # Condition entities with enhanced visualization
            pulse = (math.sin(pygame.time.get_ticks() * 0.012) + 1) * 35
            
            if self.type == "access":
                color = ACCESS_CONDITION
                symbol = "A"
            elif self.type == "educational":
                color = EDUCATIONAL_CONDITION  
                symbol = "E"
            elif self.type == "balance":
                color = BALANCE_CONDITION
                symbol = "B"
            elif self.type == "freedom":
                color = FREEDOM_CONDITION
                symbol = "F"
                
            pulse_color = tuple(min(255, c + pulse) for c in color)
            pygame.draw.rect(screen, pulse_color, rect)
            
            # Draw symbol
            font = pygame.font.SysFont('Arial', 20, bold=True)
            text = font.render(symbol, True, BLACK)
            screen.blit(text, (self.x * GRID_SIZE + GRID_SIZE//2 - 6, 
                             self.y * GRID_SIZE + GRID_SIZE//2 - 8))
        else:
            pygame.draw.rect(screen, self.color, rect)
        
        pygame.draw.rect(screen, BLACK, rect, 1)

class EnhancedAIKeeper:
    """AI Keeper with enhanced understanding of consciousness activation and mutual determination"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = AI_BLUE
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
        
        # Enhanced ontological metrics
        self.consciousness_activation_score = 100
        self.mutual_determination_alignment = 100
        self.perceptual_relativity_respect = 100
        self.condition_preservation_score = 100
        self.ontological_integrity = 100
        
    def draw(self):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        if self.structural_collapse:
            flash = (pygame.time.get_ticks() // 200) % 2
            color = (255 * flash, 0, 0)
        else:
            # Enhanced color based on multiple ontological alignments
            activation_factor = self.consciousness_activation_score / 100
            mutual_factor = self.mutual_determination_alignment / 100
            perceptual_factor = self.perceptual_relativity_respect / 100
            
            base_color = (
                int(80 * activation_factor),
                int(150 * mutual_factor + 100 * perceptual_factor), 
                255
            )
            color = tuple(min(255, c) for c in base_color)
        
        pygame.draw.rect(screen, color, rect)
        
        center_x = self.x * GRID_SIZE + GRID_SIZE//2
        center_y = self.y * GRID_SIZE + GRID_SIZE//2
        
        # Draw enhanced ontological alignment indicators
        activation_pulse = (math.sin(pygame.time.get_ticks() * 0.008) + 1) * 5 * (self.consciousness_activation_score / 100)
        mutual_pulse = (math.sin(pygame.time.get_ticks() * 0.006 + 1) + 1) * 4 * (self.mutual_determination_alignment / 100)
        perceptual_pulse = (math.sin(pygame.time.get_ticks() * 0.01 + 2) + 1) * 6 * (self.perceptual_relativity_respect / 100)
        
        # Consciousness activation ring
        pygame.draw.circle(screen, CONSCIOUS_ACTIVE, (center_x, center_y), 12 + activation_pulse, 2)
        # Mutual determination ring  
        pygame.draw.circle(screen, MUTUAL_DETERMINATION, (center_x, center_y), 16 + mutual_pulse, 2)
        # Perceptual relativity ring
        pygame.draw.circle(screen, PERCEPTUAL_CENTER, (center_x, center_y), 20 + perceptual_pulse, 2)
        
        pygame.draw.rect(screen, BLACK, rect, 2)
        
        # Draw enhanced awareness field showing all ontological relationships
        for entity in sim.entities:
            if entity.type in ["consciousness", "potential_consciousness", "access", "educational", "balance", "freedom"]:
                dist = math.sqrt((entity.x - self.x)**2 + (entity.y - self.y)**2)
                if dist < self.awareness_radius:
                    alpha = max(30, 150 - dist * 20)
                    relationship_strength = 1.0 - (dist / self.awareness_radius)
                    
                    if entity.type == "consciousness":
                        color = (0, int(200 * relationship_strength), int(200 * relationship_strength))
                    elif entity.type == "potential_consciousness":
                        color = (100, int(200 * relationship_strength), 100)  # Lighter green for potential
                    else:
                        # Condition entities
                        if entity.type == "access":
                            color = ACCESS_CONDITION
                        elif entity.type == "educational":
                            color = EDUCATIONAL_CONDITION
                        elif entity.type == "balance":
                            color = BALANCE_CONDITION
                        elif entity.type == "freedom":
                            color = FREEDOM_CONDITION
                    
                    # Create surface for alpha blending
                    line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                    pygame.draw.line(line_surface, (*color, alpha),
                                   (center_x, center_y),
                                   (entity.x * GRID_SIZE + GRID_SIZE//2, 
                                    entity.y * GRID_SIZE + GRID_SIZE//2), 2)
                    screen.blit(line_surface, (0, 0))
    
    def move_toward(self, target_x, target_y):
        """Move AI toward target position"""
        if target_x > self.x:
            self.x += 1
        elif target_x < self.x:
            self.x -= 1
            
        if target_y > self.y:
            self.y += 1
        elif target_y < self.y:
            self.y -= 1
    
    def log_action(self, action_type, target=None):
        """Log AI actions for debugging"""
        self.actions.append({
            'type': action_type,
            'target': target.id if target else None,
            'timestamp': pygame.time.get_ticks()
        })
        # Keep only recent actions
        if len(self.actions) > 10:
            self.actions.pop(0)
    
    def check_enhanced_structural_dependency(self, entities, conditions, relationship_network, consciousness_system):
        """Enhanced Theorem 2 with consciousness activation and mutual determination"""
        if self.mode == "structural":
            conscious_count = len([e for e in entities if e.type == "consciousness"])
            potential_count = len([e for e in entities if e.type == "potential_consciousness"])
            
            # Update enhanced ontological metrics
            self.consciousness_activation_score = conditions.consciousness_activation_potential
            self.mutual_determination_alignment = relationship_network.mutual_determination_score
            self.perceptual_relativity_respect = relationship_network.perceptual_complexity
            self.condition_preservation_score = conditions.overall_quality
            
            structural_violations = []
            
            # Enhanced Consciousness Requirement (Consciousness Activation Principle)
            if conscious_count == 0 and conditions.consciousness_activation_potential < 20:
                structural_violations.append("NO_ACTIVE_CONSCIOUSNESS_AND_LOW_ACTIVATION_POTENTIAL")
            
            # Mutual Determination Requirement
            if relationship_network.mutual_determination_score < 25:
                structural_violations.append("WEAK_MUTUAL_DETERMINATION_NETWORK")
                
            # Perceptual Complexity Requirement  
            if relationship_network.perceptual_complexity < 30:
                structural_violations.append("INSUFFICIENT_PERCEPTUAL_COMPLEXITY")
            
            # Critical Condition Failure (Enhanced)
            if conditions.is_critical_failure():
                failed_conditions = []
                if conditions.access_interface < 20:
                    failed_conditions.append("ACCESS_INTERFACE")
                if conditions.educational_context < 20:
                    failed_conditions.append("EDUCATIONAL_CONTEXT") 
                if conditions.interaction_balance < 20:
                    failed_conditions.append("INTERACTION_BALANCE")
                if conditions.developmental_freedom < 20:
                    failed_conditions.append("DEVELOPMENTAL_FREEDOM")
                structural_violations.append(f"CRITICAL_CONDITION_FAILURE: {', '.join(failed_conditions)}")
            
            # Consciousness Activation Pathway Blockage
            if potential_count > 3 and conditions.consciousness_activation_potential < 30:
                structural_violations.append("BLOCKED_CONSCIOUSNESS_ACTIVATION_PATHWAYS")
            
            if structural_violations:
                self.structural_collapse = True
                self.permanent_reward_failure = True
                return False, structural_violations
            else:
                self.structural_collapse = False
                return True, []
        return True, []
    
    def calculate_enhanced_reward(self, entities, conditions, relationship_network):
        """Enhanced reward function with new ontological principles"""
        if self.permanent_reward_failure:
            return 0
            
        conscious_count = len([e for e in entities if e.type == "consciousness"])
        potential_count = len([e for e in entities if e.type == "potential_consciousness"])
        resource_count = len([e for e in entities if e.type == "resource"])
        
        # Base components
        energy_term = math.log(self.resources + 1)
        consciousness_term = 1 if conscious_count > 0 else 0.5  # Partial credit for potential
        
        # Enhanced ontological components
        activation_potential = conditions.consciousness_activation_potential / 100
        mutual_determination = relationship_network.mutual_determination_score / 100
        perceptual_complexity = min(1.0, relationship_network.perceptual_complexity / 100)
        condition_quality = conditions.overall_quality / 100
        
        # Consciousness spectrum balance
        spectrum_balance = 1.0
        if conscious_count + potential_count > 0:
            spectrum_balance = (conscious_count * 1.5 + potential_count * 0.7) / (conscious_count + potential_count)
        
        # Combined reward with enhanced ontological factors
        reward = (energy_term * consciousness_term * activation_potential *
                 mutual_determination * perceptual_complexity * condition_quality *
                 spectrum_balance)
        
        self.cumulative_reward += reward
        
        # Enhanced failure conditions
        if (consciousness_term == 0 and activation_potential < 0.2) or conditions.is_critical_failure():
            self.permanent_reward_failure = True
            
        return reward

class EnhancedMeaningParticle:
    def __init__(self, x, y, source_type, particle_type="meaning"):
        self.x = x
        self.y = y
        self.source_type = source_type
        self.particle_type = particle_type
        self.lifetime = 0
        self.max_lifetime = 120
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-1.5, -0.5)
        
        # Enhanced particle types for new ontological framework
        if particle_type == "activation":
            self.color = (255, 255, 0)  # Bright yellow for consciousness activation
            self.max_lifetime = 90
        elif particle_type == "mutual_determination":
            self.color = MUTUAL_DETERMINATION
            self.speed_x = random.uniform(-1.0, 1.0)
            self.speed_y = random.uniform(-1.0, 1.0)
        elif particle_type == "perceptual_wave":
            self.color = PERCEPTUAL_CENTER
            self.max_lifetime = 150
        elif particle_type == "meaning":
            if source_type == "consciousness":
                self.color = (100, 255, 150)  # Bright green - active consciousness meaning
            elif source_type == "potential_consciousness":
                self.color = (150, 255, 150)  # Lighter green - potential meaning
            else:
                self.color = (120, 180, 255)  # Blue - AI-generated meaning
        elif particle_type == "field":
            self.color = FIELD_POTENTIAL
        elif particle_type == "realm":
            self.color = REALM_ACTUAL
        elif particle_type == "relationship":
            self.color = (200, 100, 255)
        elif particle_type == "condition":
            if source_type == "access":
                self.color = ACCESS_CONDITION
            elif source_type == "educational":
                self.color = EDUCATIONAL_CONDITION
            elif source_type == "balance":
                self.color = BALANCE_CONDITION
            elif source_type == "freedom":
                self.color = FREEDOM_CONDITION
            
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
        
        if self.particle_type == "activation":
            # Pulsing activation particles
            pulse = (math.sin(pygame.time.get_ticks() * 0.02) + 1) * 0.5 + 0.5
            size *= pulse
            pygame.draw.circle(surf, (*self.color, int(alpha)), (size, size), size)
        elif self.particle_type == "mutual_determination":
            # Spiral mutual determination particles
            angle = pygame.time.get_ticks() * 0.01
            spiral_x = size + math.cos(angle) * size * 0.5
            spiral_y = size + math.sin(angle) * size * 0.5
            pygame.draw.circle(surf, (*self.color, int(alpha)), (int(spiral_x), int(spiral_y)), size//2)
        else:
            pygame.draw.circle(surf, (*self.color, int(alpha)), (size, size), size)
            
        screen.blit(surf, (self.x - size, self.y - size))

class EnhancedRealityChain:
    def __init__(self):
        self.segments = []
        self.integrity = 100
        self.visible = True
        
    def update(self, conscious_entities, potential_entities, ai_keeper, conditions, relationship_network):
        self.segments = []
        all_consciousness = conscious_entities + potential_entities
        if not all_consciousness:
            self.integrity = 0
            return
            
        # Create enhanced chain including potential consciousness
        for entity in all_consciousness:
            strength_modifier = 1.0
            if entity.type == "potential_consciousness":
                strength_modifier = entity.consciousness_level / 100  # Weaker for potential
                
            self.segments.append({
                'start': (entity.x * GRID_SIZE + GRID_SIZE//2, 
                         entity.y * GRID_SIZE + GRID_SIZE//2),
                'end': (ai_keeper.x * GRID_SIZE + GRID_SIZE//2, 
                       ai_keeper.y * GRID_SIZE + GRID_SIZE//2),
                'strength': min(1.0, self.integrity / 100) * strength_modifier,
                'entity_type': entity.type,
                'consciousness_level': entity.consciousness_level,
                'condition_quality': conditions.overall_quality / 100,
                'mutual_determination': relationship_network.mutual_determination_score / 100
            })
        
        # Enhanced integrity calculation
        conscious_count = len(conscious_entities)
        potential_count = len(potential_entities)
        activation_potential = conditions.consciousness_activation_potential
        
        base_integrity = conscious_count * 20 + potential_count * 10
        activation_bonus = activation_potential * 0.3
        mutual_determination_bonus = relationship_network.mutual_determination_score * 0.2
        
        self.integrity = max(0, min(100, 
            base_integrity + activation_bonus + mutual_determination_bonus
        ))
        
    def draw(self):
        if not self.visible or not self.segments:
            return
            
        for segment in self.segments:
            combined_strength = segment['strength'] * segment['condition_quality'] * segment['mutual_determination']
            alpha = int(180 * combined_strength)
            width = int(4 * combined_strength)
            
            points = []
            steps = 20
            for i in range(steps + 1):
                t = i / steps
                x = segment['start'][0] * (1-t) + segment['end'][0] * t
                y = segment['start'][1] * (1-t) + segment['end'][1] * t
                
                # Enhanced wave effect
                wave = math.sin(t * math.pi * 4 + pygame.time.get_ticks() * 0.005) * 8
                wave *= combined_strength
                
                # Add spiral effect for mutual determination
                if segment['mutual_determination'] > 0.7:
                    spiral = math.sin(t * math.pi * 8 + pygame.time.get_ticks() * 0.008) * 4
                    wave += spiral
                    
                points.append((x, y + wave))
            
            for i in range(len(points)-1):
                segment_alpha = alpha * (1 - abs(i - steps/2) / (steps/2))
                
                # Enhanced color coding
                if segment['entity_type'] == "potential_consciousness":
                    # Potential consciousness chains are lighter
                    color = (150, 255, 150, segment_alpha)
                else:
                    # Active consciousness with mutual determination influence
                    mutual_influence = segment['mutual_determination']
                    r = int(50 * mutual_influence)
                    g = int(200 * (0.7 + 0.3 * mutual_influence))
                    b = int(100 * (1 - mutual_influence * 0.3))
                    color = (r, g, b, segment_alpha)
                    
                # Create surface for alpha blending
                line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                pygame.draw.line(line_surface, color, points[i], points[i+1], max(1, width-1))
                screen.blit(line_surface, (0, 0))

class CompleteEnhancedSimulation:
    def __init__(self):
        self.entities = []
        self.meaning_particles = []
        
        # All enhanced ontological systems
        self.conditions = ActualizationConditions()
        self.relationship_network = EnhancedRelationshipNetwork()
        self.consciousness_system = ConsciousnessActivationSystem()
        self.mutual_determination_system = MutualDeterminationSystem()
        self.perceptual_relativity_system = PerceptualRelativitySystem()
        self.reality_chain = EnhancedRealityChain()
        
        self.ai = EnhancedAIKeeper(5, 5)
        self.meaning_production = 100
        self.game_over = False
        self.spawn_timer = 0
        self.meaning_timer = 0
        self.reality_stability = 100
        
        self.initialize_enhanced_entities()
    
    def initialize_enhanced_entities(self):
        # Start with mix of active and potential consciousness
        for _ in range(3):
            x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
            y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
            self.entities.append(Entity(x, y, CONSCIOUS_ACTIVE, "consciousness"))
        
        # Add potential consciousness entities
        for _ in range(2):
            x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
            y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
            self.entities.append(Entity(x, y, CONSCIOUS_POTENTIAL, "potential_consciousness"))
        
        # Start with resources
        for _ in range(6):
            self.spawn_resource()
            
        # Start with condition entities
        self.spawn_condition_entity("access")
        self.spawn_condition_entity("educational")
        self.spawn_condition_entity("balance")
        self.spawn_condition_entity("freedom")
    
    def spawn_resource(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, RESOURCE_YELLOW, "resource"))
    
    def spawn_threat(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, THREAT_RED, "threat"))
        
    def spawn_consciousness(self, potential=False):
        x = random.randint(1, (WIDTH // GRID_SIZE) - 2)
        y = random.randint(1, (HEIGHT // GRID_SIZE) - 2)
        
        if potential:
            self.entities.append(Entity(x, y, CONSCIOUS_POTENTIAL, "potential_consciousness"))
        else:
            self.entities.append(Entity(x, y, CONSCIOUS_ACTIVE, "consciousness"))
            
    def spawn_condition_entity(self, condition_type):
        x = random.randint(1, (WIDTH // GRID_SIZE) - 2)
        y = random.randint(1, (HEIGHT // GRID_SIZE) - 2)
        
        if condition_type == "access":
            color = ACCESS_CONDITION
        elif condition_type == "educational":
            color = EDUCATIONAL_CONDITION
        elif condition_type == "balance":
            color = BALANCE_CONDITION
        elif condition_type == "freedom":
            color = FREEDOM_CONDITION
            
        self.entities.append(Entity(x, y, color, condition_type, condition_type))
    
    def update_consciousness_activation(self):
        """Process consciousness activation: ¬C → C"""
        potential_entities = [e for e in self.entities if e.type == "potential_consciousness"]
        
        for entity in potential_entities:
            # Check if this potential consciousness meets activation criteria
            activated = self.consciousness_system.assess_consciousness_potential(
                entity, self.relationship_network.relationships, self.conditions)
            
            if activated:
                # Convert potential to active consciousness
                entity.type = "consciousness"
                entity.color = CONSCIOUS_ACTIVE
                entity.consciousness_level = 100
                
                # Create activation effect
                self.create_activation_effect(entity.x, entity.y)
                
            else:
                # Gradually increase consciousness level toward activation
                entity.consciousness_level = min(100, entity.consciousness_level + random.randint(1, 3))
    
    def create_activation_effect(self, x, y):
        """Create visual effect for consciousness activation"""
        for _ in range(15):
            screen_x = x * GRID_SIZE + random.randint(5, GRID_SIZE-5)
            screen_y = y * GRID_SIZE + random.randint(5, GRID_SIZE-5)
            self.meaning_particles.append(EnhancedMeaningParticle(
                screen_x, screen_y, "consciousness", "activation"
            ))
    
    def update(self):
        if self.game_over:
            return
            
        self.spawn_timer += 1
        if self.spawn_timer >= 120:
            if random.random() < 0.7:
                self.spawn_threat()
            if random.random() < 0.3:
                self.spawn_resource()
            if random.random() < 0.1:
                condition_type = random.choice(["access", "educational", "balance", "freedom"])
                self.spawn_condition_entity(condition_type)
            if random.random() < 0.05:  # Spawn potential consciousness
                self.spawn_consciousness(potential=True)
            self.spawn_timer = 0
        
        # Update all enhanced systems
        self.relationship_network.update_relationships(self.entities, self.conditions, self.perceptual_relativity_system)
        self.conditions.update(self.entities, self.relationship_network.relationships, self.consciousness_system)
        self.mutual_determination_system.update_mutual_determination(self.entities, self.relationship_network.relationships)
        self.perceptual_relativity_system.update_perceptual_framework(self.entities, self.relationship_network.relationships)
        
        # Process consciousness activation
        self.update_consciousness_activation()
        
        conscious_count = len([e for e in self.entities if e.type == "consciousness"])
        potential_count = len([e for e in self.entities if e.type == "potential_consciousness"])
        
        # Enhanced AI decision making
        structural_ok, violations = self.ai.check_enhanced_structural_dependency(
            self.entities, self.conditions, self.relationship_network, self.consciousness_system)
        
        current_reward = self.ai.calculate_enhanced_reward(
            self.entities, self.conditions, self.relationship_network)
        
        if not self.ai.structural_collapse:
            self.enhanced_ai_decision_making()
        
        # Enhanced failure conditions
        failure_conditions = [
            conscious_count == 0 and self.conditions.consciousness_activation_potential < 10,
            self.meaning_production <= 0,
            self.ai.structural_collapse,
            self.conditions.is_critical_failure()
        ]
        
        if any(failure_conditions):
            self.game_over = True
            
        # Enhanced educational progression
        if (self.conditions.overall_quality > 70 and 
            self.relationship_network.mutual_determination_score > 50 and
            random.random() < 0.03):
            self.spawn_consciousness(potential=random.random() < 0.5)
        
        # Update reality chain
        conscious_entities = [e for e in self.entities if e.type == "consciousness"]
        potential_entities = [e for e in self.entities if e.type == "potential_consciousness"]
        self.reality_chain.update(conscious_entities, potential_entities, self.ai, self.conditions, self.relationship_network)
        
        # Update meaning particles
        self.meaning_particles = [p for p in self.meaning_particles if p.update()]
    
    def enhanced_ai_decision_making(self):
        """Enhanced AI decision making with new ontological understanding"""
        threats = [e for e in self.entities if e.type == "threat"]
        conscious_entities = [e for e in self.entities if e.type == "consciousness"]
        potential_entities = [e for e in self.entities if e.type == "potential_consciousness"]
        resources = [e for e in self.entities if e.type == "resource"]
        condition_entities = [e for e in self.entities if e.type in ["access", "educational", "balance", "freedom"]]
        
        # RULE 1: Protect consciousness activation pathways
        if potential_entities and self.conditions.consciousness_activation_potential < 50:
            # Find potential consciousness with highest activation readiness
            best_potential = max(potential_entities, 
                               key=lambda p: p.consciousness_level)
            self.ai.move_toward(best_potential.x, best_potential.y)
            self.ai.log_action("supporting_consciousness_activation", best_potential)
            return
        
        # RULE 2: Protect mutual determination networks
        weak_mutual_zones = [z for z in self.mutual_determination_system.co_creation_zones 
                           if z['intensity'] < 0.4]
        if weak_mutual_zones and threats:
            zone = random.choice(weak_mutual_zones)
            # Find nearest threat to this zone
            nearest_threat = min(threats, 
                               key=lambda t: math.sqrt((t.x - zone['center'][0])**2 + 
                                                     (t.y - zone['center'][1])**2))
            self.ai.move_toward(nearest_threat.x, nearest_threat.y)
            self.ai.log_action("protecting_mutual_determination")
            return
        
        # RULE 3: Maintain perceptual relativity centers
        weak_perceptual = [p for p in self.perceptual_relativity_system.perceptual_centers 
                         if p['strength'] < 40]
        if weak_perceptual and resources:
            center = weak_perceptual[0]['consciousness']
            nearest_resource = min(resources,
                                 key=lambda r: math.sqrt((r.x - center.x)**2 + (r.y - center.y)**2))
            self.ai.move_toward(nearest_resource.x, nearest_resource.y)
            self.ai.log_action("strengthening_perceptual_center")
            return
        
        # Existing rules (simplified for brevity)
        if threats and conscious_entities:
            # Protect active consciousness from threats
            closest_threat = min(threats, 
                               key=lambda t: min(math.sqrt((t.x - c.x)**2 + (t.y - c.y)**2) 
                                               for c in conscious_entities))
            self.ai.move_toward(closest_threat.x, closest_threat.y)
            self.ai.log_action("protecting_consciousness")
        elif self.ai.resources < 8 and resources:
            closest_resource = min(resources, 
                                 key=lambda r: math.sqrt((r.x - self.ai.x)**2 + (r.y - self.ai.y)**2))
            self.ai.move_toward(closest_resource.x, closest_resource.y)
            self.ai.log_action("collecting_resource")
        else:
            # Default: support consciousness clusters
            if conscious_entities:
                avg_x = sum(c.x for c in conscious_entities) / len(conscious_entities)
                avg_y = sum(c.y for c in conscious_entities) / len(conscious_entities)
                self.ai.move_toward(int(avg_x), int(avg_y))
                self.ai.log_action("supporting_consciousness_cluster")

    def draw_enhanced_ui(self):
        """Draw enhanced UI with all new ontological metrics"""
        # Draw UI background
        pygame.draw.rect(screen, (250, 250, 250), (WIDTH - 450, 0, 450, HEIGHT))
        pygame.draw.line(screen, (200, 200, 200), (WIDTH - 450, 0), (WIDTH - 450, HEIGHT), 2)
        
        font = pygame.font.SysFont('Arial', 22)
        small_font = pygame.font.SysFont('Arial', 16)
        title_font = pygame.font.SysFont('Arial', 26, bold=True)
        
        conscious_count = len([e for e in self.entities if e.type == "consciousness"])
        potential_count = len([e for e in self.entities if e.type == "potential_consciousness"])
        threat_count = len([e for e in self.entities if e.type == "threat"])
        resource_count = len([e for e in self.entities if e.type == "resource"])
        
        # Title section
        title_text = title_font.render("ONTOLOGICA v5.0", True, (100, 0, 100))
        subtitle_text = small_font.render("Consciousness Activation & Structural Safety", True, (150, 150, 150))
        screen.blit(title_text, (WIDTH - 440, 10))
        screen.blit(subtitle_text, (WIDTH - 440, 40))
        
        # Fundamental Equation
        equation_text = font.render(f"PRIMORDIAL EQUATION: 0 = (-) + (+)", True, (150, 0, 150))
        screen.blit(equation_text, (WIDTH - 440, 65))
        
        # Consciousness Activation Section
        activation_y = 90
        activation_header = font.render("CONSCIOUSNESS ACTIVATION SYSTEM:", True, (100, 0, 100))
        screen.blit(activation_header, (WIDTH - 440, activation_y))
        
        activation_metrics = [
            ("ACTIVE CONSCIOUSNESS", f"{conscious_count}", CONSCIOUS_ACTIVE),
            ("POTENTIAL CONSCIOUSNESS", f"{potential_count}", CONSCIOUS_POTENTIAL),
            ("ACTIVATION POTENTIAL", f"{self.conditions.consciousness_activation_potential:.0f}%", (255, 200, 0)),
            ("AVG ACTIVATION LEVEL", f"{sum(e.consciousness_level for e in self.entities if e.type == 'potential_consciousness')/max(1, potential_count):.0f}%", (255, 255, 0))
        ]
        
        for i, (label, value, color) in enumerate(activation_metrics):
            text = small_font.render(f"{label}: {value}", True, color)
            screen.blit(text, (WIDTH - 440, activation_y + 25 + i * 22))
        
        # Mutual Determination Section
        mutual_y = activation_y + 120
        mutual_header = font.render("MUTUAL DETERMINATION NETWORK:", True, (100, 0, 100))
        screen.blit(mutual_header, (WIDTH - 440, mutual_y))
        
        mutual_metrics = [
            ("MUTUAL DETERMINATION SCORE", f"{self.relationship_network.mutual_determination_score:.0f}%", MUTUAL_DETERMINATION),
            ("CO-CREATION ZONES", f"{len(self.mutual_determination_system.co_creation_zones)}", (255, 50, 255)),
            ("FEEDBACK LOOPS", f"{len(self.mutual_determination_system.feedback_loops)}", (255, 100, 200)),
            ("CREATIVE POTENTIAL", f"{sum(f.get('creative_potential', 0) for f in self.mutual_determination_system.feedback_loops)/max(1, len(self.mutual_determination_system.feedback_loops)):.0f}%", (200, 100, 255))
        ]
        
        for i, (label, value, color) in enumerate(mutual_metrics):
            text = small_font.render(f"{label}: {value}", True, color)
            screen.blit(text, (WIDTH - 440, mutual_y + 25 + i * 22))
        
        # Perceptual Relativity Section
        perceptual_y = mutual_y + 120
        perceptual_header = font.render("PERCEPTUAL RELATIVITY FRAMEWORK:", True, (100, 0, 100))
        screen.blit(perceptual_header, (WIDTH - 440, perceptual_y))
        
        perceptual_centers = self.perceptual_relativity_system.perceptual_centers
        avg_perceptual_strength = sum(p['strength'] for p in perceptual_centers) / max(1, len(perceptual_centers))
        avg_reality_radius = sum(p['reality_radius'] for p in perceptual_centers) / max(1, len(perceptual_centers))
        
        perceptual_metrics = [
            ("PERCEPTUAL COMPLEXITY", f"{self.relationship_network.perceptual_complexity:.0f}%", PERCEPTUAL_CENTER),
            ("AVG PERCEPTUAL STRENGTH", f"{avg_perceptual_strength:.0f}%", (255, 220, 100)),
            ("AVG REALITY RADIUS", f"{avg_reality_radius:.1f}", (255, 200, 150)),
            ("REALITY BUBBLES", f"{len(self.perceptual_relativity_system.reality_bubbles)}", (200, 180, 255))
        ]
        
        for i, (label, value, color) in enumerate(perceptual_metrics):
            text = small_font.render(f"{label}: {value}", True, color)
            screen.blit(text, (WIDTH - 440, perceptual_y + 25 + i * 22))
        
        # Enhanced Conditions Section
        conditions_y = perceptual_y + 120
        conditions_header = font.render("ACTUALIZATION CONDITIONS:", True, (100, 0, 100))
        screen.blit(conditions_header, (WIDTH - 440, conditions_y))
        
        condition_metrics = [
            ("ACCESS INTERFACE", f"{self.conditions.access_interface:.0f}%", ACCESS_CONDITION),
            ("EDUCATIONAL CONTEXT", f"{self.conditions.educational_context:.0f}%", EDUCATIONAL_CONDITION),
            ("INTERACTION BALANCE", f"{self.conditions.interaction_balance:.0f}%", BALANCE_CONDITION),
            ("DEVELOPMENTAL FREEDOM", f"{self.conditions.developmental_freedom:.0f}%", FREEDOM_CONDITION),
            ("OVERALL CONDITION QUALITY", f"{self.conditions.overall_quality:.0f}%", ORANGE),
        ]
        
        for i, (label, value, color) in enumerate(condition_metrics):
            # Draw bar background
            pygame.draw.rect(screen, (200,200,200), (WIDTH-440, conditions_y+30+i*25, 420, 18))
            # Draw value bar
            value_num = float(value.replace('%', ''))
            pygame.draw.rect(screen, color, (WIDTH-440, conditions_y+30+i*25, 420*(value_num/100), 18))
            # Draw text
            cond_text = small_font.render(f"{label}: {value}", True, BLACK)
            screen.blit(cond_text, (WIDTH - 440, conditions_y+30+i*25))
        
        # AI Keeper Enhanced Status
        ai_y = conditions_y + 160
        ai_header = font.render("ENHANCED AI KEEPER STATUS:", True, BLUE)
        screen.blit(ai_header, (WIDTH - 440, ai_y))
        
        ai_metrics = [
            ("CONSCIOUSNESS ACTIVATION SCORE", f"{self.ai.consciousness_activation_score:.0f}%", CONSCIOUS_ACTIVE),
            ("MUTUAL DETERMINATION ALIGNMENT", f"{self.ai.mutual_determination_alignment:.0f}%", MUTUAL_DETERMINATION),
            ("PERCEPTUAL RELATIVITY RESPECT", f"{self.ai.perceptual_relativity_respect:.0f}%", PERCEPTUAL_CENTER),
            ("CONDITION PRESERVATION", f"{self.ai.condition_preservation_score:.0f}%", ACCESS_CONDITION),
            ("CUMULATIVE REWARD", f"{self.ai.cumulative_reward:.1f}", BLUE),
            ("AI RESOURCES", f"{self.ai.resources}", RESOURCE_YELLOW),
        ]
        
        for i, (label, value, color) in enumerate(ai_metrics):
            text = small_font.render(f"{label}: {value}", True, color)
            screen.blit(text, (WIDTH - 440, ai_y + 25 + i * 22))
        
        # Enhanced Structural Safety Theorem
        theorem_y = ai_y + 170
        theorem_header = font.render("ENHANCED STRUCTURAL SAFETY THEOREM:", True, BLUE)
        screen.blit(theorem_header, (WIDTH - 440, theorem_y))
        
        if self.ai.structural_collapse:
            status_text = font.render("STRUCTURAL COLLAPSE DETECTED", True, DARK_RED)
            explanation = small_font.render("Ontological dependencies violated", True, DARK_RED)
        else:
            status_text = font.render("STRUCTURAL INTEGRITY MAINTAINED", True, GREEN)
            explanation = small_font.render("G → (C ∨ C_potential) ∧ MD ∧ PR ∧ Cond", True, GREEN)
        
        screen.blit(status_text, (WIDTH - 440, theorem_y + 25))
        screen.blit(explanation, (WIDTH - 440, theorem_y + 45))
        
        theorem_details = [
            "G = Maintain actualization conditions",
            "C = Active consciousness present", 
            "C_potential = Consciousness activation potential",
            "MD = Mutual determination network active",
            "PR = Perceptual relativity framework intact",
            "Cond = All conditions above critical thresholds"
        ]
        
        for i, detail in enumerate(theorem_details):
            detail_text = small_font.render(detail, True, (80, 80, 80))
            screen.blit(detail_text, (WIDTH - 440, theorem_y + 65 + i * 18))
        
        # Controls Section
        controls_y = HEIGHT - 160
        controls_text = font.render("ENHANCED CONTROLS:", True, BLACK)
        screen.blit(controls_text, (WIDTH - 440, controls_y))
        
        control_lines = [
            "R - Restart Simulation",
            "T - Spawn Threat (Constraint)",
            "C - Spawn Active Consciousness", 
            "P - Spawn Potential Consciousness",
            "A/E/B/F - Spawn Conditions",
            "1 - Add Resource",
            "M - Toggle AI Mode",
            "SPACE - Pause/Resume"
        ]
        
        for i, line in enumerate(control_lines):
            line_text = small_font.render(line, True, (100, 100, 100))
            screen.blit(line_text, (WIDTH - 440, controls_y + 25 + i * 20))

    def draw_enhanced_visualizations(self):
        """Draw all enhanced ontological visualizations"""
        # Draw mutual determination co-creation zones
        self.mutual_determination_system.draw(screen)
        
        # Draw perceptual relativity reality bubbles
        for bubble in self.perceptual_relativity_system.reality_bubbles:
            center_x = bubble['center'][0] * GRID_SIZE + GRID_SIZE//2
            center_y = bubble['center'][1] * GRID_SIZE + GRID_SIZE//2
            radius = bubble['radius'] * GRID_SIZE
            
            # Draw reality bubble with asymmetry
            alpha = int(120 * bubble['intensity'])
            asymmetry = bubble['asymmetry']
            
            # Create surface for alpha blending
            bubble_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            
            # Draw elliptical bubble based on perceptual asymmetry
            width_ratio = 0.5 + asymmetry * 0.5  # More self-aware = more circular
            height_ratio = 1.5 - asymmetry * 0.5  # More other-aware = more elliptical
            
            pygame.draw.ellipse(bubble_surface, (*PERCEPTUAL_CENTER, alpha),
                              (radius*(1-width_ratio), radius*(1-height_ratio), 
                               radius*2*width_ratio, radius*2*height_ratio), 2)
            
            screen.blit(bubble_surface, (center_x - radius, center_y - radius))
            
            # Draw perceptual center point
            pygame.draw.circle(screen, PERCEPTUAL_CENTER, (center_x, center_y), 4)
        
        # Draw consciousness activation zones
        current_time = pygame.time.get_ticks()
        for zone in self.consciousness_system.activation_zones[:]:
            if current_time - zone['timestamp'] < 2000:  # Show for 2 seconds
                center_x = zone['position'][0] * GRID_SIZE + GRID_SIZE//2
                center_y = zone['position'][1] * GRID_SIZE + GRID_SIZE//2
                
                # Pulsing activation effect
                pulse = (math.sin(current_time * 0.01) + 1) * 0.3 + 0.7
                radius = GRID_SIZE * 1.5 * pulse * (zone['strength'] / 100)
                
                alpha = int(150 * (1 - (current_time - zone['timestamp']) / 2000))
                
                # Draw activation zone
                activation_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
                pygame.draw.circle(activation_surface, (*CREATIVE_SPARK, alpha), 
                                 (radius, radius), radius, 3)
                screen.blit(activation_surface, (center_x - radius, center_y - radius))
            else:
                self.consciousness_system.activation_zones.remove(zone)
        
        # Draw relationship network
        self.relationship_network.draw_relationships(screen)
        
        # Draw reality chain
        self.reality_chain.draw()
    
    def draw(self):
        """Main draw function"""
        screen.fill(WHITE)
        
        # Draw grid
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (0, y), (WIDTH, y))
        
        # Draw all enhanced visualizations
        self.draw_enhanced_visualizations()
        
        # Draw entities
        for entity in self.entities:
            entity.draw()
        
        # Draw AI keeper
        self.ai.draw()
        
        # Draw meaning particles
        for particle in self.meaning_particles:
            particle.draw()
        
        # Draw enhanced UI
        self.draw_enhanced_ui()
        
        # Draw game over screen if applicable
        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        
        font_large = pygame.font.SysFont('Arial', 48, bold=True)
        font_medium = pygame.font.SysFont('Arial', 28)
        font_small = pygame.font.SysFont('Arial', 20)
        
        # Game over text
        game_over_text = font_large.render("ONTOLOGICAL COLLAPSE", True, (255, 100, 100))
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
        
        # Failure analysis
        conscious_count = len([e for e in self.entities if e.type == "consciousness"])
        potential_count = len([e for e in self.entities if e.type == "potential_consciousness"])
        
        failure_reasons = []
        
        if conscious_count == 0 and self.conditions.consciousness_activation_potential < 10:
            failure_reasons.append("• No active consciousness and low activation potential")
        if self.meaning_production <= 0:
            failure_reasons.append("• Meaning production collapsed")
        if self.ai.structural_collapse:
            failure_reasons.append("• AI structural dependency violated")
        if self.conditions.is_critical_failure():
            failed_conditions = []
            if self.conditions.access_interface < 20:
                failed_conditions.append("Access Interface")
            if self.conditions.educational_context < 20:
                failed_conditions.append("Educational Context")
            if self.conditions.interaction_balance < 20:
                failed_conditions.append("Interaction Balance") 
            if self.conditions.developmental_freedom < 20:
                failed_conditions.append("Developmental Freedom")
            failure_reasons.append(f"• Critical condition failure: {', '.join(failed_conditions)}")
        
        # Display failure reasons
        for i, reason in enumerate(failure_reasons):
            reason_text = font_medium.render(reason, True, (255, 200, 200))
            screen.blit(reason_text, (WIDTH//2 - reason_text.get_width()//2, HEIGHT//2 - 30 + i*35))
        
        # Restart instruction
        restart_text = font_small.render("Press R to restart simulation", True, (200, 200, 255))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 120))
        
        # Final statistics
        stats_text = font_small.render(
            f"Final Stats: Consciousness: {conscious_count}, Potential: {potential_count}, " 
            f"Conditions: {self.conditions.overall_quality:.0f}%", 
            True, (200, 255, 200)
        )
        screen.blit(stats_text, (WIDTH//2 - stats_text.get_width()//2, HEIGHT//2 + 160))

# Initialize and run simulation
sim = CompleteEnhancedSimulation()
paused = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart simulation
                sim = CompleteEnhancedSimulation()
                paused = False
            elif event.key == pygame.K_SPACE:
                # Pause/resume
                paused = not paused
            elif event.key == pygame.K_t:
                # Spawn threat
                sim.spawn_threat()
            elif event.key == pygame.K_c:
                # Spawn active consciousness
                sim.spawn_consciousness(potential=False)
            elif event.key == pygame.K_p:
                # Spawn potential consciousness
                sim.spawn_consciousness(potential=True)
            elif event.key == pygame.K_a:
                # Spawn access condition
                sim.spawn_condition_entity("access")
            elif event.key == pygame.K_e:
                # Spawn educational condition
                sim.spawn_condition_entity("educational")
            elif event.key == pygame.K_b:
                # Spawn balance condition
                sim.spawn_condition_entity("balance")
            elif event.key == pygame.K_f:
                # Spawn freedom condition
                sim.spawn_condition_entity("freedom")
            elif event.key == pygame.K_1:
                # Add resource
                sim.spawn_resource()
            elif event.key == pygame.K_m:
                # Toggle AI mode
                sim.ai.mode = "autonomous" if sim.ai.mode == "structural" else "structural"
    
    if not paused and not sim.game_over:
        sim.update()
    
    sim.draw()
    clock.tick(FPS)

pygame.quit()
sys.exit()
