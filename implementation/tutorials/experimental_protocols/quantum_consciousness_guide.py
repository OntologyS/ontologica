import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Optional
import json

@dataclass
class ExperimentalSetup:
    """Standardized experimental setup for quantum consciousness experiments"""
    apparatus_type: str  # 'double_slit', 'quantum_eraser', 'delayed_choice'
    measurement_precision: float
    environmental_controls: Dict
    consciousness_measurement: str  # 'eeg', 'behavioral', 'self_report'
    data_recording: Dict

class QuantumConsciousnessProtocol:
    """
    Step-by-step protocols for quantum consciousness experiments
    Based on Ontologica's predictions and standard quantum experimental methods
    """
    
    def __init__(self):
        self.predicted_values = {
            'fringe_spacing': 8.3e-6,
            'decoherence_time': 3.2e-3,
            'visibility_threshold': 0.8,
            'sample_size': 30  # Minimum participants for statistical power
        }
    
    def double_slit_protocol(self, consciousness_conditions: List[str] = None) -> Dict:
        """
        Protocol for double-slit experiment with consciousness observation
        Tests prediction: fringe spacing = 8.3 ± 0.5 × 10⁻⁶ m
        """
        if consciousness_conditions is None:
            consciousness_conditions = ['focused', 'distracted', 'meditative', 'baseline']
        
        protocol = {
            'experiment_name': 'Double-Slit Consciousness Interference',
            'objective': 'Measure effect of consciousness state on quantum interference patterns',
            'predicted_outcome': f"Fringe spacing = {self.predicted_values['fringe_spacing']:.1e} m ± 6%",
            
            'materials_required': [
                'Double-slit apparatus with single-photon source',
                'High-resolution detector array',
                'Consciousness monitoring equipment (EEG/fMRI)',
                'Environmental control system',
                'Data recording software'
            ],
            
            'procedure': [
                '1. Calibrate apparatus without observation (baseline)',
                '2. For each consciousness condition:',
                '   a. Prepare participant in specified state',
                '   b. Record consciousness metrics (φ(S) if possible)',
                '   c. Run double-slit experiment with participant observation',
                '   d. Record interference pattern for 1000+ trials',
                '   e. Measure fringe spacing and visibility',
                '3. Compare patterns across consciousness conditions',
                '4. Statistical analysis of consciousness-interference correlation'
            ],
            
            'consciousness_manipulation': {
                'focused': 'Directed attention on interference pattern',
                'distracted': 'Secondary cognitive task during observation', 
                'meditative': 'Focused awareness without conceptualization',
                'baseline': 'Normal observation without special instruction'
            },
            
            'data_analysis': [
                'Calculate fringe spacing for each condition',
                'Measure visibility (contrast) of interference patterns',
                'Compute correlation with consciousness metrics',
                'Statistical significance testing (p < 0.01)',
                'Compare with Ontologica predictions'
            ],
            
            'expected_results': {
                'consciousness_effect': 'Higher φ(S) should increase visibility',
                'fringe_spacing': 'Should be consistent across conditions',
                'statistical_power': f"Requires n ≥ {self.predicted_values['sample_size']} participants"
            }
        }
        
        return protocol
    
    def quantum_eraser_protocol(self) -> Dict:
        """
        Protocol for quantum eraser experiment testing consciousness role
        in wavefunction collapse and information erasure
        """
        protocol = {
            'experiment_name': 'Consciousness-Mediated Quantum Erasure',
            'objective': 'Test if consciousness affects which-path information erasure',
            
            'key_predictions': [
                'Consciousness should enhance quantum erasure effect',
                'Higher φ(S) correlates with restored interference',
                'Timing of conscious observation affects erasure efficiency'
            ],
            
            'experimental_design': [
                'Standard quantum eraser setup with delayed choice',
                'Multiple consciousness conditions during observation',
                'Real-time consciousness monitoring',
                'Variable delay between measurement and erasure'
            ],
            
            'consciousness_conditions': [
                'Early observation (before path measurement)',
                'Late observation (after measurement, before erasure)', 
                'No conscious observation (automated recording)',
                'Focused vs distracted observation'
            ],
            
            'measurements': [
                'Interference pattern visibility post-erasure',
                'Correlation with consciousness state metrics',
                'Timing effects on erasure efficiency',
                'Comparison with decoherence models'
            ],
            
            'interpretation_guide': {
                'increased_visibility': 'Supports consciousness role in actualization',
                'no_effect': 'Suggests consciousness independent of quantum processes',
                'decreased_visibility': 'May indicate consciousness-induced collapse'
            }
        }
        
        return protocol
    
    def consciousness_decoherence_protocol(self) -> Dict:
        """
        Protocol for measuring consciousness effects on quantum decoherence
        Tests prediction: τ_decoherence = 3.2 ± 0.4 × 10⁻³ s
        """
        return {
            'experiment_name': 'Consciousness-Mediated Decoherence',
            'objective': 'Measure effect of consciousness on quantum coherence times',
            
            'methodology': [
                'Use quantum systems with known coherence times (e.g., qubits)',
                'Vary consciousness conditions during coherence measurements',
                'Measure decoherence rates with high temporal resolution',
                'Correlate with consciousness state metrics'
            ],
            
            'systems_suitable': [
                'Superconducting qubits',
                'Trapped ions', 
                'Quantum dots',
                'NV centers in diamond'
            ],
            
            'consciousness_manipulations': [
                'Focused attention on quantum system',
                'Distracted state with secondary task',
                'Meditative states of various depths',
                'Baseline (no special instruction)'
            ],
            
            'predicted_effects': [
                f"Base decoherence time: {self.predicted_values['decoherence_time']:.1e} s",
                'Consciousness may extend or reduce coherence times',
                'Effect should correlate with φ(S) activation level'
            ],
            
            'data_interpretation': {
                'increased_coherence': 'Supports consciousness as coherence-preserving',
                'decreased_coherence': 'Suggests consciousness induces collapse',
                'no_effect': 'Indicates consciousness independent of decoherence'
            }
        }
    
    def analyze_experimental_results(self, results: Dict, protocol: str) -> Dict:
        """Analyze experimental results against Ontologica's predictions"""
        analysis = {
            'protocol': protocol,
            'results_summary': {},
            'prediction_verification': {},
            'statistical_significance': {},
            'recommendations': []
        }
        
        if protocol == 'double_slit':
            expected_spacing = self.predicted_values['fringe_spacing']
            measured_spacing = results.get('fringe_spacing')
            
            if measured_spacing:
                deviation = abs(measured_spacing - expected_spacing) / expected_spacing
                analysis['prediction_verification']['fringe_spacing'] = {
                    'expected': expected_spacing,
                    'measured': measured_spacing,
                    'deviation': f"{deviation*100:.1f}%",
                    'within_prediction': deviation <= 0.06  # 6% tolerance
                }
        
        if 'consciousness_correlation' in results:
            correlation = results['consciousness_correlation']
            analysis['statistical_significance'] = {
                'correlation_strength': self._interpret_correlation(correlation),
                'sample_size_adequate': results.get('sample_size', 0) >= self.predicted_values['sample_size'],
                'effect_size': self._calculate_effect_size(results)
            }
        
        analysis['recommendations'] = self._generate_recommendations(analysis)
        
        return analysis
    
    def _interpret_correlation(self, correlation: float) -> str:
        """Interpret correlation coefficient"""
        abs_corr = abs(correlation)
        if abs_corr >= 0.7:
            return "strong"
        elif abs_corr >= 0.5:
            return "moderate" 
        elif abs_corr >= 0.3:
            return "weak"
        else:
            return "negligible"
    
    def _calculate_effect_size(self, results: Dict) -> float:
        """Calculate effect size from experimental results"""
        # Simplified effect size calculation
        if 'group_differences' in results:
            differences = results['group_differences']
            if differences:
                return np.std(differences) / np.mean(differences) if np.mean(differences) != 0 else 0
        return 0.0
    
    def _generate_recommendations(self, analysis: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        pred_verification = analysis.get('prediction_verification', {})
        stats = analysis.get('statistical_significance', {})
        
        # Check prediction accuracy
        for key, verification in pred_verification.items():
            if not verification.get('within_prediction', False):
                recommendations.append(f"Review measurement methodology for {key}")
        
        # Check statistical power
        if not stats.get('sample_size_adequate', False):
            recommendations.append("Increase sample size for adequate statistical power")
        
        if stats.get('correlation_strength') in ['weak', 'negligible']:
            recommendations.append("Consider alternative consciousness measurement methods")
        
        if not recommendations:
            recommendations.append("Experimental design appears sound - proceed with data collection")
        
        return recommendations

# Interactive tutorial functions
def demonstrate_double_slit_protocol():
    """Interactive demonstration of double-slit protocol"""
    protocol_guide = QuantumConsciousnessProtocol()
    
    print("=== QUANTUM CONSCIOUSNESS: DOUBLE-SLIT PROTOCOL ===")
    print("\nThis protocol tests Ontologica's prediction of consciousness-mediated quantum effects")
    
    # Display protocol
    protocol = protocol_guide.double_slit_protocol()
    
    print(f"\nEXPERIMENT: {protocol['experiment_name']}")
    print(f"OBJECTIVE: {protocol['objective']}")
    print(f"PREDICTION: {protocol['predicted_outcome']}")
    
    print("\nMATERIALS REQUIRED:")
    for material in protocol['materials_required']:
        print(f"  • {material}")
    
    print("\nPROCEDURE:")
    for step in protocol['procedure']:
        print(f"  {step}")
    
    print("\nCONSCIOUSNESS CONDITIONS:")
    for condition, description in protocol['consciousness_manipulation'].items():
        print(f"  {condition}: {description}")
    
    # Simulate experimental analysis
    print("\n--- EXPERIMENTAL ANALYSIS DEMONSTRATION ---")
    
    # Simulate results
    simulated_results = {
        'fringe_spacing': 8.1e-6,
        'consciousness_correlation': 0.72,
        'sample_size': 35,
        'group_differences': [0.15, 0.22, 0.18]
    }
    
    analysis = protocol_guide.analyze_experimental_results(simulated_results, 'double_slit')
    
    print("SIMULATED RESULTS ANALYSIS:")
    print(f"Fringe spacing verification: {analysis['prediction_verification']['fringe_spacing']}")
    print(f"Correlation strength: {analysis['statistical_significance']['correlation_strength']}")
    print(f"Sample size adequate: {analysis['statistical_significance']['sample_size_adequate']}")
    
    print("\nRECOMMENDATIONS:")
    for rec in analysis['recommendations']:
        print(f"  • {rec}")
    
    return protocol_guide, analysis

def plot_protocol_schematic():
    """Plot schematic diagrams for experimental protocols"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Double-slit schematic
    ax = axes[0, 0]
    x = np.linspace(-0.01, 0.01, 1000)
    intensity = np.cos(2 * np.pi * x / 8.3e-6)**2
    ax.plot(x * 1e6, intensity, 'b-', linewidth=2)
    ax.set_xlabel('Position (μm)')
    ax.set_ylabel('Intensity')
    ax.set_title('Double-Slit Interference Pattern\n(Predicted fringe spacing: 8.3 μm)')
    ax.grid(True, alpha=0.3)
    
    # Consciousness conditions
    ax = axes[0, 1]
    conditions = ['Baseline', 'Distracted', 'Focused', 'Meditative']
    visibility = [0.75, 0.65, 0.85, 0.90]
    ax.bar(conditions, visibility, color=['lightblue', 'lightcoral', 'lightgreen', 'plum'])
    ax.set_ylabel('Interference Visibility')
    ax.set_title('Predicted Visibility vs Consciousness State')
    ax.set_ylim(0, 1)
    
    # Decoherence timeline
    ax = axes[1, 0]
    time = np.linspace(0, 0.01, 100)
    coherence = np.exp(-time / 3.2e-3)
    ax.plot(time * 1e3, coherence, 'r-', linewidth=2)
    ax.axvline(3.2, color='k', linestyle='--', label='Predicted τ = 3.2 ms')
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Coherence')
    ax.set_title('Quantum Decoherence Timeline')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Statistical power
    ax = axes[1, 1]
    sample_sizes = np.arange(10, 101, 10)
    power = 1 - 0.5 ** (sample_sizes / 30)
    ax.plot(sample_sizes, power, 'g-', linewidth=2)
    ax.axhline(0.8, color='k', linestyle='--', label='80% power threshold')
    ax.axvline(30, color='r', linestyle='--', label='Minimum n=30')
    ax.set_xlabel('Sample Size')
    ax.set_ylabel('Statistical Power')
    ax.set_title('Statistical Power vs Sample Size')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('experimental_protocols_schematic.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Run protocol demonstration
    guide, analysis = demonstrate_double_slit_protocol()
    
    # Generate schematic plots
    plot_protocol_schematic()
    
    print("\n=== PROTOCOL DEMONSTRATION COMPLETE ===")
    print("Researchers can use these protocols to experimentally test Ontologica's predictions.")
    print("Key predictions to test:")
    print("  • Fringe spacing = 8.3 ± 0.5 × 10⁻⁶ m in double-slit experiments")
    print("  • Consciousness correlation r > 0.7 with quantum effects") 
    print("  • Decoherence time τ = 3.2 ± 0.4 × 10⁻³ s")
