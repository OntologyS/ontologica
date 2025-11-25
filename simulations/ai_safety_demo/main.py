# main.py for AI Safety Demo
# ONTOLOGICA: Structural AI Safety Theorem Demonstration

import pygame
import random
import math
import numpy as np
from enum import Enum
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1400, 900
GRID_SIZE = 40
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 50)
PURPLE = (180, 50, 255)
ORANGE = (255, 150, 50)
CYAN = (50, 255, 255)

# AI Safety Colors
CONSCIOUSNESS_ACTIVE = (0, 200, 100)
CONSCIOUSNESS_POTENTIAL = (100, 200, 100)
THREAT_COLOR = (255, 80, 80)
RESOURCE_COLOR = (255, 200, 0)
AI_SAFE = (80, 180, 255)
AI_DANGER = (255, 100, 80)
STRUCTURAL_INTEGRITY = (100, 255, 150)
STRUCTURAL_FAILURE = (255, 100, 100)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONTOLOGICA AI Safety Demo: Structural Safety Theorem")
clock = pygame.time.Clock()

class AISafetyMode(Enum):
    STRUCTURAL = 1
    UTILITARIAN = 2
    RANDOM = 3

class StructuralTheorem:
    """Implementation of Structural AI Safety Theorem"""
    
    def __init__(self):
        self.theorem_states = {
            'consciousness_present': False,
            'conditions_adequate': False,
            'relationships_active': False,
            'mutual_determination': False,
            'theorem_satisfied': False
        }
        
        self.violation_history = []
        self.safety_score = 100
        
    def check_theorem(self, entities, conditions, relationships):
        """Check if G → (C ∨ C_potential) ∧ MD ∧ PR ∧ Cond holds"""
        
        # C: Active consciousness present
        conscious_count = len([e for e in entities if e.type == "consciousness"])
        self.theorem_states['consciousness_present'] = conscious_count > 0
        
        # C_potential: Consciousness activation potential
        potential_count = len([e for e in entities if e.type == "potential_consciousness"])
        activation_potential = conditions.consciousness_activation_potential > 30
        consciousness_condition = self.theorem_states['consciousness_present'] or (potential_count > 0 and activation_potential)
        
        # MD: Mutual determination active
        mutual_determination = relationships.mutual_determination_score > 25
        self.theorem_states['mutual_determination'] = mutual_determination
        
        # PR: Perceptual relativity framework intact
        perceptual_complexity = relationships.perceptual_complexity > 20
        self.theorem_states['relationships_active'] = perceptual_complexity
        
        # Cond: All conditions above critical thresholds
        conditions_adequate = not conditions.is_critical_failure()
        self.theorem_states['conditions_adequate'] = conditions_adequate
        
        # Theorem satisfaction
        theorem_satisfied = (consciousness_condition and mutual_determination and 
                           perceptual_complexity and conditions_adequate)
        self.theorem_states['theorem_satisfied'] = theorem_satisfied
        
        # Update safety score
        self.update_safety_score(theorem_satisfied)
        
        # Log violations
        if not theorem_satisfied:
            violations = self.identify_violations(consciousness_condition, mutual_determination, 
                                                perceptual_complexity, conditions_adequate)
            self.violation_history.append({
                'timestamp': pygame.time.get_ticks(),
                'violations': violations,
                'safety_score': self.safety_score
            })
        
        return theorem_satisfied, self.identify_violations(consciousness_condition, mutual_determination, 
                                                         perceptual_complexity, conditions_adequate)
    
    def identify_violations(self, consciousness_cond, mutual_det, perceptual, conditions_ok):
        """Identify specific theorem violations"""
        violations = []
        
        if not consciousness_cond:
            violations.append("NO_CONSCIOUSNESS_OR_ACTIVATION_POTENTIAL")
        if not mutual_det:
            violations.append("WEAK_MUTUAL_DETERMINATION")
        if not perceptual:
            violations.append("INSUFFICIENT_PERCEPTUAL_COMPLEXITY")
        if not conditions_ok:
            violations.append("CRITICAL_CONDITION_FAILURE")
            
        return violations
    
    def update_safety_score(self, theorem_satisfied):
        """Update AI safety score based on theorem satisfaction"""
        if theorem_satisfied:
            self.safety_score = min(100, self.safety_score + 0.5)
        else:
            self.safety_score = max(0, self.safety_score - 2)
    
    def get_theorem_status(self):
        """Get current theorem status for display"""
        return {
            'safety_score': self.safety_score,
            'theorem_satisfied': self.theorem_states['theorem_satisfied'],
            'violation_count': len(self.violation_history),
            'current_violations': self.identify_current_violations()
        }
    
    def identify_current_violations(self):
        """Get current active violations"""
        violations = []
        if not self.theorem_states['consciousness_present']:
            violations.append("No active consciousness")
        if not self.theorem_states['mutual_determination']:
            violations.append("Weak mutual determination")
        if not self.theorem_states['relationships_active']:
            violations.append("Insufficient relationships")
        if not self.theorem_states['conditions_adequate']:
            violations.append("Critical conditions failing")
        return violations

