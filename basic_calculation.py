"""Run an energy calculation on isoprene."""

import rowan
from stjames import Method, Molecule

result = rowan.submit_basic_calculation_workflow(
    initial_molecule=Molecule.from_smiles("CC(=C)C=C"),
    method=Method.OMOL25_CONSERVING_S,
    tasks=["energy"],
    mode="auto",
    engine="omol25",
    name="Isoprene Energy",
)

print(f"View workflow privately at: https://labs.rowansci.com/workflow/{result.uuid}\n")
result.wait_for_result().fetch_latest(in_place=True)

print("Final Results:")
print(result)
