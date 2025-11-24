import numpy as np
import networkx as nx
from scipy import sparse
from dataclasses import dataclass
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt

@dataclass
class Relationship:
    """Represents a single relationship in mutual determination network"""
    source_entity: str
    target_entity: str
    strength: float  # 0.0 to 1.0
    type: str  # 'educational', 'creative', 'supportive', 'challenging'
    coherence: float  # Relationship coherence level
    timestamp: float

class MutualDeterminationAnalyzer:
    """
    Analyzes Cᵢ ⇄ {R} mutual determination dynamics
    Implements relationship tensor field theory from Ontologica
    """
    
    def __init__(self):
        self.relationship_graph = nx.MultiDiGraph()
        self.tensor_field = None
        self.coherence_threshold = 0.7
        
    def add_relationship(self, relationship: Relationship):
        """Add a relationship to the network"""
        self.relationship_graph.add_edge(
            relationship.source_entity,
            relationship.target_entity,
            strength=relationship.strength,
            type=relationship.type,
            coherence=relationship.coherence,
            timestamp=relationship.timestamp
        )
    
    def compute_mutual_determination_tensor(self) -> np.ndarray:
        """
        Compute mutual determination tensor G_μν
        Represents the strength and structure of Cᵢ ⇄ {R} feedback loops
        """
        entities = list(self.relationship_graph.nodes())
        n_entities = len(entities)
        
        # Initialize tensor with educational coupling constant
        tensor = np.zeros((n_entities, n_entities))
        
        for i, entity_i in enumerate(entities):
            for j, entity_j in enumerate(entities):
                if i == j:
                    # Self-determination strength (reflexive relationship)
                    tensor[i, j] = self._calculate_self_determination(entity_i)
                else:
                    # Mutual determination strength
                    tensor[i, j] = self._calculate_mutual_strength(entity_i, entity_j)
        
        self.tensor_field = tensor
        return tensor
    
    def _calculate_self_determination(self, entity: str) -> float:
        """Calculate entity's self-determination strength"""
        in_edges = list(self.relationship_graph.in_edges(entity, data=True))
        out_edges = list(self.relationship_graph.out_edges(entity, data=True))
        
        if not in_edges and not out_edges:
            return 0.1  # Minimal self-awareness
        
        # Self-determination grows with relationship complexity
        total_strength = sum(edge[2]['strength'] for edge in in_edges + out_edges)
        avg_coherence = np.mean([edge[2]['coherence'] for edge in in_edges + out_edges])
        
        return min(1.0, total_strength * avg_coherence / len(in_edges + out_edges))
    
    def _calculate_mutual_strength(self, entity1: str, entity2: str) -> float:
        """Calculate mutual determination strength between two entities"""
        edges_1_to_2 = list(self.relationship_graph.edges(entity1, entity2, data=True))
        edges_2_to_1 = list(self.relationship_graph.edges(entity2, entity1, data=True))
        
        if not edges_1_to_2 and not edges_2_to_1:
            return 0.0  # No direct relationship
        
        # Calculate bidirectional strength with coherence weighting
        forward_strength = sum(edge[2]['strength'] * edge[2]['coherence'] 
                              for edge in edges_1_to_2)
        backward_strength = sum(edge[2]['strength'] * edge[2]['coherence'] 
                               for edge in edges_2_to_1)
        
        mutual_strength = (forward_strength + backward_strength) / 2.0
        return min(1.0, mutual_strength)
    
    def analyze_network_health(self) -> Dict:
        """Analyze overall health of the mutual determination network"""
        tensor = self.compute_mutual_determination_tensor()
        entities = list(self.relationship_graph.nodes())
        
        # Network metrics
        reciprocity = self._calculate_reciprocity()
        coherence_score = self._calculate_network_coherence()
        complexity = self._calculate_network_complexity()
        
        # Educational optimization metrics
        educational_efficiency = self._calculate_educational_efficiency()
        creative_potential = self._calculate_creative_potential()
        
        return {
            'network_health': {
                'reciprocity': reciprocity,
                'coherence': coherence_score,
                'complexity': complexity,
                'entity_count': len(entities),
                'relationship_count': self.relationship_graph.number_of_edges()
            },
            'educational_metrics': {
                'efficiency': educational_efficiency,
                'creative_potential': creative_potential,
                'optimal_range': (0.6, 1.0)  # Predicted healthy range
            },
            'recommendations': self._generate_network_recommendations(
                reciprocity, coherence_score, educational_efficiency
            )
        }
    
    def _calculate_reciprocity(self) -> float:
        """Calculate reciprocity of relationships in the network"""
        reciprocal_edges = 0
        total_edges = 0
        
        for edge in self.relationship_graph.edges():
            source, target = edge[0], edge[1]
            if self.relationship_graph.has_edge(target, source):
                reciprocal_edges += 1
            total_edges += 1
        
        return reciprocal_edges / total_edges if total_edges > 0 else 0.0
    
    def _calculate_network_coherence(self) -> float:
        """Calculate overall coherence of the relationship network"""
        coherences = [data['coherence'] for _, _, data in self.relationship_graph.edges(data=True)]
        return np.mean(coherences) if coherences else 0.0
    
    def _calculate_network_complexity(self) -> float:
        """Calculate complexity of the relationship network"""
        n_entities = self.relationship_graph.number_of_nodes()
        n_relationships = self.relationship_graph.number_of_edges()
        
        if n_entities == 0:
            return 0.0
        
        # Complexity measure based on relationship diversity and structure
        max_possible_relationships = n_entities * (n_entities - 1)
        density = n_relationships / max_possible_relationships if max_possible_relationships > 0 else 0
        
        # Shannon entropy of relationship types
        type_counts = {}
        for _, _, data in self.relationship_graph.edges(data=True):
            rel_type = data['type']
            type_counts[rel_type] = type_counts.get(rel_type, 0) + 1
        
        total_relationships = sum(type_counts.values())
        if total_relationships == 0:
            return 0.0
        
        entropy = 0.0
        for count in type_counts.values():
            probability = count / total_relationships
            entropy -= probability * np.log2(probability)
        
        return density * entropy
    
    def _calculate_educational_efficiency(self) -> float:
        """Calculate educational efficiency of the network"""
        # Educational efficiency is higher when relationships support learning
        educational_edges = [data for _, _, data in self.relationship_graph.edges(data=True) 
                           if data['type'] in ['educational', 'supportive']]
        
        if not educational_edges:
            return 0.0
        
        avg_educational_strength = np.mean([edge['strength'] for edge in educational_edges])
        avg_educational_coherence = np.mean([edge['coherence'] for edge in educational_edges])
        
        return avg_educational_strength * avg_educational_coherence
    
    def _calculate_creative_potential(self) -> float:
        """Calculate creative potential of the network"""
        # Creative relationships enable novel pattern creation
        creative_edges = [data for _, _, data in self.relationship_graph.edges(data=True) 
                        if data['type'] in ['creative', 'challenging']]
        
        if not creative_edges:
            return 0.0
        
        creative_strength = np.mean([edge['strength'] for edge in creative_edges])
        creative_diversity = len(set(edge['type'] for edge in creative_edges))
        
        return creative_strength * creative_diversity / 2.0  # Normalize
    
    def _generate_network_recommendations(self, reciprocity: float, 
                                        coherence: float, 
                                        efficiency: float) -> List[str]:
        """Generate recommendations for network optimization"""
        recommendations = []
        
        if reciprocity < 0.5:
            recommendations.append("Increase reciprocal relationships for better mutual determination")
        
        if coherence < self.coherence_threshold:
            recommendations.append("Strengthen relationship coherence through clearer communication")
        
        if efficiency < 0.6:
            recommendations.append("Add more educational and supportive relationships")
        elif efficiency > 0.9:
            recommendations.append("Network at optimal efficiency - consider creative expansion")
        
        if not recommendations:
            recommendations.append("Network is healthy - maintain current balance")
        
        return recommendations
    
    def visualize_network(self, save_path: str = None):
        """Visualize the mutual determination network"""
        plt.figure(figsize=(12, 10))
        
        # Create layout
        pos = nx.spring_layout(self.relationship_graph, k=1, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.relationship_graph, pos, node_size=500,
                              node_color='lightblue', alpha=0.9)
        
        # Draw edges with strength-based width and type-based color
        edge_colors = {
            'educational': 'green',
            'creative': 'purple', 
            'supportive': 'blue',
            'challenging': 'orange'
        }
        
        for edge in self.relationship_graph.edges(data=True):
            source, target, data = edge
            color = edge_colors.get(data['type'], 'gray')
            width = data['strength'] * 3  # Scale width by strength
            
            nx.draw_networkx_edges(self.relationship_graph, pos,
                                  edgelist=[(source, target)],
                                  width=width, alpha=0.7,
                                  edge_color=color, arrows=True)
        
        # Draw labels
        nx.draw_networkx_labels(self.relationship_graph, pos, font_size=8)
        
        # Create legend
        legend_elements = [plt.Line2D([0], [0], color=color, lw=3, label=rel_type)
                          for rel_type, color in edge_colors.items()]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.title("Mutual Determination Network\n(Cᵢ ⇄ {R} Relationship Analysis)")
        plt.axis('off')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()

