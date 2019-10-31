"""
The utils test module contains tests for pycalphad utilities.
"""

import pytest
from pycalphad import Database, Model, ConditionError
from pycalphad.core.utils import filter_phases, unpack_components, instantiate_models

from pycalphad.tests.datasets import ALNIPT_TDB, ALCRNI_TDB

ALNIPT_DBF = Database(ALNIPT_TDB)
ALCRNI_DBF = Database(ALCRNI_TDB)

def test_filter_phases_removes_disordered_phases_from_order_disorder():
    """Databases with order-disorder models should have the disordered phases be filtered if candidate_phases kwarg is not passed to filter_phases.
    If candidate_phases kwarg is passed, disordered phases just are filtered if respective ordered phases are inactive"""
    all_phases = set(ALNIPT_DBF.phases.keys())
    filtered_phases = set(filter_phases(ALNIPT_DBF, unpack_components(ALNIPT_DBF, ['AL', 'NI', 'PT', 'VA'])))
    assert all_phases.difference(filtered_phases) == {'FCC_A1'}
    comps = unpack_components(ALCRNI_DBF, ['NI', 'AL', 'CR', 'VA'])
    filtered_phases = set(filter_phases(ALCRNI_DBF, comps, ['FCC_A1', 'L12_FCC', 'LIQUID', 'BCC_A2']))
    assert filtered_phases == {'L12_FCC', 'LIQUID', 'BCC_A2'}
    filtered_phases = set(filter_phases(ALCRNI_DBF, comps, ['FCC_A1', 'LIQUID', 'BCC_A2']))
    assert filtered_phases == {'FCC_A1', 'LIQUID', 'BCC_A2'}
    filtered_phases = set(filter_phases(ALCRNI_DBF, comps, ['FCC_A1']))
    assert filtered_phases == {'FCC_A1'}


def test_filter_phases_removes_phases_with_inactive_sublattices():
    """Phases that have no active components in any sublattice should be filtered"""
    all_phases = set(ALNIPT_DBF.phases.keys())
    filtered_phases = set(filter_phases(ALNIPT_DBF, unpack_components(ALNIPT_DBF, ['AL', 'NI', 'VA'])))
    assert all_phases.difference(filtered_phases) == {'FCC_A1', 'PT8AL21', 'PT5AL21', 'PT2AL', 'PT2AL3', 'PT5AL3', 'ALPT2'}


def test_filter_phases_raising_error_when_candidate_phases_not_in_database():
    comps = unpack_components(ALNIPT_DBF, ['AL', 'NI', 'VA'])
    candidate_phases = ['SIGMA', 'CHI']
    with pytest.raises(ConditionError):
        set(filter_phases(ALNIPT_DBF, comps, candidate_phases))


def test_instantiate_models_only_returns_desired_phases():
    """instantiate_models should only return phases passed"""
    comps = ['AL', 'NI', 'VA']
    phases = ['FCC_A1', 'LIQUID']

    # models are overspecified w.r.t. phases
    too_many_phases = ['FCC_A1', 'LIQUID', 'AL3NI1']
    too_many_models = {phase: Model(ALNIPT_DBF, comps, phase) for phase in too_many_phases}
    inst_mods = instantiate_models(ALNIPT_DBF, comps, phases, model=too_many_models)
    assert len(inst_mods) == len(phases)

    # models are underspecified w.r.t. phases
    too_few_phases = ['FCC_A1']
    too_few_models = {phase: Model(ALNIPT_DBF, comps, phase) for phase in too_few_phases}
    inst_mods = instantiate_models(ALNIPT_DBF, comps, phases, model=too_few_models)
    assert len(inst_mods) == len(phases)