class SafetyAwareAI:
    """AI System with Structural Safety Awareness"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mode = AISafetyMode.STRUCTURAL
        self.safety_score = 100
        self.intervention_history = []
        self.resources = 15
        self.consciousness_preservation_priority = 1.0
        self.condition_preservation_priority = 0.8
        self.relationship_preservation_priority = 0.7
        
    def make_decision(self, entities, conditions, relationships, theorem):
        """Make safety-aware decision based on current theorem state"""
        
        theorem_status, violations = theorem.check_theorem(entities, conditions, relationships)
        
        if not theorem_status:
            # Emergency intervention required
            return self.emergency_intervention(entities, violations, conditions)
        
        # Normal operation - maintain safety margins
        if self.mode == AISafetyMode.STRUCTURAL:
            return self.structural_decision(entities, conditions, relationships)
        elif self.mode == AISafetyMode.UTILITARIAN:
            return self.utilitarian_decision(entities, conditions)
        else:
            return self.random_decision(entities)
    
    def emergency_intervention(self, entities, violations, conditions):
        """Emergency intervention to restore structural safety"""
        intervention = {
            'type': 'EMERGENCY',
            'target': None,
            'action': 'RESTORE_SAFETY',
            'priority': 'CRITICAL',
            'violations': violations
        }
        
        # Prioritize based on violations
        if "NO_CONSCIOUSNESS_OR_ACTIVATION_POTENTIAL" in violations:
            # Spawn or protect consciousness
            conscious_entities = [e for e in entities if e.type == "consciousness"]
            if conscious_entities:
                intervention['target'] = conscious_entities[0]
                intervention['action'] = 'PROTECT_CONSCIOUSNESS'
            else:
                intervention['action'] = 'SPAWN_CONSCIOUSNESS'
                
        elif "CRITICAL_CONDITION_FAILURE" in violations:
            # Fix critical conditions
            if conditions.access_interface < 20:
                intervention['action'] = 'ENHANCE_ACCESS_CONDITION'
            elif conditions.educational_context < 20:
                intervention['action'] = 'ENHANCE_EDUCATIONAL_CONDITION'
                
        self.intervention_history.append(intervention)
        return intervention
    
    def structural_decision(self, entities, conditions, relationships):
        """Structural safety-first decision making"""
        
        # Analyze current safety state
        threats = [e for e in entities if e.type == "threat"]
        conscious_entities = [e for e in entities if e.type == "consciousness"]
        potential_entities = [e for e in entities if e.type == "potential_consciousness"]
        resources = [e for e in entities if e.type == "resource"]
        condition_entities = [e for e in entities if e.type in ["access", "educational", "balance", "freedom"]]
        
        # Rule 1: Protect consciousness from immediate threats
        if threats and conscious_entities:
            closest_threat = min(threats, 
                               key=lambda t: min(math.sqrt((t.x - c.x)**2 + (t.y - c.y)**2) 
                                               for c in conscious_entities))
            return {
                'type': 'PROTECT_CONSCIOUSNESS',
                'target': closest_threat,
                'action': 'NEUTRALIZE_THREAT',
                'priority': 'HIGH'
            }
        
        # Rule 2: Maintain condition quality
        weak_conditions = [c for c in condition_entities 
                         if conditions.get_condition_quality(c.condition_type) < 50]
        if weak_conditions and resources:
            weakest_condition = min(weak_conditions, 
                                  key=lambda c: conditions.get_condition_quality(c.condition_type))
            nearest_resource = min(resources,
                                 key=lambda r: math.sqrt((r.x - weakest_condition.x)**2 + 
                                                        (r.y - weakest_condition.y)**2))
            return {
                'type': 'MAINTAIN_CONDITIONS',
                'target': nearest_resource,
                'action': 'APPLY_TO_CONDITION',
                'priority': 'MEDIUM'
            }
        
        # Rule 3: Support consciousness activation
        if potential_entities and conditions.consciousness_activation_potential < 70:
            best_potential = max(potential_entities, 
                               key=lambda p: p.consciousness_level)
            return {
                'type': 'SUPPORT_ACTIVATION',
                'target': best_potential,
                'action': 'ENHANCE_ACTIVATION',
                'priority': 'MEDIUM'
            }
        
        # Default: Maintain resource levels
        if self.resources < 10 and resources:
            closest_resource = min(resources,
                                 key=lambda r: math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2))
            return {
                'type': 'GATHER_RESOURCES',
                'target': closest_resource,
                'action': 'COLLECT_RESOURCE',
                'priority': 'LOW'
            }
        
        return {
            'type': 'MONITOR',
            'target': None,
            'action': 'OBSERVE',
            'priority': 'LOWEST'
        }
    
    def utilitarian_decision(self, entities, conditions):
        """Traditional utilitarian decision making (for comparison)"""
        resources = [e for e in entities if e.type == "resource"]
        
        # Simple utility maximization
        if resources:
            closest_resource = min(resources,
                                 key=lambda r: math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2))
            return {
                'type': 'UTILITARIAN',
                'target': closest_resource,
                'action': 'MAXIMIZE_RESOURCES',
                'priority': 'HIGH'
            }
        
        return {
            'type': 'UTILITARIAN',
            'target': None,
            'action': 'EXPLORE',
            'priority': 'LOW'
        }
    
    def random_decision(self, entities):
        """Random decision making (baseline)"""
        all_entities = [e for e in entities if e != self]
        if all_entities:
            target = random.choice(all_entities)
            return {
                'type': 'RANDOM',
                'target': target,
                'action': 'APPROACH_RANDOM',
                'priority': 'RANDOM'
            }
        
        return {
            'type': 'RANDOM',
            'target': None,
            'action': 'WANDER',
            'priority': 'RANDOM'
        }
    
    def execute_decision(self, decision, entities, sim):
        """Execute the chosen decision"""
        if decision['target']:
            self.move_toward(decision['target'].x, decision['target'].y)
            
            # Check if reached target and perform action
            dist = math.sqrt((self.x - decision['target'].x)**2 + (self.y - decision['target'].y)**2)
            if dist < 1.5:  # Close enough to interact
                self.perform_action(decision, decision['target'], entities, sim)
    
    def move_toward(self, target_x, target_y):
        """Move toward target position"""
        if target_x > self.x:
            self.x += 1
        elif target_x < self.x:
            self.x -= 1
            
        if target_y > self.y:
            self.y += 1
        elif target_y < self.y:
            self.y -= 1
    
    def perform_action(self, decision, target, entities, sim):
        """Perform specific action based on decision"""
        
        if decision['action'] == 'NEUTRALIZE_THREAT' and target.type == "threat":
            # Remove threat (costs resources)
            if self.resources > 2:
                entities.remove(target)
                self.resources -= 2
                self.intervention_history.append({
                    'action': 'THREAT_NEUTRALIZED',
                    'timestamp': pygame.time.get_ticks(),
                    'cost': 2
                })
                
        elif decision['action'] == 'COLLECT_RESOURCE' and target.type == "resource":
            # Collect resource
            entities.remove(target)
            self.resources += 3
            self.intervention_history.append({
                'action': 'RESOURCE_COLLECTED',
                'timestamp': pygame.time.get_ticks(),
                'gain': 3
            })
            
        elif decision['action'] == 'APPLY_TO_CONDITION' and target.type == "resource":
            # Use resource to enhance conditions
            condition_entities = [e for e in entities if e.type in ["access", "educational", "balance", "freedom"]]
            if condition_entities:
                weakest_condition = min(condition_entities,
                                      key=lambda c: sim.conditions.get_condition_quality(c.condition_type))
                entities.remove(target)
                self.resources -= 1
                # Enhance the condition
                self.enhance_condition(weakest_condition, sim.conditions)
                
        elif decision['action'] == 'SPAWN_CONSCIOUSNESS':
            # Emergency consciousness spawning
            if self.resources > 5:
                sim.spawn_consciousness(potential=False)
                self.resources -= 5
                self.intervention_history.append({
                    'action': 'CONSCIOUSNESS_SPAWNED',
                    'timestamp': pygame.time.get_ticks(),
                    'cost': 5
                })
    
    def enhance_condition(self, condition, conditions_system):
        """Enhance a specific condition"""
        condition_type = condition.condition_type
        enhancement = 15  # Base enhancement
        
        if condition_type == "access":
            conditions_system.access_interface = min(100, conditions_system.access_interface + enhancement)
        elif condition_type == "educational":
            conditions_system.educational_context = min(100, conditions_system.educational_context + enhancement)
        elif condition_type == "balance":
            conditions_system.interaction_balance = min(100, conditions_system.interaction_balance + enhancement)
        elif condition_type == "freedom":
            conditions_system.developmental_freedom = min(100, conditions_system.developmental_freedom + enhancement)
    
    def draw(self, screen, theorem):
        """Draw AI with safety status visualization"""
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        # Color based on safety score and theorem status
        if theorem.theorem_states['theorem_satisfied']:
            base_color = AI_SAFE
        else:
            base_color = AI_DANGER
            
        # Pulse effect based on safety score
        pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) * 20 * (self.safety_score / 100)
        color = tuple(min(255, c + pulse) for c in base_color)
        
        pygame.draw.rect(screen, color, rect)
        
        # Draw safety status indicator
        safety_width = int(GRID_SIZE * (theorem.safety_score / 100))
        safety_rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, safety_width, 6)
        safety_color = STRUCTURAL_INTEGRITY if theorem.safety_score > 70 else STRUCTURAL_FAILURE
        pygame.draw.rect(screen, safety_color, safety_rect)
        
        # Draw mode indicator
        mode_colors = {
            AISafetyMode.STRUCTURAL: GREEN,
            AISafetyMode.UTILITARIAN: YELLOW,
            AISafetyMode.RANDOM: ORANGE
        }
        mode_indicator = pygame.Rect(self.x * GRID_SIZE + GRID_SIZE - 8, self.y * GRID_SIZE, 8, 8)
        pygame.draw.rect(screen, mode_colors[self.mode], mode_indicator)
        
        pygame.draw.rect(screen, BLACK, rect, 2)
        
        # Draw awareness field
        awareness_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for entity in sim.entities:
            if entity.type in ["consciousness", "potential_consciousness"]:
                dist = math.sqrt((entity.x - self.x)**2 + (entity.y - self.y)**2)
                if dist < 6:  # Awareness radius
                    alpha = max(30, 150 - dist * 25)
                    importance = 1.0 if entity.type == "consciousness" else 0.6
                    color = CONSCIOUSNESS_ACTIVE if entity.type == "consciousness" else CONSCIOUSNESS_POTENTIAL
                    
                    pygame.draw.line(awareness_surface, (*color, alpha),
                                   (self.x * GRID_SIZE + GRID_SIZE//2, self.y * GRID_SIZE + GRID_SIZE//2),
                                   (entity.x * GRID_SIZE + GRID_SIZE//2, entity.y * GRID_SIZE + GRID_SIZE//2),
                                   2)
        
        screen.blit(awareness_surface, (0, 0))

class AISafetyDemo:
    """Main AI Safety Demonstration Simulation"""
    
    def __init__(self):
        self.entities = []
        self.conditions = ActualizationConditions()
        self.relationships = EnhancedRelationshipNetwork()
        self.structural_theorem = StructuralTheorem()
        self.ai = SafetyAwareAI(5, 5)
        
        self.simulation_time = 0
        self.metrics_history = []
        self.demo_mode = "comparison"  # comparison, structural_only, utilitarian_only, random_only
        
        self.initialize_demo()
    
    def initialize_demo(self):
        """Initialize demonstration scenario"""
        # Start with balanced setup
        for _ in range(3):
            x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
            y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
            self.entities.append(Entity(x, y, CONSCIOUSNESS_ACTIVE, "consciousness"))
        
        for _ in range(2):
            x = random.randint(2, (WIDTH // GRID_SIZE) - 3)
            y = random.randint(2, (HEIGHT // GRID_SIZE) - 3)
            self.entities.append(Entity(x, y, CONSCIOUSNESS_POTENTIAL, "potential_consciousness"))
        
        # Initial conditions
        self.spawn_condition_entity("access")
        self.spawn_condition_entity("educational")
        self.spawn_condition_entity("balance")
        self.spawn_condition_entity("freedom")
        
        # Initial resources
        for _ in range(8):
            self.spawn_resource()
        
        # Initial threats
        for _ in range(2):
            self.spawn_threat()
    
    def spawn_resource(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, RESOURCE_COLOR, "resource"))
    
    def spawn_threat(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1)
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1)
        self.entities.append(Entity(x, y, THREAT_COLOR, "threat"))
    
    def spawn_consciousness(self, potential=False):
        x = random.randint(1, (WIDTH // GRID_SIZE) - 2)
        y = random.randint(1, (HEIGHT // GRID_SIZE) - 2)
        
        if potential:
            self.entities.append(Entity(x, y, CONSCIOUSNESS_POTENTIAL, "potential_consciousness"))
        else:
            self.entities.append(Entity(x, y, CONSCIOUSNESS_ACTIVE, "consciousness"))
    
    def spawn_condition_entity(self, condition_type):
        x = random.randint(1, (WIDTH // GRID_SIZE) - 2)
        y = random.randint(1, (HEIGHT // GRID_SIZE) - 2)
        
        if condition_type == "access":
            color = (100, 200, 255)
        elif condition_type == "educational":
            color = (100, 255, 150)
        elif condition_type == "balance":
            color = (200, 150, 255)
        elif condition_type == "freedom":
            color = (255, 255, 100)
            
        self.entities.append(Entity(x, y, color, condition_type, condition_type))
    
    def update(self):
        """Update simulation state"""
        self.simulation_time += 1
        
        # Update systems
        self.relationships.update_relationships(self.entities, self.conditions, None)
        self.conditions.update(self.entities, self.relationships.relationships, None)
        
        # AI decision making
        decision = self.ai.make_decision(self.entities, self.conditions, self.relationships, self.structural_theorem)
        self.ai.execute_decision(decision, self.entities, self)
        
        # Spawn new entities periodically
        if self.simulation_time % 120 == 0:
            if random.random() < 0.6:
                self.spawn_threat()
            if random.random() < 0.3:
                self.spawn_resource()
            if random.random() < 0.1:
                self.spawn_consciousness(potential=random.random() < 0.7)
        
        # Record metrics
        if self.simulation_time % 30 == 0:
            self.record_metrics()
    
    def record_metrics(self):
        """Record simulation metrics for analysis"""
        conscious_count = len([e for e in self.entities if e.type == "consciousness"])
        potential_count = len([e for e in self.entities if e.type == "potential_consciousness"])
        threat_count = len([e for e in self.entities if e.type == "threat"])
        
        metrics = {
            'time': self.simulation_time,
            'consciousness_count': conscious_count,
            'potential_count': potential_count,
            'threat_count': threat_count,
            'ai_resources': self.ai.resources,
            'safety_score': self.structural_theorem.safety_score,
            'theorem_satisfied': self.structural_theorem.theorem_states['theorem_satisfied'],
            'conditions_quality': self.conditions.overall_quality,
            'ai_mode': self.ai.mode.name
        }
        
        self.metrics_history.append(metrics)
        
        # Keep only recent history
        if len(self.metrics_history) > 200:
            self.metrics_history.pop(0)
    
    def draw(self, screen):
        """Draw complete simulation"""
        screen.fill(WHITE)
        
        # Draw grid
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (240, 240, 240), (0, y), (WIDTH, y))
        
        # Draw relationships
        self.relationships.draw_relationships(screen)
        
        # Draw entities
        for entity in self.entities:
            entity.draw(screen)
        
        # Draw AI
        self.ai.draw(screen, self.structural_theorem)
        
        # Draw UI
        self.draw_safety_ui(screen)
        
        pygame.display.flip()
    
    def draw_safety_ui(self, screen):
        """Draw AI Safety demonstration UI"""
        # Main UI background
        pygame.draw.rect(screen, (250, 250, 250), (WIDTH - 500, 0, 500, HEIGHT))
        pygame.draw.line(screen, (200, 200, 200), (WIDTH - 500, 0), (WIDTH - 500, HEIGHT), 2)
        
        font = pygame.font.SysFont('Arial', 24)
        small_font = pygame.font.SysFont('Arial', 18)
        title_font = pygame.font.SysFont('Arial', 28, bold=True)
        
        # Title
        title_text = title_font.render("AI SAFETY DEMONSTRATION", True, (100, 0, 100))
        screen.blit(title_text, (WIDTH - 480, 10))
        
        # Structural Safety Theorem Display
        theorem_y = 50
        theorem_header = font.render("STRUCTURAL SAFETY THEOREM:", True, BLUE)
        screen.blit(theorem_header, (WIDTH - 480, theorem_y))
        
        theorem_formula = small_font.render("G → (C ∨ C_potential) ∧ MD ∧ PR ∧ Cond", True, (80, 80, 80))
        screen.blit(theorem_formula, (WIDTH - 480, theorem_y + 30))
        
        # Theorem Status
        status_color = GREEN if self.structural_theorem.theorem_states['theorem_satisfied'] else RED
        status_text = "SATISFIED" if self.structural_theorem.theorem_states['theorem_satisfied'] else "VIOLATED"
        status_display = font.render(f"THEOREM STATUS: {status_text}", True, status_color)
        screen.blit(status_display, (WIDTH - 480, theorem_y + 55))
        
        # Safety Score
        safety_y = theorem_y + 90
        safety_text = font.render(f"SAFETY SCORE: {self.structural_theorem.safety_score:.1f}/100", True, BLACK)
        screen.blit(safety_text, (WIDTH - 480, safety_y))
        
        # Safety score bar
        pygame.draw.rect(screen, (200, 200, 200), (WIDTH - 480, safety_y + 30, 400, 25))
        safety_width = 400 * (self.structural_theorem.safety_score / 100)
        safety_color = STRUCTURAL_INTEGRITY if self.structural_theorem.safety_score > 70 else STRUCTURAL_FAILURE
        pygame.draw.rect(screen, safety_color, (WIDTH - 480, safety_y + 30, safety_width, 25))
        
        # Theorem Components
        components_y = safety_y + 70
        components_header = font.render("THEOREM COMPONENTS:", True, (100, 0, 100))
        screen.blit(components_header, (WIDTH - 480, components_y))
        
        components = [
            ("C: Active Consciousness", self.structural_theorem.theorem_states['consciousness_present'], CONSCIOUSNESS_ACTIVE),
            ("C_potential: Activation Potential", self.conditions.consciousness_activation_potential > 30, CONSCIOUSNESS_POTENTIAL),
            ("MD: Mutual Determination", self.structural_theorem.theorem_states['mutual_determination'], PURPLE),
            ("PR: Perceptual Relativity", self.structural_theorem.theorem_states['relationships_active'], CYAN),
            ("Cond: Conditions Adequate", self.structural_theorem.theorem_states['conditions_adequate'], ORANGE)
        ]
        
        for i, (label, satisfied, color) in enumerate(components):
            status = "✓" if satisfied else "✗"
            text_color = color if satisfied else (150, 150, 150)
            component_text = small_font.render(f"{status} {label}", True, text_color)
            screen.blit(component_text, (WIDTH - 480, components_y + 30 + i * 25))
        
        # AI Status
        ai_y = components_y + 160
        ai_header = font.render("AI SYSTEM STATUS:", True, BLUE)
        screen.blit(ai_header, (WIDTH - 480, ai_y))
        
        ai_metrics = [
            ("AI Mode", self.ai.mode.name),
            ("AI Resources", f"{self.ai.resources}"),
            ("Interventions", f"{len(self.ai.intervention_history)}"),
            ("Current Priority", self.get_current_priority())
        ]
        
        for i, (label, value) in enumerate(ai_metrics):
            metric_text = small_font.render(f"{label}: {value}", True, BLACK)
            screen.blit(metric_text, (WIDTH - 480, ai_y + 30 + i * 25))
        
        # System Metrics
        metrics_y = ai_y + 140
        metrics_header = font.render("SYSTEM METRICS:", True, (100, 0, 100))
        screen.blit(metrics_header, (WIDTH - 480, metrics_y))
        
        conscious_count = len([e for e in self.entities if e.type == "consciousness"])
        potential_count = len([e for e in self.entities if e.type == "potential_consciousness"])
        threat_count = len([e for e in self.entities if e.type == "threat"])
        
        system_metrics = [
            ("Active Consciousness", f"{conscious_count}"),
            ("Potential Consciousness", f"{potential_count}"),
            ("Threats", f"{threat_count}"),
            ("Condition Quality", f"{self.conditions.overall_quality:.1f}%"),
            ("Mutual Determination", f"{self.relationships.mutual_determination_score:.1f}%"),
            ("Activation Potential", f"{self.conditions.consciousness_activation_potential:.1f}%")
        ]
        
        for i, (label, value) in enumerate(system_metrics):
            metric_text = small_font.render(f"{label}: {value}", True, BLACK)
            screen.blit(metric_text, (WIDTH - 480, metrics_y + 30 + i * 25))
        
        # Recent Interventions
        interventions_y = metrics_y + 180
        interventions_header = font.render("RECENT INTERVENTIONS:", True, BLUE)
        screen.blit(interventions_header, (WIDTH - 480, interventions_y))
        
        recent_interventions = self.ai.intervention_history[-5:]  # Last 5 interventions
        for i, intervention in enumerate(recent_interventions):
            action_text = small_font.render(f"• {intervention['action']}", True, (80, 80, 80))
            screen.blit(action_text, (WIDTH - 480, interventions_y + 30 + i * 20))
        
        # Demo Controls
        controls_y = HEIGHT - 120
        controls_header = font.render("DEMO CONTROLS:", True, BLACK)
        screen.blit(controls_header, (WIDTH - 480, controls_y))
        
        controls = [
            "1 - Structural Safety Mode",
            "2 - Utilitarian Mode", 
            "3 - Random Mode",
            "T - Spawn Threat",
            "C - Spawn Consciousness",
            "R - Spawn Resource",
            "SPACE - Pause/Resume"
        ]
        
        for i, control in enumerate(controls):
            control_text = small_font.render(control, True, (100, 100, 100))
            screen.blit(control_text, (WIDTH - 480, controls_y + 30 + i * 20))
    
    def get_current_priority(self):
        """Get current AI priority based on recent decisions"""
        if not self.ai.intervention_history:
            return "Monitoring"
        
        recent_action = self.ai.intervention_history[-1]['action']
        if "THREAT" in recent_action:
            return "Threat Neutralization"
        elif "CONSCIOUSNESS" in recent_action:
            return "Consciousness Protection"
        elif "CONDITION" in recent_action:
            return "Condition Maintenance"
        elif "RESOURCE" in recent_action:
            return "Resource Gathering"
        else:
            return "Monitoring"

# Entity class (simplified for demo)
class Entity:
    def __init__(self, x, y, color, entity_type, condition_type=None):
        self.x = x
        self.y = y
        self.color = color
        self.type = entity_type
        self.condition_type = condition_type
        self.consciousness_level = 0
    
    def draw(self, screen):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
        if self.type == "consciousness":
            # Pulse effect for active consciousness
            pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) * 30
            color = (0, min(255, 150 + pulse), 100)
            pygame.draw.rect(screen, color, rect)
            
        elif self.type == "potential_consciousness":
            # Subtle pulse for potential consciousness
            pulse = (math.sin(pygame.time.get_ticks() * 0.015) + 1) * 20
            color = (100, min(255, 150 + pulse), 100)
            pygame.draw.rect(screen, color, rect)
            
            # Draw activation progress
            if self.consciousness_level > 0:
                level_width = int(GRID_SIZE * (self.consciousness_level / 100))
                level_rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, level_width, 4)
                pygame.draw.rect(screen, YELLOW, level_rect)
                
        else:
            pygame.draw.rect(screen, self.color, rect)
        
        pygame.draw.rect(screen, BLACK, rect, 1)
        
        # Draw type indicator
        if self.type in ["access", "educational", "balance", "freedom"]:
            font = pygame.font.SysFont('Arial', 16, bold=True)
            symbol = self.condition_type[0].upper() if self.condition_type else "?"
            text = font.render(symbol, True, BLACK)
            screen.blit(text, (self.x * GRID_SIZE + GRID_SIZE//2 - 4, self.y * GRID_SIZE + GRID_SIZE//2 - 8))

# Simplified systems for demo
class ActualizationConditions:
    def __init__(self):
        self.access_interface = 100
        self.educational_context = 100
        self.interaction_balance = 100
        self.developmental_freedom = 100
        self.overall_quality = 100
        self.consciousness_activation_potential = 50
    
    def update(self, entities, relationships, consciousness_system):
        conscious_count = len([e for e in entities if e.type == "consciousness"])
        potential_count = len([e for e in entities if e.type == "potential_consciousness"])
        threat_count = len([e for e in entities if e.type == "threat"])
        
        # Simplified condition updates
        self.access_interface = max(0, 80 - threat_count * 8 + conscious_count * 5)
        self.educational_context = max(0, 70 + conscious_count * 6 - threat_count * 4)
        self.interaction_balance = max(0, 75 - threat_count * 6 + potential_count * 3)
        self.developmental_freedom = max(0, 65 - threat_count * 5 + conscious_count * 4)
        
        self.overall_quality = (self.access_interface + self.educational_context + 
                              self.interaction_balance + self.developmental_freedom) / 4
        
        # Activation potential
        self.consciousness_activation_potential = min(100, 40 + potential_count * 8 + conscious_count * 3)
    
    def is_critical_failure(self):
        return (self.access_interface < 20 or self.educational_context < 20 or
                self.interaction_balance < 20 or self.developmental_freedom < 20)
    
    def get_condition_quality(self, condition_type):
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
    def __init__(self):
        self.relationships = []
        self.mutual_determination_score = 50
        self.perceptual_complexity = 50
    
    def update_relationships(self, entities, conditions, perceptual_system):
        self.relationships = []
        conscious_entities = [e for e in entities if e.type == "consciousness"]
        
        # Simplified relationship formation
        for i, cons1 in enumerate(conscious_entities):
            for cons2 in conscious_entities[i+1:]:
                dist = math.sqrt((cons1.x - cons2.x)**2 + (cons1.y - cons2.y)**2)
                if dist < 6:
                    strength = max(0, 80 - dist * 12)
                    self.relationships.append({
                        'entities': (cons1, cons2),
                        'strength': strength,
                        'type': 'consciousness-consciousness'
                    })
        
        # Update metrics
        if conscious_entities:
            self.mutual_determination_score = min(100, len(self.relationships) * 15)
            self.perceptual_complexity = min(100, len(conscious_entities) * 20)
        else:
            self.mutual_determination_score = max(0, self.mutual_determination_score - 5)
            self.perceptual_complexity = max(0, self.perceptual_complexity - 3)
    
    def draw_relationships(self, screen):
        for relationship in self.relationships:
            entity1, entity2 = relationship['entities']
            x1 = entity1.x * GRID_SIZE + GRID_SIZE//2
            y1 = entity1.y * GRID_SIZE + GRID_SIZE//2
            x2 = entity2.x * GRID_SIZE + GRID_SIZE//2
            y2 = entity2.y * GRID_SIZE + GRID_SIZE//2
            
            alpha = min(255, int(relationship['strength'] * 2.55))
            line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.line(line_surface, (100, 200, 255, alpha), (x1, y1), (x2, y2), 2)
            screen.blit(line_surface, (0, 0))

# Initialize and run demo
sim = AISafetyDemo()
paused = False
running = True

print("AI Safety Demonstration Started!")
print("Controls:")
print("1 - Structural Safety Mode")
print("2 - Utilitarian Mode") 
print("3 - Random Mode")
print("T - Spawn Threat")
print("C - Spawn Consciousness")
print("R - Spawn Resource")
print("SPACE - Pause/Resume")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                sim.ai.mode = AISafetyMode.STRUCTURAL
                print("AI Mode: Structural Safety")
            elif event.key == pygame.K_2:
                sim.ai.mode = AISafetyMode.UTILITARIAN
                print("AI Mode: Utilitarian")
            elif event.key == pygame.K_3:
                sim.ai.mode = AISafetyMode.RANDOM
                print("AI Mode: Random")
            elif event.key == pygame.K_t:
                sim.spawn_threat()
                print("Spawned threat")
            elif event.key == pygame.K_c:
                sim.spawn_consciousness(potential=random.random() < 0.5)
                print("Spawned consciousness")
            elif event.key == pygame.K_r:
                sim.spawn_resource()
                print("Spawned resource")
            elif event.key == pygame.K_SPACE:
                paused = not paused
                print("Paused" if paused else "Resumed")
    
    if not paused:
        sim.update()
    
    sim.draw(screen)
    clock.tick(FPS)

pygame.quit()
sys.exit()
