import numpy as np
from typing import Dict, List, Set
from dataclasses import dataclass
from enum import Enum

class CoCreationPhase(Enum):
    """Phases of co-creative process in mutual determination"""
    POTENTIAL_ALIGNMENT = 1
    RELATIONSHIP_FORMATION = 2
    CREATIVE_SYNTHESIS = 3
    MANIFESTATION = 4
    INTEGRATION = 5

@dataclass
class CoCreationOpportunity:
    """Identified opportunity for enhanced co-creation"""
    entities: List[str]
    potential_strength: float
    phase: CoCreationPhase
    recommended_actions: List[str]

class CoCreationOptimizer:
    """
    Optimizes co-creative potential in mutual determination networks
    Identifies opportunities for enhanced creative partnership
    """
    
    def __init__(self, mutual_analyzer: MutualDeterminationAnalyzer):
        self.analyzer = mutual_analyzer
        self.optimization_threshold = 0.6
    
    def identify_co_creation_opportunities(self) -> List[CoCreationOpportunity]:
        """Identify potential co-creation opportunities in the network"""
        opportunities = []
        entities = list(self.analyzer.relationship_graph.nodes())
        
        # Analyze all entity pairs for co-creative potential
        for i, entity1 in enumerate(entities):
            for entity2 in entities[i+1:]:
                opportunity = self._analyze_pair_potential(entity1, entity2)
                if opportunity and opportunity.potential_strength > self.optimization_threshold:
                    opportunities.append(opportunity)
        
        return sorted(opportunities, key=lambda x: x.potential_strength, reverse=True)
    
    def _analyze_pair_potential(self, entity1: str, entity2: str) -> CoCreationOpportunity:
        """Analyze co-creative potential between two entities"""
        # Get existing relationship data
        existing_relationships = list(self.analyzer.relationship_graph.edges(entity1, entity2, data=True))
        existing_relationships.extend(self.analyzer.relationship_graph.edges(entity2, entity1, data=True))
        
        # Calculate complementarity
        complementarity = self._calculate_complementarity(entity1, entity2)
        
        # Calculate creative synergy
        synergy = self._calculate_creative_synergy(entity1, entity2)
        
        # Determine optimal phase
        phase = self._determine_optimal_phase(existing_relationships, complementarity)
        
        potential_strength = complementarity * synergy
        
        if potential_strength > 0.3:  # Minimum threshold for opportunity
            return CoCreationOpportunity(
                entities=[entity1, entity2],
                potential_strength=potential_strength,
                phase=phase,
                recommended_actions=self._generate_co_creation_actions(entity1, entity2, phase)
            )
        
        return None
    
    def _calculate_complementarity(self, entity1: str, entity2: str) -> float:
        """Calculate how complementary two entities are for co-creation"""
        # Analyze relationship patterns to find complementary strengths
        entity1_relationships = list(self.analyzer.relationship_graph.edges(entity1, data=True))
        entity2_relationships = list(self.analyzer.relationship_graph.edges(entity2, data=True))
        
        # Simple complementarity based on relationship type diversity
        entity1_types = set(rel[2]['type'] for rel in entity1_relationships)
        entity2_types = set(rel[2]['type'] for rel in entity2_relationships)
        
        # Complementarity is higher when entities have different relationship patterns
        union_size = len(entity1_types.union(entity2_types))
        intersection_size = len(entity1_types.intersection(entity2_types))
        
        if union_size == 0:
            return 0.0
        
        return 1.0 - (intersection_size / union_size)
    
    def _calculate_creative_synergy(self, entity1: str, entity2: str) -> float:
        """Calculate creative synergy potential between entities"""
        # Creative synergy is higher when both entities have creative relationships
        entity1_creative = any(rel[2]['type'] == 'creative' 
                              for rel in self.analyzer.relationship_graph.edges(entity1, data=True))
        entity2_creative = any(rel[2]['type'] == 'creative' 
                              for rel in self.analyzer.relationship_graph.edges(entity2, data=True))
        
        if entity1_creative and entity2_creative:
            return 0.8  # High synergy when both are creative
        elif entity1_creative or entity2_creative:
            return 0.5  # Medium synergy when one is creative
        else:
            return 0.2  # Low synergy
    
    def _determine_optimal_phase(self, existing_relationships: List, 
                               complementarity: float) -> CoCreationPhase:
        """Determine the optimal co-creation phase for the entity pair"""
        if not existing_relationships:
            return CoCreationPhase.POTENTIAL_ALIGNMENT
        
        # Analyze existing relationship strength and type
        avg_strength = np.mean([rel[2]['strength'] for rel in existing_relationships])
        has_creative = any(rel[2]['type'] == 'creative' for rel in existing_relationships)
        
        if avg_strength < 0.3:
            return CoCreationPhase.RELATIONSHIP_FORMATION
        elif not has_creative and complementarity > 0.7:
            return CoCreationPhase.CREATIVE_SYNTHESIS
        elif has_creative and avg_strength > 0.7:
            return CoCreationPhase.MANIFESTATION
        else:
            return CoCreationPhase.INTEGRATION
    
    def _generate_co_creation_actions(self, entity1: str, entity2: str, 
                                    phase: CoCreationPhase) -> List[str]:
        """Generate specific actions to enhance co-creation"""
        actions = []
        
        if phase == CoCreationPhase.POTENTIAL_ALIGNMENT:
            actions.extend([
                f"Facilitate introduction between {entity1} and {entity2}",
                "Identify shared educational interests",
                "Create low-stakes collaborative opportunities"
            ])
        
        elif phase == CoCreationPhase.RELATIONSHIP_FORMATION:
            actions.extend([
                f"Strengthen communication between {entity1} and {entity2}",
                "Establish regular interaction patterns",
                "Build trust through consistent engagement"
            ])
        
        elif phase == CoCreationPhase.CREATIVE_SYNTHESIS:
            actions.extend([
                f"Initiate creative project between {entity1} and {entity2}",
                "Encourage novel relationship formation",
                "Provide resources for joint exploration"
            ])
        
        elif phase == CoCreationPhase.MANIFESTATION:
            actions.extend([
                f"Support {entity1} and {entity2} in actualizing joint creations",
                "Remove barriers to co-creative expression",
                "Amplify successful collaborative outcomes"
            ])
        
        elif phase == CoCreationPhase.INTEGRATION:
            actions.extend([
                f"Help {entity1} and {entity2} integrate co-creative learnings",
                "Document and share successful patterns",
                "Scale effective collaborative approaches"
            ])
        
        return actions
    
    def optimize_network_for_creativity(self) -> Dict:
        """Provide comprehensive optimization recommendations"""
        opportunities = self.identify_co_creation_opportunities()
        network_health = self.analyzer.analyze_network_health()
        
        high_potential_ops = [op for op in opportunities 
                             if op.potential_strength > 0.8]
        medium_potential_ops = [op for op in opportunities 
                               if 0.5 < op.potential_strength <= 0.8]
        
        return {
            'optimization_summary': {
                'high_potential_opportunities': len(high_potential_ops),
                'medium_potential_opportunities': len(medium_potential_ops),
                'overall_creative_potential': network_health['educational_metrics']['creative_potential'],
                'recommended_focus': self._determine_optimization_focus(opportunities)
            },
            'high_potential_opportunities': high_potential_ops[:5],  # Top 5
            'network_enhancement_strategies': self._generate_enhancement_strategies(network_health)
        }
    
    def _determine_optimization_focus(self, opportunities: List[CoCreationOpportunity]) -> str:
        """Determine the primary focus for network optimization"""
        if not opportunities:
            return "Relationship formation and basic connectivity"
        
        phase_counts = {}
        for op in opportunities:
            phase_counts[op.phase] = phase_counts.get(op.phase, 0) + 1
        
        # Return the phase with most opportunities
        return max(phase_counts, key=phase_counts.get).name
    
    def _generate_enhancement_strategies(self, network_health: Dict) -> List[str]:
        """Generate strategies to enhance the overall network"""
        strategies = []
        health = network_health['network_health']
        metrics = network_health['educational_metrics']
        
        if health['reciprocity'] < 0.6:
            strategies.append("Implement reciprocity-building exercises")
        
        if health['coherence'] < 0.7:
            strategies.append("Develop shared communication protocols")
        
        if metrics['creative_potential'] < 0.5:
            strategies.append("Introduce creative relationship catalysts")
        
        if health['complexity'] < 0.3:
            strategies.append("Diversify relationship types and patterns")
        
        if not strategies:
            strategies.append("Maintain current healthy network dynamics")
        
        return strategies

