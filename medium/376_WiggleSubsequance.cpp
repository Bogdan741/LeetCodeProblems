#include <vector>
using namespace std;
class Solution
{
public:
	int wiggleMaxLength(vector<int> &nums)
	{
		int prev_diff = nums[1] - nums[0];
		int count = prev_diff != 0 ? 2 : 1;

		for (int i{2}; i < nums.size(); ++i)
		{
			int diff = nums[i] - nums[i - 1];
			if ((diff > 0 && prev_diff <= 0) || (prev_diff >= 0 && diff < 0))
			{
				// Has been switched (+- < 0, -+ < 0)
				count++;
				prev_diff = diff;
			}
		}
		return count;
	}
};
