from typing import List, Dict


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        # We assume len(req_skills) <= 16, since it is the constraint of the problem
        m = len(req_skills)
        # We assume len(people) <= 60, since it is the constraint of the problem
        n = len(people)

        skillBitMasks = {}
        for power, skill in enumerate(req_skills):
            skillBitMasks[skill] = 1 << power

        skillPeopleBitMasks = [0] * n
        for i in range(n):
            for skill in people[i]:
                skillPeopleBitMasks[i] |= skillBitMasks[skill]

        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0

        for skillsMask in range(1, 1 << m):
            for i in range(n):
                smallerSkillMask = skillsMask & ~skillPeopleBitMasks[i]
                if smallerSkillMask != skillsMask:
                    # Peoples that has the skills that current does not have + the current one
                    peopleMask = dp[smallerSkillMask] | (1 << i)
                    # Compare set bits for case when we hire the person or we skip it
                    if peopleMask.bit_count() < dp[skillsMask].bit_count():
                        # Update in case the set bits i lower
                        dp[skillsMask] = peopleMask

        answerMask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            if (answerMask >> i) & 1:
                ans.append(i)
        return ans


# With memoization
class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        n = len(people)
        m = len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        # -1 indicate that the skill_set was not yet tested
        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(n):
                new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)
                    # The same as in previous solution but we need to check the case when the skill_set was not yet tested
                    if (
                        dp[skills_mask] == -1
                        or people_mask.bit_count() < dp[skills_mask].bit_count()
                    ):
                        dp[skills_mask] = people_mask
            return dp[skills_mask]

        # Calculated people bit mask for all skills needed
        answer_mask = f((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans
