import unittest
from types import SimpleNamespace
from skillopt_sleep.decision_shadow import observe_attempt


class CompanionTests(unittest.IsolatedAsyncioTestCase):
    async def test_existing_outcome_and_input_are_not_replaced_or_mutated(self):
        class Observer:
            async def observe(self,ctx,facts,existing):
                existing['status']='passed'
                return {'effective_result':{'status':'passed'},'audit':{'recommendation':'reported_claim','permission':False}}
        outcome={'status':'unverified','unresolved_ids':['APK9-01'],'deferred':['device'],'owner':'Chase'}
        result=await observe_attempt(Observer(),SimpleNamespace(category='skillopt'),{},outcome)
        self.assertEqual(result['effective_result'],outcome)
        self.assertEqual(outcome['status'],'unverified')
        self.assertFalse(result['audit']['permission'])

    async def test_non_skillopt_context_rejected(self):
        with self.assertRaises(ValueError): await observe_attempt(None,SimpleNamespace(category='orchestrator'),{},'old')
