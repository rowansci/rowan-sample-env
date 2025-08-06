"""Run a rowan micro-pKa calculation for phenol."""

import rowan
import stjames

result = rowan.submit_workflow(
    name="phenol pka",
    initial_molecule=stjames.Molecule.from_smiles("c1ccccc1O"),
    workflow_type="pka",
    workflow_data={},
)

result.wait_for_result()
result.fetch_latest(in_place=True)

print(result.data["strongest_acid"])  # 10.17