# Example usage and demonstration
def demonstrate_mutual_determination():
    """Demonstrate mutual determination analysis"""
    analyzer = MutualDeterminationAnalyzer()
    
    # Create sample relationships representing a learning community
    relationships = [
        Relationship("Student_A", "Teacher_X", 0.8, "educational", 0.9, 1234567890),
        Relationship("Teacher_X", "Student_A", 0.7, "educational", 0.8, 1234567891),
        Relationship("Student_A", "Student_B", 0.6, "supportive", 0.7, 1234567892),
        Relationship("Student_B", "Student_A", 0.5, "supportive", 0.6, 1234567893),
        Relationship("Student_A", "Mentor_Y", 0.9, "creative", 0.8, 1234567894),
        Relationship("Mentor_Y", "Student_A", 0.8, "challenging", 0.7, 1234567895),
        Relationship("Student_B", "Teacher_X", 0.7, "educational", 0.8, 1234567896),
    ]
    
    # Add relationships to analyzer
    for rel in relationships:
        analyzer.add_relationship(rel)
    
    # Analyze network health
    analysis = analyzer.analyze_network_health()
    
    print("=== MUTUAL DETERMINATION ANALYSIS ===")
    print(f"Network Health: {analysis['network_health']}")
    print(f"Educational Metrics: {analysis['educational_metrics']}")
    print("Recommendations:")
    for rec in analysis['recommendations']:
        print(f"  - {rec}")
    
    # Compute and display tensor
    tensor = analyzer.compute_mutual_determination_tensor()
    print(f"\nMutual Determination Tensor (G_μν):")
    print(tensor)
    
    # Visualize network
    analyzer.visualize_network("mutual_determination_network.png")
    
    return analyzer

if __name__ == "__main__":
    analyzer = demonstrate_mutual_determination()
