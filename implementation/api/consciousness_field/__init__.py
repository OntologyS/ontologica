"""
Consciousness Field API for Ontologica
Implementation of φ-field dynamics and quantum consciousness operators
"""

from .phi_calculator import PhiActivationCalculator, ConsciousnessState
from .field_operator import (
    ConsciousnessFieldOperator,
    QuantumConsciousnessState, 
    DoubleSlitSimulator,
    demonstrate_consciousness_field
)

__all__ = [
    'PhiActivationCalculator',
    'ConsciousnessState',
    'ConsciousnessFieldOperator',
    'QuantumConsciousnessState',
    'DoubleSlitSimulator', 
    'demonstrate_consciousness_field'
]

__version__ = "1.0.0"
