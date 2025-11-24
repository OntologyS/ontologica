"""
Test suite for Ontologica framework validation
Comprehensive testing of mathematical predictions, computational implementations, and experimental verification
"""

__version__ = "1.0.0"
__author__ = "Ontologica Research Team"

from .unit_tests import test_educational_manifold, test_consciousness_field
from .integration_tests import test_complete_workflow
from .validation_suites import experimental_predictions_validation

__all__ = [
    'test_educational_manifold',
    'test_consciousness_field', 
    'test_complete_workflow',
    'experimental_predictions_validation'
]
