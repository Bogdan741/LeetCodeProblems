package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var inorderIndexMap map[int]int
var preorderIndex int

func helpFunction(preorder []int, left, right int) *TreeNode {
	if left > right {
		return nil
	}
	rootVal := preorder[preorderIndex]
	preorderIndex++
	root := new(TreeNode)
	root.Val = rootVal
	root.Left = helpFunction(preorder, left, inorderIndexMap[rootVal]-1)
	root.Right = helpFunction(preorder, inorderIndexMap[rootVal]+1, right)
	return root
}
func buildTree(preorder []int, inorder []int) *TreeNode {
	preorderIndex = 0
	inorderIndexMap = make(map[int]int)
	for i := 0; i < len(preorder); i++ {
		inorderIndexMap[inorder[i]] = i
	}
	return helpFunction(preorder, 0, len(preorder)-1)
}
