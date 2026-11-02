"""Optional read-only companion. Not an optimizer Backend or a scoring authority.

Pass the shared ACC DecisionsAdapter explicitly. No SDK/key dependency, implicit
imports, collector access, state checkpoint or adoption hooks are introduced.
"""
from copy import deepcopy


async def observe_attempt(adapter, context, minimized_facts, existing_outcome):
    if context.category != 'skillopt':
        raise ValueError('skillopt context required')
    before = deepcopy(existing_outcome)
    result = await adapter.observe(context, minimized_facts, before)
    # Never accept a replacement score, completion, or optimizer state from an observer.
    return {'effective_result': deepcopy(existing_outcome), 'audit': result['audit']}