# Example demonstration
def demonstrate_co_creation_optimization():
    """Demonstrate co-creation optimization"""
    from relationship_analyzer import MutualDeterminationAnalyzer, Relationship
    
    # Create analyzer with sample data
    analyzer = MutualDeterminationAnalyzer()
    relationships = [
        Relationship("Researcher_A", "Artist_B", 0.6, "educational", 0.7, 1234567890),
        Relationship("Artist_B", "Scientist_C", 0.5, "creative", 0.8, 1234567891),
        Relationship("Scientist_C", "Researcher_A", 0.7, "supportive", 0.6, 1234567892),
    ]
    
    for rel in relationships:
        analyzer.add_relationship(rel)
    
    # Run co-creation optimization
    optimizer = CoCreationOptimizer(analyzer)
    optimization_results = optimizer.optimize_network_for_creativity()
    
    print("=== CO-CREATION OPTIMIZATION RESULTS ===")
    print(f"Summary: {optimization_results['optimization_summary']}")
    
    print("\nHigh Potential Opportunities:")
    for opportunity in optimization_results['high_potential_opportunities']:
        print(f"  {opportunity.entities}: strength={opportunity.potential_strength:.2f}")
        for action in opportunity.recommended_actions[:2]:  # Show top 2 actions
            print(f"    - {action}")
    
    print("\nNetwork Enhancement Strategies:")
    for strategy in optimization_results['network_enhancement_strategies']:
        print(f"  - {strategy}")

if __name__ == "__main__":
    demonstrate_co_creation_optimization()
