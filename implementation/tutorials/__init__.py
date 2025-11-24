"""
Tutorials module for Ontologica practical implementation
Educational materials for researchers and developers
"""

from .mathematical_foundations.ontology_calculator import (
    OntologyMathematicsTutorial,
    run_ontology_tutorial
)

from .experimental_protocols.quantum_consciousness_guide import (
    QuantumConsciousnessProtocol,
    ExperimentalSetup,
    demonstrate_double_slit_protocol,
    plot_protocol_schematic
)

from .technology_applications.dai_development_guide import (
    DAIDevelopmentGuide,
    DAIDevelopmentStage,
    demonstrate_dai_development,
    plot_development_timeline
)

__all__ = [
    # Mathematical foundations
    'OntologyMathematicsTutorial',
    'run_ontology_tutorial',
    
    # Experimental protocols
    'QuantumConsciousnessProtocol', 
    'ExperimentalSetup',
    'demonstrate_double_slit_protocol',
    'plot_protocol_schematic',
    
    # Technology applications
    'DAIDevelopmentGuide',
    'DAIDevelopmentStage',
    'demonstrate_dai_development',
    'plot_development_timeline'
]

__version__ = "1.0.0"
